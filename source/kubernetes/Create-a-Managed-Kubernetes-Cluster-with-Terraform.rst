Create a Managed Kubernetes Cluster with Terraform on |brand-name|
==================================================================

You can provision and manage |MK8s| clusters declaratively using Terraform with **.tf** configuration files. This approach enables consistent, repeatable cluster deployments aligned with Infrastructure as Code.

.. raw:: html

   <h2>What we are going to cover</h2>

.. contents::
   :local:
   :depth: 2
   :backlinks: none


Prerequisites
-------------

.. jinja:: brand_names

   **1. Hosting account**

   You need:

   * your `{{ brand_name }} account <{{ brand_name_site_auth_link }}>`_
   * access to the |MK8s| dashboard at https://{{ mk8s_url }}

**2. Parameters for creating a new Managed Kubernetes cluster**

You should know which cluster name, Kubernetes version, control plane flavor, and control plane size you want to use.

.. jinja:: brand_names

   The same parameters are described in the GUI-based cluster creation article: :doc:`/kubernetes/How-to-create-a-Managed-Kubernetes-cluster-using-ECIS-launcher-GUI`.

**3. Regional endpoints**

.. jinja:: brand_names

   Select the appropriate regional Terraform endpoint from :doc:`/kubernetes/Programmatic-Endpoints-for-Managed-Kubernetes`.

Use the endpoint for the same region where you want to create the cluster.

.. jinja:: mk8s_regions

   {% if has_regions %}

   Available |MK8s| regions for {{ brand_name }}:

   {% for region in regions %}

   * **{{ region.display_name }}** -- ``{{ region.mk8s_terraform_endpoint }}``

   {% endfor %}

   {% endif %}

**4. Managed Kubernetes API token**

Terraform needs a **Managed Kubernetes API token**.

.. jinja:: brand_names

   Generate it as described in :doc:`/kubernetes/Obtain-managed-Kubernetes-API-token` and store it securely.

The token must be valid for the same region as the Terraform endpoint and must include permissions for the operations you want Terraform to perform.

.. note::

   For cluster creation, the API token must include at least the roles needed to list regions, list versions, list machine specs, and create clusters.

   If you also create worker nodes with Terraform, include the node pool roles required for creating, listing, updating, and deleting node pools.

**5. Terraform installed**

Install Terraform from the official documentation: `Terraform <https://developer.hashicorp.com/terraform>`_.

Terraform also requires the CloudFerro provider, available from the Terraform Registry:

https://registry.terraform.io/providers/CloudFerro/cloudferro/latest

Here is what it looks like:

.. jinja:: mk8s_images

   .. figure:: {{ mk8s084 }}
      :align: center
      :class: image-with-border

      CloudFerro provider for Terraform.

In the red rectangle, you can see the latest provider version. Use that version in your Terraform code unless the documentation for your environment specifies another one.

Because the provider is available from the official Terraform Registry, the Terraform configuration only needs the provider source and version:

.. code-block:: hcl

   terraform {
     required_providers {
       cloudferro = {
         source = "cloudferro/cloudferro"
         # At the time of writing, the following version was used successfully:
         version = "0.1.3"
       }
     }
   }

.. note::

   If you change the provider version in an existing Terraform directory, run:

   .. code-block:: bash

      terraform init -upgrade

   This updates **.terraform.lock.hcl** to match the provider version configured in your **.tf** files.


Create a cluster using a single Terraform file
----------------------------------------------

Create a working directory:

.. code-block:: bash

   mkdir mk8s-tf
   cd mk8s-tf

Create a single file named **sample.tf**.

Use the tab that matches the region where you want to create the cluster:

.. jinja:: mk8s_regions

   {% if has_regions %}

   .. tabs::

   {% for region in regions %}

      .. tab:: {{ region.display_name }}

         .. code-block:: hcl

            terraform {
              required_providers {
                cloudferro = {
                  source = "cloudferro/cloudferro"
                  # At the time of writing, the following version was used successfully:
                  version = "0.1.3"
                }
              }
            }

            variable "api_token" {
              description = "{{ region.display_name }} Managed Kubernetes API token"
              type = string
              sensitive = true
            }

            provider "cloudferro" {
              host = "{{ region.mk8s_terraform_endpoint }}"
              token = var.api_token
            }

            resource "cloudferro_kubernetes_cluster_v1" "cluster" {
              name = "tf-created-{{ region.slug }}"
              version = "1.32.6"

              control_plane = {
                # Replace with a control plane flavor available in the selected region.
                # Example for R1: "16cpu-128gbmem"
                flavor = "CONTROL_PLANE_FLAVOR_AVAILABLE_IN_SELECTED_REGION"
                size = 1
              }
            }

   {% endfor %}

   {% else %}

   No Managed Kubernetes Terraform endpoint is currently configured for {{ brand_name }}.

   {% endif %}


Store the token as an environment variable
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Set the API token as an environment variable:

.. code-block:: bash

   export TF_VAR_api_token="paste-your-managed-kubernetes-token-here"

Terraform automatically uses this value for the variable:

.. code-block:: hcl

   token = var.api_token

To verify that the variable is set in your current shell, run:

.. code-block:: bash

   echo "Token length: ${#TF_VAR_api_token}"

The result should be greater than **0**.

.. warning::

   Use normal straight quotes when exporting the token. Do not paste typographic quotes such as ``“`` or ``”`` into the shell.

   If the shell changes to the continuation prompt ``>``, press **Ctrl+C** and re-enter the command with straight quotes.


Define the control plane flavor
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The control plane flavor is defined in this part of **sample.tf**:

