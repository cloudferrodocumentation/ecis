import os
import re
import time
from os.path import exists
from pathlib import Path

import requests
import github
from github import Github
from sphinx.util import logging

logger = logging.getLogger(__name__)

brand_name = "ECIS"
string_to_replace = "Eumetsat-Elasticity"

cloud_name = ""
cloud_name_to_replace = "-WAW3-1"


IMAGE_EXTENSIONS = {
    ".png",
    ".jpg",
    ".jpeg",
    ".webp",
    ".gif",
    ".svg",
}


BRAND_IMAGE_PREFIXES = [
    "creodias_",
    "cloudferro-cloud_",
    "ecis_",
    "eumetsat_",
    "wekeo_",
    "wekeo-elasticity_",
    "eolab_",
    "eolab-de_",
    "esa-hpc_",
    "copphil_",
    "nsis_",
    "dedl-central_",
    "dedl-lumi_",
    "codede_",
]


BRAND_TO_IMAGE_PREFIX = {
    # Direct brand keys
    "creodias": "creodias_",
    "cloudferro_cloud": "cloudferro-cloud_",
    "cloudferro-cloud": "cloudferro-cloud_",
    "ecis": "ecis_",
    "eumetsat": "eumetsat_",
    "eumetsat_elasticity": "eumetsat_",
    "eumetsat-elasticity": "eumetsat_",
    "wekeo": "wekeo_",
    "wekeoelasticity": "wekeo-elasticity_",
    "wekeo_elasticity": "wekeo-elasticity_",
    "wekeo-elasticity": "wekeo-elasticity_",
    "eolab": "eolab_",
    "eolab_en": "eolab_",
    "eolab_de": "eolab-de_",
    "esa_hpc": "esa-hpc_",
    "esahpc": "esa-hpc_",
    "esa-hpc": "esa-hpc_",
    "copphil": "copphil_",
    "nsis": "nsis_",
    "nsis_en": "nsis_",
    "nsis_pl": "nsis_",
    "dedl_central": "dedl-central_",
    "dedl-central": "dedl-central_",
    "dedl_lumi": "dedl-lumi_",
    "dedl-lumi": "dedl-lumi_",
    "codede": "codede_",
    "codede_en": "codede_",
    "codede_de": "codede_",

    # Display names / common replacements
    "cloudferro cloud": "cloudferro-cloud_",
    "eumetsat elasticity": "eumetsat_",
    "wekeo elasticity": "wekeo-elasticity_",
    "esa hpc": "esa-hpc_",
    "dedl central": "dedl-central_",
    "dedl lumi": "dedl-lumi_",
    "code-de": "codede_",
    "code de": "codede_",
}


# Visible-brand cleanup is intentionally separate from internal brand handling.
#
# must remain usable as:
# - the active brand key,
# - image-prefix selector,
# - repository/project identifier,
# - configuration branch selector.
#
# must be removed only from user-visible generated article names, titles,
# toctree labels, doc links, and text created by this import script.
VISIBLE_BRANDING_HIDDEN_FOR = {
    "ecis",
}


def _truthy_env(name: str, default: bool = True) -> bool:
    """
    Read a boolean value from environment variables.

    True values:
    - 1
    - true
    - yes
    - y
    - on

    False values:
    - 0
    - false
    - no
    - n
    - off
    """
    value = os.environ.get(name)

    if value is None:
        return default

    value = value.strip().lower()

    if value in {"1", "true", "yes", "y", "on"}:
        return True

    if value in {"0", "false", "no", "n", "off"}:
        return False

    return default


def normalize_brand_key(value: str) -> str:
    """
    Normalize a brand name or brand key so it can be used for lookups.

    Examples:
    - -> ecis
    - Eumetsat Elasticity -> eumetsat_elasticity
    - cloudferro-cloud -> cloudferro_cloud
    """
    value = (value or "").strip().lower()
    value = value.replace("-", "_")
    value = re.sub(r"\s+", "_", value)
    value = re.sub(r"[^a-z0-9_]", "", value)
    return value


def get_active_brand_key() -> str:
    """
    Return the normalized active brand key.

    Priority:
    1. BRAND environment variable
    2. brand_name variable in this file
    """
    candidates = [
        os.environ.get("BRAND", "").strip(),
        brand_name,
    ]

    for candidate in candidates:
        normalized = normalize_brand_key(candidate)
        if normalized:
            return normalized

    return ""


