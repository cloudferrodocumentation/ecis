# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# -- Path setup --------------------------------------------------------------

import os
import json
import time
import shutil
from pathlib import Path
from datetime import date, datetime

from get_rst_files import get_files

# -- Project information -----------------------------------------------------

project = "ECIS"
copyright = f"{datetime.now().year}, EUMETSAT"
author = "CloudFerro"

def load_array(filename):
    path = os.path.join(os.path.dirname(__file__), '_copyright_data', filename)

    if not os.path.exists(path):
        return []

    with open(path, 'r', encoding='utf-8') as file:
        return json.load(file)

array1 = load_array('array1.json')
array2 = load_array('array2.json')
array3 = load_array('array3.json')
array4 = load_array('array4.json')

TWO_FA_ACTIVATED_BRANDS = [
    "Creodias",
    "CloudFerro Cloud",
    "EO-Lab",
    "CODE-DE",
    "NSIS Cloud",
]

def setup(app):
   # >>> CF_BRAND_BLOCK: setup_config_values
   app.add_config_value('brand_name', '', True)
   app.add_config_value('cloud_name', '', True)
   app.add_config_value('second_cloud_name', '', True)
   app.add_config_value('brands_without_eodata', ['Eumetsat Elasticity', 'CloudFerro Cloud', 'Destination Earth', 'WEkEO', 'ECIS'], True, [])
   app.add_config_value('two_fa_activated', TWO_FA_ACTIVATED_BRANDS, True, [])
   app.add_config_value('special_eodata', ['EO-Lab', 'CODE-DE'], True, [])
   app.add_config_value('single_cloud', ['EO-Lab', 'CODE-DE', 'Eumetsat Elasticity', 'ESA HPC', 'NSIS Cloud'], True, [])
   app.add_config_value('multi_cloud', ['Creodias', 'CloudFerro Cloud','WEkEO', 'WEkEO Elasticity', 'ECIS'],True, [])
   app.add_config_value('vgpu_compliant', ['EO-Lab', 'CODE-DE', 'Creodias', 'CloudFerro Cloud', 'WEkEO', 'WEkEO Elasticity', 'ESA HPC', 'ECIS'], True, [])
   app.add_config_value('localstorage_present', ['Creodias', 'CloudFerro Cloud', 'WEkEO', 'WEkEO Elasticity', 'ESA HPC', 'Eumetsat Elasticity','NSIS Cloud'], True, [])
   app.add_config_value('windows_image_present', ['Creodias',  'WEkEO', 'WEkEO Elasticity', 'EO-Lab', 'CODE-DE','NSIS Cloud', 'ECIS'], True, [])
   app.add_config_value('with_note', ['Creodias', 'CloudFerro Cloud'], True, [])
   app.add_config_value('dashboard_extension_existing', ['Creodias', 'CloudFerro Cloud', 'WEkEO Elasticity'],True, [])
   app.add_config_value('without_ppu', ['NSIS Cloud'],True, [])
   app.add_config_value('has_heat_templates', ['Creodias', 'CloudFerro Cloud','WEkEO', 'WEkEO Elasticity', 'ESA HPC', 'EO-Lab', 'CODE-DE', 'Destination Earth', 'Eumetsat Elasticity', 'ECIS'],True, [])
   app.add_config_value('has_clusterapi_templates', ['Creodias', 'CloudFerro Cloud','WEkEO', 'WEkEO Elasticity','NSIS Cloud', 'Destination Earth'],True, [])
   app.add_config_value('has_dualstack_templates', ['Destination Earth'],True, [])
   app.add_config_value('has_vgpu_templates', ['ESA HPC'],True, [])
   app.add_config_value('managed_kubernetes_with_magnum', ['Creodias', 'CloudFerro Cloud','WEkEO', 'WEkEO Elasticity', 'ESA HPC', 'EO-Lab', 'CODE-DE', 'Destination Earth', 'Eumetsat Elasticity', 'NSIS Cloud'],True, [])
   # <<< CF_BRAND_BLOCK: setup_config_values

# make sure you have this already
html_static_path = ['_static']


# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration
import sphinx_rtd_theme

html_theme = "sphinx_rtd_theme"


from sphinx.util import i18n
"""
language = 'pl'  # Set the language to Polish
if language == 'pl':
    i18n.translations = {
        'note': 'Uwaga',
        'warning': 'Ostrzeżenie',
        'tip': 'Wskazówka',
        'important': 'Ważne',
        'caution': 'Ostrzeżenie',
        'danger': 'Niebezpieczeństwo',
        'admonition': 'Adnotacja',
        'hint': 'Wskazówka',
        'question': 'Pytanie'
    }
"""

language = 'en'  # Set the language to German
"""
language = 'de'  # Set the language to German
i18n.translations = {
    'note': 'Hinweis',
    'warning': 'Warnung',
    'tip': 'Tipp',
    'important': 'Wichtig',
    'caution': 'Vorsicht',
    'danger': 'Gefahr',
    'admonition': 'Ermahnung',
    'hint': 'Hinweis',
    'question': 'Frage'
}
"""


# sphinx-tags configuration
tags_create_tags = True
tags_list_template = 'tags.html'
tags_link_template = 'tags/%s.html'

extensions = [
    'sphinx_substitution_extensions',
    'sphinx.ext.ifconfig',
    'sphinx_jinja',
    'sphinx_tabs.tabs',
    'sphinx_favicon',
    'sphinx_tags',
    'nbsphinx',
    "sphinx_design",
    'sphinx_copybutton',

]

copybutton_prompt_text = r"^\s*(\$ |>>> |\.\.\. )"
copybutton_prompt_is_regexp = True
copybutton_add_css = False


# Optional: specify the path to Jupyter executable if it's not in your PATH
nbsphinx_execute = 'never'  # or 'always', 'auto', etc. depending on your needs

# Optional: configure other nbsphinx options
nbsphinx_allow_errors = True  # Continue processing if errors occur in notebooks

# Do not include tag files for translation
exclude_patterns = [
    "**/*.ipynb",
    "**/*.gpkg",
]


# >>> CF_BRAND_BLOCK: brand_registry
# creodias cloudferro_cloud wekeoelasticity wekeo eumetsat esahpc
# eolab_en eolab_de codede_en codede_de nsis_en nsis_pl dedl_central dedl_lumi ecis
BRAND = os.environ.get("BRAND", "ecis")

BRANDS = {

    "ecis": {
        "brand_name": "cloud environment",
        "brand_name_full": "EUMETSAT Cloud Infrastructure Service",
        "brand_name_hyphen": "Eumetsat-Elasticity",
        "brand_name_site_link": "https://horizon.cloudferro.com/auth/login/?next=/",
        "brand_name_site_auth_link": "https://my.cloud.eumetsat.int",
        "images_root_accounts": "",
        "images_root_billing": "ecis",
        "images_forgotten_password": "ecis",
        "images_registration": "ecis",
        "images_use_python_2fa": "ecis",
        "images_kubernetes_templates": "ecis",
        "project_name": "cloud_078649_2",
        "region_name": "fra1-3",
        "MK8s": "Managed Kubernetes",
        "mk8s_url": "mks.cloud.eumetsat.int/",
        "server_cert": "managed-kubernetes-cloudferro-com-chain.pem",
        "main_site_url": "https://eumetsat.int",
        "main_site_name": "Eumetsat",
        "images_cloud": "ecis",
        "images_datavolume": "ecis",
        "images_cuttingedge": "ecis",
        "images_eodata": "ecis",
        "images_networking": "ecis",
        "images_openstackcli": "ecis",
        "images_openstackdev": "ecis",
        "images_shares": "ecis",
        "images_windows": "ecis",
        "images_s3": "ecis",

        "horizon_interfaces": [
            {
                "label": "R1",
                "url": "https://horizon.api.r1.cloud.eumetsat.int/",
                "note": "",
            },
            {
                "label": "R2",
                "url": "https://horizon.api.r2.cloud.eumetsat.int/",
                "note": "",
            },
            {
                "label": "ELA",
                "url": "https://horizon.cloudferro.com/",
                "note": "Choose **ECIS** and **FRA1-3** as the region.",
            },
        ],
    },

}



brand_cfg = BRANDS[BRAND]

IMAGES_ACCOUNTS = f"{brand_cfg['images_root_accounts']}/"
IMAGES_BILLING  = f"{brand_cfg['images_root_billing']}/"
IMAGES_FORGOTTEN  = f"{brand_cfg['images_forgotten_password']}_"
IMAGES_REGISTRATION = f"{brand_cfg['images_registration']}_"
IMAGES_USE_PYTHON_2FA = f"{brand_cfg['images_use_python_2fa']}"
IMAGES_KUBERNETES_TEMPLATES = f"{brand_cfg['images_kubernetes_templates']}"
IMAGES_MK8S_PREFIX = f"{BRAND}_"
IMAGES_CLOUD_PREFIX = f"{brand_cfg['images_cloud']}_"
IMAGES_DATAVOLUME_PREFIX = f"{brand_cfg['images_datavolume']}_"
IMAGES_CUTTINGEDGE_PREFIX = f"{brand_cfg['images_cuttingedge']}_"
IMAGES_EODATA_PREFIX = f"{brand_cfg['images_eodata']}_"
IMAGES_NETWORKING_PREFIX = f"{brand_cfg['images_networking']}_"
IMAGES_OPENSTACKCLI_PREFIX = f"{brand_cfg['images_openstackcli']}_"
IMAGES_OPENSTACKDEV_PREFIX = f"{brand_cfg['images_openstackdev']}_"
IMAGES_SHARES_PREFIX = f"{brand_cfg['images_shares']}_"
IMAGES_WINDOWS_PREFIX = f"{brand_cfg['images_windows']}_"
IMAGES_S3_PREFIX = f"{brand_cfg['images_s3']}_"

project = brand_cfg["brand_name"]

rst_prolog = f"""
.. |brand-name| replace:: {brand_cfg["brand_name"]}
.. |brand-name-full| replace:: {brand_cfg["brand_name_full"]}
.. |brand-name-hyphen| replace:: {brand_cfg["brand_name_hyphen"]}
.. |brand-name-site-link| replace:: {brand_cfg["brand_name_site_link"]}
.. |brand-name-site-auth-link| replace:: {brand_cfg["brand_name_site_auth_link"]}

.. |cloud-name| replace:: {brand_cfg["brand_name"]}
.. |brand-name-support-en| replace:: https://www.eumetsat.int/contact-us
.. |brand-name-support-de| replace:: https://www.eumetsat.int/contact-us
.. |datahub-address| replace:: datahub.code-de.org
.. |explorer| replace:: https://explore.creodias.eu
.. |finder| replace:: https://finder.creodias.eu/www/
.. |eodata-network| replace:: eodata
.. include:: <s5defs.txt>
.. |brand-name-security-groups| replace:: https://horizon.cloudferro.com/project/security_groups/
.. |JupyterLab| replace:: https://jupyterhub-creodias.apps.acronix.intra.cloudferro.com/
.. |MK8s| replace:: {brand_cfg["MK8s"]}
"""


mk8s_url = "https://" + brand_cfg["mk8s_url"]
brand_name = brand_cfg["brand_name"]
# brand_name = 'NSIS Cloud'
# brand_name = 'CloudFerro Cloud'
cloud_name = ''
show_leonardo = 'yes'

# <<< CF_BRAND_BLOCK: brand_registry

language = 'en'
locale_dirs = ['locale/']

# >>> CF_BRAND_BLOCK: regional_clouds
# ---------------------------------------------------------------------------
# Regional cloud configuration
# ---------------------------------------------------------------------------
# Keep region-specific URLs here, not inside articles.  Articles should render
# tabs and code blocks from the ``regional_clouds`` Jinja context below.

COMMON_CLOUDFERRO_REGIONS = {
    "WAW4-1": {
        "display_name": "WAW4-1",
        "internal_name": "waw4-1",
        "slug": "waw4-1",
        "identity_endpoint": "",
        "keystone_endpoint": "https://keystone.cloudferro.com:5000",
        "horizon_endpoint": "https://horizon.cloudferro.com",
        "s3_endpoint": "https://s3.waw4-1.cloudferro.com",
        "eodata_endpoint": "https://eodata.cloudferro.com",
        "s3cmd_region": "RegionOne",
        "eodata_bucket": "eodata",
        "eodata_use_https": True,
    },
    "WAW3-1": {
        "display_name": "WAW3-1",
        "internal_name": "waw3-1",
        "slug": "waw3-1",
        "identity_endpoint": "",
        "keystone_endpoint": "https://keystone.cloudferro.com:5000",
        "horizon_endpoint": "https://horizon.cloudferro.com",
        "s3_endpoint": "https://s3.waw3-1.cloudferro.com",
        "eodata_endpoint": "http://data.cloudferro.com",
        "s3cmd_region": "US",
        "eodata_bucket": "eodata",
        "eodata_use_https": False,
    },
    "WAW3-2": {
        "display_name": "WAW3-2",
        "internal_name": "waw3-2",
        "slug": "waw3-2",
        "identity_endpoint": "",
        "keystone_endpoint": "https://keystone.cloudferro.com:5000",
        "horizon_endpoint": "https://horizon.cloudferro.com",
        "s3_endpoint": "https://s3.waw3-2.cloudferro.com",
        "eodata_endpoint": "https://eodata.cloudferro.com",
        "s3cmd_region": "RegionOne",
        "eodata_bucket": "eodata",
        "eodata_use_https": True,
    },
    "FRA1-2": {
        "display_name": "FRA1-2",
        "internal_name": "fra1-2",
        "slug": "fra1-2",
        "identity_endpoint": "",
        "keystone_endpoint": "https://keystone.cloudferro.com:5000",
        "horizon_endpoint": "https://horizon.cloudferro.com",
        "s3_endpoint": "https://s3.fra1-2.cloudferro.com",
        "eodata_endpoint": "https://eodata.cloudferro.com",
        "s3cmd_region": "RegionOne",
        "eodata_bucket": "eodata",
        "eodata_use_https": True,
    },
    "FRA1-3": {
        "display_name": "FRA1-3",
        "internal_name": "fra1-3",
        "slug": "fra1-3",
        "identity_endpoint": "",
        "keystone_endpoint": "https://keystone.cloudferro.com:5000",
        "horizon_endpoint": "https://horizon.cloudferro.com",
        "s3_endpoint": "https://s3.fra1-3.cloudferro.com",
        "eodata_endpoint": "https://eodata.cloudferro.com",
        "s3cmd_region": "RegionOne",
        "eodata_bucket": "eodata",
        "eodata_use_https": True,
    },
    "LCJ1-1": {
        "display_name": "LCJ1-1",
        "internal_name": "lcj1-1",
        "slug": "lcj1-1",
        "identity_endpoint": "",
        "keystone_endpoint": "https://keystone.cloudferro.com:5000",
        "horizon_endpoint": "https://horizon.cloudferro.com",
        "s3_endpoint": "https://s3.lcj1-1.cloudferro.com",
        "eodata_endpoint": "https://eodata.cloudferro.com",
        "s3cmd_region": "RegionOne",
        "eodata_bucket": "eodata",
        "eodata_use_https": True,
    },
}

ECIS_REGIONS = {
    # ECIS FRA1-3 is also referred to as ELA in endpoint hostnames.
    "FRA1-3": {
        "display_name": "FRA1-3",
        "internal_name": "ela",
        "slug": "fra1-3",
        "identity_endpoint": "https://identity.ela.cloud.eumetsat.int/auth/realms/ECIS/.well-known/openid-configuration",
        "keystone_endpoint": "https://keystone.cloudferro.com:5000",
        "horizon_endpoint": "https://horizon.cloudferro.com",
        "s3_endpoint": "https://s3.fra1-3.cloudferro.com",
        "eodata_endpoint": "https://eodata.cloudferro.com",
        "s3cmd_region": "RegionOne",
        "eodata_bucket": "eodata",
        "eodata_use_https": True,
    },
    "R1": {
        "display_name": "R1",
        "internal_name": "r1",
        "slug": "r1",
        "identity_endpoint": "https://identity.r1.cloud.eumetsat.int/auth/realms/ECIS/.well-known/openid-configuration",
        "keystone_endpoint": "https://keystone.api.r1.cloud.eumetsat.int",
        "horizon_endpoint": "https://horizon.api.r1.cloud.eumetsat.int",
        "s3_endpoint": "https://s3.r1.cloud.eumetsat.int",
        "eodata_endpoint": "https://s3.r1.cloud.eumetsat.int",
        "s3cmd_region": "RegionOne",
        "eodata_bucket": "eodata",
        "eodata_use_https": True,
    },
    "R2": {
        "display_name": "R2",
        "internal_name": "r2",
        "slug": "r2",
        "identity_endpoint": "https://identity.r2.cloud.eumetsat.int/auth/realms/ECIS/.well-known/openid-configuration",
        "keystone_endpoint": "https://keystone.api.r2.cloud.eumetsat.int",
        "horizon_endpoint": "https://horizon.api.r2.cloud.eumetsat.int",
        "s3_endpoint": "https://s3.r2.cloud.eumetsat.int",
        "eodata_endpoint": "https://s3.r2.cloud.eumetsat.int",
        "s3cmd_region": "RegionOne",
        "eodata_bucket": "eodata",
        "eodata_use_https": True,
    },
}

BRAND_REGIONS = {
    "creodias": ["WAW4-1", "WAW3-1", "WAW3-2", "FRA1-2", "FRA1-3", "LCJ1-1"],
    "cloudferro_cloud": ["WAW4-1", "WAW3-1", "WAW3-2", "FRA1-2", "FRA1-3", "LCJ1-1"],
    "wekeo": ["WAW4-1", "WAW3-1", "WAW3-2", "FRA1-2", "FRA1-3", "LCJ1-1"],
    "wekeoelasticity": ["WAW4-1", "WAW3-1", "WAW3-2", "FRA1-2", "FRA1-3", "LCJ1-1"],
    "ecis": ["R1", "R2", "FRA1-3" ],
    "nsis_en": ["WAW4-1"],
    "codede_en": ["FRA1-3"],
    "esahpc": ["EOHPC"],
}

# ---------------------------------------------------------------------------
# Managed Kubernetes regions and programmatic endpoints
# ---------------------------------------------------------------------------
#
# COMMON_CLOUDFERRO_REGIONS and ECIS_REGIONS remain the general cloud/region
# registries. They describe Horizon, Keystone, S3, EODATA and similar services.
#
# The structures below describe where Managed Kubernetes is available and how
# to build MK8s-specific API, Swagger and Terraform endpoints.

MK8S_REGIONS_BY_BRAND = {
    "creodias": ["LCJ1-1", "FRA1-3"],
    "cloudferro_cloud": ["LCJ1-1", "FRA1-3"],

    # ECIS shows FRA1-3 to users, but the ECIS FRA1-3 MK8s endpoint uses
    # the ELA hostname.
    "ecis": ["R1", "R2", "FRA1-3"],

    # CODE-DE / CODE-DE Lab variants. These keys are harmless if some of
    # them are not currently used by this repository.
    "codede_lab": ["FRA1-3"],
    "code_de_lab": ["FRA1-3"],
    "codede_en": ["FRA1-3"],
    "codede_de": ["FRA1-3"],

    # DEDL variants. Endpoint hostnames are intentionally kept separate below
    # and should be enabled only after they are confirmed.
    "dedl": ["CENTRAL", "LUMI", "LEONARDO", "MARENOSTRUM", "EUMETSAT"],
    "dedl_central": ["CENTRAL", "LUMI", "LEONARDO", "MARENOSTRUM", "EUMETSAT"],
    "dedl_lumi": ["CENTRAL", "LUMI", "LEONARDO", "MARENOSTRUM", "EUMETSAT"],
    "dedl_leonardo": ["CENTRAL", "LUMI", "LEONARDO", "MARENOSTRUM", "EUMETSAT"],
    "dedl_marenostrum": ["CENTRAL", "LUMI", "LEONARDO", "MARENOSTRUM", "EUMETSAT"],
    "dedl_eumetsat": ["CENTRAL", "LUMI", "LEONARDO", "MARENOSTRUM", "EUMETSAT"],
}


COMMON_CLOUDFERRO_MK8S_ENDPOINTS = {
    "LCJ1-1": "managed-kubernetes.lcj1-1.cloudferro.com",
    "FRA1-3": "managed-kubernetes.fra1-3.cloudferro.com",
}


ECIS_MK8S_ENDPOINTS = {
    "R1": "mks.r1.cloud.eumetsat.int",
    "R2": "mks.r2.cloud.eumetsat.int",
    "FRA1-3": "mks.ela.cloud.eumetsat.int",
}


# Fill this dictionary only after DEDL MK8s endpoint hostnames are confirmed.
DEDL_MK8S_ENDPOINTS = {
    # "CENTRAL": "TO_BE_CONFIRMED",
    # "LUMI": "TO_BE_CONFIRMED",
    # "LEONARDO": "TO_BE_CONFIRMED",
    # "MARENOSTRUM": "TO_BE_CONFIRMED",
    # "EUMETSAT": "TO_BE_CONFIRMED",
}


DEDL_REGION_STUBS = {
    "CENTRAL": {
        "display_name": "CENTRAL",
        "internal_name": "central",
        "slug": "central",
    },
    "LUMI": {
        "display_name": "LUMI",
        "internal_name": "lumi",
        "slug": "lumi",
    },
    "LEONARDO": {
        "display_name": "LEONARDO",
        "internal_name": "leonardo",
        "slug": "leonardo",
    },
    "MARENOSTRUM": {
        "display_name": "MARENOSTRUM",
        "internal_name": "marenostrum",
        "slug": "marenostrum",
    },
    "EUMETSAT": {
        "display_name": "EUMETSAT",
        "internal_name": "eumetsat",
        "slug": "eumetsat",
    },
}


def get_mk8s_base_regions_for_brand(brand_key):
    if brand_key == "ecis":
        return ECIS_REGIONS

    if brand_key.startswith("dedl"):
        return DEDL_REGION_STUBS

    return COMMON_CLOUDFERRO_REGIONS


def get_mk8s_endpoint_hosts_for_brand(brand_key):
    if brand_key == "ecis":
        return ECIS_MK8S_ENDPOINTS

    if brand_key.startswith("dedl"):
        return DEDL_MK8S_ENDPOINTS

    return COMMON_CLOUDFERRO_MK8S_ENDPOINTS


def build_mk8s_region(region_name, base_regions, endpoint_hosts):
    base = base_regions.get(region_name, {}).copy()

    if not base:
        base = {
            "display_name": region_name,
            "internal_name": region_name.lower(),
            "slug": region_name.lower().replace("_", "-"),
        }

    host = endpoint_hosts.get(region_name, "").strip()

    base["mk8s_available"] = bool(host)
    base["mk8s_host"] = host

    if host:
        base["mk8s_api_url"] = f"https://{host}/api/v1"
        base["mk8s_swagger_url"] = f"https://{host}/swagger"
        base["mk8s_terraform_endpoint"] = f"{host}:443"
    else:
        base["mk8s_api_url"] = ""
        base["mk8s_swagger_url"] = ""
        base["mk8s_terraform_endpoint"] = ""

    return base


current_mk8s_region_names = MK8S_REGIONS_BY_BRAND.get(BRAND, [])
current_mk8s_base_regions = get_mk8s_base_regions_for_brand(BRAND)
current_mk8s_endpoint_hosts = get_mk8s_endpoint_hosts_for_brand(BRAND)

current_mk8s_regions = [
    build_mk8s_region(
        region_name,
        current_mk8s_base_regions,
        current_mk8s_endpoint_hosts,
    )
    for region_name in current_mk8s_region_names
]

current_active_mk8s_regions = [
    region for region in current_mk8s_regions
    if region.get("mk8s_available")
]

# <<< CF_BRAND_BLOCK: regional_clouds


# >>> CF_BRAND_BLOCK: doc_links_and_region_helpers
# ---------------------------------------------------------------------------
# Brand-specific documentation links
# ---------------------------------------------------------------------------
DEFAULT_DOC_LINKS = {
    "object_storage": "/s3/How-to-use-Object-Storage-on-{brand_name_hyphen}",
    "s3cmd_install": "/s3/How-to-install-s3cmd-on-Linux-on-{brand_name_hyphen}",
    "s3cmd_access": "/s3/How-to-access-object-storage-from-{brand_name_hyphen}-using-s3cmd",
    "s3cmd_config": "/s3/Configuration-files-for-s3cmd-command-on-{brand_name_hyphen}",
    "bucket_policy": "/s3/Bucket-sharing-using-s3-bucket-policy-on-{brand_name_hyphen}",
    "boto3_access": "/s3/How-to-access-object-storage-from-{brand_name_hyphen}-using-boto3",
    "boto3_windows": "/s3/How-To-Install-boto3-In-Windows-on-{brand_name_hyphen}",

    "ec2_credentials": "/cloud/How-to-generate-ec2-credentials-on-{brand_name_hyphen}",
    "linux_vm_from_windows": "/cloud/How-to-create-a-Linux-VM-and-access-it-from-Windows-desktop-on-{brand_name_hyphen}",
    "linux_vm_from_linux": "/cloud/How-to-create-a-Linux-VM-and-access-it-from-Linux-command-line-on-{brand_name_hyphen}",

    "eodata_s3cmd_access": "/eodata/How-to-access-EODATA-using-s3cmd-on-{brand_name_hyphen}",
    "eodata_boto3_access": "/eodata/How-to-access-EODATA-using-boto3-on-{brand_name_hyphen}",

    "openstackclient_windows": "/openstackcli/How-to-install-OpenStackClient-GitBash-or-Cygwin-for-Windows-on-{brand_name_hyphen}",
    "slurm_mpi_workflow": "/cuttingedge/Sample-Workflow-Running-EO-Processing-MPI-jobs-on-a-SLURM-cluster-on-{brand_name_hyphen}-Cloud",
    "eodata_s3fs_mount": "/eodata/How-to-mount-eodata-using-S3FS-in-Linux-on-{brand_name_hyphen}",

    "openstackclient_windows_wsl": "/openstackcli/How-to-install-OpenStackClient-on-Windows-using-Windows-Subsystem-for-Linux-on-{brand_name_hyphen}-OpenStack-Hosting",
    "object_storage_windows_vm_mount": "/networking/How-to-mount-object-storage-container-as-file-system-on-Windows-VM-on-{brand_name_hyphen}",
    "s3fs_linux_mount": "/s3/How-to-mount-object-storage-container-as-a-file-system-in-Linux-using-s3fs-on-{brand_name_hyphen}",
    "s3_private_access": "",
    "remote_transfer_eodata": "",

    # Internal OpenStack CLI authentication variants.
    # Articles should use only ``openstack_cli_auth``.
    "openstack_cli_auth_standard": "/accountmanagement/How-to-activate-OpenStack-CLI-access-to-{brand_name_hyphen}-cloud",
    "openstack_cli_auth_2fa": "/accountmanagement/How-to-activate-OpenStack-CLI-access-to-{brand_name_hyphen}-cloud-using-one-or-two-factor-authentication",
    "openstack_cli_auth_wekeo": "/accountmanagement/How-to-activate-OpenStack-CLI-access-to-WEkEO-cloud-using-Federated-IDP-authorization-and-application-credentials",
    "start_vm_from_snapshot_cli": "/openstackcli/How-to-start-a-VM-from-instance-snapshot-using-OpenStack-CLI-on-{brand_name_hyphen}",
    "bootable_vs_nonbootable_volumes": "/datavolume/Bootable-versus-non-bootable-volumes-on-{brand_name_hyphen}",
    "instance_migration_cli": "/networking/OpenStack-instance-migrationcommand-line-on-{brand_name_hyphen}",

    "object_storage_windows_mount": "/s3/How-to-mount-object-storage-container-from-{brand_name_hyphen}-as-file-system-on-local-Windows-computer",

    "openstack_object_storage_cli": "/openstackcli/How-to-access-object-storage-using-OpenStack-CLI-on-{brand_name_hyphen}",
    "linux_vm_horizon": "/cloud/How-to-create-new-Linux-VM-in-OpenStack-Dashboard-Horizon-on-{brand_name_hyphen}",
    "windows_vm_horizon": "/cloud/How-to-create-Windows-VM-on-OpenStack-Horizon-and-access-it-via-web-console-on-{brand_name_hyphen}",
    "ephemeral_vs_persistent": "/datavolume/Ephemeral-vs-Persistent-storage-option-Create-New-Volume-on-{brand_name_hyphen}",
    "application_credentials_cli": "/cloud/How-to-generate-or-use-Application-Credentials-via-CLI-on-{brand_name_hyphen}",
    "create_vm_cli": "/cloud/How-to-create-a-VM-using-the-OpenStack-CLI-client-on-{brand_name_hyphen}-cloud",
    "instance_snapshot_horizon": "/cloud/How-to-create-instance-snapshot-using-Horizon-on-{brand_name_hyphen}",
    "backup_command_rotating": "/openstackcli/Use-backup-command-to-create-rotating-backups-of-virtual-machines-on-{brand_name_hyphen}",
    "backup_script_rotating": "/openstackcli/Use-script-to-create-daily-weekly-and-monthly-rotating-backups-of-virtual-machines-using-on-{brand_name_hyphen}",
    "backup_instance_download": "/openstackcli/How-to-backup-an-instance-and-download-it-to-the-desktop-on-{brand_name_hyphen}",
    "eodata_windows_vm_mount": "/eodata/How-to-mount-eodata-on-Windows-virtual-machine-on-{brand_name_hyphen}-hosting",
    "windows_vm_rdp_bastion": "/windows/Connecting-to-a-Windows-VM-via-RDP-through-a-Linux-bastion-host-port-forwarding-on-{brand_name_hyphen}",
    "security_groups_horizon": "/cloud/How-to-use-Security-Groups-in-Horizon-on-{brand_name_hyphen}",
    "python_virtualenv": "/cloud/How-to-install-Python-virtualenv-or-virtualenvwrapper-on-{brand_name_hyphen}",
    "move_volume_between_vms_horizon": "/datavolume/How-to-move-data-volume-between-two-VMs-using-OpenStack-Horizon-on-{brand_name_hyphen}",
    "transfer_volume_cli": "/openstackcli/How-to-transfer-volumes-between-domains-and-projects-using-OpenStack-CLI-client-on-{brand_name_hyphen}",
    "openstack_user_roles": "/cloud/OpenStack-user-roles-on-{brand_name_hyphen}",
    "openstackclient_linux": "/openstackcli/How-to-install-OpenStackClient-for-Linux-on-{brand_name_hyphen}",
    "heat_create_vms": "/openstackcli/How-to-create-a-set-of-VMs-using-OpenStack-Heat-Orchestration-on-{brand_name_hyphen}",
    "terraform_keycloak_auth": "/openstackdev/Generating-and-authorizing-Terraform-using-Keycloak-user-on-{brand_name_hyphen}",
    "custom_image_upload_cli": "/cloud/How-to-upload-your-custom-image-using-OpenStack-CLI-on-{brand_name_hyphen}",
    "create_vm_cli_cloud": "/cloud/How-to-create-a-VM-using-the-OpenStack-CLI-client-on-{brand_name_hyphen}-cloud",
    "magnum_kubernetes_cli": "/kubernetes/How-To-Use-Command-Line-Interface-for-Kubernetes-Clusters-On-{brand_name_hyphen}-OpenStack-Magnum",
    "instance_snapshot_cli": "/openstackcli/How-to-create-instance-snapshot-using-OpenStack-CLI-on-{brand_name_hyphen}",
    "add_ssh_key_horizon": "/networking/How-to-add-SSH-key-from-Horizon-web-console-on-{brand_name_hyphen}",
    "forgot_ssh_key_vm": "/networking/What-If-I-Forgot-To-Add-The-SSH-Key-To-My-VM-Or-Deleted-It-{brand_name_hyphen}",
    "access_vm_console": "/cloud/How-to-access-the-VM-from-OpenStack-console-on-{brand_name_hyphen}",
    "start_vm_from_snapshot_horizon": "/cloud/How-to-start-a-VM-from-instance-snapshot-using-Horizon-dashboard-on-{brand_name_hyphen}",
    "delete_all_project_resources_cli": "/networking/How-to-correctly-delete-all-the-resources-in-the-project-via-OpenStack-commandline-Clients-on-{brand_name_hyphen}",
    "volume_snapshot_create_delete": "/datavolume/How-to-create-or-delete-volume-snapshot-on-{brand_name_hyphen}",
    "transfer_volume_horizon": "/cloud/How-to-transfer-volumes-between-domains-and-projects-using-Horizon-dashboard-on-{brand_name_hyphen}",
    "vm_status_power_state_billing": "/cloud/Status-Power-State-and-dependences-in-billing-of-instances-VMs-on-{brand_name_hyphen}",
    "openstack_magnum_clients_cli": "/kubernetes/How-To-Install-OpenStack-and-Magnum-Clients-for-Command-Line-Interface-to-{brand_name_hyphen}-Horizon",

}


