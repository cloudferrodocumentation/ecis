Managed Kubernetes Shared Responsibility Model on |brand-name|
==============================================================

Managed Kubernetes on |brand-name| enables users to deploy ready-to-use, production-grade Kubernetes clusters. A key benefit of |MK8s| is that |brand-name| manages the lifecycle of the Kubernetes platform, including cluster provisioning and ongoing maintenance of platform components.

At the same time, users remain responsible for the applications, data, access rules, and operational decisions inside their clusters. To keep the service reliable and secure, both |brand-name| and users must operate within a clear shared responsibility model.

This article explains that responsibility split and outlines the operational practices expected from users of |MK8s|.

.. raw:: html

   <h2>What We Are Going To Cover</h2>

.. contents::
   :depth: 2
   :local:
   :backlinks: none


Prerequisites
-------------

.. jinja:: brand_names

   **1. Hosting account on {{ brand_name }}**

   To use |MK8s|, you need:

   * a general {{ brand_name }} account {{ brand_name_site_auth_link }}
   * access to the |MK8s| dashboard at https://{{ mk8s_url }}

.. jinja:: brand_names

   **2. Supported {{ MK8s }} region**

The exact set of available regions depends on the brand and service deployment. Cluster operations, node pools, storage, backups, and regional endpoints must be used consistently within the selected region.

.. jinja:: mk8s_regions

   {% if has_regions %}

   Available |MK8s| regions for {{ brand_name }}:

   {% for region in regions %}

   * **{{ region.display_name }}**

   {% endfor %}

   {% endif %}


Service boundary
----------------

|brand-name| is responsible for the availability, maintenance, and security of the managed platform layer. This includes the underlying infrastructure, the managed Kubernetes control plane, node pool provisioning, and default platform add-ons delivered as part of |MK8s|.

Users are responsible for what they deploy and configure inside the cluster. This includes applications, workloads, namespaces, secrets, access rules, storage usage, and any custom configuration applied on top of the managed platform.


Adherence to Kubernetes best practices
--------------------------------------

|brand-name| follows Kubernetes best practices on the platform layer and maintains the managed components required to operate the service.

Users are responsible for applying Kubernetes best practices to their workloads. This includes, for example:

* defining appropriate CPU and memory requests and limits,
* using health checks where appropriate,
* configuring workloads for high availability,
* applying suitable network policies,
* managing RBAC permissions,
* protecting secrets and sensitive data,
* monitoring application health and logs.

The managed platform provides the foundation, but application correctness, workload design, and runtime behavior remain the user's responsibility.


Sufficient cluster specification
--------------------------------

|brand-name| provides a choice of control plane and node pool flavors. Users are responsible for selecting a specification that is sufficient for their workloads throughout the cluster lifecycle.

This includes choosing:

* the number of control plane nodes,
* the number and size of worker nodes,
* appropriate node pool flavors,
* autoscaling settings where available,
* storage classes and persistent volume sizes,
* resource requests and limits for workloads.

If the cluster is undersized, workloads may remain pending, become unstable, or compete for resources. If the cluster is oversized, unnecessary costs may be incurred. Users should review workload requirements before creating or scaling the cluster.


Security by design
------------------

|brand-name| protects the infrastructure and the Managed Kubernetes service. This includes the managed platform layer, default service configuration, and infrastructure-level security controls.

Users are responsible for securing their applications, data, and access configuration inside the cluster. This includes:

* securing application images and dependencies,
* managing Kubernetes RBAC permissions,
* protecting secrets,
* controlling access to namespaces and workloads,
* configuring network policies where needed,
* securing exposed services and ingress resources,
* validating third-party components before installation.

Users should follow the principle of least privilege and avoid granting broad administrative access unless it is required.


Controlled customization
------------------------

The |MK8s| platform supplies additional components and add-ons that simplify day-to-day cluster operation. These add-ons are provided with opinionated defaults so that the service can be maintained consistently.

Some user-side customizations of managed add-ons may be overwritten by |MK8s| during updates, reconciliation, or configuration changes. Users are responsible for the impact of custom changes they apply to managed components.

If you need a fully custom configuration for a component that is normally managed by |MK8s|, verify first whether that component can safely be customized. Otherwise, the managed service may restore its expected configuration.


Lifecycle management
--------------------

|brand-name| ensures the availability of new Kubernetes versions and performs upgrades or patches of components on the provisioning layer. For each release, |brand-name| may provide information about expected impact and recommended user actions.

Users are responsible for verifying that their workloads are compatible with the target Kubernetes version before initiating an upgrade. This includes checking:

* application manifests,
* container images,
* Helm charts,
* custom resource definitions,
* admission webhooks,
* operators,
* storage integrations,
* ingress and networking configuration.

Once compatibility is confirmed, users can initiate the upgrade through the |MK8s| interface.

.. jinja:: brand_names

   To upgrade an existing cluster, see :doc:`/kubernetes/Upgrade-Managed-Kubernetes`.


Cluster backups
---------------

Users are responsible for defining and maintaining a coherent backup policy that matches their operational and compliance requirements. Users are also responsible for validating that restore procedures work as expected.

For critical data, we strongly recommend using an additional, independent backup mechanism as a fallback.

As a convenience feature, |brand-name| provides a third-party Kubernetes plugin, Velero, to back up |MK8s| clusters. Velero can:

* back up cluster state, including persistent volumes,
* store backups in an S3-compatible location within the same cloud region as the protected cluster.

|brand-name| provides documentation for using this feature, but users remain responsible for backup configuration, restore validation, and deciding whether the backup policy is sufficient for their workloads.

|brand-name| is not responsible for Velero plugin malfunctions, restore failures caused by user-side misconfiguration, or data loss caused by incomplete backup policies.

.. jinja:: brand_names

   For details, see :doc:`/kubernetes/Managed-Kubernetes-backups`.


What to do next
---------------

Before running production workloads on |MK8s|, review:

* cluster sizing and quotas,
* region selection,
* workload resource requests and limits,
* application security,
* RBAC and access rules,
* backup and restore procedures,
* Kubernetes version compatibility.

.. jinja:: brand_names

   To create a cluster, see :doc:`/kubernetes/How-to-create-a-Managed-Kubernetes-cluster-using-ECIS-launcher-GUI`.

   To add worker nodes, see :doc:`/kubernetes/Add-node-pools-to-Managed-ECIS-cluster-using-the-launcher-GUI`.

   To obtain an API token for automation, see :doc:`/kubernetes/Obtain-managed-Kubernetes-API-token`.