def should_hide_visible_branding() -> bool:
    """
    Return True when the current build should remove visible brand suffixes.

    For, customer-facing documentation must not show in:
    - article titles,
    - filenames / slugs,
    - toctree labels,
    - doc links,
    - rendered body text created by this import script.

    Set CF_HIDE_VISIBLE_BRANDING=0 to disable this during debugging.
    """
    if not _truthy_env("CF_HIDE_VISIBLE_BRANDING", default=True):
        return False

    return get_active_brand_key() in VISIBLE_BRANDING_HIDDEN_FOR


def get_visible_brand_tokens() -> list[str]:
    """
    Return visible brand names that may need to be removed from imported RST.

    The default for is only. Additional tokens can be supplied by
    setting CF_VISIBLE_BRAND_TOKENS as a comma-separated list.

    Example:
        CF_VISIBLE_BRAND_TOKENS="ECIS,ECIS Cloud"
    """
    tokens = []

    if should_hide_visible_branding():
        tokens.append(brand_name)

    extra_tokens = os.environ.get("CF_VISIBLE_BRAND_TOKENS", "").strip()
    if extra_tokens:
        tokens.extend(token.strip() for token in extra_tokens.split(",") if token.strip())

    # Longest tokens first, deduplicated case-insensitively.
    seen = set()
    result = []
    for token in sorted(tokens, key=len, reverse=True):
        key = token.lower()
        if key in seen:
            continue
        seen.add(key)
        result.append(token)

    return result


def get_active_image_prefix() -> str:
    """
    Return the image prefix for the active brand.

    Priority:
    1. CF_IMAGE_BRAND environment variable
    2. BRAND environment variable
    3. brand_name variable in this file

    Examples:
    - -> ecis_
    - ecis -> ecis_
    - eumetsat -> eumetsat_
    - cloudferro_cloud -> cloudferro-cloud_
    """
    candidates = [
        os.environ.get("CF_IMAGE_BRAND", "").strip(),
        os.environ.get("BRAND", "").strip(),
        brand_name,
    ]

    for candidate in candidates:
        if not candidate:
            continue

        direct = candidate.strip().lower()
        normalized = normalize_brand_key(candidate)

        if direct in BRAND_TO_IMAGE_PREFIX:
            return BRAND_TO_IMAGE_PREFIX[direct]

        if normalized in BRAND_TO_IMAGE_PREFIX:
            return BRAND_TO_IMAGE_PREFIX[normalized]

    return ""


def is_image_file(filename: str) -> bool:
    """
    Return True if filename looks like an image file.
    """
    return Path(filename).suffix.lower() in IMAGE_EXTENSIONS


def has_known_brand_image_prefix(filename: str) -> bool:
    """
    Return True if filename already starts with one of the known brand image prefixes.
    """
    return any(filename.startswith(prefix) for prefix in BRAND_IMAGE_PREFIXES)


def should_download_content(content) -> bool:
    """
    Decide whether a GitHub ContentFile should be downloaded.

    Non-image files are always downloaded.

    Image files are filtered by brand:
    - keep images starting with the active brand prefix
    - skip images starting with another known brand prefix
    - keep unprefixed images by default, for backward compatibility

    To download only active-brand images and skip unprefixed fallback images, set:

        CF_KEEP_UNPREFIXED_IMAGES=0

    To override the active brand used for image filtering, set:

        CF_IMAGE_BRAND=ecis
    """
    if content.type != "file":
        return False

    filename = content.name

    if not is_image_file(filename):
        return True

    active_prefix = get_active_image_prefix()
    keep_unprefixed_images = _truthy_env("CF_KEEP_UNPREFIXED_IMAGES", default=True)

    if not active_prefix:
        logger.warning(
            "No active image prefix could be determined. Downloading image without brand filtering: %s",
            getattr(content, "path", filename),
        )
        return True

    if filename.startswith(active_prefix):
        return True

    if has_known_brand_image_prefix(filename):
        logger.info(
            "Skipping image for another brand: %s",
            getattr(content, "path", filename),
        )
        return False

    if keep_unprefixed_images:
        return True

    logger.info(
        "Skipping unprefixed image because CF_KEEP_UNPREFIXED_IMAGES=0: %s",
        getattr(content, "path", filename),
    )
    return False


def process_url(url: str):
    """
    Extract repository and path from GitHub blob/tree URL.

    Supports both:
    - https://github.com/org/repo/blob/main/source/file.rst
    - https://github.com/org/repo/tree/main/source/folder
    """
    m = re.match(r"https://github\.com/([^/]+/[^/]+)/(?:blob|tree)/[^/]+/(.+)", url)
    if not m:
        return None, None

    return m.group(1), m.group(2)


