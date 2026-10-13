Obtain |MK8s| API token
==========================================================

To interact with |MK8s| programmatically, you need an **API token**. It grants secure access to the |MK8s| API and is typically used with external tools such as:

* Terraform: https://registry.terraform.io/providers/CloudFerro/cloudferro/latest
* |MK8s| CLI: https://github.com/CloudFerro/cf-mkcli
* automation tools such as **curl**, CI/CD pipelines, and custom scripts

With an **API token** for |MK8s|, you can programmatically initiate cluster lifecycle operations such as creating node pools, scaling them, and reading cluster parameters.

.. raw:: html

   <h2>What We Are Going to Cover</h2>

.. contents::
   :depth: 2
   :local:
   :backlinks: none


Prerequisites
------------------------

.. jinja:: brand_names

   No. 1 **Hosting account**

   To use |MK8s|, you need:

   * a general {{ brand_name }} account {{ brand_name_site_auth_link }}
   * access to the |MK8s| dashboard at https://{{ mk8s_url }}

   No. 2 **Programmatic endpoints**

   Select the appropriate regional programmatic endpoint from:

   :doc:`/kubernetes/Programmatic-Endpoints-for-Managed-Kubernetes/Programmatic-Endpoints-for-Managed-Kubernetes`

Use the endpoint for the same cloud region in which your cluster is running.


Generate token from GUI
----------------------------------------

1) Show **Tokens** option on screen

To get to the tokens view in |MK8s|, find the **Tokens** button in the left sidebar:

If the browser window or device screen is narrow, first click the hamburger icon in the upper-left corner.

2) Go to **Tokens** view

Click **Tokens** to open the tokens view in |MK8s|. The list is empty if no tokens have been created yet.

3) Click **Create token**, then choose validity, permissions, and add optional information.

4) Create the token

Click **Create token** in that form.

.. jinja:: mk8s_images

   .. figure:: /kubernetes/{{ mk8s056 }}
      :alt: Generate token from GUI
      :class: image-with-border

As a result, the token is generated. Make sure to note it down and store it securely, because it will not be shown again.

The list of tokens will now contain an additional entry:

Click the eye icon in the **Roles** column to see the activated roles for the specific token:

.. jinja:: mk8s_images

   .. figure:: /kubernetes/{{ mk8s058 }}
      :alt: Generate token from GUI
      :class: image-with-border

This list reflects the options you selected while creating the token.

.. note::

   The image above shows API operations permitted by the token. Other operations may remain inaccessible if they were not selected while creating the token.

Problems with old tokens
----------------------------------------

Old API tokens may cause authentication or authorization errors when they are used with |MK8s| API tools.

This usually happens when a token was created for an older workflow, with insufficient permissions, for a different region, or before your current access rights were changed.

Typical symptoms include:

* **401 Unauthorized**
* **403 Forbidden**
* token or API key validation errors
* Terraform errors when reading or creating |MK8s| resources
* successful read-only API calls, but failed create, update, scale, or delete operations

An old token may still be visible in the **Tokens** view. However, the token can perform only the operations selected when it was created.

Check permissions of an existing token
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In the **Tokens** view, click the eye icon in the **Roles** column for the token you are using.

Check whether the token contains permissions required for your operation. For example, a token created only for reading cluster data may not be sufficient for creating clusters, creating node pools, scaling node pools, or deleting resources.

If the required permissions are missing, create a new token and select the required operations.

Test the token directly
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Before troubleshooting Terraform, CI/CD pipelines, or custom scripts, test the token directly with **curl**.

Use the API endpoint for the same region in which the cluster is running.

.. code-block:: bash

   export MK8S_API_URL=""
   export CLUSTER_ID=""
   export TOKEN=""

   curl -i -X GET "${MK8S_API_URL}/cluster/${CLUSTER_ID}" \
     -H "Authorization: Token ${TOKEN}" \
     -H "Content-Type: application/json"

If the token is valid and has sufficient permissions, the command returns cluster data.

If the response contains **401 Unauthorized** or **403 Forbidden**, create a new token and repeat the test.

Replace the old token
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

After creating a new token, replace the old token everywhere it is used.

Check especially:

* shell variables
* local scripts
* CI/CD secrets
* Terraform variables
* environment variables used by Terraform or other automation tools

If Terraform uses the token from an environment variable, set the new value before running Terraform again:

.. code-block:: bash

   export CLOUDFERRO_TOKEN=""

Then run:

.. code-block:: bash

   terraform plan

.. important::

   Treat the token as a password. Do not paste it into tickets, screenshots, documentation, Git commits, shell history, or public logs.

Recommended solution
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If you are not sure when a token was created, which permissions were selected, or where the token came from, create a new token.

This is usually faster and safer than troubleshooting an old token copied from an old script, Terraform variable, CI/CD secret, or previous test environment.



Access |MK8s| API using the token
----------------------------------------------------------

Work with API documentation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The detailed API documentation is available in Swagger. Use the Swagger URL for the same region in which your cluster is running.

.. jinja:: mk8s_regions

   {% if has_regions %}

   Available Swagger URLs for {{ brand_name }}:

   {% for region in regions %}

   * **{{ region.display_name }}:** {{ region.mk8s_swagger_url }}

   {% endfor %}

   {% else %}

   No Managed Kubernetes Swagger endpoint is currently configured for {{ brand_name }}.

   {% endif %}

Obtain cluster ID
^^^^^^^^^^^^^^^^^^^^^^^^^

API access allows you to interact with |MK8s| clusters and node pools. Most operations are performed in the context of a specific Kubernetes cluster, so you need the cluster ID before running cluster-specific API calls.

To obtain the cluster ID, click **Home**, select the region, and review the list of clusters. Select the cluster you want to work with. For example, let the cluster be called **networktest**. Clicking its name displays cluster data, including the **Cluster ID**.

Example: list cluster parameters
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Assume that you have:

* selected the correct programmatic endpoint from Prerequisite No. 2
* obtained the value of **CLUSTER_ID**
* generated the value of **TOKEN**

Replace the empty strings with your values of **CLUSTER_ID** and **TOKEN**. Then use the command for the region in which your cluster is running.

.. jinja:: mk8s_regions

   {% if has_regions %}

   .. tabs::

   {% for region in regions %}

      .. tab:: {{ region.display_name }}

         .. code-block:: bash

            export CLUSTER_ID=""
            export TOKEN=""

            curl -X GET "{{ region.mk8s_api_url }}/cluster/${CLUSTER_ID}" \
              -H "Authorization: Token ${TOKEN}" \
              -H "Content-Type: application/json"

   {% endfor %}

   {% else %}

   No Managed Kubernetes API endpoint is currently configured for {{ brand_name }}.

   {% endif %}

**Sample response**:

.. code-block:: json

   {
     "id": "ece35b5a-8ffe-4d07-9523-639323abbfbb",
     "created_at": "2026-02-12T11:09:05.046651Z",
     "updated_at": "2026-02-12T11:19:16.923479Z",
     "name": "tf-waw4",
     "status": "Running",
     "control_plane": {
       "custom": {
         "size": 1,
         "machine_spec": {
           "id": "b003e1cf-fd40-4ad1-827c-cc20c2ddd519",
           "created_at": "2025-02-05T11:14:35Z",
           "updated_at": "2025-11-06T14:00:03.702987Z",
           "name": "eo2a.large",
           "provider": "CloudFerro",
           "cpu": 2,
           "memory": "7632",
           "local_disk_size": "32",
           "is_active": true,
           "tags": [
             "control-plane",
             "worker"
           ],
           "gpu": "NONE"
         },
         "name": "eccentric-salmon"
       }
     },
     "errors": [],
     "version": {
       "id": "d70785b2-4b01-4f59-8103-2c37479fbee2",
       "created_at": "2025-08-11T07:15:57.771816Z",
       "updated_at": "2025-08-11T07:15:57.771816Z",
       "version": "1.32.6",
       "eol": "2025-12-27T23:00:00Z",
       "info": "",
       "is_active": true
     },
     "metadata": {
       "openstack_project_id": "e04f93656a5748d3b3b493dd4dfec0ea"
     }
   }

Best practices and additional precautions
------------------------------------------------