BRAND_DOC_LINK_OVERRIDES = {
    "ecis": {
        "ec2_credentials": "/accountmanagement/S3-keys/S3-keys",
        "magnum_kubernetes_cli": None,
        "object_storage": "/s3/Deep-dive-into-using-s3cmd-to-access-object-storage-on-{brand_name_hyphen}",


        # Add ECIS-specific alternatives here when those pages exist
        # or when the generic /cloud/... article is not present in ECIS.
        #
        # "linux_vm_from_windows": "/accountmanagement/...",
        # "linux_vm_from_linux": "/accountmanagement/...",
        # "python_virtualenv": "/...",
        # "boto3_windows": "/...",
        # "eodata_boto3_access": "/...",
        # "s3cmd_access": "/...",
    },
}


def build_doc_links(brand_key, brand_context):
    """
    Build brand-aware document links.

    DEFAULT_DOC_LINKS contains the normal links.
    BRAND_DOC_LINK_OVERRIDES can replace a link for a specific brand.
    If an override value is None, the link is intentionally disabled.

    The canonical article-facing OpenStack CLI authentication link is
    ``openstack_cli_auth``. Articles should not choose between standard,
    2FA, and WEkEO variants themselves.
    """
    links = dict(DEFAULT_DOC_LINKS)
    links.update(BRAND_DOC_LINK_OVERRIDES.get(brand_key, {}))

    brand_name = brand_context.get("brand_name", "")

    if brand_name == "WEkEO":
        links["openstack_cli_auth"] = links["openstack_cli_auth_wekeo"]
    elif brand_name in TWO_FA_ACTIVATED_BRANDS:
        links["openstack_cli_auth"] = links["openstack_cli_auth_2fa"]
    else:
        links["openstack_cli_auth"] = links["openstack_cli_auth_standard"]

    resolved = {}

    for key, value in links.items():
        if value is None:
            resolved[key] = None
        else:
            resolved[key] = value.format(**brand_context)

    return resolved

def normalize_doc_link_target(target):
    """
    Convert flat Sphinx document paths to folder-style paths when the
    folder-style .rst file exists locally.

    Example:
    /windows/How-to-access-a-VM-from-Windows-PuTTY-on-Eumetsat-Elasticity

    becomes:
    /windows/How-to-access-a-VM-from-Windows-PuTTY-on-Eumetsat-Elasticity/How-to-access-a-VM-from-Windows-PuTTY-on-Eumetsat-Elasticity

    Already-correct folder-style paths are left unchanged.
    External links, empty values and None are left unchanged.
    """
    if not target:
        return target

    if not isinstance(target, str):
        return target

    if target.startswith(("http://", "https://", "mailto:")):
        return target

    if not target.startswith("/"):
        return target

    clean = target.strip()
    parts = clean.strip("/").split("/")

    if len(parts) < 2:
        return target

    if len(parts) >= 3 and parts[-1] == parts[-2]:
        return target

    candidate = Path(__file__).parent / clean.strip("/") / f"{parts[-1]}.rst"

    if candidate.exists():
        return clean + "/" + parts[-1]

    return target


def normalize_doc_links(doc_links):
    for key, value in list(doc_links.items()):
        doc_links[key] = normalize_doc_link_target(value)
    return doc_links

def normalize_rst_prolog_doc_targets(text):
    """
    Normalize flat :doc: targets inside rst_prolog.

    Supports both forms:

    :doc:`/section/article`
    :doc:`Visible title </section/article>`

    This is needed because rst_prolog is created before doc_links, so
    normalizing doc_links alone does not affect :doc: substitutions already
    written into rst_prolog.
    """
    import re

    def normalize_bare_doc(match):
        target = match.group(1)
        normalized = normalize_doc_link_target(target)
        return f":doc:`{normalized}`"

    def normalize_titled_doc(match):
        title = match.group(1)
        target = match.group(2)
        normalized = normalize_doc_link_target(target)
        return f":doc:`{title} <{normalized}>`"

    # First normalize titled doc links:
    # :doc:`Visible title </section/article>`
    text = re.sub(
        r":doc:`([^`<>]+?)\s+<(/[^`<>]+)>`",
        normalize_titled_doc,
        text,
    )

    # Then normalize bare doc links:
    # :doc:`/section/article`
    text = re.sub(
        r":doc:`(/[^`<>]+)`",
        normalize_bare_doc,
        text,
    )

    return text


doc_links = normalize_doc_links(build_doc_links(BRAND, brand_cfg))
rst_prolog = normalize_rst_prolog_doc_targets(rst_prolog)


def strip_url_scheme(url):
    return url.replace("https://", "").replace("http://", "").rstrip("/")


def get_region_catalog_for_brand(brand_key):
    if brand_key == "ecis":
        return ECIS_REGIONS
    return COMMON_CLOUDFERRO_REGIONS


def get_brand_regions(brand_key):
    region_catalog = get_region_catalog_for_brand(brand_key)
    region_names = BRAND_REGIONS.get(brand_key, [])

    return [
        region_catalog[region_name]
        for region_name in region_names
        if region_name in region_catalog
    ]


def build_s3cmd_eodata_config(region):
    host_base = strip_url_scheme(region["eodata_endpoint"])

    return f"""[default]
access_key = ACCESS_KEY
secret_key = SECRET_KEY
host_base = {host_base}
host_bucket = {host_base}
bucket_location = {region["s3cmd_region"]}
use_https = {str(region["eodata_use_https"])}
"""


def build_s3cmd_object_storage_config(region):
    host_base = strip_url_scheme(region["s3_endpoint"])

    return f"""[default]
access_key = ACCESS_KEY
secret_key = SECRET_KEY
host_base = {host_base}
host_bucket = {host_base}
bucket_location = {region["s3cmd_region"]}
use_https = True
"""


def build_openrc_endpoint_block(region):
    return f"""export OS_AUTH_URL={region["keystone_endpoint"]}
export OS_INTERFACE=public
export OS_IDENTITY_API_VERSION=3
"""


def build_eodata_mount_config(region):
    return f"""[EODATA]
type = s3
provider = Other
access_key_id = CLOUDFERRO
secret_access_key = PUBLIC
endpoint = {region["eodata_endpoint"]}
"""


def enrich_region(region):
    enriched = dict(region)
    enriched["s3_host"] = strip_url_scheme(region["s3_endpoint"])
    enriched["eodata_host"] = strip_url_scheme(region["eodata_endpoint"])
    enriched["keystone_v3_endpoint"] = region["keystone_endpoint"].rstrip("/") + "/v3"
    enriched["s3cmd_eodata_config"] = build_s3cmd_eodata_config(region)
    enriched["s3cmd_object_storage_config"] = build_s3cmd_object_storage_config(region)
    enriched["openrc_endpoint_block"] = build_openrc_endpoint_block(region)
    enriched["eodata_mount_config"] = build_eodata_mount_config(region)
    return enriched


current_brand_regions = [
    enrich_region(region)
    for region in get_brand_regions(BRAND)
]
current_default_region = current_brand_regions[0] if current_brand_regions else None
current_brand_is_multi_cloud = brand_cfg["brand_name"] in [
    "Creodias",
    "CloudFerro Cloud",
    "WEkEO",
    "WEkEO Elasticity",
    "ECIS",
]

# DEDL / HDA MCP article endpoints
#
# The three endpoint values must belong to the same DEDL environment.
# Do not mix an identity endpoint from one environment with HDA or MCP
# endpoints from another environment.
#
# For local staging work, export all three variables before running
# sphinx-build:
#
#   export DEDL_IDENTITY_URL="https://identity.central.staging.data.destination-earth.eu/auth/realms/dedl/protocol/openid-connect/token"
#   export DEDL_HDA_URL="REAL_STAGING_HDA_BASE_URL"
#   export DEDL_MCP_URL="REAL_STAGING_MCP_SERVER_URL"
#
# Production defaults are kept only as safe defaults for published builds.

dedl_hda_mcp_context = {
    "dedl_identity_token_url": os.environ.get(
        "DEDL_IDENTITY_URL",
        "https://identity.data.destination-earth.eu/auth/realms/dedl/protocol/openid-connect/token",
    ),
    "dedl_hda_base_url": os.environ.get(
        "DEDL_HDA_URL",
        "https://hda.data.destination-earth.eu",
    ),
    "dedl_mcp_server_url": os.environ.get(
        "DEDL_MCP_URL",
        "https://mcp.data.destination-earth.eu/mcp",
    ),
}


# Backwards-compatible names for older articles that already used these values.
# New articles should prefer the ``regional_clouds`` Jinja context.
region_map = {
    BRANDS[brand_key]["brand_name"]: region_names
    for brand_key, region_names in BRAND_REGIONS.items()
    if brand_key in BRANDS
}
endpoint_urls = {
    region["display_name"]: region["eodata_endpoint"]
    for region in current_brand_regions
}
tab_config_sections = {
    region["display_name"]: region["eodata_mount_config"]
    for region in current_brand_regions
}
tab_endpoint_urls = dict(endpoint_urls)

# <<< CF_BRAND_BLOCK: doc_links_and_region_helpers