def replace_brand_and_cloud(value: str) -> str:
    """
    Apply the normal repository-to-local brand/cloud replacements.

    This keeps the original behavior:
    - Eumetsat-Elasticity ->
    - -WAW3-1 -> cloud_name value
    """
    if string_to_replace:
        value = value.replace(string_to_replace, brand_name)

    if cloud_name_to_replace:
        value = value.replace(cloud_name_to_replace, cloud_name)

    return value

def _cleanup_spaces(value: str) -> str:
    """
    Normalize spaces introduced by visible-brand removal without touching
    leading indentation.

    RST indentation is semantic. Never collapse spaces at the beginning of
    a line, because that breaks directive options and directive bodies, for
    example:

       .. figure:: image.png
          :class: with-border
    """
    match = re.match(r"^([ \t]*)(.*)$", value)

    if not match:
        return value

    indent = match.group(1)
    body = match.group(2)

    body = re.sub(r"[ \t]{2,}", " ", body)
    body = re.sub(r"[ \t]+([,.!?])", r"\1", body)
    body = re.sub(r"([(\[{])[ \t]+", r"\1", body)
    body = re.sub(r"[ \t]+([)\]}])", r"\1", body)

    return indent + body

def remove_visible_brand_from_filename(filename: str) -> str:
    """
    Remove visible brand suffixes from generated filenames for selected brands.

    Example:
    Generating-and-authorizing-Terraform-using-Keycloak-user-on.rst
    becomes:
    Generating-and-authorizing-Terraform-using-Keycloak-user.rst

    This function is conservative and targets suffix-style branding only.
    """
    if not should_hide_visible_branding():
        return filename

    path = Path(filename)
    stem = path.stem
    suffix = path.suffix

    for token in get_visible_brand_tokens():
        token_slug = re.sub(r"\s+", "-", token.strip())
        token_slug_pattern = re.escape(token_slug)

        patterns = [
            rf"-on-{token_slug_pattern}$",
            rf"-in-{token_slug_pattern}$",
            rf"-for-{token_slug_pattern}$",
            rf"-using-{token_slug_pattern}$",
            rf"-{token_slug_pattern}$",
        ]

        for pattern in patterns:
            stem = re.sub(pattern, "", stem, flags=re.IGNORECASE)

    stem = re.sub(r"-{2,}", "-", stem).strip("-")

    if path.parent == Path("."):
        return stem + suffix

    return str(path.with_name(stem + suffix))


def remove_visible_brand_from_text(text: str) -> str:
    """
    Remove visible brand mentions from imported RST content.

    This is broader than filename cleanup because imported RST may contain:
    - headings,
    - toctree labels,
    - doc links,
    - regular paragraphs.

    It intentionally removes complete phrases around the visible brand, not the
    internal brand key used by Python configuration.
    """
    if not should_hide_visible_branding():
        return text

    for token in get_visible_brand_tokens():
        token_re = re.escape(token)

        # Filename / slug fragments inside links and toctrees.
        slug = re.sub(r"\s+", "-", token.strip())
        slug_re = re.escape(slug)

        text = re.sub(rf"-on-{slug_re}(?=\.html\b|\.rst\b|\b|`|>|\)|\s|$)", "", text, flags=re.IGNORECASE)
        text = re.sub(rf"-in-{slug_re}(?=\.html\b|\.rst\b|\b|`|>|\)|\s|$)", "", text, flags=re.IGNORECASE)
        text = re.sub(rf"-for-{slug_re}(?=\.html\b|\.rst\b|\b|`|>|\)|\s|$)", "", text, flags=re.IGNORECASE)
        text = re.sub(rf"-{slug_re}(?=\.html\b|\.rst\b|`|>|\)|\s|$)", "", text, flags=re.IGNORECASE)

        # Text/title suffixes.
        text = re.sub(rf"\s+on\s+{token_re}(?=(`|$|\n|[.,;:!?)]))", "", text, flags=re.IGNORECASE)
        text = re.sub(rf"\s+in\s+{token_re}(?=(`|$|\n|[.,;:!?)]))", "", text, flags=re.IGNORECASE)
        text = re.sub(rf"\s+for\s+{token_re}(?=(`|$|\n|[.,;:!?)]))", "", text, flags=re.IGNORECASE)

        # Remaining standalone visible brand token.
        text = re.sub(rf"\b{token_re}\b", "", text, flags=re.IGNORECASE)

    lines = [_cleanup_spaces(line).rstrip() for line in text.splitlines()]
    text = "\n".join(lines)

    # Remove spaces before newlines after token deletion.
    text = re.sub(r"[ \t]+\n", "\n", text)

    # Avoid over-aggressive blank-line normalization. The imported RST may
    # intentionally contain blank lines inside directives.
    return text