.. code-block:: hcl

   control_plane = {
     flavor = "CONTROL_PLANE_FLAVOR_AVAILABLE_IN_SELECTED_REGION"
     size = 1
   }

Replace **CONTROL_PLANE_FLAVOR_AVAILABLE_IN_SELECTED_REGION** with one of the control plane flavors available in the selected region.

Open the |MK8s| dashboard, select the same region as the Terraform endpoint, start the cluster creation flow, and check the available values in the **Control plane** section.

.. note::

   The flavor name is region-specific. For example, one region may use a CloudFerro-style flavor such as **eo2a.large**, while R1 may use a name such as **16cpu-128gbmem**.

   If Terraform returns **control plane flavor not found**, the selected flavor is not available in the region used by the Terraform endpoint.


Initialize and create the cluster
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Initialize the Terraform working directory:

.. code-block:: bash

   terraform init

If you changed the provider version after a previous initialization, use:

.. code-block:: bash

   terraform init -upgrade

Create the cluster:

.. code-block:: bash

   terraform apply

When prompted, type **yes** and press **Enter**.

.. jinja:: mk8s_images

   .. figure:: {{ mk8s018 }}
      :align: center
      :class: image-with-border

You can also see the cluster in the browser while its status is **Creating**:

.. jinja:: mk8s_images

   .. figure:: {{ mk8s019 }}
      :align: center
      :class: image-with-border

      Creation of cluster started via Terraform but also visible in the GUI

.. warning::

   Cluster creation may take dozens of minutes. Do not interrupt **terraform apply** while the cluster is being created.

   If the command is interrupted after the API has already created the cluster, Terraform may mark the resource as tainted. On the next run, Terraform may try to destroy and recreate it.

   If this happens, first check the cluster status in the |MK8s| dashboard. If the cluster is healthy, recover the Terraform state with:

   .. code-block:: bash

      terraform untaint cloudferro_kubernetes_cluster_v1.cluster
      terraform refresh
      terraform plan

   The expected result is:

   .. code-block:: text

      No changes. Your infrastructure matches the configuration.

.. note::

   If the cluster cannot be deleted from the GUI and **terraform destroy** returns **cluster is busy**, contact Support or the cloud operator. Provide the cluster name, cluster ID, region, router IP, and OpenStack project ID.

   After the operator removes the stuck cluster, remove it from local Terraform state before retrying:

   .. code-block:: bash

      terraform state rm cloudferro_kubernetes_cluster_v1.cluster


Verify in the |MK8s| dashboard
------------------------------

1. Open the |MK8s| dashboard.
2. Select the region in which you created the cluster.
3. Confirm that the Terraform-created cluster appears and reaches the **Running** state.

.. jinja:: mk8s_images

   .. figure:: {{ mk8s020 }}
      :align: center
      :class: image-with-border


Export kubeconfig
-----------------

If you want Terraform to print the generated kubeconfig, add the following output block to **sample.tf**:

.. code-block:: hcl

   output "kubeconfig" {
     value = cloudferro_kubernetes_cluster_v1.cluster.kubeconfig
     sensitive = true
   }

Apply the configuration again:

.. code-block:: bash

   terraform apply

Then write the kubeconfig to a file:

.. code-block:: bash

   terraform output -raw kubeconfig > tf-created_config.yaml
   chmod 600 tf-created_config.yaml
   export KUBECONFIG="$PWD/tf-created_config.yaml"

Verify access:

.. code-block:: bash

   kubectl get nodes -o wide


Add worker nodes
----------------

You can add worker nodes by creating another **.tf** file in the same directory.

Save the following file as **add_workers.tf**:

.. code-block:: hcl

   resource "cloudferro_kubernetes_node_pool_v1" "workers" {
     name = "workers"
     cluster_id = cloudferro_kubernetes_cluster_v1.cluster.id

     flavor = "WORKER_NODE_FLAVOR_AVAILABLE_IN_SELECTED_REGION"
     shared_networks = []

     labels = []
     taints = []

     autoscale = false
     size = 3
   }

Replace **WORKER_NODE_FLAVOR_AVAILABLE_IN_SELECTED_REGION** with a worker node flavor available in the same region as the cluster.

Terraform executes all **.tf** files in the working directory as one configuration. In this case, it uses the cluster resource defined in **sample.tf** and creates the node pool defined in **add_workers.tf**.

Run:

.. code-block:: bash

   terraform apply

When prompted, type **yes** and press **Enter**.

The process of adding worker nodes starts:

.. jinja:: mk8s_images

   .. figure:: {{ mk8s021 }}
      :align: center
      :class: image-with-border


Destroy the cluster
-------------------

To remove the test cluster and node pool, run:

.. code-block:: bash

   terraform destroy

When prompted, type **yes** and press **Enter**.

.. warning::

   This command removes resources managed by the Terraform configuration in the current directory. Make sure you run it from the correct directory and against the correct |MK8s| region.


What to do next
---------------

After creating the cluster, you can:

* export kubeconfig and connect with **kubectl**,
* add more node pools,
* store **sample.tf** and **add_workers.tf** in Git for repeatable cluster creation.

.. jinja:: brand_names

   You can also create Kubernetes clusters using the GUI. See:

   * :doc:`/kubernetes/How-to-create-a-Managed-Kubernetes-cluster-using-ECIS-launcher-GUI`
   * :doc:`/kubernetes/Add-node-pools-to-Managed-ECIS-cluster-using-the-launcher-GUI`

   If you already have a cluster, you can back it up with :doc:`/kubernetes/Managed-Kubernetes-backups`.