# >>> CF_BRAND_BLOCK: jinja_contexts
# Images that change from brand to brand
jinja_contexts = {

      'vm_from_windows_putty': {
            'no_1': f"01_{brand_cfg['images_registration']}.png",

             },

      'special_eodata_rebranding': {
            'special_eodata_1': 'special_eodata_menu.png',
            'special_eodata_2': 'download_special_eodata_rc_file.png',
            'special_eodata_3': 'special_eodata_rc_file_content.png',
            'special_eodata_4': 'activate-api-2fa-01_creodias.png',
            'special_eodata_5': 'flavor_list_2fa_short.png',

             },



    "s3_images": {
        "shares001": IMAGES_S3_PREFIX + "allow-share-access-01.png",
        "s3001": IMAGES_S3_PREFIX + "boto1.png",
        "s3002": IMAGES_S3_PREFIX + "boto2.png",
        "s3003": IMAGES_S3_PREFIX + "boto3.png",
        "s3004": IMAGES_S3_PREFIX + "boto4.png",
        "s3005": IMAGES_S3_PREFIX + "code-structure.png",
        "s3006": IMAGES_S3_PREFIX + "boto3-upload-file-to-s3.png",
        "s3007": IMAGES_S3_PREFIX + "install-s3cmd-linux-01-creodias.png",
        "s3008": IMAGES_S3_PREFIX + "install-s3cmd-linux-02-creodias.png",
        "s3009": IMAGES_S3_PREFIX + "mount-object-storage-s3fs-linux-06-creodias.png",
        "s3010": IMAGES_S3_PREFIX + "mount-object-storage-s3fs-linux-03-creodias.png",
        "s3011": IMAGES_S3_PREFIX + "mount-object-storage-s3fs-linux-04-creodias.png",
        "s3012": IMAGES_S3_PREFIX + "mount-object-storage-s3fs-linux-05-creodias.png",
        "s3013": IMAGES_S3_PREFIX + "object-storage-windows-example1-creodias.png",
        "s3014": IMAGES_S3_PREFIX + "mount-eodata-windows-open-03-creodias.png",
        "s3015": IMAGES_S3_PREFIX + "mount-eodata-windows-open-04-creodias.png",
        "s3016": IMAGES_S3_PREFIX + "mount-eodata-windows-open-05-creodias.png",
        "s3017": IMAGES_S3_PREFIX + "mount-eodata-windows-open-06-creodias.png",
        "s3018": IMAGES_S3_PREFIX + "mount-eodata-windows-open-07-creodias.png",
        "s3019": IMAGES_S3_PREFIX + "mount-eodata-windows-open-10-creodias.png",
        "s3020": IMAGES_S3_PREFIX + "mount-eodata-windows-open-11-creodias.png",
        "s3021": IMAGES_S3_PREFIX + "mount-eodata-windows-open-12-creodias.png",
        "s3022": IMAGES_S3_PREFIX + "mount-eodata-windows-rclone-01-creodias.png",
        "s3023": IMAGES_S3_PREFIX + "mount-eodata-windows-rclone-02-creodias.png",
        "s3024": IMAGES_S3_PREFIX + "mount-eodata-windows-open-nssm-01-creodias.png",
        "s3025": IMAGES_S3_PREFIX + "mount-eodata-windows-open-13-creodias.png",
        "s3026": IMAGES_S3_PREFIX + "mount-object-storage-windows-horizon-01-creodias.png",
        "s3027": IMAGES_S3_PREFIX + "mount-eodata-windows-open-remove-01-creodias.png",
        "s3028": IMAGES_S3_PREFIX + "mount-eodata-windows-open-remove-03-creodias.png",
        "s3029": IMAGES_S3_PREFIX + "mount-eodata-windows-open-remove-04-creodias.png",
        "s3030": IMAGES_S3_PREFIX + "mount-eodata-windows-open-remove-05-creodias.png",
        "s3031": IMAGES_S3_PREFIX + "mount-eodata-windows-open-remove-06-creodias.png",
        "s3032": IMAGES_S3_PREFIX + "mount-eodata-windows-open-remove-07-creodias.png",
        "s3033": IMAGES_S3_PREFIX + "mount-eodata-windows-open-remove-08-creodias.png",
        "s3034": IMAGES_S3_PREFIX + "use-object-storage-01-creodias.png",
        "s3035": IMAGES_S3_PREFIX + "use-object-storage-02-creodias.png",
        "s3036": IMAGES_S3_PREFIX + "use-object-storage-03-creodias.png",
        "s3037": IMAGES_S3_PREFIX + "use-object-storage-04-creodias.png",
        "s3038": IMAGES_S3_PREFIX + "use-object-storage-05-creodias.png",
        "s3039": IMAGES_S3_PREFIX + "use-object-storage-06-creodias.png",
        "s3040": IMAGES_S3_PREFIX + "use-object-storage-07-creodias.png",
        "s3041": IMAGES_S3_PREFIX + "use-object-storage-08-creodias.png",
        "s3042": IMAGES_S3_PREFIX + "use-object-storage-09-creodias.png",
        "s3043": IMAGES_S3_PREFIX + "use-object-storage-success-creodias.png",
        "s3044": IMAGES_S3_PREFIX + "use-object-storage-10-creodias.png",
        "s3045": IMAGES_S3_PREFIX + "use-object-storage-16-creodias.png",
        "s3046": IMAGES_S3_PREFIX + "use-object-storage-17-creodias.png",
        "s3047": IMAGES_S3_PREFIX + "use-object-storage-18-creodias.png",
        "s3048": IMAGES_S3_PREFIX + "use-object-storage-19-creodias.png",
        "s3049": IMAGES_S3_PREFIX + "use-object-storage-11-creodias.png",
        "s3050": IMAGES_S3_PREFIX + "use-object-storage-13-creodias.png",
        "s3051": IMAGES_S3_PREFIX + "use-object-storage-14-creodias.png",
        "s3052": IMAGES_S3_PREFIX + "use-object-storage-15-creodias.png",
        "s3053": IMAGES_S3_PREFIX + "s3-bucket-versioning-01-creodias.png",
        "s3054": IMAGES_S3_PREFIX + "s3-bucket-versioning-02-creodias.png",
        "s3055": IMAGES_S3_PREFIX + "s3-bucket-versioning-03-creodias.png",
        "s3056": IMAGES_S3_PREFIX + "s3-bucket-versioning-04-creodias.png",
        "s3057": IMAGES_S3_PREFIX + "s3-bucket-versioning-05-creodias.png",
        "s3058": IMAGES_S3_PREFIX + "s3-bucket-versioning-06-creodias.png",
        "s3059": IMAGES_S3_PREFIX + "s3-bucket-versioning-07-creodias.png",
        "s3060": IMAGES_S3_PREFIX + "s3-bucket-versioning-08-creodias.png",
        "s3061": IMAGES_S3_PREFIX + "s3-bucket-versioning-09-creodias.png",
        "s3062": IMAGES_S3_PREFIX + "boto1.png",
        "s3063": IMAGES_S3_PREFIX + "boto2.png",
        "s3064": IMAGES_S3_PREFIX + "boto3.png",
        "s3065": IMAGES_S3_PREFIX + "boto4.png",
        "s3066": IMAGES_S3_PREFIX + "code-structure.png",
        "s3067": IMAGES_S3_PREFIX + "boto3-upload-file-to-s3.png",
        "s3068": IMAGES_S3_PREFIX + "install-s3cmd-linux-01_creodias.png",
        "s3069": IMAGES_S3_PREFIX + "install-s3cmd-linux-02_creodias.png",
        "s3070": IMAGES_S3_PREFIX + "mount-object-storage-s3fs-linux-06_creodias.png",
        "s3071": IMAGES_S3_PREFIX + "mount-object-storage-s3fs-linux-03_creodias.png",
        "s3072": IMAGES_S3_PREFIX + "mount-object-storage-s3fs-linux-04_creodias.png",
        "s3073": IMAGES_S3_PREFIX + "mount-object-storage-s3fs-linux-05_creodias.png",
        "s3074": IMAGES_S3_PREFIX + "object-storage-windows-example1-creodias.png",
        "s3075": IMAGES_S3_PREFIX + "mount-eodata-windows-open-03-creodias.png",
        "s3076": IMAGES_S3_PREFIX + "mount-eodata-windows-open-04-creodias.png",
        "s3077": IMAGES_S3_PREFIX + "mount-eodata-windows-open-05-creodias.png",
        "s3078": IMAGES_S3_PREFIX + "mount-eodata-windows-open-06-creodias.png",
        "s3079": IMAGES_S3_PREFIX + "mount-eodata-windows-open-07-creodias.png",
        "s3080": IMAGES_S3_PREFIX + "mount-eodata-windows-open-10-creodias.png",
        "s3081": IMAGES_S3_PREFIX + "mount-eodata-windows-open-11-creodias.png",
        "s3082": IMAGES_S3_PREFIX + "mount-eodata-windows-open-12-creodias.png",
        "s3083": IMAGES_S3_PREFIX + "mount-eodata-windows-rclone-01-creodias.png",
        "s3084": IMAGES_S3_PREFIX + "mount-eodata-windows-rclone-02-creodias.png",
        "s3085": IMAGES_S3_PREFIX + "mount-eodata-windows-open-nssm-01-creodias.png",
        "s3086": IMAGES_S3_PREFIX + "mount-eodata-windows-open-13-creodias.png",
        "s3087": IMAGES_S3_PREFIX + "mount-object-storage-windows-horizon-01-creodias.png",
        "s3088": IMAGES_S3_PREFIX + "mount-eodata-windows-open-remove-01-creodias.png",
        "s3089": IMAGES_S3_PREFIX + "mount-eodata-windows-open-remove-03-creodias.png",
        "s3090": IMAGES_S3_PREFIX + "mount-eodata-windows-open-remove-04-creodias.png",
        "s3091": IMAGES_S3_PREFIX + "mount-eodata-windows-open-remove-05-creodias.png",
        "s3092": IMAGES_S3_PREFIX + "mount-eodata-windows-open-remove-06-creodias.png",
        "s3093": IMAGES_S3_PREFIX + "mount-eodata-windows-open-remove-07-creodias.png",
        "s3094": IMAGES_S3_PREFIX + "mount-eodata-windows-open-remove-08_creodias.png",
        "s3095": IMAGES_S3_PREFIX + "use-object-storage-01_creodias.png",
        "s3096": IMAGES_S3_PREFIX + "use-object-storage-02_creodias.png",
        "s3097": IMAGES_S3_PREFIX + "use-object-storage-03_creodias.png",
        "s3098": IMAGES_S3_PREFIX + "use-object-storage-04_creodias.png",
        "s3099": IMAGES_S3_PREFIX + "use-object-storage-05_creodias.png",
        "s3100": IMAGES_S3_PREFIX + "use-object-storage-06_creodias.png",
        "s3101": IMAGES_S3_PREFIX + "use-object-storage-07_creodias.png",
        "s3102": IMAGES_S3_PREFIX + "use-object-storage-08_creodias.png",
        "s3103": IMAGES_S3_PREFIX + "use-object-storage-09_creodias.png",
        "s3104": IMAGES_S3_PREFIX + "use-object-storage-success_creodias.png",
        "s3105": IMAGES_S3_PREFIX + "use-object-storage-10_creodias.png",
        "s3106": IMAGES_S3_PREFIX + "use-object-storage-16_creodias.png",
        "s3107": IMAGES_S3_PREFIX + "use-object-storage-17_creodias.png",
        "s3108": IMAGES_S3_PREFIX + "use-object-storage-18_creodias.png",
        "s3109": IMAGES_S3_PREFIX + "use-object-storage-19_creodias.png",
        "s3110": IMAGES_S3_PREFIX + "use-object-storage-11_creodias.png",
        "s3111": IMAGES_S3_PREFIX + "use-object-storage-13_creodias.png",
        "s3112": IMAGES_S3_PREFIX + "use-object-storage-14_creodias.png",
        "s3113": IMAGES_S3_PREFIX + "use-object-storage-15_creodias.png",
        "s3114": IMAGES_S3_PREFIX + "s3-bucket-versioning_01_creodias.png",
        "s3115": IMAGES_S3_PREFIX + "s3-bucket-versioning_02_creodias.png",
        "s3116": IMAGES_S3_PREFIX + "s3-bucket-versioning_03_creodias.png",
        "s3117": IMAGES_S3_PREFIX + "s3-bucket-versioning_04_creodias.png",
        "s3118": IMAGES_S3_PREFIX + "s3-bucket-versioning_05_creodias.png",
        "s3119": IMAGES_S3_PREFIX + "s3-bucket-versioning_06_creodias.png",
        "s3120": IMAGES_S3_PREFIX + "s3-bucket-versioning_07_creodias.png",
        "s3121": IMAGES_S3_PREFIX + "s3-bucket-versioning_08_creodias.png",
        "s3122": IMAGES_S3_PREFIX + "s3-bucket-versioning-09_creodias.png",
},

    "shares_images": {
        "shares001": IMAGES_SHARES_PREFIX + "allow-share-access-01.png",
        "shares002": IMAGES_SHARES_PREFIX + "allow-share-access-02.png",
        "shares003": IMAGES_SHARES_PREFIX + "allow-share-access-03.png",
        "shares004": IMAGES_SHARES_PREFIX + "allow-share-access-04.png",
        "shares005": IMAGES_SHARES_PREFIX + "allow-share-access-05.png",
        "shares006": IMAGES_SHARES_PREFIX + "allow-share-access-06.png",
        "shares007": IMAGES_SHARES_PREFIX + "allow-share-access-07.png",
        "shares008": IMAGES_SHARES_PREFIX + "allow-share-access-08.png",
        "shares009": IMAGES_SHARES_PREFIX + "allow-share-access-09.png",
        "shares010": IMAGES_SHARES_PREFIX + "create-share-01.png",
        "shares011": IMAGES_SHARES_PREFIX + "create-share-02.png",
        "shares012": IMAGES_SHARES_PREFIX + "create-share-03.png",
        "shares013": IMAGES_SHARES_PREFIX + "create-share-04.png",
        "shares014": IMAGES_SHARES_PREFIX + "create-share-05.png",
        "shares015": IMAGES_SHARES_PREFIX + "create-share-06.png",
        "shares016": IMAGES_SHARES_PREFIX + "create-share-08.png",
        "shares017": IMAGES_SHARES_PREFIX + "create-share-07.png",
        "shares018": IMAGES_SHARES_PREFIX + "mount-nfs-share-03.png",
        "shares019": IMAGES_SHARES_PREFIX + "command-mount-the-nfs-share.png",
        "shares020": IMAGES_SHARES_PREFIX + "mount-nfs-share-04.png",
        "shares021": IMAGES_SHARES_PREFIX + "allow-share-access-01.png",
        "shares022": IMAGES_SHARES_PREFIX + "allow-share-access-02.png",
        "shares023": IMAGES_SHARES_PREFIX + "allow-share-access-03.png",
        "shares024": IMAGES_SHARES_PREFIX + "allow-share-access-04.png",
        "shares025": IMAGES_SHARES_PREFIX + "allow-share-access-05.png",
        "shares026": IMAGES_SHARES_PREFIX + "allow-share-access-06.png",
        "shares027": IMAGES_SHARES_PREFIX + "allow-share-access-07.png",
        "shares028": IMAGES_SHARES_PREFIX + "allow-share-access-08.png",
        "shares029": IMAGES_SHARES_PREFIX + "allow-share-access-09.png",
        "shares030": IMAGES_SHARES_PREFIX + "create-share-01.png",
        "shares031": IMAGES_SHARES_PREFIX + "create-share-02.png",
        "shares032": IMAGES_SHARES_PREFIX + "create-share-03.png",
        "shares033": IMAGES_SHARES_PREFIX + "create-share-04.png",
        "shares034": IMAGES_SHARES_PREFIX + "create-share-05.png",
        "shares035": IMAGES_SHARES_PREFIX + "create-share-06.png",
        "shares036": IMAGES_SHARES_PREFIX + "create-share-08.png",
        "shares037": IMAGES_SHARES_PREFIX + "create-share-07.png",
        "shares038": IMAGES_SHARES_PREFIX + "mount-nfs-share-03.png",
        "shares039": IMAGES_SHARES_PREFIX + "command-mount-the-nfs-share.png",
        "shares040": IMAGES_SHARES_PREFIX + "mount-nfs-share-04.png",
},

    "windows_images": {
        "windows001": IMAGES_WINDOWS_PREFIX + "run-mmc.png",
        "windows002": IMAGES_WINDOWS_PREFIX + "snap-in.png",
        "windows003": IMAGES_WINDOWS_PREFIX + "account-new.png",
        "windows004": IMAGES_WINDOWS_PREFIX + "account-menu.png",
        "windows005": IMAGES_WINDOWS_PREFIX + "account-properties.png",
        "windows006": IMAGES_WINDOWS_PREFIX + "account-groups.png",
        "windows007": IMAGES_WINDOWS_PREFIX + "account-final.png",
        "windows008": IMAGES_WINDOWS_PREFIX + "bastion-01.png",
        "windows009": IMAGES_WINDOWS_PREFIX + "windows-01.png",
        "windows010": IMAGES_WINDOWS_PREFIX + "bastion-00.png",
        "windows011": IMAGES_WINDOWS_PREFIX + "bastion-02.png",
        "windows012": IMAGES_WINDOWS_PREFIX + "bastion-03.png",
        "windows013": IMAGES_WINDOWS_PREFIX + "bastion-04.png",
        "windows014": IMAGES_WINDOWS_PREFIX + "bastion-05.png",
        "windows015": IMAGES_WINDOWS_PREFIX + "bastion-07.png",
        "windows016": IMAGES_WINDOWS_PREFIX + "bastion-08.png",
        "windows017": IMAGES_WINDOWS_PREFIX + "windows-02.png",
        "windows018": IMAGES_WINDOWS_PREFIX + "windows-03.png",
        "windows019": IMAGES_WINDOWS_PREFIX + "create-ssh-key-windows-11-03-creodias.png",
        "windows020": IMAGES_WINDOWS_PREFIX + "create-ssh-key-windows-11-04-creodias.png",
        "windows021": IMAGES_WINDOWS_PREFIX + "create-ssh-key-windows-11-07-creodias.png",
        "windows022": IMAGES_WINDOWS_PREFIX + "create-ssh-key-windows-11-08-creodias.png",
        "windows023": IMAGES_WINDOWS_PREFIX + "create-ssh-key-windows-11-09-creodias.png",
        "windows024": IMAGES_WINDOWS_PREFIX + "create-ssh-key-windows-11-10-creodias.png",
        "windows025": IMAGES_WINDOWS_PREFIX + "create-ssh-key-windows-11-11-creodias.png",
        "windows026": IMAGES_WINDOWS_PREFIX + "create-ssh-key-windows-11-12-creodias.png",
        "windows027": IMAGES_WINDOWS_PREFIX + "create-ssh-key-windows-11-13-creodias.png",
        "windows028": IMAGES_WINDOWS_PREFIX + "create-ssh-key-windows-11-14-creodias.png",
        "windows029": IMAGES_WINDOWS_PREFIX + "create-ssh-key-windows-11-15-creodias.png",
        "windows030": IMAGES_WINDOWS_PREFIX + "create-ssh-key-windows-11-16-creodias.png",
        "windows031": IMAGES_WINDOWS_PREFIX + "create-ssh-key-windows-11-19-creodias.png",
        "windows032": IMAGES_WINDOWS_PREFIX + "create-ssh-key-windows-11-20-creodias.png",
        "windows033": IMAGES_WINDOWS_PREFIX + "create-ssh-key-windows-11-21-creodias.png",
        "windows034": IMAGES_WINDOWS_PREFIX + "create-ssh-key-windows-11-22-creodias.png",
        "windows035": IMAGES_WINDOWS_PREFIX + "ssh-windows-1.png",
        "windows036": IMAGES_WINDOWS_PREFIX + "ssh-windows-2.png",
        "windows037": IMAGES_WINDOWS_PREFIX + "ssh-windows-3.png",
        "windows038": IMAGES_WINDOWS_PREFIX + "ssh-windows-4.png",
        "windows039": IMAGES_WINDOWS_PREFIX + "ssh-windows-5.png",
        "windows040": IMAGES_WINDOWS_PREFIX + "ssh-windows-6.png",
        "windows041": IMAGES_WINDOWS_PREFIX + "01.png",
        "windows042": IMAGES_WINDOWS_PREFIX + "02.png",
        "windows043": IMAGES_WINDOWS_PREFIX + "03.png",
        "windows044": IMAGES_WINDOWS_PREFIX + "04.png",
        "windows045": IMAGES_WINDOWS_PREFIX + "05.png",
        "windows046": IMAGES_WINDOWS_PREFIX + "06.png",
        "windows047": IMAGES_WINDOWS_PREFIX + "07.png",
        "windows048": IMAGES_WINDOWS_PREFIX + "08.png",
        "windows049": IMAGES_WINDOWS_PREFIX + "09.png",
        "windows050": IMAGES_WINDOWS_PREFIX + "10.png",
        "windows051": IMAGES_WINDOWS_PREFIX + "11.png",
        "windows052": IMAGES_WINDOWS_PREFIX + "12.png",
        "windows053": IMAGES_WINDOWS_PREFIX + "13.png",
        "windows054": IMAGES_WINDOWS_PREFIX + "14.png",
        "windows055": IMAGES_WINDOWS_PREFIX + "15.png",
        "windows056": IMAGES_WINDOWS_PREFIX + "c1.png",
        "windows057": IMAGES_WINDOWS_PREFIX + "c4.png",
        "windows058": IMAGES_WINDOWS_PREFIX + "run-mmc.png",
        "windows059": IMAGES_WINDOWS_PREFIX + "snap-in.png",
        "windows060": IMAGES_WINDOWS_PREFIX + "account-new.png",
        "windows061": IMAGES_WINDOWS_PREFIX + "account-menu.png",
        "windows062": IMAGES_WINDOWS_PREFIX + "account-properties.png",
        "windows063": IMAGES_WINDOWS_PREFIX + "account-groups.png",
        "windows064": IMAGES_WINDOWS_PREFIX + "account-final.png",
        "windows065": IMAGES_WINDOWS_PREFIX + "bastion-01.png",
        "windows066": IMAGES_WINDOWS_PREFIX + "windows-01.png",
        "windows067": IMAGES_WINDOWS_PREFIX + "bastion-00.png",
        "windows068": IMAGES_WINDOWS_PREFIX + "bastion-02.png",
        "windows069": IMAGES_WINDOWS_PREFIX + "bastion-03.png",
        "windows070": IMAGES_WINDOWS_PREFIX + "bastion-04.png",
        "windows071": IMAGES_WINDOWS_PREFIX + "bastion-05.png",
        "windows072": IMAGES_WINDOWS_PREFIX + "bastion-07.png",
        "windows073": IMAGES_WINDOWS_PREFIX + "bastion-08.png",
        "windows074": IMAGES_WINDOWS_PREFIX + "windows-02.png",
        "windows075": IMAGES_WINDOWS_PREFIX + "windows-03.png",
        "windows076": IMAGES_WINDOWS_PREFIX + "create-ssh-key-windows-11-03-creodias.png",
        "windows077": IMAGES_WINDOWS_PREFIX + "create-ssh-key-windows-11-04-creodias.png",
        "windows078": IMAGES_WINDOWS_PREFIX + "create-ssh-key-windows-11-07-creodias.png",
        "windows079": IMAGES_WINDOWS_PREFIX + "create-ssh-key-windows-11-08-creodias.png",
        "windows080": IMAGES_WINDOWS_PREFIX + "create-ssh-key-windows-11-09-creodias.png",
        "windows081": IMAGES_WINDOWS_PREFIX + "create-ssh-key-windows-11-10-creodias.png",
        "windows082": IMAGES_WINDOWS_PREFIX + "create-ssh-key-windows-11-11-creodias.png",
        "windows083": IMAGES_WINDOWS_PREFIX + "create-ssh-key-windows-11-12-creodias.png",
        "windows084": IMAGES_WINDOWS_PREFIX + "create-ssh-key-windows-11-13-creodias.png",
        "windows085": IMAGES_WINDOWS_PREFIX + "create-ssh-key-windows-11-14-creodias.png",
        "windows086": IMAGES_WINDOWS_PREFIX + "create-ssh-key-windows-11-15-creodias.png",
        "windows087": IMAGES_WINDOWS_PREFIX + "create-ssh-key-windows-11-16-creodias.png",
        "windows088": IMAGES_WINDOWS_PREFIX + "create-ssh-key-windows-11-19-creodias.png",
        "windows089": IMAGES_WINDOWS_PREFIX + "create-ssh-key-windows-11-20-creodias.png",
        "windows090": IMAGES_WINDOWS_PREFIX + "create-ssh-key-windows-11-21-creodias.png",
        "windows091": IMAGES_WINDOWS_PREFIX + "create-ssh-key-windows-11-22-creodias.png",
        "windows092": IMAGES_WINDOWS_PREFIX + "ssh-windows-1.png",
        "windows093": IMAGES_WINDOWS_PREFIX + "ssh-windows-2.png",
        "windows094": IMAGES_WINDOWS_PREFIX + "ssh-windows-3.png",
        "windows095": IMAGES_WINDOWS_PREFIX + "ssh-windows-4.png",
        "windows096": IMAGES_WINDOWS_PREFIX + "ssh-windows-5.png",
        "windows097": IMAGES_WINDOWS_PREFIX + "ssh-windows-6.png",
        "windows098": IMAGES_WINDOWS_PREFIX + "01.png",
        "windows099": IMAGES_WINDOWS_PREFIX + "02.png",
        "windows100": IMAGES_WINDOWS_PREFIX + "03.png",
        "windows101": IMAGES_WINDOWS_PREFIX + "04.png",
        "windows102": IMAGES_WINDOWS_PREFIX + "05.png",
        "windows103": IMAGES_WINDOWS_PREFIX + "06.png",
        "windows104": IMAGES_WINDOWS_PREFIX + "07.png",
        "windows105": IMAGES_WINDOWS_PREFIX + "08.png",
        "windows106": IMAGES_WINDOWS_PREFIX + "09.png",
        "windows107": IMAGES_WINDOWS_PREFIX + "10.png",
        "windows108": IMAGES_WINDOWS_PREFIX + "11.png",
        "windows109": IMAGES_WINDOWS_PREFIX + "12.png",
        "windows110": IMAGES_WINDOWS_PREFIX + "13.png",
        "windows111": IMAGES_WINDOWS_PREFIX + "14.png",
        "windows112": IMAGES_WINDOWS_PREFIX + "15.png",
        "windows113": IMAGES_WINDOWS_PREFIX + "c1.png",
        "windows114": IMAGES_WINDOWS_PREFIX + "c4.png",
    },


    "cloud_images": {
        "cloud001": IMAGES_CLOUD_PREFIX + "dashboard-project-overview.png",
        "cloud002": IMAGES_CLOUD_PREFIX + "dns1.png",
        "cloud003": IMAGES_CLOUD_PREFIX + "create-main-site-dns.png",
        "cloud004": IMAGES_CLOUD_PREFIX + "create-www-subdomain.png",
        "cloud005": IMAGES_CLOUD_PREFIX + "show-example-domain-record-sets.png",
        "cloud006": IMAGES_CLOUD_PREFIX + "dashboardover1-v2.png",
        "cloud007": IMAGES_CLOUD_PREFIX + "dashboardover2-v2.png",
        "cloud008": IMAGES_CLOUD_PREFIX + "compute-instances.png",
        "cloud009": IMAGES_CLOUD_PREFIX + "launch-instance.png",
        "cloud010": IMAGES_CLOUD_PREFIX + "choose-os.png",
        "cloud011": IMAGES_CLOUD_PREFIX + "createnew18.png",
        "cloud012": IMAGES_CLOUD_PREFIX + "createnew16.png",
        "cloud013": IMAGES_CLOUD_PREFIX + "createnew19.png",
        "cloud014": IMAGES_CLOUD_PREFIX + "networks5.png",
        "cloud015": IMAGES_CLOUD_PREFIX + "createnew6.png",
        "cloud016": IMAGES_CLOUD_PREFIX + "createnew7.png",
        "cloud017": IMAGES_CLOUD_PREFIX + "createnew8.png",
        "cloud018": IMAGES_CLOUD_PREFIX + "createnew9.png",
        "cloud019": IMAGES_CLOUD_PREFIX + "createnew10.png",
        "cloud020": IMAGES_CLOUD_PREFIX + "createnew11.png",
        "cloud021": IMAGES_CLOUD_PREFIX + "createnew12.png",
        "cloud022": IMAGES_CLOUD_PREFIX + "createnew13.png",
        "cloud023": IMAGES_CLOUD_PREFIX + "createnew14.png",
        "cloud024": IMAGES_CLOUD_PREFIX + "accessvm2.png",
        "cloud025": IMAGES_CLOUD_PREFIX + "accessvm3.png",
        "cloud026": IMAGES_CLOUD_PREFIX + "accessvm4v2.png",
        "cloud027": IMAGES_CLOUD_PREFIX + "sudo-su-eouser.png",
        "cloud028": IMAGES_CLOUD_PREFIX + "some-nodes.png",
        "cloud029": IMAGES_CLOUD_PREFIX + "fedora-image.png",
        "cloud030": IMAGES_CLOUD_PREFIX + "accessvm5.png",
        "cloud031": IMAGES_CLOUD_PREFIX + "clone2.png",
        "cloud032": IMAGES_CLOUD_PREFIX + "clone3.png",
        "cloud033": IMAGES_CLOUD_PREFIX + "create-windows-vm-horizon-web-console-01.png",
        "cloud034": IMAGES_CLOUD_PREFIX + "create-windows-vm-horizon-web-console-02.png",
        "cloud035": IMAGES_CLOUD_PREFIX + "create-windows-vm-horizon-web-console-03.png",
        "cloud036": IMAGES_CLOUD_PREFIX + "create-windows-vm-horizon-web-console-04.png",
        "cloud037": IMAGES_CLOUD_PREFIX + "create-windows-vm-horizon-web-console-05.png",
        "cloud038": IMAGES_CLOUD_PREFIX + "create-windows-vm-horizon-web-console-06.png",
        "cloud039": IMAGES_CLOUD_PREFIX + "create-windows-vm-horizon-web-console-07.png",
        "cloud040": IMAGES_CLOUD_PREFIX + "create-windows-vm-horizon-web-console-09.png",
        "cloud041": IMAGES_CLOUD_PREFIX + "create-windows-vm-horizon-web-console-21.png",
        "cloud042": IMAGES_CLOUD_PREFIX + "create-windows-vm-horizon-web-console-10.png",
        "cloud043": IMAGES_CLOUD_PREFIX + "create-windows-vm-horizon-web-console-11.png",
        "cloud044": IMAGES_CLOUD_PREFIX + "create-windows-vm-horizon-web-console-12.png",
        "cloud045": IMAGES_CLOUD_PREFIX + "create-windows-vm-horizon-web-console-13.png",
        "cloud046": IMAGES_CLOUD_PREFIX + "create-windows-vm-horizon-web-console-14.png",
        "cloud047": IMAGES_CLOUD_PREFIX + "create-windows-vm-horizon-web-console-15.png",
        "cloud048": IMAGES_CLOUD_PREFIX + "create-windows-vm-horizon-web-console-16.png",
        "cloud049": IMAGES_CLOUD_PREFIX + "create-windows-vm-horizon-web-console-17.png",
        "cloud050": IMAGES_CLOUD_PREFIX + "create-windows-vm-horizon-web-console-18.png",
        "cloud051": IMAGES_CLOUD_PREFIX + "create-windows-vm-horizon-web-console-19.png",
        "cloud052": IMAGES_CLOUD_PREFIX + "create-windows-vm-horizon-web-console-26.png",
        "cloud053": IMAGES_CLOUD_PREFIX + "create-windows-vm-horizon-web-console-27.png",
        "cloud054": IMAGES_CLOUD_PREFIX + "create-windows-vm-horizon-web-console-28.png",
        "cloud055": IMAGES_CLOUD_PREFIX + "create-linux-linux-04.png",
        "cloud056": IMAGES_CLOUD_PREFIX + "create-linux-linux-05.png",
        "cloud057": IMAGES_CLOUD_PREFIX + "boot-source.png",
        "cloud058": IMAGES_CLOUD_PREFIX + "create-linux-linux-06.png",
        "cloud059": IMAGES_CLOUD_PREFIX + "create-linux-linux-07.png",
        "cloud060": IMAGES_CLOUD_PREFIX + "yellow-triangles.png",
        "cloud061": IMAGES_CLOUD_PREFIX + "create-linux-linux-08.png",
        "cloud062": IMAGES_CLOUD_PREFIX + "create-linux-linux-09.png",
        "cloud063": IMAGES_CLOUD_PREFIX + "create-linux-linux-10.png",
        "cloud064": IMAGES_CLOUD_PREFIX + "create-linux-linux-12.png",
        "cloud065": IMAGES_CLOUD_PREFIX + "create-linux-linux-13.png",
        "cloud066": IMAGES_CLOUD_PREFIX + "ip-address-from-article.png",
        "cloud067": IMAGES_CLOUD_PREFIX + "putty-02.png",
        "cloud068": IMAGES_CLOUD_PREFIX + "putty-03.png",
        "cloud069": IMAGES_CLOUD_PREFIX + "putty-04.png",
        "cloud070": IMAGES_CLOUD_PREFIX + "putty-05.png",
        "cloud071": IMAGES_CLOUD_PREFIX + "putty-06.png",
        "cloud072": IMAGES_CLOUD_PREFIX + "putty-07.png",
        "cloud073": IMAGES_CLOUD_PREFIX + "putty-08.png",
        "cloud074": IMAGES_CLOUD_PREFIX + "putty-09.png",
        "cloud075": IMAGES_CLOUD_PREFIX + "putty-10.png",
        "cloud076": IMAGES_CLOUD_PREFIX + "putty-11.png",
        "cloud077": IMAGES_CLOUD_PREFIX + "key-location-putty.png",
        "cloud078": IMAGES_CLOUD_PREFIX + "putty-12.png",
        "cloud079": IMAGES_CLOUD_PREFIX + "putty-13.png",
        "cloud080": IMAGES_CLOUD_PREFIX + "putty-14.png",
        "cloud081": IMAGES_CLOUD_PREFIX + "putty-15.png",
        "cloud082": IMAGES_CLOUD_PREFIX + "putty-16.png",
        "cloud083": IMAGES_CLOUD_PREFIX + "start-vm-from-volume-snapshot-cli-08.png",
        "cloud084": IMAGES_CLOUD_PREFIX + "start-vm-from-volume-snapshot-cli-09.png",
        "cloud085": IMAGES_CLOUD_PREFIX + "start-vm-from-volume-snapshot-cli-10.png",
        "cloud086": IMAGES_CLOUD_PREFIX + "start-vm-from-volume-snapshot-cli-11.png",
        "cloud087": IMAGES_CLOUD_PREFIX + "start-vm-from-volume-snapshot-cli-13.png",
        "cloud088": IMAGES_CLOUD_PREFIX + "openstack-server-create-help.png",
        "cloud089": IMAGES_CLOUD_PREFIX + "create-vm-cli-1.png",
        "cloud090": IMAGES_CLOUD_PREFIX + "screenshot-20241006-124004.png",
        "cloud091": IMAGES_CLOUD_PREFIX + "screenshot-20241006-125234.png",
        "cloud092": IMAGES_CLOUD_PREFIX + "screenshot-20241006-132619.png",
        "cloud093": IMAGES_CLOUD_PREFIX + "screenshot-20241006-125651.png",
        "cloud094": IMAGES_CLOUD_PREFIX + "screenshot-20241006-130817.png",
        "cloud095": IMAGES_CLOUD_PREFIX + "screenshot-20241006-132113.png",
        "cloud096": IMAGES_CLOUD_PREFIX + "screenshot-20241006-133524.png",
        "cloud097": IMAGES_CLOUD_PREFIX + "screenshot-20241006-134749.png",
        "cloud098": IMAGES_CLOUD_PREFIX + "screenshot-20241006-135229.png",
        "cloud099": IMAGES_CLOUD_PREFIX + "screenshot-20241006-143434.png",
        "cloud100": IMAGES_CLOUD_PREFIX + "screenshot-20241006-145844.png",
        "cloud101": IMAGES_CLOUD_PREFIX + "ww5.png",
        "cloud102": IMAGES_CLOUD_PREFIX + "ww6.png",
        "cloud103": IMAGES_CLOUD_PREFIX + "ww7.png",
        "cloud104": IMAGES_CLOUD_PREFIX + "ww8.png",
        "cloud105": IMAGES_CLOUD_PREFIX + "ww9.png",
        "cloud106": IMAGES_CLOUD_PREFIX + "ww10.png",
        "cloud107": IMAGES_CLOUD_PREFIX + "ww11.png",
        "cloud108": IMAGES_CLOUD_PREFIX + "ww12.png",
        "cloud109": IMAGES_CLOUD_PREFIX + "ww13.png",
        "cloud110": IMAGES_CLOUD_PREFIX + "ww14.png",
        "cloud111": IMAGES_CLOUD_PREFIX + "ww15.png",
        "cloud112": IMAGES_CLOUD_PREFIX + "ww16.png",
        "cloud113": IMAGES_CLOUD_PREFIX + "ww17.png",
        "cloud114": IMAGES_CLOUD_PREFIX + "ww18.png",
        "cloud115": IMAGES_CLOUD_PREFIX + "ww19.png",
        "cloud116": IMAGES_CLOUD_PREFIX + "ww20.png",
        "cloud117": IMAGES_CLOUD_PREFIX + "lw1.png",
        "cloud118": IMAGES_CLOUD_PREFIX + "lw2.png",
        "cloud119": IMAGES_CLOUD_PREFIX + "lw3.png",
        "cloud120": IMAGES_CLOUD_PREFIX + "lw4.png",
        "cloud121": IMAGES_CLOUD_PREFIX + "lw5.png",
        "cloud122": IMAGES_CLOUD_PREFIX + "lw6.png",
        "cloud123": IMAGES_CLOUD_PREFIX + "lw7.png",
        "cloud124": IMAGES_CLOUD_PREFIX + "lw8.png",
        "cloud125": IMAGES_CLOUD_PREFIX + "lw9.png",
        "cloud126": IMAGES_CLOUD_PREFIX + "lw10.png",
        "cloud127": IMAGES_CLOUD_PREFIX + "lw11.png",
        "cloud128": IMAGES_CLOUD_PREFIX + "lw12.png",
        "cloud129": IMAGES_CLOUD_PREFIX + "lw13.png",
        "cloud130": IMAGES_CLOUD_PREFIX + "lw14.png",
        "cloud131": IMAGES_CLOUD_PREFIX + "lw15.png",
        "cloud132": IMAGES_CLOUD_PREFIX + "lw16.png",
        "cloud133": IMAGES_CLOUD_PREFIX + "lw17.png",
        "cloud134": IMAGES_CLOUD_PREFIX + "lw18.png",
        "cloud135": IMAGES_CLOUD_PREFIX + "lw19.png",
        "cloud136": IMAGES_CLOUD_PREFIX + "uses-ephemeral.png",
        "cloud137": IMAGES_CLOUD_PREFIX + "shut-off-instance.png",
        "cloud138": IMAGES_CLOUD_PREFIX + "instance-ephemeral-shut-off.png",
        "cloud139": IMAGES_CLOUD_PREFIX + "instance-ephemeral-create-snapshot.png",
        "cloud140": IMAGES_CLOUD_PREFIX + "instance-ephemeral-snapshot.png",
        "cloud141": IMAGES_CLOUD_PREFIX + "instance-blue-green.png",
        "cloud142": IMAGES_CLOUD_PREFIX + "instance-persistent-created.png",
        "cloud143": IMAGES_CLOUD_PREFIX + "instance-persistent-volumes-volumes.png",
        "cloud144": IMAGES_CLOUD_PREFIX + "instance-persistent-shut-down-indees.png",
        "cloud145": IMAGES_CLOUD_PREFIX + "instance-persistent-create-shanpshot-button.png",
        "cloud146": IMAGES_CLOUD_PREFIX + "instance-persistent-new-name.png",
        "cloud147": IMAGES_CLOUD_PREFIX + "instance-persistent-active-0bytes.png",
        "cloud148": IMAGES_CLOUD_PREFIX + "instance-persistent-show-data.png",
        "cloud149": IMAGES_CLOUD_PREFIX + "instance-persistent-volume-shapshot.png",
        "cloud150": IMAGES_CLOUD_PREFIX + "how-to-create-instance-snapshot-horizon-13.png",
        "cloud151": IMAGES_CLOUD_PREFIX + "keypair1.png",
        "cloud152": IMAGES_CLOUD_PREFIX + "keypair2.png",
        "cloud153": IMAGES_CLOUD_PREFIX + "keypair3.png",
        "cloud154": IMAGES_CLOUD_PREFIX + "keypair4.png",
        "cloud155": IMAGES_CLOUD_PREFIX + "keypair5.png",
        "cloud156": IMAGES_CLOUD_PREFIX + "newvm1.png",
        "cloud157": IMAGES_CLOUD_PREFIX + "newvm2.png",
        "cloud158": IMAGES_CLOUD_PREFIX + "newvm3.png",
        "cloud159": IMAGES_CLOUD_PREFIX + "newvm4.png",
        "cloud160": IMAGES_CLOUD_PREFIX + "newvm5.png",
        "cloud161": IMAGES_CLOUD_PREFIX + "newvm6.png",
        "cloud162": IMAGES_CLOUD_PREFIX + "newvm7.png",
        "cloud163": IMAGES_CLOUD_PREFIX + "newvm8.png",
        "cloud164": IMAGES_CLOUD_PREFIX + "newvm9.png",
        "cloud165": IMAGES_CLOUD_PREFIX + "newvm10.png",
        "cloud166": IMAGES_CLOUD_PREFIX + "newvm11.png",
        "cloud167": IMAGES_CLOUD_PREFIX + "newvm12.png",
        "cloud168": IMAGES_CLOUD_PREFIX + "newvm13.png",
        "cloud169": IMAGES_CLOUD_PREFIX + "fixconsole.png",
        "cloud170": IMAGES_CLOUD_PREFIX + "generate-credentials.png",
        "cloud171": IMAGES_CLOUD_PREFIX + "several-ec2-pairs.png",
        "cloud172": IMAGES_CLOUD_PREFIX + "removed-ec2-empty.png",
        "cloud173": IMAGES_CLOUD_PREFIX + "credential-create-help.png",
        "cloud174": IMAGES_CLOUD_PREFIX + "create-new-with-name.png",
        "cloud175": IMAGES_CLOUD_PREFIX + "complete-example.png",
        "cloud176": IMAGES_CLOUD_PREFIX + "create-credential.png",
        "cloud177": IMAGES_CLOUD_PREFIX + "nano-values.png",
        "cloud178": IMAGES_CLOUD_PREFIX + "export-os-cloud.png",
        "cloud179": IMAGES_CLOUD_PREFIX + "cli-os-cloud.png",
        "cloud180": IMAGES_CLOUD_PREFIX + "snap00.png",
        "cloud181": IMAGES_CLOUD_PREFIX + "snap01.png",
        "cloud182": IMAGES_CLOUD_PREFIX + "snap3.png",
        "cloud183": IMAGES_CLOUD_PREFIX + "snap4.png",
        "cloud184": IMAGES_CLOUD_PREFIX + "snap5.png",
        "cloud185": IMAGES_CLOUD_PREFIX + "snap6.png",
        "cloud186": IMAGES_CLOUD_PREFIX + "snap7.png",
        "cloud187": IMAGES_CLOUD_PREFIX + "snap8.png",
        "cloud188": IMAGES_CLOUD_PREFIX + "snap1.png",
        "cloud189": IMAGES_CLOUD_PREFIX + "snap2.png",
        "cloud190": IMAGES_CLOUD_PREFIX + "start-vm-instance-snapshot-horizon-09.png",
        "cloud191": IMAGES_CLOUD_PREFIX + "launch-instance-details.png",
        "cloud192": IMAGES_CLOUD_PREFIX + "launch-instance-source.png",
        "cloud193": IMAGES_CLOUD_PREFIX + "start-vm-instance-snapshot-horizon-01.png",
        "cloud194": IMAGES_CLOUD_PREFIX + "start-vm-instance-snapshot-horizon-02.png",
        "cloud195": IMAGES_CLOUD_PREFIX + "start-vm-instance-snapshot-horizon-03.png",
        "cloud196": IMAGES_CLOUD_PREFIX + "start-vm-instance-snapshot-horizon-04.png",
        "cloud197": IMAGES_CLOUD_PREFIX + "launch-instance-flavor.png",
        "cloud198": IMAGES_CLOUD_PREFIX + "launch-instance-networks.png",
        "cloud199": IMAGES_CLOUD_PREFIX + "launch-instance-security-groups.png",
        "cloud200": IMAGES_CLOUD_PREFIX + "launch-instance-key-pair.png",
        "cloud201": IMAGES_CLOUD_PREFIX + "start-vm-instance-snapshot-horizon-05.png",
        "cloud202": IMAGES_CLOUD_PREFIX + "launch-instance-launch-instance.png",
        "cloud203": IMAGES_CLOUD_PREFIX + "launch-instance-created-instances.png",
        "cloud204": IMAGES_CLOUD_PREFIX + "unavailable-network.png",
        "cloud205": IMAGES_CLOUD_PREFIX + "start-vm-instance-snapshot-horizon-06.png",
        "cloud206": IMAGES_CLOUD_PREFIX + "start-vm-instance-snapshot-horizon-07.png",
        "cloud207": IMAGES_CLOUD_PREFIX + "start-vm-instance-snapshot-horizon-08.png",
        "cloud208": IMAGES_CLOUD_PREFIX + "transfer-volume-between-projects-horizon-32.png",
        "cloud209": IMAGES_CLOUD_PREFIX + "transfer-volume-between-projects-horizon-37.png",
        "cloud210": IMAGES_CLOUD_PREFIX + "transfer-volume-between-projects-horizon-33.png",
        "cloud211": IMAGES_CLOUD_PREFIX + "transfer-volume-between-projects-horizon-15.png",
        "cloud212": IMAGES_CLOUD_PREFIX + "transfer-volume-between-projects-horizon-16.png",
        "cloud213": IMAGES_CLOUD_PREFIX + "transfer-volume-between-projects-horizon-17.png",
        "cloud214": IMAGES_CLOUD_PREFIX + "transfer-volume-between-projects-horizon-18.png",
        "cloud215": IMAGES_CLOUD_PREFIX + "transfer-volume-between-projects-horizon-19.png",
        "cloud216": IMAGES_CLOUD_PREFIX + "transfer-volume-between-projects-horizon-20.png",
        "cloud217": IMAGES_CLOUD_PREFIX + "transfer-volume-between-projects-horizon-21.png",
        "cloud218": IMAGES_CLOUD_PREFIX + "transfer-volume-between-projects-horizon-35.png",
        "cloud219": IMAGES_CLOUD_PREFIX + "transfer-volume-between-projects-horizon-36.png",
        "cloud220": IMAGES_CLOUD_PREFIX + "transfer-volume-between-projects-horizon-38.png",
        "cloud221": IMAGES_CLOUD_PREFIX + "transfer-volume-between-projects-horizon-11.png",
        "cloud222": IMAGES_CLOUD_PREFIX + "upload-image-horizon-01.png",
        "cloud223": IMAGES_CLOUD_PREFIX + "upload-image-horizon-02.png",
        "cloud224": IMAGES_CLOUD_PREFIX + "image-options-explanation.png",
        "cloud225": IMAGES_CLOUD_PREFIX + "format-image-upload.png",
        "cloud226": IMAGES_CLOUD_PREFIX + "upload-image-horizon-10.png",
        "cloud227": IMAGES_CLOUD_PREFIX + "upload-image-horizon-03.png",
        "cloud228": IMAGES_CLOUD_PREFIX + "upload-image-horizon-04.png",
        "cloud229": IMAGES_CLOUD_PREFIX + "debian-test-created.png",
        "cloud230": IMAGES_CLOUD_PREFIX + "upload-image-horizon-07.png",
        "cloud231": IMAGES_CLOUD_PREFIX + "upload-image-horizon-08.png",
        "cloud232": IMAGES_CLOUD_PREFIX + "upload-image-cli-10.png",
        "cloud233": IMAGES_CLOUD_PREFIX + "upload-image-cli-01.png",
        "cloud234": IMAGES_CLOUD_PREFIX + "upload-image-cli-12.png",
        "cloud235": IMAGES_CLOUD_PREFIX + "upload-image-cli-02.png",
        "cloud236": IMAGES_CLOUD_PREFIX + "upload-image-cli-03.png",
        "cloud237": IMAGES_CLOUD_PREFIX + "upload-image-cli-11.png",
        "cloud238": IMAGES_CLOUD_PREFIX + "new-docker-1.png",
        "cloud239": IMAGES_CLOUD_PREFIX + "use-docker-9.png",
        "cloud240": IMAGES_CLOUD_PREFIX + "use-docker-4.png",
        "cloud241": IMAGES_CLOUD_PREFIX + "use-docker-5.png",
        "cloud242": IMAGES_CLOUD_PREFIX + "use-docker-6.png",
        "cloud243": IMAGES_CLOUD_PREFIX + "use-docker-7.png",
        "cloud244": IMAGES_CLOUD_PREFIX + "linux-gui-03.png",
        "cloud245": IMAGES_CLOUD_PREFIX + "linux-gui-04.png",
        "cloud246": IMAGES_CLOUD_PREFIX + "linux-gui-05.png",
        "cloud247": IMAGES_CLOUD_PREFIX + "linux-gui-06.png",
        "cloud248": IMAGES_CLOUD_PREFIX + "linux-gui-07.png",
        "cloud249": IMAGES_CLOUD_PREFIX + "linux-gui-08.png",
        "cloud250": IMAGES_CLOUD_PREFIX + "linux-gui-09.png",
        "cloud251": IMAGES_CLOUD_PREFIX + "linux-gui-11.png",
        "cloud252": IMAGES_CLOUD_PREFIX + "linux-gui-12.png",
        "cloud253": IMAGES_CLOUD_PREFIX + "linux-gui-13.png",
        "cloud254": IMAGES_CLOUD_PREFIX + "linux-gui-14.png",
        "cloud255": IMAGES_CLOUD_PREFIX + "linux-gui-15.png",
        "cloud256": IMAGES_CLOUD_PREFIX + "linux-gui-16.png",
        "cloud257": IMAGES_CLOUD_PREFIX + "linux-gui-17.png",
        "cloud258": IMAGES_CLOUD_PREFIX + "use-security-groups-1.png",
        "cloud259": IMAGES_CLOUD_PREFIX + "use-security-groups-2.png",
        "cloud260": IMAGES_CLOUD_PREFIX + "use-security-groups-3.png",
        "cloud261": IMAGES_CLOUD_PREFIX + "use-security-groups-4.png",
        "cloud262": IMAGES_CLOUD_PREFIX + "use-security-groups-5.png",
        "cloud263": IMAGES_CLOUD_PREFIX + "use-security-groups-6.png",
        "cloud264": IMAGES_CLOUD_PREFIX + "use-security-groups-7.png",
        "cloud265": IMAGES_CLOUD_PREFIX + "install01.png",
        "cloud266": IMAGES_CLOUD_PREFIX + "install02.png",
        "cloud267": IMAGES_CLOUD_PREFIX + "install03.png",
        "cloud268": IMAGES_CLOUD_PREFIX + "install04-noted.png",
        "cloud269": IMAGES_CLOUD_PREFIX + "screenshot-20241014-112929.png",
        "cloud270": IMAGES_CLOUD_PREFIX + "image-2024-04-24-15-13-21.png",
        "cloud271": IMAGES_CLOUD_PREFIX + "openstack-user-roles-create-4.png",
        "cloud272": IMAGES_CLOUD_PREFIX + "user-roles-list-create-2.png",
        "cloud273": IMAGES_CLOUD_PREFIX + "user-roles-list-create-1.png",
        "cloud274": IMAGES_CLOUD_PREFIX + "user-roles-list-create-4.png",
        "cloud275": IMAGES_CLOUD_PREFIX + "user-roles-list-create-5.png",
        "cloud276": IMAGES_CLOUD_PREFIX + "user-roles-list-create-6.png",
        "cloud277": IMAGES_CLOUD_PREFIX + "user-roles-list-create-3.png",
        "cloud278": IMAGES_CLOUD_PREFIX + "resize-vm-horizon-1.png",
        "cloud279": IMAGES_CLOUD_PREFIX + "resize-vm-horizon-2.png",
        "cloud280": IMAGES_CLOUD_PREFIX + "resize-vm-horizon-3.png",
        "cloud281": IMAGES_CLOUD_PREFIX + "resize-vm-horizon-4.png",
        "cloud282": IMAGES_CLOUD_PREFIX + "resize-vm-horizon-5.png",
        "cloud283": IMAGES_CLOUD_PREFIX + "fwaas-openvpn-v2-34.png",
        "cloud284": IMAGES_CLOUD_PREFIX + "resize-vm-horizon-10.png",
        "cloud285": IMAGES_CLOUD_PREFIX + "resize-vm-horizon-11.png",
        "cloud286": IMAGES_CLOUD_PREFIX + "resize-vm-horizon-8.png",
        "cloud287": IMAGES_CLOUD_PREFIX + "resize-vm-horizon-7.png",
        "cloud288": IMAGES_CLOUD_PREFIX + "waw3-2-cloud-activated.png",
        "cloud289": IMAGES_CLOUD_PREFIX + "flavors-listed-spot.png",
        "cloud290": IMAGES_CLOUD_PREFIX + "spot-flavors-when-creating.png",
        "cloud291": IMAGES_CLOUD_PREFIX + "spot-hma-created.png",
        "cloud292": IMAGES_CLOUD_PREFIX + "value-of-spot.png",
        "cloud293": IMAGES_CLOUD_PREFIX + "resize-instance.png",
        "cloud294": IMAGES_CLOUD_PREFIX + "statuspower.png",
        "cloud295": IMAGES_CLOUD_PREFIX + "volno1.png",
        "cloud296": IMAGES_CLOUD_PREFIX + "volno2.png",
        "cloud297": IMAGES_CLOUD_PREFIX + "volno3.png",
        "cloud298": IMAGES_CLOUD_PREFIX + "volno4.png",
        "cloud299": IMAGES_CLOUD_PREFIX + "volno5.png",
        "cloud300": IMAGES_CLOUD_PREFIX + "volyes1.png",
        "cloud301": IMAGES_CLOUD_PREFIX + "volyes2.png",
        "cloud302": IMAGES_CLOUD_PREFIX + "volyes3.png",
        "cloud303": IMAGES_CLOUD_PREFIX + "volyes4.png",
        "cloud304": IMAGES_CLOUD_PREFIX + "volyes5.png",
        "cloud305": IMAGES_CLOUD_PREFIX + "volyes6.png",
        "cloud306": IMAGES_CLOUD_PREFIX + "volyes7.png",
        "cloud307": IMAGES_CLOUD_PREFIX + "volyes8.png",
        "cloud308": IMAGES_CLOUD_PREFIX + "volyes9.png",
        "cloud309": IMAGES_CLOUD_PREFIX + "volyes10.png",
        "cloud310": IMAGES_CLOUD_PREFIX + "volyes11.png",
        "cloud311": IMAGES_CLOUD_PREFIX + "volyes12.png",
        "cloud312": IMAGES_CLOUD_PREFIX + "volyes13.png",
        "cloud313": IMAGES_CLOUD_PREFIX + "volyes14.png",
        "cloud314": IMAGES_CLOUD_PREFIX + "volyes15.png",
        "cloud315": IMAGES_CLOUD_PREFIX + "volyes16.png",
        "cloud316": IMAGES_CLOUD_PREFIX + "project1.png",
        "cloud317": IMAGES_CLOUD_PREFIX + "project2.png",
        "cloud318": IMAGES_CLOUD_PREFIX + "dns1.png",
        "cloud319": IMAGES_CLOUD_PREFIX + "create-main-site-dns.png",
        "cloud320": IMAGES_CLOUD_PREFIX + "create-www-subdomain.png",
        "cloud321": IMAGES_CLOUD_PREFIX + "show-example-domain-record-sets.png",
        "cloud322": IMAGES_CLOUD_PREFIX + "dashboardover1-v2.png",
        "cloud323": IMAGES_CLOUD_PREFIX + "dashboardover2-v2.png",
        "cloud324": IMAGES_CLOUD_PREFIX + "compute-instances.png",
        "cloud325": IMAGES_CLOUD_PREFIX + "launch-instance.png",
        "cloud326": IMAGES_CLOUD_PREFIX + "choose-os.png",
        "cloud327": IMAGES_CLOUD_PREFIX + "createnew18.png",
        "cloud328": IMAGES_CLOUD_PREFIX + "createnew16.png",
        "cloud329": IMAGES_CLOUD_PREFIX + "createnew19.png",
        "cloud330": IMAGES_CLOUD_PREFIX + "networks5.png",
        "cloud331": IMAGES_CLOUD_PREFIX + "createnew6.png",
        "cloud332": IMAGES_CLOUD_PREFIX + "createnew7.png",
        "cloud333": IMAGES_CLOUD_PREFIX + "createnew8.png",
        "cloud334": IMAGES_CLOUD_PREFIX + "createnew9.png",
        "cloud335": IMAGES_CLOUD_PREFIX + "createnew10.png",
        "cloud336": IMAGES_CLOUD_PREFIX + "createnew11.png",
        "cloud337": IMAGES_CLOUD_PREFIX + "createnew12.png",
        "cloud338": IMAGES_CLOUD_PREFIX + "createnew13.png",
        "cloud339": IMAGES_CLOUD_PREFIX + "createnew14.png",
        "cloud340": IMAGES_CLOUD_PREFIX + "accessvm2.png",
        "cloud341": IMAGES_CLOUD_PREFIX + "accessvm3.png",
        "cloud342": IMAGES_CLOUD_PREFIX + "accessvm4v2.png",
        "cloud343": IMAGES_CLOUD_PREFIX + "sudo-su-eouser.png",
        "cloud344": IMAGES_CLOUD_PREFIX + "some-nodes.png",
        "cloud345": IMAGES_CLOUD_PREFIX + "fedora-image.png",
        "cloud346": IMAGES_CLOUD_PREFIX + "accessvm5.png",
        "cloud347": IMAGES_CLOUD_PREFIX + "clone2.png",
        "cloud348": IMAGES_CLOUD_PREFIX + "clone3.png",
        "cloud349": IMAGES_CLOUD_PREFIX + "create-windows-vm-horizon-web-console-01.png",
        "cloud350": IMAGES_CLOUD_PREFIX + "create-windows-vm-horizon-web-console-02.png",
        "cloud351": IMAGES_CLOUD_PREFIX + "create-windows-vm-horizon-web-console-03.png",
        "cloud352": IMAGES_CLOUD_PREFIX + "create-windows-vm-horizon-web-console-04.png",
        "cloud353": IMAGES_CLOUD_PREFIX + "create-windows-vm-horizon-web-console-05.png",
        "cloud354": IMAGES_CLOUD_PREFIX + "create-windows-vm-horizon-web-console-06.png",
        "cloud355": IMAGES_CLOUD_PREFIX + "create-windows-vm-horizon-web-console-07.png",
        "cloud356": IMAGES_CLOUD_PREFIX + "create-windows-vm-horizon-web-console-09.png",
        "cloud357": IMAGES_CLOUD_PREFIX + "create-windows-vm-horizon-web-console-21.png",
        "cloud358": IMAGES_CLOUD_PREFIX + "create-windows-vm-horizon-web-console-10.png",
        "cloud359": IMAGES_CLOUD_PREFIX + "create-windows-vm-horizon-web-console-11.png",
        "cloud360": IMAGES_CLOUD_PREFIX + "create-windows-vm-horizon-web-console-12.png",
        "cloud361": IMAGES_CLOUD_PREFIX + "create-windows-vm-horizon-web-console-13.png",
        "cloud362": IMAGES_CLOUD_PREFIX + "create-windows-vm-horizon-web-console-14.png",
        "cloud363": IMAGES_CLOUD_PREFIX + "create-windows-vm-horizon-web-console-15.png",
        "cloud364": IMAGES_CLOUD_PREFIX + "create-windows-vm-horizon-web-console-16.png",
        "cloud365": IMAGES_CLOUD_PREFIX + "create-windows-vm-horizon-web-console-17.png",
        "cloud366": IMAGES_CLOUD_PREFIX + "create-windows-vm-horizon-web-console-18.png",
        "cloud367": IMAGES_CLOUD_PREFIX + "create-windows-vm-horizon-web-console-19.png",
        "cloud368": IMAGES_CLOUD_PREFIX + "create-windows-vm-horizon-web-console-26.png",
        "cloud369": IMAGES_CLOUD_PREFIX + "create-windows-vm-horizon-web-console-27.png",
        "cloud370": IMAGES_CLOUD_PREFIX + "create-windows-vm-horizon-web-console-28.png",
        "cloud371": IMAGES_CLOUD_PREFIX + "create-linux-linux-04.png",
        "cloud372": IMAGES_CLOUD_PREFIX + "create-linux-linux-05.png",
        "cloud373": IMAGES_CLOUD_PREFIX + "boot-source.png",
        "cloud374": IMAGES_CLOUD_PREFIX + "create-linux-linux-06.png",
        "cloud375": IMAGES_CLOUD_PREFIX + "create-linux-linux-07.png",
        "cloud376": IMAGES_CLOUD_PREFIX + "yellow-triangles.png",
        "cloud377": IMAGES_CLOUD_PREFIX + "create-linux-linux-08.png",
        "cloud378": IMAGES_CLOUD_PREFIX + "create-linux-linux-09.png",
        "cloud379": IMAGES_CLOUD_PREFIX + "create-linux-linux-10.png",
        "cloud380": IMAGES_CLOUD_PREFIX + "create-linux-linux-12.png",
        "cloud381": IMAGES_CLOUD_PREFIX + "create-linux-linux-13.png",
        "cloud382": IMAGES_CLOUD_PREFIX + "ip-address-from-article.png",
        "cloud383": IMAGES_CLOUD_PREFIX + "putty-02.png",
        "cloud384": IMAGES_CLOUD_PREFIX + "putty-03.png",
        "cloud385": IMAGES_CLOUD_PREFIX + "putty-04.png",
        "cloud386": IMAGES_CLOUD_PREFIX + "putty-05.png",
        "cloud387": IMAGES_CLOUD_PREFIX + "putty-06.png",
        "cloud388": IMAGES_CLOUD_PREFIX + "putty-07.png",
        "cloud389": IMAGES_CLOUD_PREFIX + "putty-08.png",
        "cloud390": IMAGES_CLOUD_PREFIX + "putty-09.png",
        "cloud391": IMAGES_CLOUD_PREFIX + "putty-10.png",
        "cloud392": IMAGES_CLOUD_PREFIX + "putty-11.png",
        "cloud393": IMAGES_CLOUD_PREFIX + "key-location-putty.png",
        "cloud394": IMAGES_CLOUD_PREFIX + "putty-12.png",
        "cloud395": IMAGES_CLOUD_PREFIX + "putty-13.png",
        "cloud396": IMAGES_CLOUD_PREFIX + "putty-14.png",
        "cloud397": IMAGES_CLOUD_PREFIX + "putty-15.png",
        "cloud398": IMAGES_CLOUD_PREFIX + "putty-16.png",
        "cloud399": IMAGES_CLOUD_PREFIX + "start-vm-from-volume-snapshot-cli-08.png",
        "cloud400": IMAGES_CLOUD_PREFIX + "start-vm-from-volume-snapshot-cli-09.png",
        "cloud401": IMAGES_CLOUD_PREFIX + "start-vm-from-volume-snapshot-cli-10.png",
        "cloud402": IMAGES_CLOUD_PREFIX + "start-vm-from-volume-snapshot-cli-11.png",
        "cloud403": IMAGES_CLOUD_PREFIX + "start-vm-from-volume-snapshot-cli-13.png",
        "cloud404": IMAGES_CLOUD_PREFIX + "openstack-server-create-help.png",
        "cloud405": IMAGES_CLOUD_PREFIX + "create-vm-cli-1.png",
        "cloud406": IMAGES_CLOUD_PREFIX + "screenshot-20241006-124004.png",
        "cloud407": IMAGES_CLOUD_PREFIX + "screenshot-20241006-125234.png",
        "cloud408": IMAGES_CLOUD_PREFIX + "screenshot-20241006-132619.png",
        "cloud409": IMAGES_CLOUD_PREFIX + "screenshot-20241006-125651.png",
        "cloud410": IMAGES_CLOUD_PREFIX + "screenshot-20241006-130817.png",
        "cloud411": IMAGES_CLOUD_PREFIX + "screenshot-20241006-132113.png",
        "cloud412": IMAGES_CLOUD_PREFIX + "screenshot-20241006-133524.png",
        "cloud413": IMAGES_CLOUD_PREFIX + "screenshot-20241006-134749.png",
        "cloud414": IMAGES_CLOUD_PREFIX + "screenshot-20241006-135229.png",
        "cloud415": IMAGES_CLOUD_PREFIX + "screenshot-20241006-143434.png",
        "cloud416": IMAGES_CLOUD_PREFIX + "screenshot-20241006-145844.png",
        "cloud417": IMAGES_CLOUD_PREFIX + "ww5.png",
        "cloud418": IMAGES_CLOUD_PREFIX + "ww6.png",
        "cloud419": IMAGES_CLOUD_PREFIX + "ww7.png",
        "cloud420": IMAGES_CLOUD_PREFIX + "ww8.png",
        "cloud421": IMAGES_CLOUD_PREFIX + "ww9.png",
        "cloud422": IMAGES_CLOUD_PREFIX + "ww10.png",
        "cloud423": IMAGES_CLOUD_PREFIX + "ww11.png",
        "cloud424": IMAGES_CLOUD_PREFIX + "ww12.png",
        "cloud425": IMAGES_CLOUD_PREFIX + "ww13.png",
        "cloud426": IMAGES_CLOUD_PREFIX + "ww14.png",
        "cloud427": IMAGES_CLOUD_PREFIX + "ww15.png",
        "cloud428": IMAGES_CLOUD_PREFIX + "ww16.png",
        "cloud429": IMAGES_CLOUD_PREFIX + "ww17.png",
        "cloud430": IMAGES_CLOUD_PREFIX + "ww18.png",
        "cloud431": IMAGES_CLOUD_PREFIX + "ww19.png",
        "cloud432": IMAGES_CLOUD_PREFIX + "ww20.png",
        "cloud433": IMAGES_CLOUD_PREFIX + "lw1.png",
        "cloud434": IMAGES_CLOUD_PREFIX + "lw2.png",
        "cloud435": IMAGES_CLOUD_PREFIX + "lw3.png",
        "cloud436": IMAGES_CLOUD_PREFIX + "lw4.png",
        "cloud437": IMAGES_CLOUD_PREFIX + "lw5.png",
        "cloud438": IMAGES_CLOUD_PREFIX + "lw6.png",
        "cloud439": IMAGES_CLOUD_PREFIX + "lw7.png",
        "cloud440": IMAGES_CLOUD_PREFIX + "lw8.png",
        "cloud441": IMAGES_CLOUD_PREFIX + "lw9.png",
        "cloud442": IMAGES_CLOUD_PREFIX + "lw10.png",
        "cloud443": IMAGES_CLOUD_PREFIX + "lw11.png",
        "cloud444": IMAGES_CLOUD_PREFIX + "lw12.png",
        "cloud445": IMAGES_CLOUD_PREFIX + "lw13.png",
        "cloud446": IMAGES_CLOUD_PREFIX + "lw14.png",
        "cloud447": IMAGES_CLOUD_PREFIX + "lw15.png",
        "cloud448": IMAGES_CLOUD_PREFIX + "lw16.png",
        "cloud449": IMAGES_CLOUD_PREFIX + "lw17.png",
        "cloud450": IMAGES_CLOUD_PREFIX + "lw18.png",
        "cloud451": IMAGES_CLOUD_PREFIX + "lw19.png",
        "cloud452": IMAGES_CLOUD_PREFIX + "uses-ephemeral.png",
        "cloud453": IMAGES_CLOUD_PREFIX + "shut-off-instance.png",
        "cloud454": IMAGES_CLOUD_PREFIX + "instance-ephemeral-shut-off.png",
        "cloud455": IMAGES_CLOUD_PREFIX + "instance-ephemeral-create-snapshot.png",
        "cloud456": IMAGES_CLOUD_PREFIX + "instance-ephemeral-snapshot.png",
        "cloud457": IMAGES_CLOUD_PREFIX + "instance-blue-green.png",
        "cloud458": IMAGES_CLOUD_PREFIX + "instance-persistent-created.png",
        "cloud459": IMAGES_CLOUD_PREFIX + "instance-persistent-volumes-volumes.png",
        "cloud460": IMAGES_CLOUD_PREFIX + "instance-persistent-shut-down-indees.png",
        "cloud461": IMAGES_CLOUD_PREFIX + "instance-persistent-create-shanpshot-button.png",
        "cloud462": IMAGES_CLOUD_PREFIX + "instance-persistent-new-name.png",
        "cloud463": IMAGES_CLOUD_PREFIX + "instance-persistent-active-0bytes.png",
        "cloud464": IMAGES_CLOUD_PREFIX + "instance-persistent-show-data.png",
        "cloud465": IMAGES_CLOUD_PREFIX + "instance-persistent-volume-shapshot.png",
        "cloud466": IMAGES_CLOUD_PREFIX + "how-to-create-instance-snapshot-horizon-13.png",
        "cloud467": IMAGES_CLOUD_PREFIX + "keypair1.png",
        "cloud468": IMAGES_CLOUD_PREFIX + "keypair2.png",
        "cloud469": IMAGES_CLOUD_PREFIX + "keypair3.png",
        "cloud470": IMAGES_CLOUD_PREFIX + "keypair4.png",
        "cloud471": IMAGES_CLOUD_PREFIX + "keypair5.png",
        "cloud472": IMAGES_CLOUD_PREFIX + "newvm1.png",
        "cloud473": IMAGES_CLOUD_PREFIX + "newvm2.png",
        "cloud474": IMAGES_CLOUD_PREFIX + "newvm3.png",
        "cloud475": IMAGES_CLOUD_PREFIX + "newvm4.png",
        "cloud476": IMAGES_CLOUD_PREFIX + "newvm5.png",
        "cloud477": IMAGES_CLOUD_PREFIX + "newvm6.png",
        "cloud478": IMAGES_CLOUD_PREFIX + "newvm7.png",
        "cloud479": IMAGES_CLOUD_PREFIX + "newvm8.png",
        "cloud480": IMAGES_CLOUD_PREFIX + "newvm9.png",
        "cloud481": IMAGES_CLOUD_PREFIX + "newvm10.png",
        "cloud482": IMAGES_CLOUD_PREFIX + "newvm11.png",
        "cloud483": IMAGES_CLOUD_PREFIX + "newvm12.png",
        "cloud484": IMAGES_CLOUD_PREFIX + "newvm13.png",
        "cloud485": IMAGES_CLOUD_PREFIX + "fixconsole.png",
        "cloud486": IMAGES_CLOUD_PREFIX + "generate-credentials.png",
        "cloud487": IMAGES_CLOUD_PREFIX + "several-ec2-pairs.png",
        "cloud488": IMAGES_CLOUD_PREFIX + "removed-ec2-empty.png",
        "cloud489": IMAGES_CLOUD_PREFIX + "credential-create-help.png",
        "cloud490": IMAGES_CLOUD_PREFIX + "create-new-with-name.png",
        "cloud491": IMAGES_CLOUD_PREFIX + "complete-example.png",
        "cloud492": IMAGES_CLOUD_PREFIX + "create-credential.png",
        "cloud493": IMAGES_CLOUD_PREFIX + "nano-values.png",
        "cloud494": IMAGES_CLOUD_PREFIX + "export-os-cloud.png",
        "cloud495": IMAGES_CLOUD_PREFIX + "cli-os-cloud.png",
        "cloud496": IMAGES_CLOUD_PREFIX + "snap00.png",
        "cloud497": IMAGES_CLOUD_PREFIX + "snap01.png",
        "cloud498": IMAGES_CLOUD_PREFIX + "snap3.png",
        "cloud499": IMAGES_CLOUD_PREFIX + "snap4.png",
        "cloud500": IMAGES_CLOUD_PREFIX + "snap5.png",
        "cloud501": IMAGES_CLOUD_PREFIX + "snap6.png",
        "cloud502": IMAGES_CLOUD_PREFIX + "snap7.png",
        "cloud503": IMAGES_CLOUD_PREFIX + "snap8.png",
        "cloud504": IMAGES_CLOUD_PREFIX + "snap1.png",
        "cloud505": IMAGES_CLOUD_PREFIX + "snap2.png",
        "cloud506": IMAGES_CLOUD_PREFIX + "start-vm-instance-snapshot-horizon-09.png",
        "cloud507": IMAGES_CLOUD_PREFIX + "launch-instance-details.png",
        "cloud508": IMAGES_CLOUD_PREFIX + "launch-instance-source.png",
        "cloud509": IMAGES_CLOUD_PREFIX + "start-vm-instance-snapshot-horizon-01.png",
        "cloud510": IMAGES_CLOUD_PREFIX + "start-vm-instance-snapshot-horizon-02.png",
        "cloud511": IMAGES_CLOUD_PREFIX + "start-vm-instance-snapshot-horizon-03.png",
        "cloud512": IMAGES_CLOUD_PREFIX + "start-vm-instance-snapshot-horizon-04.png",
        "cloud513": IMAGES_CLOUD_PREFIX + "launch-instance-flavor.png",
        "cloud514": IMAGES_CLOUD_PREFIX + "launch-instance-networks.png",
        "cloud515": IMAGES_CLOUD_PREFIX + "launch-instance-security-groups.png",
        "cloud516": IMAGES_CLOUD_PREFIX + "launch-instance-key-pair.png",
        "cloud517": IMAGES_CLOUD_PREFIX + "start-vm-instance-snapshot-horizon-05.png",
        "cloud518": IMAGES_CLOUD_PREFIX + "launch-instance-launch-instance.png",
        "cloud519": IMAGES_CLOUD_PREFIX + "launch-instance-created-instances.png",
        "cloud520": IMAGES_CLOUD_PREFIX + "unavailable-network.png",
        "cloud521": IMAGES_CLOUD_PREFIX + "start-vm-instance-snapshot-horizon-06.png",
        "cloud522": IMAGES_CLOUD_PREFIX + "start-vm-instance-snapshot-horizon-07.png",
        "cloud523": IMAGES_CLOUD_PREFIX + "start-vm-instance-snapshot-horizon-08.png",
        "cloud524": IMAGES_CLOUD_PREFIX + "transfer-volume-between-projects-horizon-32.png",
        "cloud525": IMAGES_CLOUD_PREFIX + "transfer-volume-between-projects-horizon-37.png",
        "cloud526": IMAGES_CLOUD_PREFIX + "transfer-volume-between-projects-horizon-33.png",
        "cloud527": IMAGES_CLOUD_PREFIX + "transfer-volume-between-projects-horizon-15.png",
        "cloud528": IMAGES_CLOUD_PREFIX + "transfer-volume-between-projects-horizon-16.png",
        "cloud529": IMAGES_CLOUD_PREFIX + "transfer-volume-between-projects-horizon-17.png",
        "cloud530": IMAGES_CLOUD_PREFIX + "transfer-volume-between-projects-horizon-18.png",
        "cloud531": IMAGES_CLOUD_PREFIX + "transfer-volume-between-projects-horizon-19.png",
        "cloud532": IMAGES_CLOUD_PREFIX + "transfer-volume-between-projects-horizon-20.png",
        "cloud533": IMAGES_CLOUD_PREFIX + "transfer-volume-between-projects-horizon-21.png",
        "cloud534": IMAGES_CLOUD_PREFIX + "transfer-volume-between-projects-horizon-35.png",
        "cloud535": IMAGES_CLOUD_PREFIX + "transfer-volume-between-projects-horizon-36.png",
        "cloud536": IMAGES_CLOUD_PREFIX + "transfer-volume-between-projects-horizon-38.png",
        "cloud537": IMAGES_CLOUD_PREFIX + "transfer-volume-between-projects-horizon-11.png",
        "cloud538": IMAGES_CLOUD_PREFIX + "upload-image-horizon-01.png",
        "cloud539": IMAGES_CLOUD_PREFIX + "upload-image-horizon-02.png",
        "cloud540": IMAGES_CLOUD_PREFIX + "image-options-explanation.png",
        "cloud541": IMAGES_CLOUD_PREFIX + "format-image-upload.png",
        "cloud542": IMAGES_CLOUD_PREFIX + "upload-image-horizon-10.png",
        "cloud543": IMAGES_CLOUD_PREFIX + "upload-image-horizon-03.png",
        "cloud544": IMAGES_CLOUD_PREFIX + "upload-image-horizon-04.png",
        "cloud545": IMAGES_CLOUD_PREFIX + "debian-test-created.png",
        "cloud546": IMAGES_CLOUD_PREFIX + "upload-image-horizon-07.png",
        "cloud547": IMAGES_CLOUD_PREFIX + "upload-image-horizon-08.png",
        "cloud548": IMAGES_CLOUD_PREFIX + "upload-image-cli-10.png",
        "cloud549": IMAGES_CLOUD_PREFIX + "upload-image-cli-01.png",
        "cloud550": IMAGES_CLOUD_PREFIX + "upload-image-cli-12.png",
        "cloud551": IMAGES_CLOUD_PREFIX + "upload-image-cli-02.png",
        "cloud552": IMAGES_CLOUD_PREFIX + "upload-image-cli-03.png",
        "cloud553": IMAGES_CLOUD_PREFIX + "upload-image-cli-11.png",
        "cloud554": IMAGES_CLOUD_PREFIX + "new-docker-1.png",
        "cloud555": IMAGES_CLOUD_PREFIX + "use-docker-9.png",
        "cloud556": IMAGES_CLOUD_PREFIX + "use-docker-4.png",
        "cloud557": IMAGES_CLOUD_PREFIX + "use-docker-5.png",
        "cloud558": IMAGES_CLOUD_PREFIX + "use-docker-6.png",
        "cloud559": IMAGES_CLOUD_PREFIX + "use-docker-7.png",
        "cloud560": IMAGES_CLOUD_PREFIX + "linux-gui-03.png",
        "cloud561": IMAGES_CLOUD_PREFIX + "linux-gui-04.png",
        "cloud562": IMAGES_CLOUD_PREFIX + "linux-gui-05.png",
        "cloud563": IMAGES_CLOUD_PREFIX + "linux-gui-06.png",
        "cloud564": IMAGES_CLOUD_PREFIX + "linux-gui-07.png",
        "cloud565": IMAGES_CLOUD_PREFIX + "linux-gui-08.png",
        "cloud566": IMAGES_CLOUD_PREFIX + "linux-gui-09.png",
        "cloud567": IMAGES_CLOUD_PREFIX + "linux-gui-11.png",
        "cloud568": IMAGES_CLOUD_PREFIX + "linux-gui-12.png",
        "cloud569": IMAGES_CLOUD_PREFIX + "linux-gui-13.png",
        "cloud570": IMAGES_CLOUD_PREFIX + "linux-gui-14.png",
        "cloud571": IMAGES_CLOUD_PREFIX + "linux-gui-15.png",
        "cloud572": IMAGES_CLOUD_PREFIX + "linux-gui-16.png",
        "cloud573": IMAGES_CLOUD_PREFIX + "linux-gui-17.png",
        "cloud574": IMAGES_CLOUD_PREFIX + "use-security-groups-1.png",
        "cloud575": IMAGES_CLOUD_PREFIX + "use-security-groups-2.png",
        "cloud576": IMAGES_CLOUD_PREFIX + "use-security-groups-3.png",
        "cloud577": IMAGES_CLOUD_PREFIX + "use-security-groups-4.png",
        "cloud578": IMAGES_CLOUD_PREFIX + "use-security-groups-5.png",
        "cloud579": IMAGES_CLOUD_PREFIX + "use-security-groups-6.png",
        "cloud580": IMAGES_CLOUD_PREFIX + "use-security-groups-7.png",
        "cloud581": IMAGES_CLOUD_PREFIX + "install01.png",
        "cloud582": IMAGES_CLOUD_PREFIX + "install02.png",
        "cloud583": IMAGES_CLOUD_PREFIX + "install03.png",
        "cloud584": IMAGES_CLOUD_PREFIX + "install04-noted.png",
        "cloud585": IMAGES_CLOUD_PREFIX + "screenshot-20241014-112929.png",
        "cloud586": IMAGES_CLOUD_PREFIX + "image-2024-04-24-15-13-21.png",
        "cloud587": IMAGES_CLOUD_PREFIX + "openstack-user-roles-create-4.png",
        "cloud588": IMAGES_CLOUD_PREFIX + "user-roles-list-create-2.png",
        "cloud589": IMAGES_CLOUD_PREFIX + "user-roles-list-create-1.png",
        "cloud590": IMAGES_CLOUD_PREFIX + "user-roles-list-create-4.png",
        "cloud591": IMAGES_CLOUD_PREFIX + "user-roles-list-create-5.png",
        "cloud592": IMAGES_CLOUD_PREFIX + "user-roles-list-create-6.png",
        "cloud593": IMAGES_CLOUD_PREFIX + "user-roles-list-create-3.png",
        "cloud594": IMAGES_CLOUD_PREFIX + "resize-vm-horizon-1.png",
        "cloud595": IMAGES_CLOUD_PREFIX + "resize-vm-horizon-2.png",
        "cloud596": IMAGES_CLOUD_PREFIX + "resize-vm-horizon-3.png",
        "cloud597": IMAGES_CLOUD_PREFIX + "resize-vm-horizon-4.png",
        "cloud598": IMAGES_CLOUD_PREFIX + "resize-vm-horizon-5.png",
        "cloud599": IMAGES_CLOUD_PREFIX + "fwaas-openvpn-v2-34.png",
        "cloud600": IMAGES_CLOUD_PREFIX + "resize-vm-horizon-10.png",
        "cloud601": IMAGES_CLOUD_PREFIX + "resize-vm-horizon-11.png",
        "cloud602": IMAGES_CLOUD_PREFIX + "resize-vm-horizon-8.png",
        "cloud603": IMAGES_CLOUD_PREFIX + "resize-vm-horizon-7.png",
        "cloud604": IMAGES_CLOUD_PREFIX + "waw3-2-cloud-activated.png",
        "cloud605": IMAGES_CLOUD_PREFIX + "flavors-listed-spot.png",
        "cloud606": IMAGES_CLOUD_PREFIX + "spot-flavors-when-creating.png",
        "cloud607": IMAGES_CLOUD_PREFIX + "spot-hma-created.png",
        "cloud608": IMAGES_CLOUD_PREFIX + "value-of-spot.png",
        "cloud609": IMAGES_CLOUD_PREFIX + "resize-instance.png",
        "cloud610": IMAGES_CLOUD_PREFIX + "statuspower.png",
        "cloud611": IMAGES_CLOUD_PREFIX + "volno1.png",
        "cloud612": IMAGES_CLOUD_PREFIX + "volno2.png",
        "cloud613": IMAGES_CLOUD_PREFIX + "volno3.png",
        "cloud614": IMAGES_CLOUD_PREFIX + "volno4.png",
        "cloud615": IMAGES_CLOUD_PREFIX + "volno5.png",
        "cloud616": IMAGES_CLOUD_PREFIX + "volyes1.png",
        "cloud617": IMAGES_CLOUD_PREFIX + "volyes2.png",
        "cloud618": IMAGES_CLOUD_PREFIX + "volyes3.png",
        "cloud619": IMAGES_CLOUD_PREFIX + "volyes4.png",
        "cloud620": IMAGES_CLOUD_PREFIX + "volyes5.png",
        "cloud621": IMAGES_CLOUD_PREFIX + "volyes6.png",
        "cloud622": IMAGES_CLOUD_PREFIX + "volyes7.png",
        "cloud623": IMAGES_CLOUD_PREFIX + "volyes8.png",
        "cloud624": IMAGES_CLOUD_PREFIX + "volyes9.png",
        "cloud625": IMAGES_CLOUD_PREFIX + "volyes10.png",
        "cloud626": IMAGES_CLOUD_PREFIX + "volyes11.png",
        "cloud627": IMAGES_CLOUD_PREFIX + "volyes12.png",
        "cloud628": IMAGES_CLOUD_PREFIX + "volyes13.png",
        "cloud629": IMAGES_CLOUD_PREFIX + "volyes14.png",
        "cloud630": IMAGES_CLOUD_PREFIX + "volyes15.png",
        "cloud631": IMAGES_CLOUD_PREFIX + "volyes16.png",
        "cloud632": IMAGES_CLOUD_PREFIX + "project1.png",
        "cloud633": IMAGES_CLOUD_PREFIX + "project2.png",
    },

    "datavolume_images": {
        "datavolume001": IMAGES_DATAVOLUME_PREFIX + "create-volume.png",
        "datavolume002": IMAGES_DATAVOLUME_PREFIX + "bootable-versus-nonbootable-volume-21.png",
        "datavolume003": IMAGES_DATAVOLUME_PREFIX + "bootable-versus-nonbootable-volume-22.png",
        "datavolume004": IMAGES_DATAVOLUME_PREFIX + "bootable-versus-nonbootable-volume-09.png",
        "datavolume005": IMAGES_DATAVOLUME_PREFIX + "bootable-versus-nonbootable-volume-16.png",
        "datavolume006": IMAGES_DATAVOLUME_PREFIX + "bootable-versus-nonbootable-volume-07.png",
        "datavolume007": IMAGES_DATAVOLUME_PREFIX + "bootable-versus-nonbootable-volume-01.png",
        "datavolume008": IMAGES_DATAVOLUME_PREFIX + "bootable-versus-nonbootable-volume-02.png",
        "datavolume009": IMAGES_DATAVOLUME_PREFIX + "bootable-versus-nonbootable-volume-03.png",
        "datavolume010": IMAGES_DATAVOLUME_PREFIX + "bootable-versus-nonbootable-volume-04.png",
        "datavolume011": IMAGES_DATAVOLUME_PREFIX + "bootable-versus-nonbootable-volume-05.png",
        "datavolume012": IMAGES_DATAVOLUME_PREFIX + "bootable-versus-nonbootable-volume-06.png",
        "datavolume013": IMAGES_DATAVOLUME_PREFIX + "bootable-versus-nonbootable-volume-10.png",
        "datavolume014": IMAGES_DATAVOLUME_PREFIX + "bootable-versus-nonbootable-volume-11.png",
        "datavolume015": IMAGES_DATAVOLUME_PREFIX + "bootable-versus-nonbootable-volume-12.png",
        "datavolume016": IMAGES_DATAVOLUME_PREFIX + "bootable-versus-nonbootable-volume-13.png",
        "datavolume017": IMAGES_DATAVOLUME_PREFIX + "bootable-versus-nonbootable-volume-14.png",
        "datavolume018": IMAGES_DATAVOLUME_PREFIX + "bootable-versus-nonbootable-volume-08.png",
        "datavolume019": IMAGES_DATAVOLUME_PREFIX + "create-volume-windows-01.png",
        "datavolume020": IMAGES_DATAVOLUME_PREFIX + "create-volume-windows-02.png",
        "datavolume021": IMAGES_DATAVOLUME_PREFIX + "create-volume-windows-03.png",
        "datavolume022": IMAGES_DATAVOLUME_PREFIX + "create-volume-windows-04.png",
        "datavolume023": IMAGES_DATAVOLUME_PREFIX + "create-volume-windows-05.png",
        "datavolume024": IMAGES_DATAVOLUME_PREFIX + "create-volume-windows-06.png",
        "datavolume025": IMAGES_DATAVOLUME_PREFIX + "create-volume-windows-07.png",
        "datavolume026": IMAGES_DATAVOLUME_PREFIX + "create-volume-windows-08.png",
        "datavolume027": IMAGES_DATAVOLUME_PREFIX + "create-volume-windows-09.png",
        "datavolume028": IMAGES_DATAVOLUME_PREFIX + "create-volume-windows-10.png",
        "datavolume029": IMAGES_DATAVOLUME_PREFIX + "create-volume-windows-11.png",
        "datavolume030": IMAGES_DATAVOLUME_PREFIX + "create-volume-windows-12.png",
        "datavolume031": IMAGES_DATAVOLUME_PREFIX + "create-volume-windows-13.png",
        "datavolume032": IMAGES_DATAVOLUME_PREFIX + "create-volume-windows-14.png",
        "datavolume033": IMAGES_DATAVOLUME_PREFIX + "create-volume-windows-15.png",
        "datavolume034": IMAGES_DATAVOLUME_PREFIX + "create-volume-windows-16.png",
        "datavolume035": IMAGES_DATAVOLUME_PREFIX + "create-volume-windows-17.png",
        "datavolume036": IMAGES_DATAVOLUME_PREFIX + "volume-backup-01.png",
        "datavolume037": IMAGES_DATAVOLUME_PREFIX + "volume-backup-02.png",
        "datavolume038": IMAGES_DATAVOLUME_PREFIX + "volume-backup-03.png",
        "datavolume039": IMAGES_DATAVOLUME_PREFIX + "volume-backup-04.png",
        "datavolume040": IMAGES_DATAVOLUME_PREFIX + "volume-backup-05.png",
        "datavolume041": IMAGES_DATAVOLUME_PREFIX + "volume-backup-06.png",
        "datavolume042": IMAGES_DATAVOLUME_PREFIX + "volume-backup-07.png",
        "datavolume043": IMAGES_DATAVOLUME_PREFIX + "volume-backup-08.png",
        "datavolume044": IMAGES_DATAVOLUME_PREFIX + "volume-backup-09.png",
        "datavolume045": IMAGES_DATAVOLUME_PREFIX + "volume-backup-10.png",
        "datavolume046": IMAGES_DATAVOLUME_PREFIX + "volume-backup-11.png",
        "datavolume047": IMAGES_DATAVOLUME_PREFIX + "volume-backup-12.png",
        "datavolume048": IMAGES_DATAVOLUME_PREFIX + "volume-backup-13.png",
        "datavolume049": IMAGES_DATAVOLUME_PREFIX + "volume-backup-14.png",
        "datavolume050": IMAGES_DATAVOLUME_PREFIX + "volume-backup-15.png",
        "datavolume051": IMAGES_DATAVOLUME_PREFIX + "volume-backup-16.png",
        "datavolume052": IMAGES_DATAVOLUME_PREFIX + "volume-backup-17.png",
        "datavolume053": IMAGES_DATAVOLUME_PREFIX + "volume-backup-18.png",
        "datavolume054": IMAGES_DATAVOLUME_PREFIX + "volume-less-01.png",
        "datavolume055": IMAGES_DATAVOLUME_PREFIX + "volume-less-02.png",
        "datavolume056": IMAGES_DATAVOLUME_PREFIX + "volume-less-03.png",
        "datavolume057": IMAGES_DATAVOLUME_PREFIX + "volume-less-04.png",
        "datavolume058": IMAGES_DATAVOLUME_PREFIX + "volume-less-05.png",
        "datavolume059": IMAGES_DATAVOLUME_PREFIX + "volume-less-06.png",
        "datavolume060": IMAGES_DATAVOLUME_PREFIX + "volume-less-07.png",
        "datavolume061": IMAGES_DATAVOLUME_PREFIX + "volume-less-08.png",
        "datavolume062": IMAGES_DATAVOLUME_PREFIX + "volume-less-09.png",
        "datavolume063": IMAGES_DATAVOLUME_PREFIX + "volume-less-10.png",
        "datavolume064": IMAGES_DATAVOLUME_PREFIX + "volume-less-11.png",
        "datavolume065": IMAGES_DATAVOLUME_PREFIX + "volume-more-01.png",
        "datavolume066": IMAGES_DATAVOLUME_PREFIX + "volume-more-02.png",
        "datavolume067": IMAGES_DATAVOLUME_PREFIX + "volume-more-03.png",
        "datavolume068": IMAGES_DATAVOLUME_PREFIX + "volume-more-04.png",
        "datavolume069": IMAGES_DATAVOLUME_PREFIX + "volume-more-05.png",
        "datavolume070": IMAGES_DATAVOLUME_PREFIX + "volume-more-06.png",
        "datavolume071": IMAGES_DATAVOLUME_PREFIX + "volume-more-07.png",
        "datavolume072": IMAGES_DATAVOLUME_PREFIX + "volume-more-08.png",
        "datavolume073": IMAGES_DATAVOLUME_PREFIX + "volume-more-09.png",
        "datavolume074": IMAGES_DATAVOLUME_PREFIX + "volume-more-10.png",
        "datavolume075": IMAGES_DATAVOLUME_PREFIX + "volume-more-11.png",
        "datavolume076": IMAGES_DATAVOLUME_PREFIX + "vol1.png",
        "datavolume077": IMAGES_DATAVOLUME_PREFIX + "vol2.png",
        "datavolume078": IMAGES_DATAVOLUME_PREFIX + "vol3.png",
        "datavolume079": IMAGES_DATAVOLUME_PREFIX + "vol4.png",
        "datavolume080": IMAGES_DATAVOLUME_PREFIX + "vol5.png",
        "datavolume081": IMAGES_DATAVOLUME_PREFIX + "vol6.png",
        "datavolume082": IMAGES_DATAVOLUME_PREFIX + "how-to-move-data-volume-horizon-33.png",
        "datavolume083": IMAGES_DATAVOLUME_PREFIX + "how-to-move-data-volume-horizon-34.png",
        "datavolume084": IMAGES_DATAVOLUME_PREFIX + "how-to-move-data-volume-horizon-05.png",
        "datavolume085": IMAGES_DATAVOLUME_PREFIX + "how-to-move-data-volume-horizon-30.png",
        "datavolume086": IMAGES_DATAVOLUME_PREFIX + "how-to-move-data-volume-horizon-06.png",
        "datavolume087": IMAGES_DATAVOLUME_PREFIX + "how-to-move-data-volume-horizon-07.png",
        "datavolume088": IMAGES_DATAVOLUME_PREFIX + "how-to-move-data-volume-horizon-08.png",
        "datavolume089": IMAGES_DATAVOLUME_PREFIX + "how-to-move-data-volume-horizon-09.png",
        "datavolume090": IMAGES_DATAVOLUME_PREFIX + "how-to-move-data-volume-horizon-10.png",
        "datavolume091": IMAGES_DATAVOLUME_PREFIX + "how-to-move-data-volume-horizon-27.png",
        "datavolume092": IMAGES_DATAVOLUME_PREFIX + "how-to-move-data-volume-horizon-28.png",
        "datavolume093": IMAGES_DATAVOLUME_PREFIX + "how-to-move-data-volume-horizon-29.png",
        "datavolume094": IMAGES_DATAVOLUME_PREFIX + "how-to-restore-volume-from-snapshot-horizon-01.png",
        "datavolume095": IMAGES_DATAVOLUME_PREFIX + "how-to-restore-volume-from-snapshot-horizon-02.png",
        "datavolume096": IMAGES_DATAVOLUME_PREFIX + "how-to-restore-volume-from-snapshot-horizon-03.png",
        "datavolume097": IMAGES_DATAVOLUME_PREFIX + "how-to-restore-volume-from-snapshot-horizon-04.png",
        "datavolume098": IMAGES_DATAVOLUME_PREFIX + "how-to-restore-volume-from-snapshot-cli-01.png",
        "datavolume099": IMAGES_DATAVOLUME_PREFIX + "how-to-restore-volume-from-snapshot-cli-02.png",
        "datavolume100": IMAGES_DATAVOLUME_PREFIX + "how-to-restore-volume-from-snapshot-cli-03.png",
        "datavolume101": IMAGES_DATAVOLUME_PREFIX + "volsnap1.png",
        "datavolume102": IMAGES_DATAVOLUME_PREFIX + "volsnap2.png",
        "datavolume103": IMAGES_DATAVOLUME_PREFIX + "volsnap3.png",
        "datavolume104": IMAGES_DATAVOLUME_PREFIX + "volsnap4.png",
        "datavolume105": IMAGES_DATAVOLUME_PREFIX + "volsnap5.png",
    },

    "cuttingedge_images": {
        "cuttingedge001": IMAGES_CUTTINGEDGE_PREFIX + "jupyter-notebook-start.png",
    },

    "eodata_images": {
        "eodata001": IMAGES_EODATA_PREFIX + "eodata-mounted.png",
    },

    "networking_images": {
        "networking001": IMAGES_NETWORKING_PREFIX + "router-interfaces.png",
        "networking002": "ecis-lb-concept.png",
        "networking003": "ecis-lbflavors.png",
        "networking004": "ecis-lbcreate1.png",
        "networking005": "ecis-lbcreate2.png",
        "networking006": "ecis-lbcreate3.png",
        "networking007": "ecis-lbcreate4.png",
        "networking008": "ecis-lbcreate5.png",
        "networking009": "ecis-lbcreate6.png",
        "networking010": IMAGES_NETWORKING_PREFIX + "ssh1.png",
        "networking011": IMAGES_NETWORKING_PREFIX + "ssh2.png",
        "networking012": IMAGES_NETWORKING_PREFIX + "ssh3.png",
        "networking013": IMAGES_NETWORKING_PREFIX + "edit.png",
        "networking014": IMAGES_NETWORKING_PREFIX + "fip1.png",
        "networking015": IMAGES_NETWORKING_PREFIX + "fip2.png",
        "networking016": IMAGES_NETWORKING_PREFIX + "fip3.png",
        "networking017": IMAGES_NETWORKING_PREFIX + "fip4.png",
        "networking018": IMAGES_NETWORKING_PREFIX + "fip5.png",
        "networking019": IMAGES_NETWORKING_PREFIX + "fip6.png",
        "networking020": IMAGES_NETWORKING_PREFIX + "fip7.png",
        "networking021": IMAGES_NETWORKING_PREFIX + "fip8.png",
        "networking022": IMAGES_NETWORKING_PREFIX + "fip9.png",
        "networking023": IMAGES_NETWORKING_PREFIX + "ssh-import-01.png",
        "networking024": IMAGES_NETWORKING_PREFIX + "ssh-import-02.png",
        "networking025": IMAGES_NETWORKING_PREFIX + "ssh-import-03.png",
        "networking026": IMAGES_NETWORKING_PREFIX + "ssh-import-04.png",
        "networking027": IMAGES_NETWORKING_PREFIX + "pastebin1.png",
        "networking028": IMAGES_NETWORKING_PREFIX + "pastebin2.png",
        "networking029": IMAGES_NETWORKING_PREFIX + "pastebin3.png",
        "networking030": IMAGES_NETWORKING_PREFIX + "pastebin4.png",
        "networking031": IMAGES_NETWORKING_PREFIX + "pastebin5.png",
        "networking032": IMAGES_NETWORKING_PREFIX + "ssh-linux1.png",
        "networking033": IMAGES_NETWORKING_PREFIX + "ssh-linux2.png",
        "networking034": IMAGES_NETWORKING_PREFIX + "irf-select-project.png",
        "networking035": IMAGES_NETWORKING_PREFIX + "irf-delete-floating-ip.png",
        "networking036": IMAGES_NETWORKING_PREFIX + "irf-delete-router.png",
        "networking037": IMAGES_NETWORKING_PREFIX + "irf-delete-snapshot.png",
        "networking038": IMAGES_NETWORKING_PREFIX + "irf-delete-volume.png",
        "networking039": IMAGES_NETWORKING_PREFIX + "irf-delete-instance.png",
        "networking040": IMAGES_NETWORKING_PREFIX + "irf-delete-project.png",
        "networking041": IMAGES_NETWORKING_PREFIX + "net1.png",
        "networking042": IMAGES_NETWORKING_PREFIX + "net2.png",
        "networking043": IMAGES_NETWORKING_PREFIX + "net3.png",
        "networking044": IMAGES_NETWORKING_PREFIX + "net4.png",
        "networking045": IMAGES_NETWORKING_PREFIX + "net5.png",
        "networking046": IMAGES_NETWORKING_PREFIX + "net6.png",
        "networking047": IMAGES_NETWORKING_PREFIX + "net7.png",
        "networking048": IMAGES_NETWORKING_PREFIX + "net8.png",
        "networking049": IMAGES_NETWORKING_PREFIX + "net9.png",
        "networking050": IMAGES_NETWORKING_PREFIX + "net10.png",
        "networking051": IMAGES_NETWORKING_PREFIX + "net11.png",
        "networking052": IMAGES_NETWORKING_PREFIX + "net12.png",
        "networking053": IMAGES_NETWORKING_PREFIX + "net13.png",
        "networking054": IMAGES_NETWORKING_PREFIX + "coz-py1.png",
        "networking055": IMAGES_NETWORKING_PREFIX + "coz-py2.png",
        "networking056": IMAGES_NETWORKING_PREFIX + "coz-py3.png",
        "networking057": IMAGES_NETWORKING_PREFIX + "coz-py4.png",
        "networking058": IMAGES_NETWORKING_PREFIX + "coz-py5.png",
        "networking059": IMAGES_NETWORKING_PREFIX + "coz-faqpython.png",
        "networking060": IMAGES_NETWORKING_PREFIX + "coz-py6.png",
        "networking061": IMAGES_NETWORKING_PREFIX + "mount-object-storage-file-with-eodata.png",
        "networking062": IMAGES_NETWORKING_PREFIX + "mount-eodata-windows-rclone-01.png",
        "networking063": IMAGES_NETWORKING_PREFIX + "mount-eodata-windows-rclone-02.png",
        "networking064": IMAGES_NETWORKING_PREFIX + "mount-eodata-windows-open-nssm-01.png",
        "networking065": IMAGES_NETWORKING_PREFIX + "mount-object-storage-windows-horizon-01.png",
        "networking066": IMAGES_NETWORKING_PREFIX + "screen224.png",
        "networking067": IMAGES_NETWORKING_PREFIX + "screen3-ds.png",
        "networking068": IMAGES_NETWORKING_PREFIX + "screen4-ds.png",
        "networking069": IMAGES_NETWORKING_PREFIX + "screen44-ds.png",
        "networking070": IMAGES_NETWORKING_PREFIX + "screen5-ds.png",
        "networking071": IMAGES_NETWORKING_PREFIX + "screen6-ds.png",
        "networking072": IMAGES_NETWORKING_PREFIX + "screen7.png",
        "networking073": IMAGES_NETWORKING_PREFIX + "screen8-ds.png",
        "networking074": IMAGES_NETWORKING_PREFIX + "screen9-ds.png",
        "networking075": IMAGES_NETWORKING_PREFIX + "scrn10-ds.png",
        "networking076": IMAGES_NETWORKING_PREFIX + "screen11.png",
        "networking077": IMAGES_NETWORKING_PREFIX + "screen12.png",
        "networking078": IMAGES_NETWORKING_PREFIX + "screen13.png",
        "networking079": IMAGES_NETWORKING_PREFIX + "screen14.png",
        "networking080": IMAGES_NETWORKING_PREFIX + "screen15-new.png",
        "networking081": IMAGES_NETWORKING_PREFIX + "fwaas-1.png",
        "networking082": IMAGES_NETWORKING_PREFIX + "screen16.png",
        "networking083": IMAGES_NETWORKING_PREFIX + "screen17b.png",
        "networking084": IMAGES_NETWORKING_PREFIX + "screen177-new.png",
        "networking085": IMAGES_NETWORKING_PREFIX + "screen178-new.png",
        "networking086": IMAGES_NETWORKING_PREFIX + "screen18-new.png",
        "networking087": IMAGES_NETWORKING_PREFIX + "screen19-new.png",
        "networking088": IMAGES_NETWORKING_PREFIX + "screen21.png",
        "networking089": IMAGES_NETWORKING_PREFIX + "screen22.png",
        "networking090": IMAGES_NETWORKING_PREFIX + "screen23-new.png",
        "networking091": IMAGES_NETWORKING_PREFIX + "firewall-v3-15-new.png",
        "networking092": IMAGES_NETWORKING_PREFIX + "configure-firewall-1.png",
        "networking093": IMAGES_NETWORKING_PREFIX + "configure-firewall-2.png",
        "networking094": IMAGES_NETWORKING_PREFIX + "configure-firewall-3.png",
        "networking095": IMAGES_NETWORKING_PREFIX + "configure-firewall-4.png",
        "networking096": IMAGES_NETWORKING_PREFIX + "configure-firewall-5.png",
        "networking097": IMAGES_NETWORKING_PREFIX + "configure-firewall-7.png",
        "networking098": IMAGES_NETWORKING_PREFIX + "configure-firewall-8.png",
        "networking099": IMAGES_NETWORKING_PREFIX + "configure-firewall-9-new.png",
        "networking100": IMAGES_NETWORKING_PREFIX + "configure-firewall-11-new.png",
        "networking101": IMAGES_NETWORKING_PREFIX + "configure-firewall-13.png",
        "networking102": IMAGES_NETWORKING_PREFIX + "configure-firewall-14-new.png",
        "networking103": IMAGES_NETWORKING_PREFIX + "fwaas-ssh.png",
        "networking104": IMAGES_NETWORKING_PREFIX + "fwaas-ssh2.png",
        "networking105": IMAGES_NETWORKING_PREFIX + "firewall-v3-9-new.png",
        "networking106": IMAGES_NETWORKING_PREFIX + "firewall-v3-1-new.png",
        "networking107": IMAGES_NETWORKING_PREFIX + "firewall-v3-2-new.png",
        "networking108": IMAGES_NETWORKING_PREFIX + "firewall-v3-3.png",
        "networking109": IMAGES_NETWORKING_PREFIX + "firewall-v3-4-new.png",
        "networking110": IMAGES_NETWORKING_PREFIX + "firewall-v3-18-new.png",
        "networking111": IMAGES_NETWORKING_PREFIX + "enter-root-pass.png",
        "networking112": IMAGES_NETWORKING_PREFIX + "firewall-v3-21.png",
        "networking113": IMAGES_NETWORKING_PREFIX + "firewall-v3-10.png",
        "networking114": IMAGES_NETWORKING_PREFIX + "firewall-v3-11-new.png",
        "networking115": IMAGES_NETWORKING_PREFIX + "firewall-v3-12-new.png",
        "networking116": IMAGES_NETWORKING_PREFIX + "fwaas-openvpn-v2-5.png",
        "networking117": IMAGES_NETWORKING_PREFIX + "firewall-v3-13-new.png",
        "networking118": IMAGES_NETWORKING_PREFIX + "create-user.png",
        "networking119": IMAGES_NETWORKING_PREFIX + "fwaas-openvpn-v2-7-new.png",
        "networking120": IMAGES_NETWORKING_PREFIX + "fwaas-openvpn-v2-8.png",
        "networking121": IMAGES_NETWORKING_PREFIX + "fwaas-openvpn-v2-9-new.png",
        "networking122": IMAGES_NETWORKING_PREFIX + "fwaas-openvpn-v2-10.png",
        "networking123": IMAGES_NETWORKING_PREFIX + "fwaas-openvpn-v2-11.png",
        "networking124": IMAGES_NETWORKING_PREFIX + "fwaas-openvpn-v2-12.png",
        "networking125": IMAGES_NETWORKING_PREFIX + "fwaas-openvpn-v2-13.png",
        "networking126": IMAGES_NETWORKING_PREFIX + "fwaas-openvpn-v2-14-new.png",
        "networking127": IMAGES_NETWORKING_PREFIX + "fwaas-openvpn-v2-16-new.png",
        "networking128": IMAGES_NETWORKING_PREFIX + "fwaas-openvpn-v2-20-new.png",
        "networking129": IMAGES_NETWORKING_PREFIX + "fwaas-openvpn-v2-21.png",
        "networking130": IMAGES_NETWORKING_PREFIX + "fwaas-openvpn-v2-22-new.png",
        "networking131": IMAGES_NETWORKING_PREFIX + "fwaas-openvpn-v2-23-new.png",
        "networking132": IMAGES_NETWORKING_PREFIX + "rule1.png",
        "networking133": IMAGES_NETWORKING_PREFIX + "rule2.png",
        "networking134": IMAGES_NETWORKING_PREFIX + "opt-interface.png",
        "networking135": IMAGES_NETWORKING_PREFIX + "rules-to-opt.png",
        "networking136": IMAGES_NETWORKING_PREFIX + "lan-interface.png",
        "networking137": IMAGES_NETWORKING_PREFIX + "lan-rule1.png",
        "networking138": IMAGES_NETWORKING_PREFIX + "lan-rule2.png",
        "networking139": IMAGES_NETWORKING_PREFIX + "lan-rule3.png",
        "networking140": IMAGES_NETWORKING_PREFIX + "lan-rule4.png",
        "networking141": IMAGES_NETWORKING_PREFIX + "clients-export.png",
        "networking142": IMAGES_NETWORKING_PREFIX + "top-corner.png",
        "networking143": IMAGES_NETWORKING_PREFIX + "top-corner2.png",
        "networking144": IMAGES_NETWORKING_PREFIX + "top-corner3.png",
        "networking145": IMAGES_NETWORKING_PREFIX + "fwaas-authuser-ovpn.png",
        "networking146": IMAGES_NETWORKING_PREFIX + "fwaas-ovpn-connected.png",
        "networking147": IMAGES_NETWORKING_PREFIX + "fwaas-test-connectopn-new.png",
        "networking148": IMAGES_NETWORKING_PREFIX + "ping.png",
        "networking149": IMAGES_NETWORKING_PREFIX + "test-ping-ds.png",
        "networking150": IMAGES_NETWORKING_PREFIX + "migratino-server-list.png",
        "networking151": IMAGES_NETWORKING_PREFIX + "instance-shut-off.png",
        "networking152": IMAGES_NETWORKING_PREFIX + "instance-shutoff-twice.png",
        "networking153": IMAGES_NETWORKING_PREFIX + "image-created-for-migration.png",
        "networking154": IMAGES_NETWORKING_PREFIX + "min-disk-instance-migration.png",
        "networking155": IMAGES_NETWORKING_PREFIX + "migration-image-upload.png",
        "networking156": IMAGES_NETWORKING_PREFIX + "ssh1.png",
        "networking157": IMAGES_NETWORKING_PREFIX + "ssh2.png",
        "networking158": IMAGES_NETWORKING_PREFIX + "ssh3.png",
        "networking159": IMAGES_NETWORKING_PREFIX + "edit.png",
        "networking160": IMAGES_NETWORKING_PREFIX + "fip1.png",
        "networking161": IMAGES_NETWORKING_PREFIX + "fip2.png",
        "networking162": IMAGES_NETWORKING_PREFIX + "fip3.png",
        "networking163": IMAGES_NETWORKING_PREFIX + "fip4.png",
        "networking164": IMAGES_NETWORKING_PREFIX + "fip5.png",
        "networking165": IMAGES_NETWORKING_PREFIX + "fip6.png",
        "networking166": IMAGES_NETWORKING_PREFIX + "fip7.png",
        "networking167": IMAGES_NETWORKING_PREFIX + "fip8.png",
        "networking168": IMAGES_NETWORKING_PREFIX + "fip9.png",
        "networking169": IMAGES_NETWORKING_PREFIX + "ssh-import-01.png",
        "networking170": IMAGES_NETWORKING_PREFIX + "ssh-import-02.png",
        "networking171": IMAGES_NETWORKING_PREFIX + "ssh-import-03.png",
        "networking172": IMAGES_NETWORKING_PREFIX + "ssh-import-04.png",
        "networking173": IMAGES_NETWORKING_PREFIX + "pastebin1.png",
        "networking174": IMAGES_NETWORKING_PREFIX + "pastebin2.png",
        "networking175": IMAGES_NETWORKING_PREFIX + "pastebin3.png",
        "networking176": IMAGES_NETWORKING_PREFIX + "pastebin4.png",
        "networking177": IMAGES_NETWORKING_PREFIX + "pastebin5.png",
        "networking178": IMAGES_NETWORKING_PREFIX + "ssh-linux1.png",
        "networking179": IMAGES_NETWORKING_PREFIX + "ssh-linux2.png",
        "networking180": IMAGES_NETWORKING_PREFIX + "irf-select-project.png",
        "networking181": IMAGES_NETWORKING_PREFIX + "irf-delete-floating-ip.png",
        "networking182": IMAGES_NETWORKING_PREFIX + "irf-delete-router.png",
        "networking183": IMAGES_NETWORKING_PREFIX + "irf-delete-snapshot.png",
        "networking184": IMAGES_NETWORKING_PREFIX + "irf-delete-volume.png",
        "networking185": IMAGES_NETWORKING_PREFIX + "irf-delete-instance.png",
        "networking186": IMAGES_NETWORKING_PREFIX + "irf-delete-project.png",
        "networking187": IMAGES_NETWORKING_PREFIX + "net1.png",
        "networking188": IMAGES_NETWORKING_PREFIX + "net2.png",
        "networking189": IMAGES_NETWORKING_PREFIX + "net3.png",
        "networking190": IMAGES_NETWORKING_PREFIX + "net4.png",
        "networking191": IMAGES_NETWORKING_PREFIX + "net5.png",
        "networking192": IMAGES_NETWORKING_PREFIX + "net6.png",
        "networking193": IMAGES_NETWORKING_PREFIX + "net7.png",
        "networking194": IMAGES_NETWORKING_PREFIX + "net8.png",
        "networking195": IMAGES_NETWORKING_PREFIX + "net9.png",
        "networking196": IMAGES_NETWORKING_PREFIX + "net10.png",
        "networking197": IMAGES_NETWORKING_PREFIX + "net11.png",
        "networking198": IMAGES_NETWORKING_PREFIX + "net12.png",
        "networking199": IMAGES_NETWORKING_PREFIX + "net13.png",
        "networking200": IMAGES_NETWORKING_PREFIX + "coz-py1.png",
        "networking201": IMAGES_NETWORKING_PREFIX + "coz-py2.png",
        "networking202": IMAGES_NETWORKING_PREFIX + "coz-py3.png",
        "networking203": IMAGES_NETWORKING_PREFIX + "coz-py4.png",
        "networking204": IMAGES_NETWORKING_PREFIX + "coz-py5.png",
        "networking205": IMAGES_NETWORKING_PREFIX + "coz-faqpython.png",
        "networking206": IMAGES_NETWORKING_PREFIX + "coz-py6.png",
        "networking207": IMAGES_NETWORKING_PREFIX + "mount-object-storage-file-with-eodata.png",
        "networking208": IMAGES_NETWORKING_PREFIX + "mount-eodata-windows-rclone-01.png",
        "networking209": IMAGES_NETWORKING_PREFIX + "mount-eodata-windows-rclone-02.png",
        "networking210": IMAGES_NETWORKING_PREFIX + "mount-eodata-windows-open-nssm-01.png",
        "networking211": IMAGES_NETWORKING_PREFIX + "mount-object-storage-windows-horizon-01.png",
        "networking212": IMAGES_NETWORKING_PREFIX + "screen224.png",
        "networking213": IMAGES_NETWORKING_PREFIX + "screen3-ds.png",
        "networking214": IMAGES_NETWORKING_PREFIX + "screen4-ds.png",
        "networking215": IMAGES_NETWORKING_PREFIX + "screen44-ds.png",
        "networking216": IMAGES_NETWORKING_PREFIX + "screen5-ds.png",
        "networking217": IMAGES_NETWORKING_PREFIX + "screen6-ds.png",
        "networking218": IMAGES_NETWORKING_PREFIX + "screen7.png",
        "networking219": IMAGES_NETWORKING_PREFIX + "screen8-ds.png",
        "networking220": IMAGES_NETWORKING_PREFIX + "screen9-ds.png",
        "networking221": IMAGES_NETWORKING_PREFIX + "scrn10-ds.png",
        "networking222": IMAGES_NETWORKING_PREFIX + "screen11.png",
        "networking223": IMAGES_NETWORKING_PREFIX + "screen12.png",
        "networking224": IMAGES_NETWORKING_PREFIX + "screen13.png",
        "networking225": IMAGES_NETWORKING_PREFIX + "screen14.png",
        "networking226": IMAGES_NETWORKING_PREFIX + "screen15-new.png",
        "networking227": IMAGES_NETWORKING_PREFIX + "fwaas-1.png",
        "networking228": IMAGES_NETWORKING_PREFIX + "screen16.png",
        "networking229": IMAGES_NETWORKING_PREFIX + "screen17b.png",
        "networking230": IMAGES_NETWORKING_PREFIX + "screen177-new.png",
        "networking231": IMAGES_NETWORKING_PREFIX + "screen178-new.png",
        "networking232": IMAGES_NETWORKING_PREFIX + "screen18-new.png",
        "networking233": IMAGES_NETWORKING_PREFIX + "screen19-new.png",
        "networking234": IMAGES_NETWORKING_PREFIX + "screen21.png",
        "networking235": IMAGES_NETWORKING_PREFIX + "screen22.png",
        "networking236": IMAGES_NETWORKING_PREFIX + "screen23-new.png",
        "networking237": IMAGES_NETWORKING_PREFIX + "firewall-v3-15-new.png",
        "networking238": IMAGES_NETWORKING_PREFIX + "configure-firewall-1.png",
        "networking239": IMAGES_NETWORKING_PREFIX + "configure-firewall-2.png",
        "networking240": IMAGES_NETWORKING_PREFIX + "configure-firewall-3.png",
        "networking241": IMAGES_NETWORKING_PREFIX + "configure-firewall-4.png",
        "networking242": IMAGES_NETWORKING_PREFIX + "configure-firewall-5.png",
        "networking243": IMAGES_NETWORKING_PREFIX + "configure-firewall-7.png",
        "networking244": IMAGES_NETWORKING_PREFIX + "configure-firewall-8.png",
        "networking245": IMAGES_NETWORKING_PREFIX + "configure-firewall-9-new.png",
        "networking246": IMAGES_NETWORKING_PREFIX + "configure-firewall-11-new.png",
        "networking247": IMAGES_NETWORKING_PREFIX + "configure-firewall-13.png",
        "networking248": IMAGES_NETWORKING_PREFIX + "configure-firewall-14-new.png",
        "networking249": IMAGES_NETWORKING_PREFIX + "fwaas-ssh.png",
        "networking250": IMAGES_NETWORKING_PREFIX + "fwaas-ssh2.png",
        "networking251": IMAGES_NETWORKING_PREFIX + "firewall-v3-9-new.png",
        "networking252": IMAGES_NETWORKING_PREFIX + "firewall-v3-1-new.png",
        "networking253": IMAGES_NETWORKING_PREFIX + "firewall-v3-2-new.png",
        "networking254": IMAGES_NETWORKING_PREFIX + "firewall-v3-3.png",
        "networking255": IMAGES_NETWORKING_PREFIX + "firewall-v3-4-new.png",
        "networking256": IMAGES_NETWORKING_PREFIX + "firewall-v3-18-new.png",
        "networking257": IMAGES_NETWORKING_PREFIX + "enter-root-pass.png",
        "networking258": IMAGES_NETWORKING_PREFIX + "firewall-v3-21.png",
        "networking259": IMAGES_NETWORKING_PREFIX + "firewall-v3-10.png",
        "networking260": IMAGES_NETWORKING_PREFIX + "firewall-v3-11-new.png",
        "networking261": IMAGES_NETWORKING_PREFIX + "firewall-v3-12-new.png",
        "networking262": IMAGES_NETWORKING_PREFIX + "fwaas-openvpn-v2-5.png",
        "networking263": IMAGES_NETWORKING_PREFIX + "firewall-v3-13-new.png",
        "networking264": IMAGES_NETWORKING_PREFIX + "create-user.png",
        "networking265": IMAGES_NETWORKING_PREFIX + "fwaas-openvpn-v2-7-new.png",
        "networking266": IMAGES_NETWORKING_PREFIX + "fwaas-openvpn-v2-8.png",
        "networking267": IMAGES_NETWORKING_PREFIX + "fwaas-openvpn-v2-9-new.png",
        "networking268": IMAGES_NETWORKING_PREFIX + "fwaas-openvpn-v2-10.png",
        "networking269": IMAGES_NETWORKING_PREFIX + "fwaas-openvpn-v2-11.png",
        "networking270": IMAGES_NETWORKING_PREFIX + "fwaas-openvpn-v2-12.png",
        "networking271": IMAGES_NETWORKING_PREFIX + "fwaas-openvpn-v2-13.png",
        "networking272": IMAGES_NETWORKING_PREFIX + "fwaas-openvpn-v2-14-new.png",
        "networking273": IMAGES_NETWORKING_PREFIX + "fwaas-openvpn-v2-16-new.png",
        "networking274": IMAGES_NETWORKING_PREFIX + "fwaas-openvpn-v2-20-new.png",
        "networking275": IMAGES_NETWORKING_PREFIX + "fwaas-openvpn-v2-21.png",
        "networking276": IMAGES_NETWORKING_PREFIX + "fwaas-openvpn-v2-22-new.png",
        "networking277": IMAGES_NETWORKING_PREFIX + "fwaas-openvpn-v2-23-new.png",
        "networking278": IMAGES_NETWORKING_PREFIX + "rule1.png",
        "networking279": IMAGES_NETWORKING_PREFIX + "rule2.png",
        "networking280": IMAGES_NETWORKING_PREFIX + "opt-interface.png",
        "networking281": IMAGES_NETWORKING_PREFIX + "rules-to-opt.png",
        "networking282": IMAGES_NETWORKING_PREFIX + "lan-interface.png",
        "networking283": IMAGES_NETWORKING_PREFIX + "lan-rule1.png",
        "networking284": IMAGES_NETWORKING_PREFIX + "lan-rule2.png",
        "networking285": IMAGES_NETWORKING_PREFIX + "lan-rule3.png",
        "networking286": IMAGES_NETWORKING_PREFIX + "lan-rule4.png",
        "networking287": IMAGES_NETWORKING_PREFIX + "clients-export.png",
        "networking288": IMAGES_NETWORKING_PREFIX + "top-corner.png",
        "networking289": IMAGES_NETWORKING_PREFIX + "top-corner2.png",
        "networking290": IMAGES_NETWORKING_PREFIX + "top-corner3.png",
        "networking291": IMAGES_NETWORKING_PREFIX + "fwaas-authuser-ovpn.png",
        "networking292": IMAGES_NETWORKING_PREFIX + "fwaas-ovpn-connected.png",
        "networking293": IMAGES_NETWORKING_PREFIX + "fwaas-test-connectopn-new.png",
        "networking294": IMAGES_NETWORKING_PREFIX + "ping.png",
        "networking295": IMAGES_NETWORKING_PREFIX + "test-ping-ds.png",
        "networking296": IMAGES_NETWORKING_PREFIX + "migratino-server-list.png",
        "networking297": IMAGES_NETWORKING_PREFIX + "instance-shut-off.png",
        "networking298": IMAGES_NETWORKING_PREFIX + "instance-shutoff-twice.png",
        "networking299": IMAGES_NETWORKING_PREFIX + "image-created-for-migration.png",
        "networking300": IMAGES_NETWORKING_PREFIX + "min-disk-instance-migration.png",
        "networking301": IMAGES_NETWORKING_PREFIX + "migration-image-upload.png",
    },

    "openstackcli_images": {
        "openstackcli001": IMAGES_OPENSTACKCLI_PREFIX + "openrc-download.png",
        "openstackcli002": IMAGES_OPENSTACKCLI_PREFIX + "present-networks.png",
        "openstackcli003": IMAGES_OPENSTACKCLI_PREFIX + "default-security-groups.png",
        "openstackcli004": IMAGES_OPENSTACKCLI_PREFIX + "identity-projects.png",
        "openstackcli005": IMAGES_OPENSTACKCLI_PREFIX + "create-project.png",
        "openstackcli006": IMAGES_OPENSTACKCLI_PREFIX + "screen03.png",
        "openstackcli007": IMAGES_OPENSTACKCLI_PREFIX + "screen03a.png",
        "openstackcli008": IMAGES_OPENSTACKCLI_PREFIX + "select-role.png",
        "openstackcli009": IMAGES_OPENSTACKCLI_PREFIX + "new-project.png",
        "openstackcli010": IMAGES_OPENSTACKCLI_PREFIX + "projects-present.png",
        "openstackcli011": IMAGES_OPENSTACKCLI_PREFIX + "testproject.png",
        "openstackcli012": IMAGES_OPENSTACKCLI_PREFIX + "no-networks-present.png",
        "openstackcli013": IMAGES_OPENSTACKCLI_PREFIX + "api-access.png",
        "openstackcli014": IMAGES_OPENSTACKCLI_PREFIX + "user-credentials.png",
        "openstackcli015": IMAGES_OPENSTACKCLI_PREFIX + "add-ticket.png",
        "openstackcli016": IMAGES_OPENSTACKCLI_PREFIX + "screen07.png",
        "openstackcli017": IMAGES_OPENSTACKCLI_PREFIX + "start-vm-from-volume-snapshot-cli-01.png",
        "openstackcli018": IMAGES_OPENSTACKCLI_PREFIX + "heat-test2.png",
        "openstackcli019": IMAGES_OPENSTACKCLI_PREFIX + "heat-test2-stacks.png",
        "openstackcli020": IMAGES_OPENSTACKCLI_PREFIX + "heat-test2-instances.png",
        "openstackcli021": IMAGES_OPENSTACKCLI_PREFIX + "stacks-menu.png",
        "openstackcli022": IMAGES_OPENSTACKCLI_PREFIX + "orch4.png",
        "openstackcli023": IMAGES_OPENSTACKCLI_PREFIX + "select-template-yaml.png",
        "openstackcli024": IMAGES_OPENSTACKCLI_PREFIX + "launch-stack.png",
        "openstackcli025": IMAGES_OPENSTACKCLI_PREFIX + "create-new-template.png",
        "openstackcli026": IMAGES_OPENSTACKCLI_PREFIX + "heat-instance.png",
        "openstackcli027": IMAGES_OPENSTACKCLI_PREFIX + "create-heat-4.png",
        "openstackcli028": IMAGES_OPENSTACKCLI_PREFIX + "four-created.png",
        "openstackcli029": IMAGES_OPENSTACKCLI_PREFIX + "template-generator.png",
        "openstackcli030": IMAGES_OPENSTACKCLI_PREFIX + "how-to-create-instance-snapshot-cli-13.png",
        "openstackcli031": IMAGES_OPENSTACKCLI_PREFIX + "how-to-create-instance-snapshot-cli-12.png",
        "openstackcli032": IMAGES_OPENSTACKCLI_PREFIX + "how-to-create-instance-snapshot-cli-14.png",
        "openstackcli033": IMAGES_OPENSTACKCLI_PREFIX + "how-to-create-instance-snapshot-cli-15.png",
        "openstackcli034": IMAGES_OPENSTACKCLI_PREFIX + "how-to-create-instance-snapshot-cli-16.png",
        "openstackcli035": IMAGES_OPENSTACKCLI_PREFIX + "how-to-create-instance-snapshot-cli-17.png",
        "openstackcli036": IMAGES_OPENSTACKCLI_PREFIX + "how-to-create-instance-snapshot-cli-21.png",
        "openstackcli037": IMAGES_OPENSTACKCLI_PREFIX + "how-to-create-instance-snapshot-cli-18.png",
        "openstackcli038": IMAGES_OPENSTACKCLI_PREFIX + "how-to-create-instance-snapshot-cli-22.png",
        "openstackcli039": IMAGES_OPENSTACKCLI_PREFIX + "how-to-create-instance-snapshot-cli-19.png",
        "openstackcli040": IMAGES_OPENSTACKCLI_PREFIX + "how-to-create-instance-snapshot-cli-20.png",
        "openstackcli041": IMAGES_OPENSTACKCLI_PREFIX + "how-to-create-instance-snapshot-cli-23.png",
        "openstackcli042": IMAGES_OPENSTACKCLI_PREFIX + "git-bash01.png",
        "openstackcli043": IMAGES_OPENSTACKCLI_PREFIX + "git-bash02.png",
        "openstackcli044": IMAGES_OPENSTACKCLI_PREFIX + "git-bash03.png",
        "openstackcli045": IMAGES_OPENSTACKCLI_PREFIX + "git-bash04.png",
        "openstackcli046": IMAGES_OPENSTACKCLI_PREFIX + "git-bash05.png",
        "openstackcli047": IMAGES_OPENSTACKCLI_PREFIX + "git-bash17.png",
        "openstackcli048": IMAGES_OPENSTACKCLI_PREFIX + "git-bash06.png",
        "openstackcli049": IMAGES_OPENSTACKCLI_PREFIX + "git-bash07.png",
        "openstackcli050": IMAGES_OPENSTACKCLI_PREFIX + "git-bash09.png",
        "openstackcli051": IMAGES_OPENSTACKCLI_PREFIX + "git-bash10.png",
        "openstackcli052": IMAGES_OPENSTACKCLI_PREFIX + "git-bash11.png",
        "openstackcli053": IMAGES_OPENSTACKCLI_PREFIX + "git-bash12.png",
        "openstackcli054": IMAGES_OPENSTACKCLI_PREFIX + "enter-the-six-digit-code2.png",
        "openstackcli055": IMAGES_OPENSTACKCLI_PREFIX + "activate-environment.png",
        "openstackcli056": IMAGES_OPENSTACKCLI_PREFIX + "install-new-pip.png",
        "openstackcli057": IMAGES_OPENSTACKCLI_PREFIX + "openstack-cli-install-linux-help.png",
        "openstackcli058": IMAGES_OPENSTACKCLI_PREFIX + "openstackcli-flavor-list.png",
        "openstackcli059": IMAGES_OPENSTACKCLI_PREFIX + "wsl01.png",
        "openstackcli060": IMAGES_OPENSTACKCLI_PREFIX + "wsl02.png",
        "openstackcli061": IMAGES_OPENSTACKCLI_PREFIX + "wsl03.png",
        "openstackcli062": IMAGES_OPENSTACKCLI_PREFIX + "wsl04.png",
        "openstackcli063": IMAGES_OPENSTACKCLI_PREFIX + "wsl05.png",
        "openstackcli064": IMAGES_OPENSTACKCLI_PREFIX + "wsl06.png",
        "openstackcli065": IMAGES_OPENSTACKCLI_PREFIX + "wsl07.png",
        "openstackcli066": IMAGES_OPENSTACKCLI_PREFIX + "wsl08.png",
        "openstackcli067": IMAGES_OPENSTACKCLI_PREFIX + "wsl09.png",
        "openstackcli068": IMAGES_OPENSTACKCLI_PREFIX + "wsl10.png",
        "openstackcli069": IMAGES_OPENSTACKCLI_PREFIX + "wsl11.png",
        "openstackcli070": IMAGES_OPENSTACKCLI_PREFIX + "wsl12.png",
        "openstackcli071": IMAGES_OPENSTACKCLI_PREFIX + "wsl13.png",
        "openstackcli072": IMAGES_OPENSTACKCLI_PREFIX + "wsl14.png",
        "openstackcli073": IMAGES_OPENSTACKCLI_PREFIX + "wsl15.png",
        "openstackcli074": IMAGES_OPENSTACKCLI_PREFIX + "wsl16.png",
        "openstackcli075": IMAGES_OPENSTACKCLI_PREFIX + "wsl17.png",
        "openstackcli076": IMAGES_OPENSTACKCLI_PREFIX + "wsl18.png",
        "openstackcli077": IMAGES_OPENSTACKCLI_PREFIX + "wsl19.png",
        "openstackcli078": IMAGES_OPENSTACKCLI_PREFIX + "wsl20.png",
        "openstackcli079": IMAGES_OPENSTACKCLI_PREFIX + "how-to-move-data-volume-cli-12.png",
        "openstackcli080": IMAGES_OPENSTACKCLI_PREFIX + "how-to-move-data-volume-cli-31.png",
        "openstackcli081": IMAGES_OPENSTACKCLI_PREFIX + "how-to-move-data-volume-cli-32.png",
        "openstackcli082": IMAGES_OPENSTACKCLI_PREFIX + "how-to-move-data-volume-cli-13.png",
        "openstackcli083": IMAGES_OPENSTACKCLI_PREFIX + "how-to-move-data-volume-cli-14.png",
        "openstackcli084": IMAGES_OPENSTACKCLI_PREFIX + "how-to-move-data-volume-cli-15.png",
        "openstackcli085": IMAGES_OPENSTACKCLI_PREFIX + "start-vm-instance-snapshot-cli-01.png",
        "openstackcli086": IMAGES_OPENSTACKCLI_PREFIX + "start-vm-instance-snapshot-cli-02.png",
        "openstackcli087": IMAGES_OPENSTACKCLI_PREFIX + "start-vm-instance-snapshot-cli-03.png",
        "openstackcli088": IMAGES_OPENSTACKCLI_PREFIX + "start-vm-instance-snapshot-cli-04.png",
        "openstackcli089": IMAGES_OPENSTACKCLI_PREFIX + "start-vm-instance-snapshot-cli-05.png",
        "openstackcli090": IMAGES_OPENSTACKCLI_PREFIX + "transfer-volume-between-projects-cli-32.png",
        "openstackcli091": IMAGES_OPENSTACKCLI_PREFIX + "transfer-volume-between-projects-cli-14.png",
        "openstackcli092": IMAGES_OPENSTACKCLI_PREFIX + "transfer-volume-between-projects-cli-25.png",
        "openstackcli093": IMAGES_OPENSTACKCLI_PREFIX + "transfer-volume-between-projects-cli-26.png",
        "openstackcli094": IMAGES_OPENSTACKCLI_PREFIX + "transfer-volume-between-projects-cli-27.png",
        "openstackcli095": IMAGES_OPENSTACKCLI_PREFIX + "transfer-volume-between-projects-cli-33.png",
        "openstackcli096": IMAGES_OPENSTACKCLI_PREFIX + "transfer-volume-between-projects-cli-34.png",
        "openstackcli097": IMAGES_OPENSTACKCLI_PREFIX + "resize-vm-horizon-cli-3.png",
        "openstackcli098": IMAGES_OPENSTACKCLI_PREFIX + "resize-vm-horizon-cli-2.png",
        "openstackcli099": IMAGES_OPENSTACKCLI_PREFIX + "resize-vm-horizon-cli-4.png",
        "openstackcli100": IMAGES_OPENSTACKCLI_PREFIX + "install-cron-1.png",
        "openstackcli101": IMAGES_OPENSTACKCLI_PREFIX + "how-to-create-rotating-backups-05.png",
        "openstackcli102": IMAGES_OPENSTACKCLI_PREFIX + "install-cron-2.png",
        "openstackcli103": IMAGES_OPENSTACKCLI_PREFIX + "use-script-rotating-backups-01.png",
        "openstackcli104": IMAGES_OPENSTACKCLI_PREFIX + "use-script-rotating-backups-02.png",
        "openstackcli105": IMAGES_OPENSTACKCLI_PREFIX + "install-cron-mulitple-1.png",
        "openstackcli106": IMAGES_OPENSTACKCLI_PREFIX + "use-script-rotating-backups-03.png",
        "openstackcli107": IMAGES_OPENSTACKCLI_PREFIX + "use-script-rotating-backups-04.png",
        "openstackcli108": IMAGES_OPENSTACKCLI_PREFIX + "use-script-rotating-backups-05.png",
        "openstackcli109": IMAGES_OPENSTACKCLI_PREFIX + "backup-command-rotating-backups-05.png",
        "openstackcli110": IMAGES_OPENSTACKCLI_PREFIX + "backup-command-rotating-backups-06.png",
        "openstackcli111": IMAGES_OPENSTACKCLI_PREFIX + "backup-command-rotating-backups-08.png",
        "openstackcli112": IMAGES_OPENSTACKCLI_PREFIX + "present-networks.png",
        "openstackcli113": IMAGES_OPENSTACKCLI_PREFIX + "default-security-groups.png",
        "openstackcli114": IMAGES_OPENSTACKCLI_PREFIX + "identity-projects.png",
        "openstackcli115": IMAGES_OPENSTACKCLI_PREFIX + "create-project.png",
        "openstackcli116": IMAGES_OPENSTACKCLI_PREFIX + "screen03.png",
        "openstackcli117": IMAGES_OPENSTACKCLI_PREFIX + "screen03a.png",
        "openstackcli118": IMAGES_OPENSTACKCLI_PREFIX + "select-role.png",
        "openstackcli119": IMAGES_OPENSTACKCLI_PREFIX + "new-project.png",
        "openstackcli120": IMAGES_OPENSTACKCLI_PREFIX + "projects-present.png",
        "openstackcli121": IMAGES_OPENSTACKCLI_PREFIX + "testproject.png",
        "openstackcli122": IMAGES_OPENSTACKCLI_PREFIX + "no-networks-present.png",
        "openstackcli123": IMAGES_OPENSTACKCLI_PREFIX + "api-access.png",
        "openstackcli124": IMAGES_OPENSTACKCLI_PREFIX + "user-credentials.png",
        "openstackcli125": IMAGES_OPENSTACKCLI_PREFIX + "add-ticket.png",
        "openstackcli126": IMAGES_OPENSTACKCLI_PREFIX + "screen07.png",
        "openstackcli127": IMAGES_OPENSTACKCLI_PREFIX + "start-vm-from-volume-snapshot-cli-01.png",
        "openstackcli128": IMAGES_OPENSTACKCLI_PREFIX + "heat-test2.png",
        "openstackcli129": IMAGES_OPENSTACKCLI_PREFIX + "heat-test2-stacks.png",
        "openstackcli130": IMAGES_OPENSTACKCLI_PREFIX + "heat-test2-instances.png",
        "openstackcli131": IMAGES_OPENSTACKCLI_PREFIX + "stacks-menu.png",
        "openstackcli132": IMAGES_OPENSTACKCLI_PREFIX + "orch4.png",
        "openstackcli133": IMAGES_OPENSTACKCLI_PREFIX + "select-template-yaml.png",
        "openstackcli134": IMAGES_OPENSTACKCLI_PREFIX + "launch-stack.png",
        "openstackcli135": IMAGES_OPENSTACKCLI_PREFIX + "create-new-template.png",
        "openstackcli136": IMAGES_OPENSTACKCLI_PREFIX + "heat-instance.png",
        "openstackcli137": IMAGES_OPENSTACKCLI_PREFIX + "create-heat-4.png",
        "openstackcli138": IMAGES_OPENSTACKCLI_PREFIX + "four-created.png",
        "openstackcli139": IMAGES_OPENSTACKCLI_PREFIX + "template-generator.png",
        "openstackcli140": IMAGES_OPENSTACKCLI_PREFIX + "how-to-create-instance-snapshot-cli-13.png",
        "openstackcli141": IMAGES_OPENSTACKCLI_PREFIX + "how-to-create-instance-snapshot-cli-12.png",
        "openstackcli142": IMAGES_OPENSTACKCLI_PREFIX + "how-to-create-instance-snapshot-cli-14.png",
        "openstackcli143": IMAGES_OPENSTACKCLI_PREFIX + "how-to-create-instance-snapshot-cli-15.png",
        "openstackcli144": IMAGES_OPENSTACKCLI_PREFIX + "how-to-create-instance-snapshot-cli-16.png",
        "openstackcli145": IMAGES_OPENSTACKCLI_PREFIX + "how-to-create-instance-snapshot-cli-17.png",
        "openstackcli146": IMAGES_OPENSTACKCLI_PREFIX + "how-to-create-instance-snapshot-cli-21.png",
        "openstackcli147": IMAGES_OPENSTACKCLI_PREFIX + "how-to-create-instance-snapshot-cli-18.png",
        "openstackcli148": IMAGES_OPENSTACKCLI_PREFIX + "how-to-create-instance-snapshot-cli-22.png",
        "openstackcli149": IMAGES_OPENSTACKCLI_PREFIX + "how-to-create-instance-snapshot-cli-19.png",
        "openstackcli150": IMAGES_OPENSTACKCLI_PREFIX + "how-to-create-instance-snapshot-cli-20.png",
        "openstackcli151": IMAGES_OPENSTACKCLI_PREFIX + "how-to-create-instance-snapshot-cli-23.png",
        "openstackcli152": IMAGES_OPENSTACKCLI_PREFIX + "git-bash01.png",
        "openstackcli153": IMAGES_OPENSTACKCLI_PREFIX + "git-bash02.png",
        "openstackcli154": IMAGES_OPENSTACKCLI_PREFIX + "git-bash03.png",
        "openstackcli155": IMAGES_OPENSTACKCLI_PREFIX + "git-bash04.png",
        "openstackcli156": IMAGES_OPENSTACKCLI_PREFIX + "git-bash05.png",
        "openstackcli157": IMAGES_OPENSTACKCLI_PREFIX + "git-bash17.png",
        "openstackcli158": IMAGES_OPENSTACKCLI_PREFIX + "git-bash06.png",
        "openstackcli159": IMAGES_OPENSTACKCLI_PREFIX + "git-bash07.png",
        "openstackcli160": IMAGES_OPENSTACKCLI_PREFIX + "git-bash09.png",
        "openstackcli161": IMAGES_OPENSTACKCLI_PREFIX + "git-bash10.png",
        "openstackcli162": IMAGES_OPENSTACKCLI_PREFIX + "git-bash11.png",
        "openstackcli163": IMAGES_OPENSTACKCLI_PREFIX + "git-bash12.png",
        "openstackcli164": IMAGES_OPENSTACKCLI_PREFIX + "enter-the-six-digit-code2.png",
        "openstackcli165": IMAGES_OPENSTACKCLI_PREFIX + "activate-environment.png",
        "openstackcli166": IMAGES_OPENSTACKCLI_PREFIX + "install-new-pip.png",
        "openstackcli167": IMAGES_OPENSTACKCLI_PREFIX + "openstack-cli-install-linux-help.png",
        "openstackcli168": IMAGES_OPENSTACKCLI_PREFIX + "openstackcli-flavor-list.png",
        "openstackcli169": IMAGES_OPENSTACKCLI_PREFIX + "wsl01.png",
        "openstackcli170": IMAGES_OPENSTACKCLI_PREFIX + "wsl02.png",
        "openstackcli171": IMAGES_OPENSTACKCLI_PREFIX + "wsl03.png",
        "openstackcli172": IMAGES_OPENSTACKCLI_PREFIX + "wsl04.png",
        "openstackcli173": IMAGES_OPENSTACKCLI_PREFIX + "wsl05.png",
        "openstackcli174": IMAGES_OPENSTACKCLI_PREFIX + "wsl06.png",
        "openstackcli175": IMAGES_OPENSTACKCLI_PREFIX + "wsl07.png",
        "openstackcli176": IMAGES_OPENSTACKCLI_PREFIX + "wsl08.png",
        "openstackcli177": IMAGES_OPENSTACKCLI_PREFIX + "wsl09.png",
        "openstackcli178": IMAGES_OPENSTACKCLI_PREFIX + "wsl10.png",
        "openstackcli179": IMAGES_OPENSTACKCLI_PREFIX + "wsl11.png",
        "openstackcli180": IMAGES_OPENSTACKCLI_PREFIX + "wsl12.png",
        "openstackcli181": IMAGES_OPENSTACKCLI_PREFIX + "wsl13.png",
        "openstackcli182": IMAGES_OPENSTACKCLI_PREFIX + "wsl14.png",
        "openstackcli183": IMAGES_OPENSTACKCLI_PREFIX + "wsl15.png",
        "openstackcli184": IMAGES_OPENSTACKCLI_PREFIX + "wsl16.png",
        "openstackcli185": IMAGES_OPENSTACKCLI_PREFIX + "wsl17.png",
        "openstackcli186": IMAGES_OPENSTACKCLI_PREFIX + "wsl18.png",
        "openstackcli187": IMAGES_OPENSTACKCLI_PREFIX + "wsl19.png",
        "openstackcli188": IMAGES_OPENSTACKCLI_PREFIX + "wsl20.png",
        "openstackcli189": IMAGES_OPENSTACKCLI_PREFIX + "how-to-move-data-volume-cli-12.png",
        "openstackcli190": IMAGES_OPENSTACKCLI_PREFIX + "how-to-move-data-volume-cli-31.png",
        "openstackcli191": IMAGES_OPENSTACKCLI_PREFIX + "how-to-move-data-volume-cli-32.png",
        "openstackcli192": IMAGES_OPENSTACKCLI_PREFIX + "how-to-move-data-volume-cli-13.png",
        "openstackcli193": IMAGES_OPENSTACKCLI_PREFIX + "how-to-move-data-volume-cli-14.png",
        "openstackcli194": IMAGES_OPENSTACKCLI_PREFIX + "how-to-move-data-volume-cli-15.png",
        "openstackcli195": IMAGES_OPENSTACKCLI_PREFIX + "start-vm-instance-snapshot-cli-01.png",
        "openstackcli196": IMAGES_OPENSTACKCLI_PREFIX + "start-vm-instance-snapshot-cli-02.png",
        "openstackcli197": IMAGES_OPENSTACKCLI_PREFIX + "start-vm-instance-snapshot-cli-03.png",
        "openstackcli198": IMAGES_OPENSTACKCLI_PREFIX + "start-vm-instance-snapshot-cli-04.png",
        "openstackcli199": IMAGES_OPENSTACKCLI_PREFIX + "start-vm-instance-snapshot-cli-05.png",
        "openstackcli200": IMAGES_OPENSTACKCLI_PREFIX + "transfer-volume-between-projects-cli-32.png",
        "openstackcli201": IMAGES_OPENSTACKCLI_PREFIX + "transfer-volume-between-projects-cli-14.png",
        "openstackcli202": IMAGES_OPENSTACKCLI_PREFIX + "transfer-volume-between-projects-cli-25.png",
        "openstackcli203": IMAGES_OPENSTACKCLI_PREFIX + "transfer-volume-between-projects-cli-26.png",
        "openstackcli204": IMAGES_OPENSTACKCLI_PREFIX + "transfer-volume-between-projects-cli-27.png",
        "openstackcli205": IMAGES_OPENSTACKCLI_PREFIX + "transfer-volume-between-projects-cli-33.png",
        "openstackcli206": IMAGES_OPENSTACKCLI_PREFIX + "transfer-volume-between-projects-cli-34.png",
        "openstackcli207": IMAGES_OPENSTACKCLI_PREFIX + "resize-vm-horizon-cli-3.png",
        "openstackcli208": IMAGES_OPENSTACKCLI_PREFIX + "resize-vm-horizon-cli-2.png",
        "openstackcli209": IMAGES_OPENSTACKCLI_PREFIX + "resize-vm-horizon-cli-4.png",
        "openstackcli210": IMAGES_OPENSTACKCLI_PREFIX + "install-cron-1.png",
        "openstackcli211": IMAGES_OPENSTACKCLI_PREFIX + "how-to-create-rotating-backups-05.png",
        "openstackcli212": IMAGES_OPENSTACKCLI_PREFIX + "install-cron-2.png",
        "openstackcli213": IMAGES_OPENSTACKCLI_PREFIX + "use-script-rotating-backups-01.png",
        "openstackcli214": IMAGES_OPENSTACKCLI_PREFIX + "use-script-rotating-backups-02.png",
        "openstackcli215": IMAGES_OPENSTACKCLI_PREFIX + "install-cron-mulitple-1.png",
        "openstackcli216": IMAGES_OPENSTACKCLI_PREFIX + "use-script-rotating-backups-03.png",
        "openstackcli217": IMAGES_OPENSTACKCLI_PREFIX + "use-script-rotating-backups-04.png",
        "openstackcli218": IMAGES_OPENSTACKCLI_PREFIX + "use-script-rotating-backups-05.png",
        "openstackcli219": IMAGES_OPENSTACKCLI_PREFIX + "backup-command-rotating-backups-05.png",
        "openstackcli220": IMAGES_OPENSTACKCLI_PREFIX + "backup-command-rotating-backups-06.png",
        "openstackcli221": IMAGES_OPENSTACKCLI_PREFIX + "backup-command-rotating-backups-08.png",
    },

    "openstackdev_images": {
        "openstackdev001": IMAGES_OPENSTACKDEV_PREFIX + "api-token.png",
        "openstackdev002": IMAGES_OPENSTACKDEV_PREFIX + "terraform-adding-repository.png",
        "openstackdev003": IMAGES_OPENSTACKDEV_PREFIX + "terraform-flavor-list-short.png",
        "openstackdev004": IMAGES_OPENSTACKDEV_PREFIX + "terraform-init.png",
        "openstackdev005": IMAGES_OPENSTACKDEV_PREFIX + "terraform-yes.png",
        "openstackdev006": IMAGES_OPENSTACKDEV_PREFIX + "terraform-apply.png",
        "openstackdev007": IMAGES_OPENSTACKDEV_PREFIX + "terraform-horizon.png",
        "openstackdev008": IMAGES_OPENSTACKDEV_PREFIX + "terraform-adding-repository.png",
        "openstackdev009": IMAGES_OPENSTACKDEV_PREFIX + "terraform-flavor-list-short.png",
        "openstackdev010": IMAGES_OPENSTACKDEV_PREFIX + "terraform-init.png",
        "openstackdev011": IMAGES_OPENSTACKDEV_PREFIX + "terraform-yes.png",
        "openstackdev012": IMAGES_OPENSTACKDEV_PREFIX + "terraform-apply.png",
        "openstackdev013": IMAGES_OPENSTACKDEV_PREFIX + "terraform-horizon.png",
        "openstackdev014": IMAGES_OPENSTACKDEV_PREFIX + "terraform-adding-repository.png",
        "openstackdev015": IMAGES_OPENSTACKDEV_PREFIX + "terraform-flavor-list-short.png",
        "openstackdev016": IMAGES_OPENSTACKDEV_PREFIX + "terraform-init.png",
        "openstackdev017": IMAGES_OPENSTACKDEV_PREFIX + "terraform-yes.png",
        "openstackdev018": IMAGES_OPENSTACKDEV_PREFIX + "terraform-apply.png",
        "openstackdev019": IMAGES_OPENSTACKDEV_PREFIX + "terraform-horizon.png",
        "openstackdev020": IMAGES_OPENSTACKDEV_PREFIX + "terraform-adding-repository.png",
        "openstackdev021": IMAGES_OPENSTACKDEV_PREFIX + "terraform-flavor-list-short.png",
        "openstackdev022": IMAGES_OPENSTACKDEV_PREFIX + "terraform-init.png",
        "openstackdev023": IMAGES_OPENSTACKDEV_PREFIX + "terraform-yes.png",
        "openstackdev024": IMAGES_OPENSTACKDEV_PREFIX + "terraform-apply.png",
        "openstackdev025": IMAGES_OPENSTACKDEV_PREFIX + "terraform-horizon.png",
},

    'regional_clouds': {
        'brand_key': BRAND,
        'brand_name': brand_cfg["brand_name"],
        'brand_name_hyphen': brand_cfg["brand_name_hyphen"],
        'is_multi_cloud': current_brand_is_multi_cloud,
        'regions': current_brand_regions,
        'default_region': current_default_region,
        'caption': 'black',
        'header': 'white',
        'tab_header': 'brown',
    },

    "mk8s_regions": {
        "brand_key": BRAND,
        "brand_name": brand_cfg["brand_name"],
        "brand_name_hyphen": brand_cfg["brand_name_hyphen"],
        "mk8s_name": brand_cfg.get("MK8s", "Managed Kubernetes"),
        "regions": current_active_mk8s_regions,
        "all_configured_regions": current_mk8s_regions,
        "has_regions": bool(current_active_mk8s_regions),
    },

    'doc_links': doc_links,

    'image_names': {
        'register': f"register_{brand_cfg['images_registration']}.png",
        'create': f"create_account_{brand_cfg['images_registration']}.png",
        'registered': f"registration_successful_{brand_cfg['images_registration']}.png",
    },

    "openstack_domain": {
        "brand_name": brand_cfg["brand_name"],
        "brand_name_hyphen": brand_cfg["brand_name_hyphen"],
        "project_name": brand_cfg["project_name"],
        "domain_name": brand_cfg["project_name"],
        "region_name": brand_cfg["region_name"],
        "default_region": current_default_region,
        "regions": current_brand_regions,
    },

    'forgotten_password_names': {
         'for_01': IMAGES_FORGOTTEN + 'image1.png',
         'for_02': IMAGES_FORGOTTEN + 'image2.png',
         'for_03': IMAGES_FORGOTTEN + 'image3.png',
         'for_04': IMAGES_FORGOTTEN + 'image4.png',
         'for_05': IMAGES_FORGOTTEN + 'image5.png',
         'for_06': IMAGES_FORGOTTEN + 'image6.png',
         'for_07': IMAGES_FORGOTTEN + 'image7.png',
     },

    'nvidia': {
        'nvidia': 'nvidia_chosen_eumetsat-elasticity.png',
        },

   'accounts_and_projects_management': {
	'acc_01': IMAGES_ACCOUNTS + 'acc_01.png',
	'acc_02': IMAGES_ACCOUNTS + 'note-activate-accounts.png',
	'acc_03': IMAGES_ACCOUNTS + 'add-new-project.png',
	'acc_04': IMAGES_ACCOUNTS + 'select-cloud-region.png',
	'acc_05': IMAGES_ACCOUNTS + 'activation-in-progress.png',
	'acc_06': IMAGES_ACCOUNTS + 'activation-add-still-pending.png',
	'acc_07': IMAGES_ACCOUNTS + 'horizon-login-waw4-1.png',
	'acc_08': IMAGES_ACCOUNTS + 'cloud-00341.png',
	'acc_09': IMAGES_ACCOUNTS + 'quotes-00341-3.png',
	'acc_10': IMAGES_ACCOUNTS + 'quota-00341-4.png',
	'acc_11': IMAGES_ACCOUNTS + 'change-current-or-next-wallet.png',
	'acc_12': IMAGES_ACCOUNTS + 'change-current-wallet.png',
	'acc_13': IMAGES_ACCOUNTS + 'services-to-chech-upon-spending.png',
	'acc_14': IMAGES_ACCOUNTS + 'complete-billings-report.png',
	'acc_15': IMAGES_ACCOUNTS + 'view-project-details.png',
	'acc_16': IMAGES_ACCOUNTS + 'account-details-resources.png',
	'acc_17': IMAGES_ACCOUNTS + 'extend-project.png',
	'acc_18': IMAGES_ACCOUNTS + 'given-project-already-provisioned.png',
	'acc_19': IMAGES_ACCOUNTS + 'extended-activation-in-progress.png',
	'acc_20': IMAGES_ACCOUNTS + 'new-project-extended-to-cloud.png',
	'acc_21': IMAGES_ACCOUNTS + 'what-the-table-contains-at-first.png',
	'acc_22': IMAGES_ACCOUNTS + 'remove-project-from-horizon.png',
	'acc_23': IMAGES_ACCOUNTS + 'list-projects-in-horizon.png',
	'acc_24': brand_cfg["project_name"],
	'acc_25': brand_cfg["region_name"],
	'acc_26': '_4',
	'acc_27': '_3',
	'acc_28': '',
	'acc_29': '',
	'acc_30': '',
    },


   'billings_reports': {
	'bill_01': IMAGES_BILLING + 'usage-summary-september-2025-creodias.png',
	'bill_02': IMAGES_BILLING + 'billin-reports-first-time.png',
	'bill_03': IMAGES_BILLING + 'billing-by-product-creodias.png',
	'bill_04': IMAGES_BILLING + 'billing-by-resource-creodias.png',
    },

    'use_python_2fa' : {
         'image1': 'use-python-pip-automate_04_' + IMAGES_USE_PYTHON_2FA + '.png',
         'image2': 'use-python-pip-automate_01_' + IMAGES_USE_PYTHON_2FA + '.png',
         'image3': 'use-python-pip-automate_02_' + IMAGES_USE_PYTHON_2FA + '.png',
         'image4': 'xxx_yyy_account_qr_code_' + IMAGES_USE_PYTHON_2FA + '.png',
         'image5': 'secret_code_otp_' + IMAGES_USE_PYTHON_2FA + '.png',
         'image6': 'use-python-pip-automate_03_' + IMAGES_USE_PYTHON_2FA + '.png',
    },


   'default_kubernetes_templates': {
	'dkt_01': IMAGES_KUBERNETES_TEMPLATES + '-3.png', # creodias_
	'dkt_02': IMAGES_KUBERNETES_TEMPLATES + '-2.png',
	'dkt_03': IMAGES_KUBERNETES_TEMPLATES + '-1.png',
	'dkt_04': IMAGES_KUBERNETES_TEMPLATES + '-4.png',
	'dkt_05': IMAGES_KUBERNETES_TEMPLATES + '-5.png',
	'dkt_06': IMAGES_KUBERNETES_TEMPLATES + '-6.png',
	'dkt_07': IMAGES_KUBERNETES_TEMPLATES + '-7.png', # cluster template list nsis
	'dkt_08': IMAGES_KUBERNETES_TEMPLATES + '-8.png',
	'dkt_09': IMAGES_KUBERNETES_TEMPLATES + '-3.png',
	'dkt_10': IMAGES_KUBERNETES_TEMPLATES + '-1.png', # eumetsat_
	'dkt_11': IMAGES_KUBERNETES_TEMPLATES + '-2.png',
	'dkt_12': IMAGES_KUBERNETES_TEMPLATES + '-3.png',
	'dkt_13': IMAGES_KUBERNETES_TEMPLATES + '-1.png', # eohpc_
	'dkt_14': IMAGES_KUBERNETES_TEMPLATES + '-2.png',
	'dkt_15': IMAGES_KUBERNETES_TEMPLATES + '-3.png',
	'dkt_16': IMAGES_KUBERNETES_TEMPLATES + '-1.png', # code-de_ eo-lab_
	'dkt_17': IMAGES_KUBERNETES_TEMPLATES + '-2.png',
	'dkt_18': IMAGES_KUBERNETES_TEMPLATES + '-3.png',
    },

    'mk8s_images': {
        # Accessing-OpenStack-resources-from-Eumetsat-Elasticity-Managed-Kubernetes-using-shared-networks/Accessing-OpenStack-resources-from-Eumetsat-Elasticity-Managed-Kubernetes-using-shared-networks.rst
        'mk8s001': IMAGES_MK8S_PREFIX + 'kubernetes-upgrade-1.png',
        # Accessing-OpenStack-resources-from-Eumetsat-Elasticity-Managed-Kubernetes-using-shared-networks/Accessing-OpenStack-resources-from-Eumetsat-Elasticity-Managed-Kubernetes-using-shared-networks.rst
        'mk8s002': IMAGES_MK8S_PREFIX + 'create-node-pool-network.png',
        # Accessing-OpenStack-resources-from-Eumetsat-Elasticity-Managed-Kubernetes-using-shared-networks/Accessing-OpenStack-resources-from-Eumetsat-Elasticity-Managed-Kubernetes-using-shared-networks.rst
        'mk8s003': IMAGES_MK8S_PREFIX + 'shared-network-8.png',
        # Accessing-OpenStack-resources-from-Eumetsat-Elasticity-Managed-Kubernetes-using-shared-networks/Accessing-OpenStack-resources-from-Eumetsat-Elasticity-Managed-Kubernetes-using-shared-networks.rst
        'mk8s004': IMAGES_MK8S_PREFIX + 'change_status_to_creating-456.png',
        # Accessing-OpenStack-resources-from-Eumetsat-Elasticity-Managed-Kubernetes-using-shared-networks/Accessing-OpenStack-resources-from-Eumetsat-Elasticity-Managed-Kubernetes-using-shared-networks.rst
        'mk8s005': IMAGES_MK8S_PREFIX + 'shared-network-9.png',
        # Add-node-pools-to-Managed-Eumetsat-Elasticity-cluster-using-the-launcher-GUI/Add-node-pools-to-Managed-Eumetsat-Elasticity-cluster-using-the-launcher-GUI.rst
        'mk8s006': IMAGES_MK8S_PREFIX + 'kubernetes-upgrade-15.png',
        # Add-node-pools-to-Managed-Eumetsat-Elasticity-cluster-using-the-launcher-GUI/Add-node-pools-to-Managed-Eumetsat-Elasticity-cluster-using-the-launcher-GUI.rst
        'mk8s007': IMAGES_MK8S_PREFIX + 'kubernetes-launcher-gui-5.png',
        # Add-node-pools-to-Managed-Eumetsat-Elasticity-cluster-using-the-launcher-GUI/Add-node-pools-to-Managed-Eumetsat-Elasticity-cluster-using-the-launcher-GUI.rst
        'mk8s008': IMAGES_MK8S_PREFIX + 'select_flavor_for_node_pool.png',
        # Add-node-pools-to-Managed-Eumetsat-Elasticity-cluster-using-the-launcher-GUI/Add-node-pools-to-Managed-Eumetsat-Elasticity-cluster-using-the-launcher-GUI.rst
        'mk8s009': IMAGES_MK8S_PREFIX + 'edit_node_pool_333.png',
        # Add-node-pools-to-Managed-Eumetsat-Elasticity-cluster-using-the-launcher-GUI/Add-node-pools-to-Managed-Eumetsat-Elasticity-cluster-using-the-launcher-GUI.rst
        'mk8s010': IMAGES_MK8S_PREFIX + 'kubernetes-upgrade-8.png',
        # Add-node-pools-to-Managed-Eumetsat-Elasticity-cluster-using-the-launcher-GUI/Add-node-pools-to-Managed-Eumetsat-Elasticity-cluster-using-the-launcher-GUI.rst
        'mk8s011': IMAGES_MK8S_PREFIX + 'kubernetes-upgrade-9.png',
        # Attach-Cinder-block-storage-volumes-to-pods-in-ReadWriteOnce-mode-on-Eumetsat-Elasticity-Managed-Kubernetes/Attach-Cinder-block-storage-volumes-to-pods-in-ReadWriteOnce-mode-on-Eumetsat-Elasticity-Managed-Kubernetes.rst
        'mk8s012': IMAGES_MK8S_PREFIX + 'available_storage_classes_for_cinder.png',
        # Attach-Cinder-block-storage-volumes-to-pods-in-ReadWriteOnce-mode-on-Eumetsat-Elasticity-Managed-Kubernetes/Attach-Cinder-block-storage-volumes-to-pods-in-ReadWriteOnce-mode-on-Eumetsat-Elasticity-Managed-Kubernetes.rst
        'mk8s013': IMAGES_MK8S_PREFIX + 'cinder_rwo_pvc_created.png',
        # Attach-Cinder-block-storage-volumes-to-pods-in-ReadWriteOnce-mode-on-Eumetsat-Elasticity-Managed-Kubernetes/Attach-Cinder-block-storage-volumes-to-pods-in-ReadWriteOnce-mode-on-Eumetsat-Elasticity-Managed-Kubernetes.rst
        'mk8s014': IMAGES_MK8S_PREFIX + 'cinder_rwo_pod_running.png',
        # Attach-Cinder-block-storage-volumes-to-pods-in-ReadWriteOnce-mode-on-Eumetsat-Elasticity-Managed-Kubernetes/Attach-Cinder-block-storage-volumes-to-pods-in-ReadWriteOnce-mode-on-Eumetsat-Elasticity-Managed-Kubernetes.rst
        'mk8s015': IMAGES_MK8S_PREFIX + 'file_stored_on_cinder_volume.png',
        # Attach-Cinder-block-storage-volumes-to-pods-in-ReadWriteOnce-mode-on-Eumetsat-Elasticity-Managed-Kubernetes/Attach-Cinder-block-storage-volumes-to-pods-in-ReadWriteOnce-mode-on-Eumetsat-Elasticity-Managed-Kubernetes.rst
        'mk8s016': IMAGES_MK8S_PREFIX + 'the_data_has_survived.png',
        # Automatic-Kubernetes-cluster-upgrade-on-Eumetsat-Elasticity-OpenStack-Magnum/Automatic-Kubernetes-cluster-upgrade-on-Eumetsat-Elasticity-OpenStack-Magnum.rst
        'mk8s017': IMAGES_MK8S_PREFIX + 'upgrade-kubernetes-17.png',
        # Create-a-Managed-Kubernetes-Cluster-with-Terraform-on-Eumetsat-Elasticity/Create-a-Managed-Kubernetes-Cluster-with-Terraform-on-Eumetsat-Elasticity.rst
        'mk8s018': IMAGES_MK8S_PREFIX + 'terraform_create_cluster.png',
        # Create-a-Managed-Kubernetes-Cluster-with-Terraform-on-Eumetsat-Elasticity/Create-a-Managed-Kubernetes-Cluster-with-Terraform-on-Eumetsat-Elasticity.rst
        'mk8s019': IMAGES_MK8S_PREFIX + 'terraform_create_cluster_ui.png',
        # Create-a-Managed-Kubernetes-Cluster-with-Terraform-on-Eumetsat-Elasticity/Create-a-Managed-Kubernetes-Cluster-with-Terraform-on-Eumetsat-Elasticity.rst
        'mk8s020': IMAGES_MK8S_PREFIX + 'terraform_has_created_cluster.png',
        # Create-a-Managed-Kubernetes-Cluster-with-Terraform-on-Eumetsat-Elasticity/Create-a-Managed-Kubernetes-Cluster-with-Terraform-on-Eumetsat-Elasticity.rst
        'mk8s021': IMAGES_MK8S_PREFIX + 'adding_workers.png',
        # Create-and-use-volume-snapshots-on-Eumetsat-Elasticity-Managed-Kubernetes/Create-and-use-volume-snapshots-on-Eumetsat-Elasticity-Managed-Kubernetes.rst
        'mk8s022': IMAGES_MK8S_PREFIX + 'kubectl_showing_active_pods.png',
        # Create-and-use-volume-snapshots-on-Eumetsat-Elasticity-Managed-Kubernetes/Create-and-use-volume-snapshots-on-Eumetsat-Elasticity-Managed-Kubernetes.rst
        'mk8s023': IMAGES_MK8S_PREFIX + 'available_storage_classes_for_cinder.png',
        # Create-and-use-volume-snapshots-on-Eumetsat-Elasticity-Managed-Kubernetes/Create-and-use-volume-snapshots-on-Eumetsat-Elasticity-Managed-Kubernetes.rst
        'mk8s024': IMAGES_MK8S_PREFIX + 'snapshot_created_and_ready.png',
        # Create-and-use-volume-snapshots-on-Eumetsat-Elasticity-Managed-Kubernetes/Create-and-use-volume-snapshots-on-Eumetsat-Elasticity-Managed-Kubernetes.rst
        'mk8s025': IMAGES_MK8S_PREFIX + 'snapshot_restored_pvc_bound.png',
        # Create-and-use-volume-snapshots-on-Eumetsat-Elasticity-Managed-Kubernetes/Create-and-use-volume-snapshots-on-Eumetsat-Elasticity-Managed-Kubernetes.rst
        'mk8s026': IMAGES_MK8S_PREFIX + 'verify_the_restored_data.png',
        # How-to-create-a-Managed-Kubernetes-cluster-using-Eumetsat-Elasticity-launcher-GUI/How-to-create-a-Managed-Kubernetes-cluster-using-Eumetsat-Elasticity-launcher-GUI.rst
        'mk8s027': IMAGES_MK8S_PREFIX + 'kubernetes-launcher-gui-1.png',
        # How-to-create-a-Managed-Kubernetes-cluster-using-Eumetsat-Elasticity-launcher-GUI/How-to-create-a-Managed-Kubernetes-cluster-using-Eumetsat-Elasticity-launcher-GUI.rst
        'mk8s028': IMAGES_MK8S_PREFIX + 'kubernetes-launcher-gui-3.png',
        # How-to-create-a-Managed-Kubernetes-cluster-using-Eumetsat-Elasticity-launcher-GUI/How-to-create-a-Managed-Kubernetes-cluster-using-Eumetsat-Elasticity-launcher-GUI.rst
        'mk8s029': IMAGES_MK8S_PREFIX + 'machine-specs-1.png',
        # How-to-create-a-Managed-Kubernetes-cluster-using-Eumetsat-Elasticity-launcher-GUI/How-to-create-a-Managed-Kubernetes-cluster-using-Eumetsat-Elasticity-launcher-GUI.rst
        'mk8s030': IMAGES_MK8S_PREFIX + 'kubernetes-launcher-gui-7.png',
        # How-to-create-a-Managed-Kubernetes-cluster-using-Eumetsat-Elasticity-launcher-GUI/How-to-create-a-Managed-Kubernetes-cluster-using-Eumetsat-Elasticity-launcher-GUI.rst
        'mk8s031': IMAGES_MK8S_PREFIX + 'kubernetes-launcher-gui-10.png',
        # How-to-create-a-Managed-Kubernetes-cluster-using-Eumetsat-Elasticity-launcher-GUI/How-to-create-a-Managed-Kubernetes-cluster-using-Eumetsat-Elasticity-launcher-GUI.rst
        'mk8s032': IMAGES_MK8S_PREFIX + 'kubernetes-upgrade-12.png',
        # How-to-create-a-Managed-Kubernetes-cluster-using-Eumetsat-Elasticity-launcher-GUI/How-to-create-a-Managed-Kubernetes-cluster-using-Eumetsat-Elasticity-launcher-GUI.rst
        'mk8s033': IMAGES_MK8S_PREFIX + 'kubernetes-upgrade-13.png',
        # How-to-create-a-Managed-Kubernetes-cluster-using-Eumetsat-Elasticity-launcher-GUI/How-to-create-a-Managed-Kubernetes-cluster-using-Eumetsat-Elasticity-launcher-GUI.rst
        'mk8s034': IMAGES_MK8S_PREFIX + 'namespaces_0987.png',
        # How-to-create-a-Managed-Kubernetes-cluster-using-Eumetsat-Elasticity-launcher-GUI/How-to-create-a-Managed-Kubernetes-cluster-using-Eumetsat-Elasticity-launcher-GUI.rst
        'mk8s035': IMAGES_MK8S_PREFIX + 'some_other_screenshot_resources.png',
        # How-to-create-a-Managed-Kubernetes-cluster-using-Eumetsat-Elasticity-launcher-GUI/How-to-create-a-Managed-Kubernetes-cluster-using-Eumetsat-Elasticity-launcher-GUI.rst
        'mk8s036': IMAGES_MK8S_PREFIX + 'both_clusters_running.png',
        # How-to-create-a-Managed-Kubernetes-cluster-using-Eumetsat-Elasticity-launcher-GUI/How-to-create-a-Managed-Kubernetes-cluster-using-Eumetsat-Elasticity-launcher-GUI.rst
        'mk8s037': IMAGES_MK8S_PREFIX + 'kubernetes-launcher-gui-12.png',
        # How-to-create-a-Managed-Kubernetes-cluster-using-Eumetsat-Elasticity-launcher-GUI/How-to-create-a-Managed-Kubernetes-cluster-using-Eumetsat-Elasticity-launcher-GUI.rst
        'mk8s038': IMAGES_MK8S_PREFIX + 'the_cluster_has_been_deleted_twice.png',
        # How-to-create-a-Managed-Kubernetes-cluster-using-Eumetsat-Elasticity-launcher-GUI/Upgrade-a-Managed-Kubernetes-on-Eumetsat-Elasticity.rst
        'mk8s039': IMAGES_MK8S_PREFIX + 'cluster_starting_point.png',
        # How-to-create-a-Managed-Kubernetes-cluster-using-Eumetsat-Elasticity-launcher-GUI/Upgrade-a-Managed-Kubernetes-on-Eumetsat-Elasticity.rst
        'mk8s040': IMAGES_MK8S_PREFIX + 'upgrade_to_cluster_1_31.png',
        # How-to-create-a-Managed-Kubernetes-cluster-using-Eumetsat-Elasticity-launcher-GUI/Upgrade-a-Managed-Kubernetes-on-Eumetsat-Elasticity.rst
        'mk8s041': IMAGES_MK8S_PREFIX + 'kubernetes_upgrade_window.png',
        # How-to-create-a-Managed-Kubernetes-cluster-using-Eumetsat-Elasticity-launcher-GUI/Upgrade-a-Managed-Kubernetes-on-Eumetsat-Elasticity.rst
        'mk8s042': IMAGES_MK8S_PREFIX + 'managed_cluster_upgrading.png',
        # How-to-create-a-Managed-Kubernetes-cluster-using-Eumetsat-Elasticity-launcher-GUI/Upgrade-a-Managed-Kubernetes-on-Eumetsat-Elasticity.rst
        'mk8s043': IMAGES_MK8S_PREFIX + 'managed_kubernetes_upgraded.png',
        # Managed-Kubernetes-backups-on-Eumetsat-Elasticity/Managed-Kubernetes-backups-on-Eumetsat-Elasticity.rst
        'mk8s044': IMAGES_MK8S_PREFIX + 'backup_01.png',
        # Managed-Kubernetes-backups-on-Eumetsat-Elasticity/Managed-Kubernetes-backups-on-Eumetsat-Elasticity.rst
        'mk8s045': IMAGES_MK8S_PREFIX + 'backup_image_02.png',
        # Managed-Kubernetes-backups-on-Eumetsat-Elasticity/Managed-Kubernetes-backups-on-Eumetsat-Elasticity.rst
        'mk8s046': IMAGES_MK8S_PREFIX + 'third_image_ina_row.png',
        # Managed-Kubernetes-backups-on-Eumetsat-Elasticity/Managed-Kubernetes-backups-on-Eumetsat-Elasticity.rst
        'mk8s047': IMAGES_MK8S_PREFIX + 'multiple_copies_cluster.png',
        # Managed-Kubernetes-backups-on-Eumetsat-Elasticity/Managed-Kubernetes-backups-on-Eumetsat-Elasticity.rst
        'mk8s048': IMAGES_MK8S_PREFIX + 'image-2025-8-29_9-37-27.png',
        # Managed-Kubernetes-backups-on-Eumetsat-Elasticity/Managed-Kubernetes-backups-on-Eumetsat-Elasticity.rst
        'mk8s049': IMAGES_MK8S_PREFIX + 'the-process-part-3.png',
        # Managed-Kubernetes-version-support-model-on-Eumetsat-Elasticity/Managed-Kubernetes-version-support-model-on-Eumetsat-Elasticity.rst
        'mk8s050': IMAGES_MK8S_PREFIX + 'managed-kubernetes-details-version.png',
        # Managed-Kubernetes-version-support-model-on-Eumetsat-Elasticity/Managed-Kubernetes-version-support-model-on-Eumetsat-Elasticity.rst
        'mk8s051': IMAGES_MK8S_PREFIX + 'managed-kubernetes-create-version-selection.png',
        # Managed-Kubernetes-version-support-model-on-Eumetsat-Elasticity/Managed-Kubernetes-version-support-model-on-Eumetsat-Elasticity.rst
        'mk8s052': IMAGES_MK8S_PREFIX + 'managed-kubernetes-upgrade-version-selection.png',
        # Obtain-managed-Kubernetes-API-token-on-Eumetsat-Elasticity/Obtain-managed-Kubernetes-API-token-on-Eumetsat-Elasticity.rst
        'mk8s053': IMAGES_MK8S_PREFIX + 'get_to_token_button.png',
        # Obtain-managed-Kubernetes-API-token-on-Eumetsat-Elasticity/Obtain-managed-Kubernetes-API-token-on-Eumetsat-Elasticity.rst
        'mk8s054': IMAGES_MK8S_PREFIX + '1password-image-3.png',
        # Obtain-managed-Kubernetes-API-token-on-Eumetsat-Elasticity/Obtain-managed-Kubernetes-API-token-on-Eumetsat-Elasticity.rst
        'mk8s055': IMAGES_MK8S_PREFIX + '1password-image-349.png',
        # Obtain-managed-Kubernetes-API-token-on-Eumetsat-Elasticity/Obtain-managed-Kubernetes-API-token-on-Eumetsat-Elasticity.rst
        'mk8s056': IMAGES_MK8S_PREFIX + 'create_token_234.png',
        # Obtain-managed-Kubernetes-API-token-on-Eumetsat-Elasticity/Obtain-managed-Kubernetes-API-token-on-Eumetsat-Elasticity.rst
        'mk8s057': IMAGES_MK8S_PREFIX + '1password-image-345.png',
        # Obtain-managed-Kubernetes-API-token-on-Eumetsat-Elasticity/Obtain-managed-Kubernetes-API-token-on-Eumetsat-Elasticity.rst
        'mk8s058': IMAGES_MK8S_PREFIX + '1password-image-346.png',
        # Obtain-managed-Kubernetes-API-token-on-Eumetsat-Elasticity/Obtain-managed-Kubernetes-API-token-on-Eumetsat-Elasticity.rst
        'mk8s059': IMAGES_MK8S_PREFIX + 'cloudferr-managed-kubernetes.png',
        # Obtain-managed-Kubernetes-API-token-on-Eumetsat-Elasticity/Obtain-managed-Kubernetes-API-token-on-Eumetsat-Elasticity.rst
        'mk8s060': IMAGES_MK8S_PREFIX + '1password-image-347.png',
        # Sharing-a-MIG-enabled-GPU-card-between-Kubernetes-pods-on-Eumetsat-Elasticity/Sharing-a-MIG-enabled-GPU-card-between-Kubernetes-pods-on-Eumetsat-Elasticity.rst
        'mk8s061': IMAGES_MK8S_PREFIX + 'cpu_quota_for_cluster_exceeded.png',
        # Sharing-a-MIG-enabled-GPU-card-between-Kubernetes-pods-on-Eumetsat-Elasticity/Sharing-a-MIG-enabled-GPU-card-between-Kubernetes-pods-on-Eumetsat-Elasticity.rst
        'mk8s062': IMAGES_MK8S_PREFIX + 'quota_limits.png',
        # Sharing-a-MIG-enabled-GPU-card-between-Kubernetes-pods-on-Eumetsat-Elasticity/Sharing-a-MIG-enabled-GPU-card-between-Kubernetes-pods-on-Eumetsat-Elasticity.rst
        'mk8s063': IMAGES_MK8S_PREFIX + 'selecting-h100-for-nodepool.png',
        # Sharing-a-MIG-enabled-GPU-card-between-Kubernetes-pods-on-Eumetsat-Elasticity/Sharing-a-MIG-enabled-GPU-card-between-Kubernetes-pods-on-Eumetsat-Elasticity.rst
        'mk8s064': IMAGES_MK8S_PREFIX + 'creation_of_h100_started.png',
        # Sharing-a-MIG-enabled-GPU-card-between-Kubernetes-pods-on-Eumetsat-Elasticity/Sharing-a-MIG-enabled-GPU-card-between-Kubernetes-pods-on-Eumetsat-Elasticity.rst
        'mk8s065': IMAGES_MK8S_PREFIX + 'ha10_running_normally.png',
        # Sharing-a-MIG-enabled-GPU-card-between-Kubernetes-pods-on-Eumetsat-Elasticity/Sharing-a-MIG-enabled-GPU-card-between-Kubernetes-pods-on-Eumetsat-Elasticity.rst
        'mk8s066': IMAGES_MK8S_PREFIX + 'resources_nodes_get_values.png',
        # Sharing-a-MIG-enabled-GPU-card-between-Kubernetes-pods-on-Eumetsat-Elasticity/Sharing-a-MIG-enabled-GPU-card-between-Kubernetes-pods-on-Eumetsat-Elasticity.rst
        'mk8s067': IMAGES_MK8S_PREFIX + 'running_code_from_step_3.png',
        # Sharing-a-MIG-enabled-GPU-card-between-Kubernetes-pods-on-Eumetsat-Elasticity/Sharing-a-MIG-enabled-GPU-card-between-Kubernetes-pods-on-Eumetsat-Elasticity.rst
        'mk8s068': IMAGES_MK8S_PREFIX + 'long_json_as_result.png',
        # Sharing-a-MIG-enabled-GPU-card-between-Kubernetes-pods-on-Eumetsat-Elasticity/Sharing-a-MIG-enabled-GPU-card-between-Kubernetes-pods-on-Eumetsat-Elasticity.rst
        'mk8s069': IMAGES_MK8S_PREFIX + 'allocatable_and_actual_are_same.png',
        # Sharing-a-vGPU-card-between-Kubernetes-pods-with-time-slicing-on-Eumetsat-Elasticity/Sharing-a-vGPU-card-between-Kubernetes-pods-with-time-slicing-on-Eumetsat-Elasticity.rst
        'mk8s070': IMAGES_MK8S_PREFIX + 'cpu_quota_for_cluster_exceeded.png',
        # Sharing-a-vGPU-card-between-Kubernetes-pods-with-time-slicing-on-Eumetsat-Elasticity/Sharing-a-vGPU-card-between-Kubernetes-pods-with-time-slicing-on-Eumetsat-Elasticity.rst
        'mk8s071': IMAGES_MK8S_PREFIX + 'quota_limits.png',
        # Sharing-a-vGPU-card-between-Kubernetes-pods-with-time-slicing-on-Eumetsat-Elasticity/Sharing-a-vGPU-card-between-Kubernetes-pods-with-time-slicing-on-Eumetsat-Elasticity.rst
        'mk8s072': IMAGES_MK8S_PREFIX + 'select_vm_l40s_1_for_vgpu_support_new.png',
        # Sharing-a-vGPU-card-between-Kubernetes-pods-with-time-slicing-on-Eumetsat-Elasticity/Sharing-a-vGPU-card-between-Kubernetes-pods-with-time-slicing-on-Eumetsat-Elasticity.rst
        'mk8s073': IMAGES_MK8S_PREFIX + 'creating_vm_l40s_1_nodepool.png',
        # Upgrade-Managed-Kubernetes-on-Eumetsat-Elasticity/Upgrade-Managed-Kubernetes-on-Eumetsat-Elasticity.rst
        'mk8s074': IMAGES_MK8S_PREFIX + 'cluster_starting_point.png',
        # Upgrade-Managed-Kubernetes-on-Eumetsat-Elasticity/Upgrade-Managed-Kubernetes-on-Eumetsat-Elasticity.rst
        'mk8s075': IMAGES_MK8S_PREFIX + 'upgrade_to_cluster_1_31.png',
        # Upgrade-Managed-Kubernetes-on-Eumetsat-Elasticity/Upgrade-Managed-Kubernetes-on-Eumetsat-Elasticity.rst
        'mk8s076': IMAGES_MK8S_PREFIX + 'kubernetes_upgrade_window.png',
        # Upgrade-Managed-Kubernetes-on-Eumetsat-Elasticity/Upgrade-Managed-Kubernetes-on-Eumetsat-Elasticity.rst
        'mk8s077': IMAGES_MK8S_PREFIX + 'managed_cluster_upgrading.png',
        # Upgrade-Managed-Kubernetes-on-Eumetsat-Elasticity/Upgrade-Managed-Kubernetes-on-Eumetsat-Elasticity.rst
        'mk8s078': IMAGES_MK8S_PREFIX + 'managed_kubernetes_upgraded.png',
        # Use-SFS-shared-file-storage-with-pods-in-ReadWriteMany-mode-on-Eumetsat-Elasticity-Managed-Kubernetes/Use-SFS-shared-file-storage-with-pods-in-ReadWriteMany-mode-on-Eumetsat-Elasticity-Managed-Kubernetes.rst
        'mk8s079': IMAGES_MK8S_PREFIX + 'available_storage_classes_for_cinder.png',
        # Volume-cloning-on-Eumetsat-Elasticity-Managed-Kubernetes/Volume-cloning-on-Eumetsat-Elasticity-Managed-Kubernetes.rst
        'mk8s080': IMAGES_MK8S_PREFIX + 'kubectl_showing_active_pods.png',
        # Volume-cloning-on-Eumetsat-Elasticity-Managed-Kubernetes/Volume-cloning-on-Eumetsat-Elasticity-Managed-Kubernetes.rst
        'mk8s081': IMAGES_MK8S_PREFIX + 'available_storage_classes_for_cinder.png',
        # Volume-cloning-on-Eumetsat-Elasticity-Managed-Kubernetes/Volume-cloning-on-Eumetsat-Elasticity-Managed-Kubernetes.rst
        'mk8s082': IMAGES_MK8S_PREFIX + 'kubectl_describe_clone_restored_pvc.png',
        # Volume-cloning-on-Eumetsat-Elasticity-Managed-Kubernetes/Volume-cloning-on-Eumetsat-Elasticity-Managed-Kubernetes.rst
        'mk8s083': IMAGES_MK8S_PREFIX + 'final_success_the_pod_prints_ok.png',
        # Create-a-Managed-Kubernetes-Cluster-with-Terraform-on-Eumetsat-Elasticity/Create-a-Managed-Kubernetes-Cluster-with-Terraform-on-Eumetsat-Elasticity.rst
        'mk8s084': IMAGES_MK8S_PREFIX + 'cloudferro-driver-for-terraform.png',
        # Managed-Kubernetes-backups-on-Eumetsat-Elasticity/Managed-Kubernetes-backups-on-Eumetsat-Elasticity.rst
        'mk8s085': IMAGES_MK8S_PREFIX + 'configuring-backup-with-velero.png',
    },


    'caption_colors': {
        'caption': 'white',
        'header': 'white',
        'tab_header': 'black',
        'red': 'red',
    },

    'editing_profiles': {
        'editing_profile': 'editing_profile_eumetsat.png',
    },
    'contracts_and_wallets': {
        'contracts_wallets': 'wallets_contracts_creodias.png',
    },

    'help_desk_and_support': {
        'tickets': 'tickets_creodias.png', 'add_ticket': 'add_ticket_creodias.png',
    },
    'inviting_new_user': {
        'inv_01': 'inv_01_eumetsat.png', 'inv_02': 'inv_02_eumetsat.png',
    },
    'removing_user': {
        'users_roles_01': 'inv_01_eumetsat.png', 
    },
    'users_roles': {
        'users_roles': 'users_roles_eumetsat.png', 
    },

    'services': {
        'services': 'services_eumetsat.png', 
    },
    'adding_editing_organizations': {
        'org_01': 'register_organization_eumetsat.png', 
    },
    'login_vm': {
        'login': 'login_eumetsat.png', 
    },
    'service_organization': {
        'login': 'requeste_2.jpg',
    },
    'request_resources': {
        'login': 'requeste_3.png',
    },
    's3_login': {
        's3_login': current_default_region["s3_host"] if current_default_region else '',
        'region': current_default_region["s3cmd_region"] if current_default_region else '',
    },
    'openstack_domain': {
        'openstack_domain': 'domain_eumetsat.png', 
    },
    'cloud_name': {
        'cloud_name': current_default_region["display_name"] if current_default_region else '',
    },

   'template_created': {
        'template_created': 'new_template2.png',
    },
    'eodata_endpoint': {
        'eodata_endpoint': current_default_region["eodata_host"] if current_default_region else '',
        'https_eodata_endpoint': current_default_region["eodata_endpoint"] if current_default_region else '',
    },
    'remote_transfer_for_eodata': {
        'remote_transfer_for_eodata': 's3.cloudferro.com',
    },

    'create_windows_wm_server': {
		'ww1': 'ww1_eumetsat.png', 
		'ww2': 'ww2_eumetsat.png',
		'ww3': 'ww3.png',
		'ww4': 'ww4.png',
		'access_option' : 'Eumetsat Elasticity',
	},
    'rapideye': {
		'rapideye' : 'rapideye_s3_credentials_eolab.png',
		'contact_form' : 'contact_form_rapideye.png',
	},

   'data_explorer': {
        'data_explorer_01' : 'login-data-explorer-01_creodias.png',
        'data_explorer_02' : 'login-data-explorer-02_creodias.png',
        'data_explorer_03' : 'login_creodias_data_explorer.png',
        'data_explorer_04' : 'login-data-explorer-04_creodias.png',
        'data_explorer_05' : 'data-explorer-download-01-modified_creodias.png',
        'data_explorer_06' : 'cropped_04_creodias.png',
        'data_explorer_07' : 'data-explorer-download-products_creodias.png',
        'data_explorer_08' : 'data-explorer-download-05-modified_creodias.png',
        'data_explorer_09' : 'data-explorer-download-06_creodias.png',

    },

    'help_desk_and_support': {
        'tickets': 'tickets_eumetsat.png', 'add_ticket': 'add_ticket_eumetsat.png',
    },

    'dual_factor_authentication': {
		'eefa_qr_screen': 'eefa_qr_screen_eumetsat.png', 
		'eefa_start': 'eefa_start_eumetsat.png', 
		'eefa_sign_regular': 'eefa_sign_regular_eumetsat.png',
		'eefa_mobile_auth_setup': 'eefa_mobile_auth_setup_eumetsat.png',
		'eefa_normal-Login': 'eefa_normal-Login_eumetsat.png',
		'eefa_sign_regular': 'eefa_sign_regular_eumetsat.png',
		'eefa_restart_login': 'eefa_restart_login_eumetsat.png',
		'eefa_restart_code': 'eefa_restart_code_eumetsat.png',
		'eefa_828966': 'eefa_828966_eumetsat.png',
		'eefa_logged_in': 'eefa_logged_in_eumetsat.png',
	},


  'access_sen4cap': {
		'access_sen4cap_01': 'access_sen4cap_eo-lab.png',
		'access_sen4cap_02': 'saml_eumetsat-elasticity.png',
		'access_sen4cap_03': 'management_eo-lab.png'

		 },


  'ecommerce_images': {
		'ecommerce_images_1': 'cloudferro_cloud_1.png', # Screenshot_20241017_144736.png',
		'ecommerce_images_2': 'cloudferro_cloud_2.png', #image-2024-10-11_12-21-43.png',
		'ecommerce_images_3': 'cloudferro_cloud_3.png', #Screenshot_20241017_150413.png',
		'ecommerce_images_4': 'cloudferro_cloud_4.png', #Screenshot_20241017_150413.png',
		'ecommerce_images_5': 'cloudferro_cloud_5.png', #image-2024-10-11_12-22-31.png',
		'ecommerce_images_6': 'cloudferro_cloud_6.png', #blurred_qqq_www.jpg',
		'ecommerce_images_7': 'cloudferro_cloud_7.png', #image-2024-10-11_11-50-44.png',
		'ecommerce_images_8': 'cloudferro_cloud_8.png', #blurred_list_of.png',
		'ecommerce_images_9': 'cloudferro_cloud_9.png', #blurred2_ggg_fff_rrr.png',
		'ecommerce_images_10': 'cloudferro_cloud_10.png', #Screenshot_20241017_153449.png',
		'ecommerce_images_11': 'cloudferro_cloud_11.png', #image-2024-10-11_11-10-15.png',

		 },

    'brand_names': {
		'brand_name': brand_cfg["brand_name"],
        'noobaa01' : 'create_object_container.png',
        'noobaa02' : 'image2023-7-20_11-58-22.png',
		'brand_name_hyphen': brand_cfg["brand_name_hyphen"] ,
		'brand_name_site_link': brand_cfg["brand_name_site_link"],
		'brand_name_site_auth_link': brand_cfg["brand_name_site_auth_link"],
		'tenant_manager_link': brand_cfg["brand_name_site_auth_link"],
        'regions': current_brand_regions,
        'doc_links': doc_links,
        'default_region': current_default_region,
        'default_region_name': current_default_region["display_name"] if current_default_region else '',
        'default_s3_endpoint': current_default_region["s3_endpoint"] if current_default_region else '',
        'default_eodata_endpoint': current_default_region["eodata_endpoint"] if current_default_region else '',
        'default_keystone_endpoint': current_default_region["keystone_endpoint"] if current_default_region else '',
        'default_horizon_endpoint': current_default_region["horizon_endpoint"] if current_default_region else '',

		'MK8s' : brand_cfg["MK8s"],
        "mk8s_url": brand_cfg["mk8s_url"],
        "server_cert": brand_cfg["server_cert"],

        'brand_name_cloud': 'Eumetsat-Elasticity-WAW3-1',
		'ecommerce_link': 'https://ecommerce.creodias.eu',
        'satellite_repository': '/eodata',
		'waw3_1': 'WAW3-1',
		'client_id' : 'CLOUDFERRO_PUBLIC',
        'datahub_address' : 'datahub.creodias.eu',
        'sales_support': 'sales@cloudferro.com',
        'product_name_link' : 'S1A_IW_GRDH_1SDV_20141031T161924_20141031T161949_003076_003856_634E.SAFE',
        'product_name_image' : 'find_id_from_link_creodias.png',
        'product_name_id' : 'c23d5ffd-bc2a-54c1-a2cf-e2dc18bc945f',
        'output_datahub_link' : 'output_datahub_link.png',
        'product_name_image' : 'output_datahub_link_creodias.png',
        'product_name_link_creodias' : 'S1A_IW_GRDH_1SDV_20141031T161924_20141031T161949_003076_003856_634E.SAFE',
        'product_name_id_creodias' : 'c23d5ffd-bc2a-54c1-a2cf-e2dc18bc945f',
        'output_datahub_link_creodias' : 'output_datahub_link_creodias.png',
        'product_name_directory' : 'preview',
        'product_name_directory_file' : 'preview',
        'product_name_file' : 'quick-look.png',
        'terminal_output' : 'terminal_output_creodias.png',
        'wget_output' : 'wget_output_creodias.png',
        'quick_look' : 'quick-look_creodias.png',
        'zipper_address' : 'zipper.creodias.eu',
#         'zipper_address' : 'download.dataspace.copernicus.eu',
        'client_id' : 'CLOUDFERRO_PUBLIC',

        'manage_totp' : 'manage-totp-05_creodias.png',
        'brand_identity' : 'Eumetsat-elasticity',
        'keycloak_identity' : 'https://identity.cloudferro.com/auth/realms/Eumetsat-elasticity',
        'site_link' : 'https://docs.cloud.eumetsat.int',
        'datavolume': 'datavolume',
		'openstack': 'openstack', 
		'openstackcli': 'openstackcli', 
		'eodata': 'eodata', 
		'gettingstarted': 'accountmanagement',
		'general': 'cloud',
		's3': 's3',
		'sfs': 'sfs',
		'versions': 'versions',
		'vgpu': 'vgpu',
		'kubernetes': 'kubernetes',
		'networking': 'networking',
		'windows': 'windows',
		'security': 'security',
        'site_name': 'Eumetsat Elasticity',
        'site_address': 'www.eumetsat.int',
        'ecommerce_link': '',

        'MK8s' : brand_cfg["MK8s"],
        "mk8s_url": brand_cfg["mk8s_url"],
        "server_cert": brand_cfg["server_cert"],
        "main_site_name": brand_cfg["main_site_name"],
        "main_site_url": brand_cfg["main_site_url"],

    },

    'tenant_manager_user_and_roles': {
		'tenant_manager_001' : 'Tenant_manager_01_eumetsat.png',
		'tenant_manager_002' : 'Tenant_manager_02_eumetsat.png',
		'tenant_manager_003' : 'Tenant_manager_03_eumetsat.png',
		'tenant_manager_004' : 'Tenant_manager_04_eumetsat.png',
		'tenant_manager_005' : 'Tenant_manager_05_eumetsat.png',
	},

  'dashboard_services': {
		'dashboard_services_1': 'dashboard-services-1-creodias.png',
		'dashboard_services_2': 'dashboard-services-2-creodias.png',
		'dashboard_services_3': 'dashboard-services-3-creodias.png',
		'dashboard_services_4': 'dashboard-services-4-creodias.png',
		'dashboard_services_5': 'dashboard-services-5-creodias.png',
		'dashboard_services_6': 'dashboard-services-6-creodias.png',
		'dashboard_services_7': 'dashboard-services-7-creodias.png',
		'dashboard_services_8': 'dashboard-services-8-creodias.png',
		'dashboard_services_9': 'dashboard-services-9-creodias.png',
		'dashboard_services_10': 'dashboard-services-10-creodias.png',
		'dashboard_services_11': 'dashboard-services-11-creodias.png',
		'dashboard_services_12': 'dashboard-services-12-creodias.png',

		 },

  'cookie_consent': {
		'cookie_consent_1': 'cookie-consent-cloudferro-cloud-1.png',
		'cookie_consent_2': 'cookie-consent-cloudferro-cloud-2.png',
		'cookie_consent_3': 'cookie-consent-cloudferro-cloud-3.png',
		'cookie_consent_4': 'cookie-consent-cloudferro-cloud-4.png',
		'cookie_consent_5': 'cookie-consent-cloudferro-cloud-5.png',
		'cookie_consent_6': 'cookie-consent-cloudferro-cloud-6.png',
		'cookie_consent_7': 'cookie-consent-cloudferro-cloud-7.png',
		'cookie_consent_8': 'cookie-consent-cloudferro-cloud-8.png',
		'cookie_consent_9': 'cookie-consent-cloudferro-cloud-9.png',
		'cookie_consent_10': 'cookie-consent-cloudferro-cloud-10.png',
		'cookie_consent_11': 'cookie-consent-cloudferro-cloud-11.png',
		'cookie_consent_12': 'cookie-consent-cloudferro-cloud-12.png',
		'cookie_consent_15': 'cookie-consent-cloudferro-cloud-15.png',

		 },


      'verification': {
            'verification_1': 'verification-creodias-1.png',
            'verification_2': 'verification-creodias-2.png',
            'verification_3': 'verification-creodias-3.png',
            'verification_4': 'verification-creodias-4.png',
            'verification_5': 'verification-creodias-5.png',
            'verification_6': 'verification-creodias-6.png',
            'verification_7': 'verification-creodias-7.png',
            'verification_8': 'verification-creodias-8.png',
            'verification_9': 'verification-creodias-9.png',
            'verification_10': 'verification-creodias-10.png',
            'verification_11': 'verification-creodias-11.png',
            'verification_12': 'verification-creodias-12.png',

             },


      'special_eodata_rebranding': {
            'special_eodata_1': 'special_eodata_menu.png',
            'special_eodata_2': 'download_special_eodata_rc_file.png',
            'special_eodata_3': 'special_eodata_rc_file_content.png',
            'special_eodata_4': 'activate-api-2fa-01_creodias.png',
            'special_eodata_5': 'flavor_list_2fa_short.png',

             },


 's3cmd_configuration': {
            's3cmd_config_1': 'configure-firewall-creo-1.png',
            's3cmd_config_2': 'configure-firewall-creo-3.png',
            's3cmd_config_3': 'configure-firewall-creo-5.png',
            's3cmd_config_4': 'configure-firewall-creo-6.png',

         },

      '1password': {
           'password1': '1password_password1.png',
           'password2': '1password_password2.png',
           'password3': '1password_password3.png',
      },


      'kubernetes_managed': {
           'image1': 'get_to_token_button.png',
           'swagger': 'https://managed-kubernetes.cloudferro.com/swagger',
           'address': 'https://managed-kubernetes.cloudferro.com',
      },

}