def normalize_simple_heading_underlines(text: str) -> str:
    """
    Normalize simple RST heading underline lengths after title cleanup.

    Only underline-only lines directly following a non-empty title line are
    changed. This avoids touching directive bodies, literal blocks, and
    transition lines surrounded by blank lines.
    """
    lines = text.splitlines()
    heading_chars = set("=-^+*#~")

    for index in range(1, len(lines)):
        line = lines[index]
        stripped = line.strip()

        if not stripped:
            continue

        if len(set(stripped)) != 1:
            continue

        if stripped[0] not in heading_chars:
            continue

        previous = lines[index - 1].rstrip()

        if not previous:
            continue

        if previous.lstrip().startswith(".. "):
            continue

        indent = line[: len(line) - len(line.lstrip())]
        lines[index] = indent + stripped[0] * len(previous.strip())

    return "\n".join(lines)


def process_content_name(content):
    """
    Return the final local filename after brand/cloud replacements.

    Only the basename is used because files are written into the local target folder.

    For builds, visible suffixes are removed from generated RST names.
    This affects only local output filenames, not GitHub source paths.
    """
    content_name = content.name

    if content.type == "file" and content_name.endswith(".rst"):
        content_name = replace_brand_and_cloud(content_name)
        content_name = remove_visible_brand_from_filename(content_name)

    return content_name


def transform_rst_content(raw_bytes: bytes) -> bytes:
    """
    Rewrite downloaded RST content so titles, toctree references, doc links,
    and inline text stay aligned with the locally renamed filenames.

    Processing order:
    1. Apply existing brand/cloud replacements.
    2. For brands configured in VISIBLE_BRANDING_HIDDEN_FOR, remove the visible
       brand token from generated titles, links, toctree entries, and prose.

    Internal configuration identifiers are not processed by this function.
    It only touches downloaded RST content.
    """
    text = raw_bytes.decode("utf-8")

    text = replace_brand_and_cloud(text)
    text = remove_visible_brand_from_text(text)
    text = normalize_simple_heading_underlines(text)

    return text.encode("utf-8")


def urls_list_to_dict(urls_list: list) -> dict:
    """
    Convert list of GitHub URLs into a dictionary grouped by repository.
    """
    urls_dict = {}

    for url in urls_list:
        repo_name, repo_path = process_url(url)

        if not repo_name or not repo_path:
            continue

        urls_dict.setdefault(repo_name, []).append(repo_path)

    return urls_dict


def ensure_parent_dir(local_file_path: str):
    """
    Create the parent directory for a local file if it does not exist.
    """
    parent = os.path.dirname(local_file_path)

    if parent and not exists(parent):
        os.makedirs(parent, exist_ok=True)


def check_updates(final_bytes: bytes, local_file_path: str) -> bool:
    """
    Return True if file should be written, False if unchanged.
    """
    ensure_parent_dir(local_file_path)

    if exists(local_file_path):
        with open(local_file_path, "rb") as f:
            if f.read() == final_bytes:
                return False

    return True


def _safe_github_exc_message(e) -> str:
    """
    Return a readable message from PyGithub exceptions.
    """
    data = getattr(e, "data", None)

    if isinstance(data, dict):
        return data.get("message", "No message")

    return str(data) if data else str(e)


def _get_token_for_repo(repo_name: str) -> str:
    """
    Return the correct token for a given repo.

    Expected RTD environment variables:
    - github_token
    - github_token_managed
    """
    if repo_name == "cloudferrodocumentation/kubernetes-managed":
        token = os.environ.get("github_token_managed", "").strip()

        if not token:
            logger.warning(
                'Repo "%s" requires env var github_token_managed, but it is missing or empty.',
                repo_name,
            )

        return token

    token = os.environ.get("github_token", "").strip()

    if not token:
        logger.warning(
            'Default env var github_token is missing or empty while accessing repo "%s".',
            repo_name,
        )

    return token


def _get_github_client_for_repo(repo_name: str) -> Github:
    """
    Return a PyGithub client configured with the token for the requested repo.
    """
    token = _get_token_for_repo(repo_name)

    return Github(token)


def _get_contents_with_retries(repo_obj, repo_path: str, max_attempts: int = 3):
    """
    Retry transient API errors for GitHub contents lookup.

    Also handle file-style paths that may omit the .rst extension.

    Returns either:
    - list[ContentFile] for directories
    - ContentFile for single files
    """
    last_exc = None
    candidate_paths = [repo_path]

    base_name = os.path.basename(repo_path)

    if not repo_path.endswith(".rst") and "." not in base_name:
        candidate_paths.append(repo_path + ".rst")

    for candidate in candidate_paths:
        last_exc = None

        for attempt in range(1, max_attempts + 1):
            try:
                return repo_obj.get_contents(candidate)
            except github.GithubException as e:
                last_exc = e
                status = getattr(e, "status", None)

                if status == 404:
                    break

                if status == 504 and attempt < max_attempts:
                    time.sleep(2 * attempt)
                    continue

                raise

    raise last_exc


