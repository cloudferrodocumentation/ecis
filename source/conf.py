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
import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))

from get_rst_files import get_files
from datetime import date

# -- Project information -----------------------------------------------------

project = "Eumetsat"
from datetime import datetime
copyright = f"{datetime.now().year}, CloudFerro"
author = "CloudFerro"

# The full version, including alpha/beta/rc tags
release = "0.0.1"

# Define the canonical URL if you are using a custom domain on Read the Docs
html_baseurl = os.environ.get("READTHEDOCS_CANONICAL_URL", "")
# print("html_baseurl = " , html_baseurl)

# Tell Jinja2 templates the build is running on Read the Docs
if os.environ.get("READTHEDOCS", "") == "True":
    if "html_context" not in globals():
        html_context = {}
    html_context["READTHEDOCS"] = True


def setup(app):
   app.add_config_value('brand_name', '', True)
   app.add_config_value('cloud_name', '', True)
   app.add_config_value('second_cloud_name', '', True)
   app.add_config_value('brands_without_eodata', ['Eumetsat Elasticity', 'CloudFerro Cloud', 'Destination Earth', 'WEkEO'], True, [])
   app.add_config_value('two_fa_activated', ['Creodias', 'CloudFerro Cloud','EO-Lab', 'CODE-DE','NSIS Cloud'], True, [])
   app.add_config_value('special_eodata', ['EO-Lab', 'CODE-DE'], True, [])
   app.add_config_value('single_cloud', ['EO-Lab', 'CODE-DE', 'Eumetsat Elasticity', 'ESA HPC', 'NSIS Cloud'], True, [])
   app.add_config_value('multi_cloud', ['Creodias', 'CloudFerro Cloud','WEkEO', 'WEkEO Elasticity'],True, [])
   app.add_config_value('vgpu_compliant', ['EO-Lab', 'CODE-DE', 'Creodias', 'CloudFerro Cloud', 'WEkEO', 'WEkEO Elasticity', 'ESA HPC'], True, [])
   app.add_config_value('localstorage_present', ['Creodias', 'CloudFerro Cloud', 'WEkEO', 'WEkEO Elasticity', 'ESA HPC', 'NSIS Cloud'], True, [])
   app.add_config_value('windows_image_present', ['Creodias',  'WEkEO', 'WEkEO Elasticity', 'EO-Lab', 'CODE-DE','NSIS Cloud'], True, [])
   app.add_config_value('with_note', ['Creodias', 'CloudFerro Cloud'], True, [])
   app.add_config_value('dashboard_extension_existing', ['Creodias', 'CloudFerro Cloud', 'WEkEO Elasticity'],True, [])
   app.add_config_value('without_ppu', ['NSIS Cloud'],True, [])
   app.add_config_value('has_heat_templates', ['Creodias', 'CloudFerro Cloud','WEkEO', 'WEkEO Elasticity', 'ESA HPC', 'EO-Lab', 'CODE-DE', 'Destination Earth', 'Eumetsat Elasticity'],True, [])
   app.add_config_value('has_clusterapi_templates', ['Creodias', 'CloudFerro Cloud','WEkEO', 'WEkEO Elasticity','NSIS Cloud', 'Destination Earth'],True, [])
   app.add_config_value('has_dualstack_templates', ['Destination Earth'],True, [])
   app.add_config_value('has_vgpu_templates', ['ESA HPC'],True, [])

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones. 

extensions = ['sphinx_substitution_extensions',  'sphinx.ext.ifconfig',
'sphinx_jinja', 'sphinx_tabs.tabs','sphinx_favicon',
	"sphinx_design",
'sphinx_copybutton',

	]

copybutton_prompt_text = r"^\s*(\$ |>>> |\.\.\. )"
copybutton_prompt_is_regexp = True
copybutton_add_css = False

BRAND = os.environ.get("BRAND", "ecis")

BRANDS = {
    "ecis": {
        "brand_name": "Eumetsat Elasticity",
        "brand_name_full": "Eumetsat Elasticity",
        "brand_name_hyphen": "Eumetsat-Elasticity",
        "brand_name_site_link": "https://horizon.cloudferro.com/auth/login/?next=/",
        "brand_name_site_auth_link": "https://ecis.staging-dolores.apps.staging.intra.cloudferro.com/login",
        "images_root_accounts": "eumetsat",
        "images_root_billing": "eumetsat",
        "images_forgotten_password": "eumetsat",
        "images_registration": "eumetsat",
        "images_use_python_2fa": "eumetsat",
        "images_kubernetes_templates" : "eumetsat",
        "project_name": "cloud_078649_2",
        "region_name": "",
        'MK8s' : 'Eumetsat Elasticity Managed Kubernetes',
        "mk8s_url": "mks.cloud.eumetsat.int/",
        "server_cert": "managed-kubernetes-cloudferro-com-chain.pem",
        "main_site_url": "https://eumetsat.int",
        "main_site_name": "Eumetsat Elasticity",
    },
}

