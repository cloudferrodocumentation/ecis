Roles and permissions model
================================

Portal roles versus services roles
---------------------------------------

The portal uses two independent role sets: portal roles and service roles.

Portal roles control what a user can see and do in the portal UI (for example, billing views, or user management).

Service roles control what a user can do within a specific service (for example, permissions in S3).

These role domains are managed separately and serve different purposes: portal roles enable portal functionality, while service roles enforce service-level access and capabilities.

Portal roles
---------------------

The following portal roles are available and allow users to perform the actions described below.

**EUMETSAT Operator R1/R2**

   **Description**
      High-privilege role that allows managing users and access in the portal, including onboarding, role assignment, OS project provisioning, service quota management

   **Key permissions**
      Creating and editing organizations, adding, editing, and removing users, granting access to cloud regions and services, editing service quotas.

   **Assigned by**
      CF Customer Support

**EUMETSAT Operator ELA**

   **Description**
      High-privilege role that allows managing users and access in the portal, including onboarding, role assignment, OS project provisioning, service quota management

   **Key permissions**
      Creating and editing organizations, adding, editing, and removing users, granting access to cloud regions and services, editing service quotas.

   **Assigned by**
      CF Customer Support

**dolores-admin**

   **Description**
      Organization-level administrative role that can invite and remove users, request access to additional cloud regions, request changes to service quotas, and access billing information (if available).

   **Key permissions**
      Inviting new users to organization, removing users from organization, managing portal roles, requesting access to additional cloud regions, requesting changes to quotas, accessing organization and billing details (if available).

   **Assigned by**
      EUMETSAT Operator, EWC IAM Tenant Admin

**dolores-member+**

   **Description**
      Has restricted permissions within Organization

   **Key permissions**
      Access to all organization services except billing-related matters. Access to ticket module.

   **Assigned by**
      EUMETSAT Operator, EWC IAM Tenant Admin

**dolores-member**

   **Description**
      Read only role

   **Key permissions**
      User has read-only permission in Services within Organization/Workspace (all resources)

   **Assigned by**
      EUMETSAT Operator, EWC IAM Tenant Admin

Service roles
---------------

Service roles control what users can do within a specific service after they launch it from the portal. These roles are evaluated by the service itself and are independent from portal roles.

S3 roles
^^^^^^^^^^^^^^^^^

**s3object-admin**

   **Cloud region**
      R1, R2, ELA

   **Assignment level**
      Service

   **Description**
      Has full administrator permissions in S3 within Organization

   **Key permissions**
      Managing S3 keys. Managing S3 Service within Organization account. Full control over S3 resources.

   **Assigned by**
      EUMETSAT Operator, EWC IAM Tenant Admin

**s3object-memberplus**

   **Cloud region**
      R1, R2, ELA

   **Assignment level**
      Service

   **Description**
      Has restricted permissions in S3 within Organization

   **Key permissions**
      S3 keys. Object operations (upload, modify and delete objects). Can manage objects inside assigned buckets, but cannot change global configuration.

   **Assigned by**
      EUMETSAT Operator, EWC IAM Tenant Admin

**s3object-member**

   **Cloud region**
      R1, R2, ELA

   **Assignment level**
      Service

   **Description**
      Has read-only permissions in S3 within Organization

   **Key permissions**
      Managing S3 keys. Can only view and download data.

   **Assigned by**
      EUMETSAT Operator, EWC IAM Tenant Admin

Managed Kubernetes roles
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**mk8s-admin**

   **Cloud region**
      R1, R2, ELA

   **Assignment level**
      Service

   **Description**
      Has full administrator permissions in mk8s within Organization

   **Key permissions**
      User can CRUD MK8s clusters of this Tenant, along with CRUD of nodepools and cluster backups.

      User can access all organization clusters via kubeconfig files downloaded from MK8s panel.

   **Assigned by**
      EUMETSAT Operator, EWC IAM Tenant Admin

**mk8s-memberplus**

   **Cloud region**
      R1, R2, ELA

   **Assignment level**
      Service

   **Description**
      Has restricted permissions in mk8s within Organization

   **Key permissions**
      Access tenant's clusters via kubeconfig files downloaded from MK8s panel. User cannot CRUD clusters/nodepools/backups.

      Watchout: with kubeconfig user can also modify the backups directly from kubectl.

   **Assigned by**
      EUMETSAT Operator, EWC IAM Tenant Admin

**mk8s-member**

   **Cloud region**
      R1, R2, ELA

   **Assignment level**
      Service

   **Description**
      Has read-only permissions in mk8s within Organization

   **Key permissions**
      User can view the state of tenant's clusters via MK8s GUI (read-only).

   **Assigned by**
      EUMETSAT Operator, EWC IAM Tenant Admin

OpenStack roles
^^^^^^^^^^^^^^^^^^^

**openstack-domainadmin**

   **Cloud region**
      R1, R2, ELA

   **Assignment level**
      Service

   **Description**
      Has full administrator permissions in Openstack within Organization

   **Key permissions**
      OpenStack roles: domain_admin, member, manila_user (user can create shares), heat_stack_owner, load-balancer_member

   **Assigned by**
      EUMETSAT Operator, EWC IAM Tenant Admin

**openstack-memberplus**

   **Cloud region**
      R1, R2, ELA

   **Assignment level**
      Service

   **Description**
      Has restricted permissions in Openstack within Organization

   **Key permissions**
      OpenStack roles: member, manila_user, heat_stack_owner, load-balancer_member

   **Assigned by**
      EUMETSAT Operator, EWC IAM Tenant Admin

**openstack-reader**

   **Cloud region**
      R1, R2, ELA

   **Assignment level**
      Service

   **Description**
      Has read-only permissions in Openstack within Organization

   **Key permissions**
      OpenStack roles: reader -> We know that were issues in previous OpenStack services with this role. We’ll test it and provide a recommendation on whether it’s worth using.

   **Assigned by**
      EUMETSAT Operator, EWC IAM Tenant Admin