# >>> CF_BRAND_BLOCK: jinja_extra_contexts
jinja_contexts = globals().get("jinja_contexts", {})

jinja_contexts["dedl_hda_mcp_context"] = dedl_hda_mcp_context

jinja_contexts["horizon_interfaces"] = {
    "horizon_interfaces": brand_cfg.get("horizon_interfaces", []),
}
# <<< CF_BRAND_BLOCK: jinja_extra_contexts

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = [
    "_build",
    "**/_build",
    "Thumbs.db",
    ".DS_Store",

    "modis/**/*.ipynb",
]

CF_SHARED = "https://github.com/CloudFerro/"
CF_LOCAL = "https://github.com/cloudferrodocumentation/"

blob = "/blob/main/source/"
tree = "/tree/main/source/"

LOCAL = "ecis"

CF3 = CF_SHARED + "cf3-doc" + blob
KUBERNETES = CF_LOCAL + "kubernetes-managed" + blob
# KUBERNETES = CF_SHARED + "kubernetes-doc" + blob

LOCAL_SOURCE = CF_LOCAL + LOCAL + blob
EUMETSAT_ELASTICITY_TREE = CF_LOCAL + LOCAL + tree

# <<< CF_BRAND_BLOCK: jinja_contexts

# >>> CF_BRAND_BLOCK: jinja_horizon_interfaces
jinja_contexts = globals().get("jinja_contexts", {})

