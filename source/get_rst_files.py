import os
import re
from os.path import exists
from urllib.request import urlretrieve

import requests
import github
from github import Github
from sphinx.util import logging

logger = logging.getLogger(__name__)

brand_name = 'Eumetsat-Elasticity'
string_to_replace = 'Eumetsat-Elasticity'

cloud_name = 'WAW3-1'
cloud_name_to_replace = 'WAW3-1'

def process_url(url: str):
    """Extract repository and directory name from URL."""
    if "tree" in url:
        repo, dir_name = re.split(r"/tree/\w+/", url)
        return repo.replace("https://github.com/", ""), dir_name
    return None, None

def process_content(content):
    """Process content path for branding and cloud naming adjustments."""
    content_path = content.path
    if content.type == "file" and ".rst" in content.name:
        if string_to_replace in content.name:
            content_path = content.path.replace(string_to_replace, brand_name)
        if cloud_name_to_replace in content_path:
            content_path = content_path.replace(cloud_name_to_replace, cloud_name)
    content_path_split = content_path.split("/")[-1]
#     print("process_content:: content_path_split = ",content_path_split)
    return content_path_split

def urls_list_to_dict(urls_list: list) -> dict:
    """Convert list of URLs to a dictionary grouped by repository."""
    urls_dict = {}
    for url in urls_list:
        repo_name, dir_name = process_url(url.replace("blob", "tree"))
        if not urls_dict.get(repo_name, None):
            urls_dict[repo_name] = []
        urls_dict[repo_name].append(dir_name)
    return urls_dict

def check_updates(github_file_content: str, local_file_path: str) -> bool:
    """Check if the local file is up-to-date with the GitHub version."""
    dir_name = local_file_path.split("/")[0]
    file_path = dir_name + local_file_path
    if exists(dir_name):
        if exists(file_path) and github_file_content == open(file_path, "rb").read():
            return False
    else:
        os.makedirs(dir_name)
    return True

def download_content(content, folder):
    """Download content from GitHub, handling potential errors like chunked encoding issues."""
    content_url = {}
    content_name = process_content(content)

    if content.type == "file" and ".rst" in content.name:
        content_url[folder + "/" + content_name.replace(".rst", "")] = content.html_url

    github_file_url = content.download_url
    try:
        # Download the file with a stream and handle chunked encoding error
        response = requests.get(github_file_url, stream=True, timeout=10)
        response.raise_for_status()  # Raise exception for HTTP errors

        # Check if the file needs updating
        if check_updates(response.content, folder + "/" + content_name):
            with open(folder + "/" + content_name, 'wb') as file:
                for chunk in response.iter_content(1024):
                    file.write(chunk)
            logger.info(f"Downloaded and updated: {folder}/{content_name}")
        else:
            logger.info(f"No updates needed: {folder}/{content_name}")

    except requests.exceptions.ChunkedEncodingError as e:
        logger.error(f"Chunked encoding error while downloading {github_file_url}: {e}")
    except requests.exceptions.RequestException as e:
        logger.error(f"Error downloading {github_file_url}: {e}")

    return content_url

def get_files(urls_list: dict) -> dict:
    """Retrieve .rst and other files from specified GitHub repositories."""
    external_repos_url = {}
    for folder in urls_list.keys():
        urls_dict = urls_list_to_dict(urls_list.get(folder))
        login_or_token = os.environ.get("github_token", "")
        gh = Github(login_or_token)

        for repo, dirs in urls_dict.items():
            try:
                repo_obj = gh.get_repo(repo)
                for dir_name in dirs:
                    contents_list = repo_obj.get_contents(dir_name)
                    for content in contents_list:
                        external_repos_url.update(download_content(content, folder))
            except github.GithubException as e:
                logger.warning(
                    '"%s" is omitted, "%s", "%s"'
                    % (repo, e.status, e.data.get("message", "No message"))
                )

    return external_repos_url