def _normalize_contents(contents_obj):
    """
    Normalize PyGithub output so callers always receive a list.
    """
    if isinstance(contents_obj, list):
        return contents_obj

    return [contents_obj]


def download_content(content, folder):
    """
    Download one GitHub file into the local folder.

    RST files are renamed and rewritten.

    Brand-prefixed image files are filtered before download:
    - active-brand images are downloaded
    - unprefixed images are downloaded by default
    - images for other known brands are skipped
    """
    external_url_map = {}

    if content.type != "file":
        return external_url_map

    if not should_download_content(content):
        return external_url_map

    local_name = process_content_name(content)
    local_file_path = os.path.join(folder, local_name)

    if content.name.endswith(".rst"):
        external_url_map[os.path.join(folder, local_name[:-4])] = content.html_url

    github_file_url = content.download_url

    if not github_file_url:
        logger.warning("Skipping file without download_url: %s", getattr(content, "path", "?"))
        return external_url_map

    try:
        response = requests.get(github_file_url, timeout=20)
        response.raise_for_status()

        raw_bytes = response.content

        if content.name.endswith(".rst"):
            final_bytes = transform_rst_content(raw_bytes)
        else:
            final_bytes = raw_bytes

        if check_updates(final_bytes, local_file_path):
            with open(local_file_path, "wb") as f:
                f.write(final_bytes)

            logger.info("Downloaded and updated: %s", local_file_path)
        else:
            logger.info("No updates needed: %s", local_file_path)

    except requests.exceptions.RequestException as e:
        logger.error("Error downloading %s: %s", github_file_url, e)

    return external_url_map


def _collect_files(repo_obj, repo_path: str, recursive: bool = True):
    """
    Collect files from a repo path.

    Supports both:
    - direct file paths
    - directories

    Optionally recurses into subdirectories.
    """
    results = []

    contents_obj = _get_contents_with_retries(repo_obj, repo_path, max_attempts=3)
    contents = _normalize_contents(contents_obj)

    for item in contents:
        if item.type == "file":
            results.append(item)
        elif item.type == "dir" and recursive:
            subitems = _collect_files(repo_obj, item.path, recursive=True)
            results.extend(subitems)

    return results


def get_files(urls_list: dict) -> dict:
    """
    Retrieve .rst and other files from specified GitHub repositories.

    Returns a map of locally generated document paths to their original GitHub
    HTML URLs. This is used elsewhere in the documentation build to track where
    imported pages came from.
    """
    external_repos_url = {}
    github_clients = {}

    active_prefix = get_active_image_prefix()
    keep_unprefixed_images = _truthy_env("CF_KEEP_UNPREFIXED_IMAGES", default=True)

    if active_prefix:
        logger.info("Brand image filtering is active. Active image prefix: %s", active_prefix)
        logger.info("Keep unprefixed images: %s", keep_unprefixed_images)
    else:
        logger.warning(
            "Brand image filtering could not determine an active image prefix. "
            "All images will be downloaded."
        )

    if should_hide_visible_branding():
        logger.info(
            "Visible branding cleanup is active for brand key: %s. Tokens removed: %s",
            get_active_brand_key(),
            ", ".join(get_visible_brand_tokens()),
        )

    for folder, repo_urls in urls_list.items():
        urls_dict = urls_list_to_dict(repo_urls)

        for repo_name, repo_paths in urls_dict.items():
            if repo_name not in github_clients:
                github_clients[repo_name] = _get_github_client_for_repo(repo_name)

            gh = github_clients[repo_name]

            try:
                repo_obj = gh.get_repo(repo_name)
            except github.GithubException as e:
                logger.warning(
                    '"%s" is omitted, status=%s, message=%s',
                    repo_name,
                    getattr(e, "status", "?"),
                    _safe_github_exc_message(e),
                )
                continue

            for repo_path in repo_paths:
                try:
                    files = _collect_files(repo_obj, repo_path, recursive=True)
                except github.GithubException as e:
                    logger.warning(
                        '"%s/%s" is omitted, status=%s, message=%s',
                        repo_name,
                        repo_path,
                        getattr(e, "status", "?"),
                        _safe_github_exc_message(e),
                    )
                    continue

                for content in files:
                    external_repos_url.update(download_content(content, folder))

    return external_repos_url