jinja_contexts["horizon_interfaces"] = {
    "horizon_interfaces": brand_cfg.get("horizon_interfaces", []),
}
# <<< CF_BRAND_BLOCK: jinja_horizon_interfaces


RUN_REMOTE_IMPORTS = os.environ.get("CF_RUN_REMOTE_IMPORTS", "0").strip().lower() in {
    "1",
    "true",
    "yes",
    "on",
}

if RUN_REMOTE_IMPORTS:

    urls_dict = get_files(
        {

    "accountmanagement": [
         #   EUMETSAT_ELASTICITY_TREE + "accountmanagement",
            LOCAL_SOURCE + "accountmanagement/Login-to-dashboard",
            LOCAL_SOURCE + "accountmanagement/Service-catalog",
            LOCAL_SOURCE + "accountmanagement/S3-keys",
            LOCAL_SOURCE + "accountmanagement/Regions",
            LOCAL_SOURCE + "accountmanagement/Cloud-projects-wallets",
            LOCAL_SOURCE + "accountmanagement/Notifications",
            LOCAL_SOURCE + "accountmanagement/My-profile",
            LOCAL_SOURCE + "accountmanagement/My-organization",
            LOCAL_SOURCE + "accountmanagement/Management-interfaces",
            LOCAL_SOURCE + "accountmanagement/Invitations",
            LOCAL_SOURCE + "accountmanagement/Users-and-roles",
            LOCAL_SOURCE + "accountmanagement/Help-Desk-And-Support",
            LOCAL_SOURCE + "accountmanagement/Active-services",
            LOCAL_SOURCE + "accountmanagement/Services",
            LOCAL_SOURCE + "accountmanagement/Registration-And-Account",
            LOCAL_SOURCE + "accountmanagement/Removing-User-From-Organization",
            LOCAL_SOURCE + "accountmanagement/Use-Horizon-to-create-application-credential-on-Eumetsat-Elasticity",
            LOCAL_SOURCE + "accountmanagement/How-to-activate-OpenStack-CLI-access-to-Eumetsat-Elasticity-cloud",
         ],

         "kubernetes": [
        #    EUMETSAT_ELASTICITY_TREE + "kubernetes",
            KUBERNETES + "Add-node-pools-to-Managed-Eumetsat-Elasticity-cluster-using-the-launcher-GUI",
            KUBERNETES + "How-to-create-a-Managed-Kubernetes-cluster-using-Eumetsat-Elasticity-launcher-GUI",
            KUBERNETES + "Managed-Kubernetes-backups-on-Eumetsat-Elasticity",
            KUBERNETES + "Managed-Kubernetes-Shared-Responsibility-Model-on-Eumetsat-Elasticity",
            KUBERNETES + "Obtain-managed-Kubernetes-API-token-on-Eumetsat-Elasticity",
            KUBERNETES + "Programmatic-Endpoints-for-Managed-Kubernetes-on-Eumetsat-Elasticity",
            KUBERNETES + "Upgrade-Managed-Kubernetes-on-Eumetsat-Elasticity",
            KUBERNETES + "Create-a-Managed-Kubernetes-Cluster-with-Terraform-on-Eumetsat-Elasticity",
            KUBERNETES + "Create-and-use-volume-snapshots-on-Eumetsat-Elasticity-Managed-Kubernetes",
            KUBERNETES + "Volume-cloning-on-Eumetsat-Elasticity-Managed-Kubernetes",

	    ],

      #  "cuttingedge": [
       #     EUMETSAT_ELASTICITY_TREE + "cuttingedge",
      #      CF3 + "cuttingedge/Install-TensorFlow-on-Docker-Running-on-Eumetsat-Elasticity-WAW3-1-vGPU-Virtual-Machine",
      #      CF3 + "cuttingedge/Sample-Deep-Learning-Workflow-Using-TensorFlow-Running-on-Docker-Installed-on-Eumetsat-Elasticity-WAW3-1-vGPU-Virtual-Machine",
      #      CF3 + "cuttingedge/Install-TensorFlow-on-WAW3-1-vGPU-enabled-VM-on-Eumetsat-Elasticity",
      #      CF3 + "cuttingedge/Sample-Deep-Learning-workflow-using-WAW3-1-vGPU-and-EO-DATA-on-Eumetsat-Elasticity",
      #      CF3 + "cuttingedge/Sample-SLURM-Cluster-on-Eumetsat-Elasticity-WAW3-1-Cloud-with-ElastiCluster",
      #      CF3 + "cuttingedge/Sample-Workflow-Running-EO-Processing-MPI-jobs-on-a-SLURM-cluster-on-Eumetsat-Elasticity-WAW3-1-Cloud",

      # ],


		"datavolume": [
		#    EUMETSAT_ELASTICITY_TREE + "datavolume",
			LOCAL_SOURCE + "datavolume/How-to-attach-a-volume-to-VM-less-than-2TB-on-Linux-on-Eumetsat-Elasticity",
			LOCAL_SOURCE + "datavolume/How-to-attach-a-volume-to-VM-more-than-2TB-on-Linux-on-Eumetsat-Elasticity",
			LOCAL_SOURCE + "datavolume/Ephemeral-vs-Persistent-storage-option-Create-New-Volume-on-Eumetsat-Elasticity",
			LOCAL_SOURCE + "datavolume/How-to-export-a-volume-over-NFS-on-Eumetsat-Elasticity",
			LOCAL_SOURCE + "datavolume/How-to-export-a-volume-over-NFS-outside-of-a-project-on-Eumetsat-Elasticity",
			LOCAL_SOURCE + "datavolume/How-to-extend-the-volume-in-Linux-on-Eumetsat-Elasticity",
			LOCAL_SOURCE + "datavolume/How-many-objects-can-I-put-into-Object-Storage-container-bucket-on-Eumetsat-Elasticity",
			LOCAL_SOURCE + "datavolume/How-to-mount-object-storage-in-Linux-on-Eumetsat-Elasticity",
			LOCAL_SOURCE + "datavolume/How-to-move-data-volume-between-two-VMs-using-OpenStack-Horizon-on-Eumetsat-Elasticity",
			LOCAL_SOURCE + "datavolume/Volume-snapshot-inheritance-and-its-consequences-on-Eumetsat-Elasticity",
			LOCAL_SOURCE + "datavolume/How-To-Create-Backup-Of-Your-Volume-From-Windows-Machine-on-Eumetsat-Elasticity",
			LOCAL_SOURCE + "datavolume/How-To-Attach-Volume-To-Windows-VM-On-Eumetsat-Elasticity",
            LOCAL_SOURCE + "datavolume/How-to-restore-volume-from-snapshot-on-Eumetsat-Elasticity",
            LOCAL_SOURCE + "datavolume/Bootable-versus-non-bootable-volumes-on-Eumetsat-Elasticity",
		],


        "cloud": [
        #    EUMETSAT_ELASTICITY_TREE + "cloud",
			CF3 + "cloud/How-to-access-the-VM-from-OpenStack-console-on-Eumetsat-Elasticity",
			CF3 + "cloud/How-to-clone-existing-and-configured-VMs-on-Eumetsat-Elasticity",
			CF3 + "cloud/How-to-fix-unresponsive-console-issue-on-Eumetsat-Elasticity",
			CF3 + "cloud/How-to-generate-ec2-credentials-on-Eumetsat-Elasticity",
 			CF3 + "cloud/How-to-generate-or-use-Application-Credentials-via-CLI-on-Eumetsat-Elasticity",
			CF3 + "cloud/How-to-use-GUI-in-Linux-VM-on-Eumetsat-Elasticity-and-access-it-from-local-Linux-computer",
			CF3 + "cloud/How-To-Create-a-New-Linux-VM-With-NVIDIA-Virtual-GPU-in-the-OpenStack-Dashboard-Horizon-on-Eumetsat-Elasticity",
			CF3 + "cloud/How-to-use-Docker-on-Eumetsat-Elasticity",
			CF3 + "cloud/How-to-use-Security-Groups-in-Horizon-on-Eumetsat-Elasticity",
			CF3 + "cloud/How-to-create-key-pair-in-OpenStack-Dashboard-on-Eumetsat-Elasticity",
			CF3 + "cloud/How-to-create-new-Linux-VM-in-OpenStack-Dashboard-Horizon-on-Eumetsat-Elasticity",
			CF3 + "cloud/How-to-install-Python-virtualenv-or-virtualenvwrapper-on-Eumetsat-Elasticity",

			CF3 + "cloud/How-to-start-a-VM-from-a-snapshot-on-Eumetsat-Elasticity",
			CF3 + "cloud/Status-Power-State-and-dependences-in-billing-of-instances-VMs-on-Eumetsat-Elasticity",
			CF3 + "cloud/How-to-upload-your-custom-image-using-OpenStack-CLI-on-Eumetsat-Elasticity",
			CF3 + "cloud/VM-created-with-option-Create-New-Volume-No-on-Eumetsat-Elasticity",
			CF3 + "cloud/VM-created-with-option-Create-New-Volume-Yes-on-Eumetsat-Elasticity",
			CF3 + "cloud/Dashboard-Overview-Project-Quotas-And-Flavors-Limits-on-Eumetsat-Elasticity",
			CF3 + "cloud/How-to-create-a-Linux-VM-and-access-it-from-Linux-command-line-on-Eumetsat-Elasticity",
			CF3 + "cloud/How-to-create-a-Linux-VM-and-access-it-from-Windows-desktop-on-Eumetsat-Elasticity",
			CF3 + "cloud/What-is-an-OpenStack-domain-on-Eumetsat-Elasticity",
			CF3 + "cloud/What-is-an-OpenStack-project-on-Eumetsat-Elasticity",
			CF3 + "cloud/What-Image-Formats-are-available-in-OpenStack-Eumetsat-Elasticity-Cloud",
			CF3 + "cloud/How-to-transfer-volumes-between-domains-and-projects-using-Horizon-dashboard-on-Eumetsat-Elasticity",
            CF3 + "cloud/How-to-create-instance-snapshot-using-Horizon-on-Eumetsat-Elasticity",
            CF3 + "cloud/How-to-start-a-VM-from-instance-snapshot-using-Horizon-dashboard-on-Eumetsat-Elasticity",
            CF3 + "cloud/Resizing-a-virtual-machine-using-OpenStack-Horizon-on-Eumetsat-Elasticity",
            CF3 + "cloud/How-to-create-a-VM-using-the-OpenStack-CLI-client-on-Eumetsat-Elasticity-cloud",
            CF3 + "cloud/Block-storage-and-object-storage-performance-limits-on-Eumetsat-Elasticity",
            CF3 + "cloud/How-to-create-a-VM-from-volume-snapshot-using-Horizon-dashboard-on-Eumetsat-Elasticity",

			LOCAL_SOURCE + "cloud/DNS-as-a-Service-on-Eumetsat-Elasticity-WAW3-1-Hosting",
            LOCAL_SOURCE + "cloud/Create-an-IPv6-network-on-Eumetsat-Elasticity",
            LOCAL_SOURCE + "cloud/Technical-background-for-IPv6-on-Eumetsat-Elasticity",
  	 ],

        "networking": [
        #    EUMETSAT_ELASTICITY_TREE + "networking",
			LOCAL_SOURCE + "networking/How-can-I-access-my-VMs-using-names-instead-of-IP-addresses-on-Eumetsat-Elasticity",
			LOCAL_SOURCE + "networking/How-to-Add-or-Remove-Floating-IPs-to-your-VM-on-Eumetsat-Elasticity",
			LOCAL_SOURCE + "networking/Cannot-access-VM-with-SSH-or-PING-on-Eumetsat-Elasticity",
			LOCAL_SOURCE + "networking/Cannot-ping-VM-on-Eumetsat-Elasticity",
			LOCAL_SOURCE + "networking/How-to-connect-to-your-virtual-machine-via-SSH-in-Linux-on-Eumetsat-Elasticity",
			LOCAL_SOURCE + "networking/How-to-create-a-network-with-router-in-Horizon-Dashboard-on-Eumetsat-Elasticity",
			LOCAL_SOURCE + "networking/How-can-I-open-new-ports-port-80-for-http-for-my-service-or-instance-on-Eumetsat-Elasticity",
			LOCAL_SOURCE + "networking/Generating-a-SSH-keypair-in-Linux-on-Eumetsat-Elasticity",
			LOCAL_SOURCE + "networking/How-to-add-SSH-key-from-Horizon-web-console-on-Eumetsat-Elasticity",
			LOCAL_SOURCE + "networking/How-is-my-VM-visible-in-the-internet-with-no-Floating-IP-attached-on-Eumetsat-Elasticity",
			LOCAL_SOURCE + "networking/How-to-run-and-configure-Firewall-as-a-service-and-VPN-as-a-service-on-Eumetsat-Elasticity",
			LOCAL_SOURCE + "windows/How-to-connect-to-a-virtual-machine-via-SSH-from-Windows-10-Command-Prompt-on-Eumetsat-Elasticity",
            LOCAL_SOURCE + "networking/How-to-Import-SSH-Public-Key-to-OpenStack-Horizon-on-Eumetsat-Elasticity",
            LOCAL_SOURCE + "networking/Load-Balancer-as-a-Service-User-Documentation-on-Eumetsat-Elasticity",
            LOCAL_SOURCE + "openstackcli/How-to-access-object-storage-using-OpenStack-CLI-on-Eumetsat-Elasticity",
            LOCAL_SOURCE + "networking/How-to-correctly-delete-all-the-resources-in-the-project-via-Horizon-Dashboard-on-Eumetsat-Elasticity",
            LOCAL_SOURCE + "networking/How-to-mount-object-storage-container-from-Eumetsat-Elasticity-as-file-system-on-local-Windows-computer",
			LOCAL_SOURCE + "networking/OpenStack-instance-migrationcommand-line-on-Eumetsat-Elasticity",
			LOCAL_SOURCE + "networking/What-If-I-Forgot-To-Add-The-SSH-Key-To-My-VM-Or-Deleted-It-Eumetsat-Elasticity",
			LOCAL_SOURCE + "networking/How-to-mount-object-storage-container-as-file-system-on-Windows-VM-on-Eumetsat-Elasticity",




			],


    "openstackdev": [
       #     EUMETSAT_ELASTICITY_TREE + "openstackdev",
			LOCAL_SOURCE + "openstackdev/Authenticating-to-OpenstackSDK-using-Keycloak-Credentials-on-Eumetsat-Elasticity",
			CF3          + "openstackdev/Generating-and-authorizing-Terraform-using-Keycloak-user-on-Eumetsat-Elasticity",
        ],

      "openstackcli": [
        #    EUMETSAT_ELASTICITY_TREE + "openstackcli",
			LOCAL_SOURCE + "openstackcli/How-to-backup-an-instance-and-download-it-to-the-desktop-on-Eumetsat-Elasticity",
			LOCAL_SOURCE + "openstackcli/How-to-create-a-set-of-VMs-using-OpenStack-Heat-Orchestration-on-Eumetsat-Elasticity",
			LOCAL_SOURCE + "openstackcli/How-To-Create-and-Configure-New-Project",
			LOCAL_SOURCE + "openstackcli/How-to-install-OpenStackClient-for-Linux-on-Eumetsat-Elasticity",
			LOCAL_SOURCE + "openstackcli/How-to-install-OpenStackClient-GitBash-or-Cygwin-for-Windows-on-Eumetsat-Elasticity",
			LOCAL_SOURCE + "openstackcli/How-to-install-OpenStackClient-on-Windows-using-Windows-Subsystem-for-Linux-on-Eumetsat-Elasticity-OpenStack-Hosting",
			LOCAL_SOURCE + "openstackcli/How-to-move-data-volume-between-two-VMs-using-OpenStack-CLI-on-Eumetsat-Elasticity",
            LOCAL_SOURCE + "openstackcli/How-to-transfer-volumes-between-domains-and-projects-using-OpenStack-CLI-client-on-Eumetsat-Elasticity",
            LOCAL_SOURCE + "openstackcli/How-to-start-a-VM-from-instance-snapshot-using-OpenStack-CLI-on-Eumetsat-Elasticity",
            LOCAL_SOURCE + "openstackcli/How-to-create-instance-snapshot-using-OpenStack-CLI-on-Eumetsat-Elasticity",
            LOCAL_SOURCE + "openstackcli/Resizing-a-virtual-machine-using-OpenStack-CLI-on-Eumetsat-Elasticity",
            LOCAL_SOURCE + "openstackcli/Use-backup-command-to-create-rotating-backups-of-virtual-machines-on-Eumetsat-Elasticity",
            LOCAL_SOURCE + "openstackcli/Use-script-to-create-daily-weekly-and-monthly-rotating-backups-of-virtual-machines-using-on-Eumetsat-Elasticity",

	 ],


       "s3": [
        #   EUMETSAT_ELASTICITY_TREE + "s3",
			LOCAL_SOURCE + "s3/Bucket-sharing-using-s3-bucket-policy-on-Eumetsat-Elasticity",
            LOCAL_SOURCE + "s3/Configuration-files-for-s3cmd-command-on-Eumetsat-Elasticity",
            LOCAL_SOURCE + "s3/Deep-dive-into-using-s3cmd-to-access-object-storage-on-Eumetsat-Elasticity",
            LOCAL_SOURCE + "s3/How-to-access-object-storage-from-Eumetsat-Elasticity-using-boto3",
            LOCAL_SOURCE + "s3/How-to-access-object-storage-from-Eumetsat-Elasticity-using-s3cmd",
			LOCAL_SOURCE + "s3/How-to-delete-large-S3-bucket-on-Eumetsat-Elasticity",
			LOCAL_SOURCE + "s3/How-To-Install-boto3-In-Windows-on-Eumetsat-Elasticity",
			LOCAL_SOURCE + "s3/How-to-install-s3cmd-on-Linux-on-Eumetsat-Elasticity",
			LOCAL_SOURCE + "s3/How-to-mount-object-storage-container-as-a-file-system-in-Linux-using-s3fs-on-Eumetsat-Elasticity",
			LOCAL_SOURCE + "s3/How-to-mount-object-storage-container-from-Eumetsat-Elasticity-as-file-system-on-local-Windows-computer",
			LOCAL_SOURCE + "s3/How-to-use-Object-Storage-on-Eumetsat-Elasticity-R1-and-R2-clouds",
			LOCAL_SOURCE + "s3/How-to-use-object-storage-with-Horizon-on-Eumetsat-Elasticity-FRA1-3-cloud",
            LOCAL_SOURCE + "s3/S3-bucket-object-versioning-on-Eumetsat-Elasticity",
            LOCAL_SOURCE + "s3/S3FS-Cache-on-Eumetsat-Elasticity",
			LOCAL_SOURCE + "s3/Server-Side-Encryption-with-Customer-Managed-Keys-SSE-C-on-Eumetsat-Elasticity",

        ],


         "shares": [
        #    EUMETSAT_ELASTICITY_TREE + "shares",
            LOCAL_SOURCE + "shares/How-to-allow-access-to-a-Share",
            LOCAL_SOURCE + "shares/How-to-create-a-Share-using-Horizon",
            LOCAL_SOURCE + "shares/How-to-mount-an-NFS-Share-on-a-Linux-VM",

           ],

    "windows": [
      #      EUMETSAT_ELASTICITY_TREE + "windows",
            LOCAL_SOURCE + "windows/Connecting-to-a-Windows-VM-via-RDP-through-a-Linux-bastion-host-port-forwarding-on-Eumetsat-Elasticity",
            LOCAL_SOURCE + "windows/How-to-connect-to-a-virtual-machine-via-SSH-from-Windows-10-Command-Prompt-on-Eumetsat-Elasticity",
            LOCAL_SOURCE + "windows/How-To-Create-SSH-Key-Pair-In-Windows-On-Eumetsat-Elasticity",
            LOCAL_SOURCE + "windows/How-To-Create-SSH-Key-Pair-In-Windows-11-On-Eumetsat-Elasticity",
            LOCAL_SOURCE + "windows/Can-I-change-my-password-through-RDP-on-Eumetsat-Elasticity",

            LOCAL_SOURCE + "windows/How-to-access-a-VM-from-Windows-PuTTY-on-Eumetsat-Elasticity",

    ],
  }
)

