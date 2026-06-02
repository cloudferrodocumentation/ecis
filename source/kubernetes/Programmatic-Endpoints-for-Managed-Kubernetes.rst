Programmatic Endpoints for |MK8s|
=================================

This article lists the region-specific endpoints for interacting with |MK8s| through the API, CLI, Swagger, and Terraform. All programmatic operations, including creating clusters and node pools, run in a specific cloud region. Choose the matching endpoint and use it consistently across all tools.

Regional endpoints
------------------

Choose your region first, then use the matching endpoint format for your tool.

.. jinja:: mk8s_regions

   {% if has_regions %}

   {% for region in regions %}

   {{ region.display_name }}
   ^^^^^^^^^^^^^^^^^^^^^^^

   * **API / CLI (full URL):** {{ region.mk8s_api_url }}
   * **API Docs (browser):** {{ region.mk8s_swagger_url }}
   * **Terraform provider endpoint (host:port):** {{ region.mk8s_terraform_endpoint }}

   {% endfor %}

   {% else %}

   No Managed Kubernetes programmatic endpoints are currently configured for {{ brand_name }}.

   {% endif %}

Endpoint formats
----------------

Use the format required by your tool:

* **API / CLI:** the full URL ending with ``/api/v1``, followed by the exact API path, for example ``/clusters``.
* **Swagger:** the URL ending with ``/swagger``. Open it in your browser.
* **Terraform:** the ``host:port`` endpoint ending with ``:443``.

Authentication tokens
---------------------

You need access to the selected region and a valid token for every tool that makes API calls:

* **API / CLI endpoint:** a token is required for requests. Without it, the API typically returns ``401 Unauthorized``.
* **Terraform provider endpoint:** a token is required because Terraform calls the same API.
* **Swagger:** a token is usually not required to open the documentation page, but it is required to execute protected requests with **Try it out**.

.. jinja:: brand_names

   To obtain a Managed Kubernetes API token, see :doc:`/kubernetes/Obtain-managed-Kubernetes-API-token`.

..
   To create a Managed Kubernetes cluster with Terraform, see :doc:`/kubernetes/Create-a-Managed-Kubernetes-Cluster-with-Terraform`.