brand_cfg = BRANDS[BRAND]
IMAGES_ACCOUNTS = f"{brand_cfg["images_root_accounts"]}"
IMAGES_BILLING  = f"{brand_cfg["images_root_billing"]}_"
IMAGES_FORGOTTEN  = f"{brand_cfg['images_forgotten_password']}_"
IMAGES_KUBERNETES_TEMPLATES = f"{brand_cfg['images_kubernetes_templates']}"

rst_prolog = f"""
.. |brand-name| replace:: {brand_cfg["brand_name"]}
.. |brand-name-full| replace:: {brand_cfg["brand_name_full"]}
.. |brand-name-hyphen| replace:: {brand_cfg["brand_name_hyphen"]}
.. |brand-name-site-link| replace:: {brand_cfg["brand_name_site_link"]}
.. |brand-name-site-auth-link| replace:: {brand_cfg["brand_name_site_auth_link"]}

.. |cloud-name| replace:: {brand_cfg["region_name"]}
.. |brand-name-support-en| replace:: https://www.eumetsat.int/contact-us
.. |brand-name-support-de| replace:: https://www.eumetsat.int/contact-us
.. |datahub-address| replace:: datahub.code-de.org
.. |explorer| replace:: https://explore.creodias.eu
.. |finder| replace:: https://finder.creodias.eu/www/
.. |eodata-network| replace:: eodata\_
.. include:: <s5defs.txt>
.. |brand-name-security-groups| replace:: https://horizon.cloudferro.com/project/security_groups/
.. |JupyterLab| replace:: https://jupyterhub-creodias.apps.acronix.intra.cloudferro.com/
.. |MK8s| replace:: Eumetsat Elasticity Managed Kubernetes
"""

brand_name = brand_cfg["brand_name"]
cloud_name = ''


language = 'en'
locale_dirs = ['locale/']