else:
    urls_dict = {}




# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "sphinx_rtd_theme"
# html_theme = 'alabaster'
html_static_path = ['_static','_static/include']
# Configure the sidebars
html_sidebars = {
    "**": ["sidebar.html"],  # Use your custom sidebar template for all pages
}

favicons = [
     {"href": "favicon/favicon-32x32.png"},
     {"href": "favicon/favicon-16x16.png"},
     {"href": "favicon/android-chrome-192x192.png"},
     {"href": "favicon/android-chrome-512x512.png"},
     {
         "rel": "apple-touch-icon",
         "href": "favicon/apple-touch-icon.png",
     },
 ]

html_logo = "logo_bar_vertical_dark_mode.png"
highlight_language = "none"

html_theme_options = {
    'logo_only': True,
    'display_version': False,
}

# >>> CF_BRAND_BLOCK: html_context_brand_values

# Removes "Built with Sphinx"
html_show_sphinx = False

html_context = {
    'array1': array1,
    'array2': array2,
    'array3': array3,
    'array4': array4,
    "display_github": True,
    "urls_dict": urls_dict,
    "github_host": "github.com",
    "github_user": "CloudFerro",
    "github_repo": LOCAL,
    "github_version": "main",
    "conf_py_path": "/source/",
    "source_suffix": ".rst",
    "current_year": str(date.today().year),
    "support_ticket_url": brand_cfg["brand_name_site_auth_link"]+'panel/profile/tickets',
    "main_site_url": brand_cfg["main_site_url"],
    "main_site_name": brand_cfg["main_site_name"],
    "horizon_interfaces": brand_cfg.get("horizon_interfaces", []),
    'display_version': False,
}

html_context.update(dedl_hda_mcp_context)

# <<< CF_BRAND_BLOCK: html_context_brand_values

html_css_files = [
    'css/custom.css', 'css/legal_style.css', 'css/s4defs-roles.css',
]

html_js_files = [
    "js/custom.js",
    #"js/feedback_widget.js",
]

# -- Language Switcher Configuration --------------------------------------

available_languages = [
    ("English", "en"),
    ("German", "de"),
    ("Polish", "pl"),
]

import os
language_code = os.environ.get('READTHEDOCS_LANGUAGE') or os.environ.get('SPHINX_LANGUAGE') or 'en'
current_language = next((lang for lang in available_languages if lang[1] == language_code), ("English", "en"))
html_context.update({
    'available_languages': available_languages,
    'current_language': current_language,
})