Use one token per workflow
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Avoid using the same token for all tools and scripts. Create separate tokens for separate workflows, so, have one token for Terraform, another for CI/CD automation, yet another one for local testing with **curl**, then another one for temporary troubleshooting and so on.

In this way, you can disable one token without breaking other workflows.

Use the minimum required permissions
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Do not select more permissions than the workflow requires. If a script only reads cluster data, do not create a token with permissions for creating, scaling, or deleting resources. In this way, the impact of accidental token exposure will be smaller.

Check the region first
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Always use the |MK8s| API endpoint for the same region in which the cluster is running.

First check that the cluster exists in the selected region, that **CLUSTER_ID** belongs to that region, that the Swagger URL and API URL are from the same region and that the endpoint matches the region used by Terraform, scripts, or automation tools.

Check the authorization header
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

When using **curl** or custom scripts, verify that the authorization header has the correct format:

.. code-block:: bash

   -H "Authorization: Token ${TOKEN}"

Common mistakes include:

* using **Bearer** instead of **Token**
* adding extra quotes around the token value
* copying the token with a trailing space or newline
* using an empty environment variable
* using an old shell session where **TOKEN** still has the previous value

To check whether the variable is empty, run:

.. code-block:: bash

   test -n "${TOKEN}" && echo "TOKEN is set" || echo "TOKEN is empty"

Do not print the token value itself.

Avoid storing tokens in shell history
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Do not paste real token values directly into commands that are saved in shell history.

Instead of this:

.. code-block:: bash

   export TOKEN="real-token-value"

use:

.. code-block:: bash

   read -s TOKEN
   export TOKEN

Then paste the token when prompted.

Rotate tokens regularly
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Replace long-lived tokens periodically, especially when they are used in automation tools.

**IMMEDIATELY** rotate a token if it was pasted into a ticket, chat, or email; appeared in a screenshot; was committed to Git; was printed in CI/CD logs or the person or system using it no longer needs access.

Check CI/CD logs
^^^^^^^^^^^^^^^^^^^^^^^^^

When troubleshooting automation, check whether the token is accidentally printed in logs. If it does apper there, remove it from the logs if possible, revoke the token, and create a new one.

Check for proxy or firewall issues
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Authentication errors are not always caused by the token itself. The same command may work from one machine but not on another -- check whether the request passes through a proxy, firewall, VPN, or corporate network filter.

In particular, check whether the **Authorization** header is preserved and whether HTTPS traffic to the regional |MK8s| endpoint is allowed.

Separate authentication from authorization
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

A token problem can be either an authentication problem or an authorization problem.

401 Unauthorized
   Usually means that the token is missing, invalid, expired, copied incorrectly, or sent with the wrong header.

403 Forbidden
   Usually means that the token was accepted, but it does not have permission to perform the requested operation. Then first check the token permissions; if it looks correctly, check whether your account, project, or organization role allows the operation.

Test with a simple read operation first
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Start troubleshooting with a simple read-only API request, such as listing or reading cluster data. If the read-only request fails, fix authentication, endpoint, token, or account access first. If creation is possible, but create, update, scale, or delete operations fail, the problem is more likely related to token permissions or user roles.

Remove unused tokens
^^^^^^^^^^^^^^^^^^^^^^^^^^

Delete tokens that are no longer used: temporary test tokens, tokens for Terraform experiments, tokens for retired CI/CD jobs, tokens copied into local scripts, tokens created by users who no longer manage the workflow and so on.

Keeping only active tokens makes troubleshooting easier and reduces security risk.

What To Do Next
--------------------

With your API token, you can securely interact with |MK8s| from the command line or automation tools. Use it to connect CI/CD pipelines, manage workloads, or monitor resources programmatically.

.. jinja:: mk8s_regions

   {% if has_regions %}

   To explore available API operations, open the Swagger documentation for your region:

   {% for region in regions %}

   * **{{ region.display_name }}:** {{ region.mk8s_swagger_url }}

   {% endfor %}

   {% endif %}


.. jinja:: brand_names

   You can use the token obtained in this article to use Terraform: :doc:`/kubernetes/Create-a-Managed-Kubernetes-Cluster-with-Terraform/Create-a-Managed-Kubernetes-Cluster-with-Terraform`
