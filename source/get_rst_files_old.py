import re
import os
from os.path import exists
from urllib.request import urlretrieve

import requests
from github import Github


def process_url(url: str):
    if "tree" in url:
        repo, dir_name = re.split(r"/tree/\w+/", url)
        return repo.replace("https://github.com/", ""), dir_name
    return None, None


def urls_list_to_dict(urls_list: list) -> dict:
    urls_dict = {}
    for url in urls_list:
        repo_name, dir_name = process_url(url.replace("blob", "tree"))
        if not urls_dict.get(repo_name, None):
            urls_dict[repo_name] = []
        urls_dict[repo_name].append(dir_name)
    return urls_dict


def check_updates(github_file_content: str, local_file_path: str) -> bool:
    dir_name = local_file_path.split("/")[0]
    file_path = dir_name + local_file_path
    if exists(dir_name):
        if exists(file_path) and github_file_content == open(file_path, "rb").read():
            return False
    else:
        os.makedirs(dir_name)
    return True


def get_files(urls_list: dict) -> dict:
    external_repos_url = {}
    for folder in urls_list.keys():
        urls_dict = urls_list_to_dict(urls_list.get(folder))
        gh = Github(login_or_token=os.environ.get("github_token", ""))
        for repo, dirs in urls_dict.items():
            repo = gh.get_repo(repo)
            for dir_name in dirs:
                contents_list = repo.get_contents(dir_name)
                for content in contents_list:
                    if content.type == "file":
                        if ".rst" in content.name:
                            external_repos_url[
                                folder + "/" + content.name.replace(".rst", "")
                            ] = content.html_url
                        github_file_url = content.download_url
                        temp = folder + "/" + content.path.split("/")[-1]
                        github_file = requests.get(github_file_url)
                        if check_updates(
                            github_file.content,
                            folder + "/" + content.path.split("/")[-1],
                        ):
                            urlretrieve(
                                github_file_url,
                                folder + "/" + content.path.split("/")[-1],
                            )
    return external_repos_url