# Images that change from brand to brand
jinja_contexts = {
    'image_names': {'register': 'register_eumetsat.png', 'create': 'create_account_eumetsat.png', 'registered': 'registration_successful_eumetsat.png'},

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

    'contracts_and_wallets': {
        'contracts_wallets': 'wallets_contracts_eumetsat.png',
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
        's3_login': 's3.waw3-1.cloudferro.com',
        'region': 'US',
    },
    'openstack_domain': {
        'openstack_domain': 'domain_eumetsat.png', 
    },
    'cloud_name': {
        'cloud_name': 'WAW3-1', 
    },
   'template_created': {
        'template_created': 'new_template2.png',
    },
    'eodata_endpoint': {
        'eodata_endpoint': 'data.cloudferro.com', 
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


    'brand_names': {
		'brand_name': brand_cfg["brand_name"],
        'noobaa01' : 'create_object_container.png',
        'noobaa02' : 'image2023-7-20_11-58-22.png',
		'brand_name_hyphen': brand_cfg["brand_name_hyphen"] ,
		'brand_name_site_link': brand_cfg["brand_name_site_link"],
		'brand_name_site_auth_link': brand_cfg["brand_name_site_auth_link"],
		'tenant_manager_link': brand_cfg["brand_name_site_auth_link"],

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
        'terminal_output' : 'terminal_output_creodias.png',
        'wget_output' : 'wget_output_creodias.png',
        'quick_look' : 'quick-look_creodias.png',
        'zipper_address' : 'zipper.creodias.eu',
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
		 },

     'tenant_manager_user_and_roles': {
            'tenant_manager_001' : 'Tenant_manager_01_eumetsat.png',
            'tenant_manager_002' : 'Tenant_manager_02_eumetsat.png',
            'tenant_manager_003' : 'Tenant_manager_03_eumetsat.png',
            'tenant_manager_004' : 'Tenant_manager_04_eumetsat.png',
            'tenant_manager_005' : 'Tenant_manager_05_eumetsat.png',
        },

      'dashboard_services': {
            'dashboard_services_1': 'verification-creodias-1.png',
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

      'cookie_consent': {
            'cookie_consent_1': 'cookie_consent-creodias-1.png',
            'cookie_consent_2': 'cookie_consent-creodias-2.png',
            'cookie_consent_3': 'cookie_consent-creodias-3.png',
            'cookie_consent_4': 'cookie_consent-creodias-4.png',
            'cookie_consent_5': 'cookie_consent-creodias-5.png',
            'cookie_consent_6': 'cookie_consent-creodias-6.png',
            'cookie_consent_7': 'cookie_consent-creodias-7.png',
            'cookie_consent_8': 'cookie_consent-creodias-8.png',
            'cookie_consent_9': 'cookie_consent-creodias-9.png',
            'cookie_consent_10': 'cookie_consent-creodias-10.png',
            'cookie_consent_11': 'cookie_consent-creodias-11.png',
            'cookie_consent_12': 'cookie_consent-creodias-12.png',

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
           'address': 'https://mk.apps.capi-01-staging.waw3-2.intra.cloudferro.com',
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
}

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = [
]


CF_SHARED = "https://github.com/CloudFerro/"
CF_LOCAL = "https://github.com/cloudferrodocumentation/"

blob = "/blob/main/source/"
tree = "/tree/main/source/"

LOCAL = "ecis"

CF3 = CF_SHARED + "cf3-doc" + blob
KUBERNETES = CF_SHARED + "kubernetes-doc" + blob

LOCAL_SOURCE = CF_LOCAL + LOCAL + blob
EUMETSAT_ELASTICITY_TREE = CF_LOCAL + LOCAL + tree

urls_dict = get_files(
  {

"""
    "accountmanagement": [
            EUMETSAT_ELASTICITY_TREE + "accountmanagement",
			CF3 + "accountmanagement/Using-KeePassXC-for-Two-Factor-Authentication-on-Eumetsat-Elasticity",
            CF3 + "accountmanagement/Registration-And-Account",
			CF3 + "accountmanagement/Accounts-and-Projects-Management",
            CF3 + "accountmanagement/Forgotten-Password",
            CF3 + "accountmanagement/Privacy-Policy",
            CF3 + "accountmanagement/Adding-Editing-Organizations",
            CF3 + "accountmanagement/Contracts-Wallets",
            CF3 + "accountmanagement/Editing-Profile",
            CF3 + "accountmanagement/Inviting-New-User",
            CF3 + "accountmanagement/Removing-User-From-Organization",
            CF3 + "accountmanagement/Services",
            CF3 + "accountmanagement/Users-Roles",
            CF3 + "accountmanagement/How-to-activate-OpenStack-CLI-access-to-Eumetsat-Elasticity-cloud",
	        CF3 + "accountmanagement/Tenant-Manager-Users-And-Roles-On-Eumetsat-Elasticity",
            LOCAL_SOURCE + "accountmanagement/Help-Desk-And-Support",
            LOCAL_SOURCE + "accountmanagement/Dual-Factor-Authentication-for-Eumetsat-Elasticity-Site",
            CF3 + "accountmanagement/Billing-reports-on-Eumetsat-Elasticity",


		],

         "kubernetes": [
            EUMETSAT_ELASTICITY_TREE + "kubernetes",
            KUBERNETES + "Accessing-OpenStack-resources-from-Eumetsat-Elasticity-Managed-Kubernetes-using-shared-networks",
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

        "cuttingedge": [
            EUMETSAT_ELASTICITY_TREE + "cuttingedge",
            CF3 + "cuttingedge/Install-TensorFlow-on-Docker-Running-on-Eumetsat-Elasticity-WAW3-1-vGPU-Virtual-Machine",
            CF3 + "cuttingedge/Sample-Deep-Learning-Workflow-Using-TensorFlow-Running-on-Docker-Installed-on-Eumetsat-Elasticity-WAW3-1-vGPU-Virtual-Machine",
            CF3 + "cuttingedge/Install-TensorFlow-on-WAW3-1-vGPU-enabled-VM-on-Eumetsat-Elasticity",
            CF3 + "cuttingedge/Sample-Deep-Learning-workflow-using-WAW3-1-vGPU-and-EO-DATA-on-Eumetsat-Elasticity",
            CF3 + "cuttingedge/Sample-SLURM-Cluster-on-Eumetsat-Elasticity-WAW3-1-Cloud-with-ElastiCluster",
            CF3 + "cuttingedge/Sample-Workflow-Running-EO-Processing-MPI-jobs-on-a-SLURM-cluster-on-Eumetsat-Elasticity-WAW3-1-Cloud",

       ],


		"datavolume": [
		    EUMETSAT_ELASTICITY_TREE + "datavolume",
			CF3 + "datavolume/How-to-attach-a-volume-to-VM-less-than-2TB-on-Linux-on-Eumetsat-Elasticity",
			CF3 + "datavolume/How-to-attach-a-volume-to-VM-more-than-2TB-on-Linux-on-Eumetsat-Elasticity",
			CF3 + "datavolume/Ephemeral-vs-Persistent-storage-option-Create-New-Volume-on-Eumetsat-Elasticity",
			CF3 + "datavolume/How-to-export-a-volume-over-NFS-on-Eumetsat-Elasticity",
			CF3 + "datavolume/How-to-export-a-volume-over-NFS-outside-of-a-project-on-Eumetsat-Elasticity",
			CF3 + "datavolume/How-to-extend-the-volume-in-Linux-on-Eumetsat-Elasticity",
			CF3 + "datavolume/How-many-objects-can-I-put-into-Object-Storage-container-bucket-on-Eumetsat-Elasticity",
			CF3 + "datavolume/How-to-mount-object-storage-in-Linux-on-Eumetsat-Elasticity",
			CF3 + "datavolume/How-to-move-data-volume-between-two-VMs-using-OpenStack-Horizon-on-Eumetsat-Elasticity",
            CF3 + "datavolume/How-to-create-volume-Snapshot-and-attach-as-Volume-on-Linux-or-Windows-on-Eumetsat-Elasticity",
			CF3 + "datavolume/Volume-snapshot-inheritance-and-its-consequences-on-Eumetsat-Elasticity",
			CF3 + "datavolume/How-To-Create-Backup-Of-Your-Volume-From-Windows-Machine-on-Eumetsat-Elasticity",
			CF3 + "datavolume/How-To-Attach-Volume-To-Windows-VM-On-Eumetsat-Elasticity",
            CF3 + "datavolume/How-to-create-or-delete-volume-snapshot-on-Eumetsat-Elasticity",
            CF3 + "datavolume/How-to-restore-volume-from-snapshot-on-Eumetsat-Elasticity",
            CF3 + "datavolume/Bootable-versus-non-bootable-volumes-on-Eumetsat-Elasticity",
		],

        "cloud": [
            EUMETSAT_ELASTICITY_TREE + "cloud",
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
			CF3 + "cloud/DNS-as-a-Service-on-Eumetsat-Elasticity-WAW3-1-Hosting",
			CF3 + "cloud/What-Image-Formats-are-available-in-OpenStack-Eumetsat-Elasticity-Cloud",
			CF3 + "cloud/How-to-transfer-volumes-between-domains-and-projects-using-Horizon-dashboard-on-Eumetsat-Elasticity",
            CF3 + "cloud/How-to-create-instance-snapshot-using-Horizon-on-Eumetsat-Elasticity",
            CF3 + "cloud/How-to-start-a-VM-from-instance-snapshot-using-Horizon-dashboard-on-Eumetsat-Elasticity",
            CF3 + "cloud/Resizing-a-virtual-machine-using-OpenStack-Horizon-on-Eumetsat-Elasticity",
            CF3 + "cloud/How-to-create-a-VM-using-the-OpenStack-CLI-client-on-Eumetsat-Elasticity-cloud",
            CF3 + "cloud/Block-storage-and-object-storage-performance-limits-on-Eumetsat-Elasticity",
            CF3 + "cloud/How-to-create-new-Linux-VM-in-OpenStack-Dashboard-Horizon-on-Eumetsat-Elasticity",


			 ],

        "networking": [
            EUMETSAT_ELASTICITY_TREE + "networking",
			CF3 + "networking/How-can-I-access-my-VMs-using-names-instead-of-IP-addresses-on-Eumetsat-Elasticity",
			CF3 + "networking/How-to-Add-or-Remove-Floating-IPs-to-your-VM-on-Eumetsat-Elasticity",
			CF3 + "networking/Cannot-access-VM-with-SSH-or-PING-on-Eumetsat-Elasticity",
			CF3 + "networking/Cannot-ping-VM-on-Eumetsat-Elasticity",
			CF3 + "networking/How-to-connect-to-your-virtual-machine-via-SSH-in-Linux-on-Eumetsat-Elasticity",
			CF3 + "networking/How-to-create-a-network-with-router-in-Horizon-Dashboard-on-Eumetsat-Elasticity",
			CF3 + "networking/How-can-I-open-new-ports-port-80-for-http-for-my-service-or-instance-on-Eumetsat-Elasticity",
			CF3 + "networking/Generating-a-SSH-keypair-in-Linux-on-Eumetsat-Elasticity",
			CF3 + "networking/How-to-add-SSH-key-from-Horizon-web-console-on-Eumetsat-Elasticity",
			CF3 + "networking/How-is-my-VM-visible-in-the-internet-with-no-Floating-IP-attached-on-Eumetsat-Elasticity",
			CF3 + "networking/How-to-run-and-configure-Firewall-as-a-service-and-VPN-as-a-service-on-Eumetsat-Elasticity",
			CF3 + "windows/How-to-connect-to-a-virtual-machine-via-SSH-from-Windows-10-Command-Prompt-on-Eumetsat-Elasticity",
            CF3 + "networking/How-to-Import-SSH-Public-Key-to-OpenStack-Horizon-on-Eumetsat-Elasticity",
            CF3 + "networking/Load-Balancer-as-a-Service-User-Documentation-on-Eumetsat-Elasticity",
            CF3 + "openstackcli/How-to-access-object-storage-using-OpenStack-CLI-on-Eumetsat-Elasticity",
            CF3 + "networking/How-to-correctly-delete-all-the-resources-in-the-project-via-Horizon-Dashboard-on-Eumetsat-Elasticity",
            CF3 + "networking/How-to-mount-object-storage-container-from-Eumetsat-Elasticity-as-file-system-on-local-Windows-computer",

			],


    "openstackdev": [
            EUMETSAT_ELASTICITY_TREE + "openstackdev",
			CF3 + "openstackdev/Authenticating-to-OpenstackSDK-using-Keycloak-Credentials-on-Eumetsat-Elasticity",
			CF3 + "openstackdev/Generating-and-authorizing-Terraform-using-Keycloak-user-on-Eumetsat-Elasticity",
        ],

      "openstackcli": [
            EUMETSAT_ELASTICITY_TREE + "openstackcli",
			CF3 + "openstackcli/How-to-backup-an-instance-and-download-it-to-the-desktop-on-Eumetsat-Elasticity",
			CF3 + "openstackcli/How-to-create-a-set-of-VMs-using-OpenStack-Heat-Orchestration-on-Eumetsat-Elasticity",
			CF3 + "openstackcli/How-To-Create-and-Configure-New-Project-on-Eumetsat-Elasticity-WAW3-1-Cloud",
			CF3 + "openstackcli/How-to-install-OpenStackClient-for-Linux-on-Eumetsat-Elasticity",
			CF3 + "openstackcli/How-to-install-OpenStackClient-GitBash-or-Cygwin-for-Windows-on-Eumetsat-Elasticity",
			CF3 + "openstackcli/How-to-share-private-container-from-object-storage-to-another-user-on-Eumetsat-Elasticity",
			CF3 + "openstackcli/How-to-install-OpenStackClient-on-Windows-using-Windows-Subsystem-for-Linux-on-Eumetsat-Elasticity-OpenStack-Hosting",
			CF3 + "openstackcli/How-to-move-data-volume-between-two-VMs-using-OpenStack-CLI-on-Eumetsat-Elasticity",
            CF3 + "openstackcli/How-to-transfer-volumes-between-domains-and-projects-using-OpenStack-CLI-client-on-Eumetsat-Elasticity",
            CF3 + "openstackcli/How-to-start-a-VM-from-instance-snapshot-using-OpenStack-CLI-on-Eumetsat-Elasticity",
            CF3 + "openstackcli/How-to-create-instance-snapshot-using-OpenStack-CLI-on-Eumetsat-Elasticity",
            CF3 + "openstackcli/Resizing-a-virtual-machine-using-OpenStack-CLI-on-Eumetsat-Elasticity",
            CF3 + "openstackcli/Use-backup-command-to-create-rotating-backups-of-virtual-machines-on-Eumetsat-Elasticity",
            CF3 + "openstackcli/Use-script-to-create-daily-weekly-and-monthly-rotating-backups-of-virtual-machines-using-on-Eumetsat-Elasticity",

	 ],


       "s3": [
           EUMETSAT_ELASTICITY_TREE + "s3",
			CF3 + "s3/How-to-delete-large-S3-bucket-on-Eumetsat-Elasticity",
			CF3 + "s3/How-to-mount-object-storage-container-as-a-file-system-in-Linux-using-s3fs-on-Eumetsat-Elasticity",
            CF3 + "s3/How-to-use-Object-Storage-on-Eumetsat-Elasticity",
			CF3 + "s3/How-to-access-private-object-storage-using-S3cmd-or-boto3-on-Eumetsat-Elasticity",
			CF3 + "s3/S3FS-Cache-on-Eumetsat-Elasticity",
			CF3 + "s3/Bucket-sharing-using-s3-bucket-policy-on-Eumetsat-Elasticity",
			CF3 + "s3/How-To-Install-boto3-In-Windows-on-Eumetsat-Elasticity",
			CF3 + "s3/Server-Side-Encryption-with-Customer-Managed-Keys-SSE-C-on-Eumetsat-Elasticity",
			CF3 + "s3/How-to-install-s3cmd-on-Linux-on-Eumetsat-Elasticity",
            CF3 + "s3/Configuration-files-for-s3cmd-command-on-Eumetsat-Elasticity",
            CF3 + "s3/How-to-access-object-storage-from-Eumetsat-Elasticity-using-boto3",
            CF3 + "s3/How-to-access-object-storage-from-Eumetsat-Elasticity-using-s3cmd",
            CF3 + "s3/S3-bucket-object-versioning-on-Eumetsat-Elasticity",
        ],


         "sfs": [
            EUMETSAT_ELASTICITY_TREE + "sfs",
            LOCAL_SOURCE + "sfs/How-To-Create-A-Local-Horizon-User",
            LOCAL_SOURCE + "sfs/How-To-Create-Manila-Network-And-Manila-User-Role",
            LOCAL_SOURCE + "sfs/How-To-Enable-Command-Line-Interface-For-Local-Horizon-User",
            LOCAL_SOURCE + "sfs/How-To-Install-Shared-File-System-Based-On-Manila-OpenStack",
            LOCAL_SOURCE + "sfs/How-To-Increase-Security-For-Shared-File-System-Based-On-Manila-OpenStack",

           ],


    "releasenotes": [
            EUMETSAT_ELASTICITY_TREE + "releasenotes",
			CF3 + "releasenotes/Kubernetes-Magnum-Release-Notes-on-Eumetsat-Elasticity",
			CF3 + "releasenotes/OpenStack-Release-Notes-on-Eumetsat-Elasticity",

        ],

    "windows": [
            EUMETSAT_ELASTICITY_TREE + "windows",
			CF3 + "windows/Connecting-to-a-Windows-VM-via-RDP-through-a-Linux-bastion-host-port-forwarding-on-Eumetsat-Elasticity",
			CF3 + "windows/How-to-access-a-VM-from-Windows-PuTTY-on-Eumetsat-Elasticity",
			CF3 + "windows/How-to-connect-to-a-virtual-machine-via-SSH-from-Windows-10-Command-Prompt-on-Eumetsat-Elasticity",
  			CF3 + "windows/How-To-Create-SSH-Key-Pair-In-Windows-On-Eumetsat-Elasticity",
            CF3 + "windows/How-To-Create-SSH-Key-Pair-In-Windows-11-On-Eumetsat-Elasticity",
  			CF3 + "windows/Can-I-change-my-password-through-RDP-on-Eumetsat-Elasticity",

        ],

    }
"""
)


html_context = {
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
}

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "sphinx_rtd_theme"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]
favicons = [
    {"href": "favicon/favicon-32x32.png"},  # => use `_static/favicon-32x32.png`
    {"href": "favicon/favicon-16x16.png"},
    {"href": "favicon/android-chrome-192x192.png"},
    {"href": "favicon/android-chrome-512x512.png"},
    {
        "rel": "favicon/apple-touch-icon.png",
        "href": "favicon/favicon-16x16.png",
    },
]
html_logo = "eumetsat_logo.png"
highlight_language = "none"
html_show_sphinx = False
html_theme_options = {
    'logo_only': True,

}


html_css_files = [
    'css/custom.css', 'css/legal_style.css', 'css/s4defs-roles.css'
,
    # MUST be last so it overrides everything
    "css/copybutton_custom.css",
]
html_js_files = [
    'js/custom.js', ("readthedocs.js", {"defer": "defer"}),
]
