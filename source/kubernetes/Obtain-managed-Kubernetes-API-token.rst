Obtain |MK8s| API token
=======================

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
-------------

.. jinja:: brand_names

   No. 1 **Hosting account on {{ brand_name }}**

   To use |MK8s|, you need:

   * a general {{ brand_name }} account {{ brand_name_site_auth_link }}
   * access to the |MK8s| dashboard at https://{{ mk8s_url }}

   No. 2 **Programmatic endpoints on {{ brand_name }}**

   Select the appropriate regional programmatic endpoint from:

   :doc:`/kubernetes/Programmatic-Endpoints-for-Managed-Kubernetes`

Use the endpoint for the same cloud region in which your cluster is running.


Generate token from GUI
-----------------------

1) Show **Tokens** option on screen

To get to the tokens view in |MK8s|, find the **Tokens** button in the left sidebar:

.. jinja:: mk8s_images

   .. figure:: {{ mk8s053 }}
      :class: image-with-border

If the browser window or device screen is narrow, first click the hamburger icon in the upper-left corner.

2) Go to **Tokens** view

Click **Tokens** to open the tokens view in |MK8s|. The following screenshot shows the situation in which no tokens have been created yet:

.. jinja:: mk8s_images

   .. figure:: {{ mk8s054 }}
      :class: image-with-border

3) Click **Create token**, then choose validity, permissions, and add optional information.

.. jinja:: mk8s_images

   .. figure:: {{ mk8s055 }}
      :class: image-with-border

4) Create the token

Click **Create token** in that form.

.. jinja:: mk8s_images

   .. figure:: {{ mk8s056 }}
      :class: image-with-border

As a result, the token is generated. Make sure to note it down and store it securely, because it will not be shown again.

The list of tokens will now contain an additional entry:

.. jinja:: mk8s_images

   .. figure:: {{ mk8s057 }}
      :class: image-with-border

Click the eye icon in the **Roles** column to see the activated roles for the specific token:

.. jinja:: mk8s_images

   .. figure:: {{ mk8s058 }}
      :class: image-with-border

This list reflects the options you selected while creating the token.

.. note::

   The image above shows API operations permitted by the token. Other operations may remain inaccessible if they were not selected while creating the token.


Access |MK8s| API using the token
---------------------------------

Work with API documentation
^^^^^^^^^^^^^^^^^^^^^^^^^^^

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

.. jinja:: mk8s_images

   .. figure:: {{ mk8s059 }}
      :class: image-with-border


Obtain cluster ID
^^^^^^^^^^^^^^^^^

API access allows you to interact with |MK8s| clusters and node pools. Most operations are performed in the context of a specific Kubernetes cluster, so you need the cluster ID before running cluster-specific API calls.

To obtain the cluster ID, click **Home**, select the region, and review the list of clusters. Select the cluster you want to work with. For example, let the cluster be called **networktest**. Clicking its name displays cluster data, including the **Cluster ID**.

.. jinja:: mk8s_images

   .. figure:: {{ mk8s060 }}
      :class: image-with-border


Example: list cluster parameters
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

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


What To Do Next
---------------

With your API token, you can securely interact with |MK8s| from the command line or automation tools. Use it to connect CI/CD pipelines, manage workloads, or monitor resources programmatically.

.. jinja:: mk8s_regions

   {% if has_regions %}

   To explore available API operations, open the Swagger documentation for your region:

   {% for region in regions %}

   * **{{ region.display_name }}:** {{ region.mk8s_swagger_url }}

   {% endfor %}

   {% endif %}

..
   .. jinja:: brand_names

      You can use the token obtained in this article to use Terraform: :doc:`/kubernetes/Create-a-Managed-Kubernetes-Cluster-with-Terraform`