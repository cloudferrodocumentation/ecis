Management interfaces
=====================

This article explains how to open the management interfaces available from the portal.

The exact set of interfaces shown in your portal depends on the services and regions enabled for your account, so the options visible to you may differ from those shown in this article.

Prerequisites
-------------

Before you begin, make sure that:

.. jinja:: brand_names

   No. 1 **Account on {{ brand_name }} Dashboard**

You need an active user account and access to the |brand-name| Dashboard at |brand-name-site-auth-link|.

No. 2 **The required services are enabled for your account**

The management interfaces available in the portal depend on the services assigned to your account. Use option **Service Catalog** to see which services are active:

.. figure:: services-enabled-in-the-account.png
   :class: image-with-border

No. 3 **You have access to at least one region**

Some interfaces are region-specific, so the list of available regions may differ from one account to another. Use option **Regions** to see which regions are active:

.. figure:: regions-active-in-your-account.png
   :class: image-with-border

No. 4 **You have the necessary role to open the selected interface**

Some actions, such as obtaining **Keystone credentials**, may require administrator-level access in the portal. See article :doc:`/accountmanagement/Users-and-roles/Users-and-roles`.

No. 5 **Managed Kubernetes and OpenStack**

There are several management interfaces that you can open from the portal.

.. figure:: management-interfaces-options-ecis-portal.png
   :class: image-with-border

**Managed Kubernetes** is a Kubernetes service that runs separately from **OpenStack**. The other interfaces -- **R1**, **R2** and **FRA1-3** -- are **OpenStack** based, each within its own region.

For further details, see the :doc:`Managed Kubernetes section </kubernetes/kubernetes>` as well as :doc:`Cloud Services </cloud/cloud>`.

Managed Kubernetes
------------------

For this interface, click on **Managed Kubernetes** and then select one of the regions available to your account.

.. figure:: managed-kubernetes-interface-ecis-portal.png
   :class: image-with-border

For example, you can select **FRA1-3**:

.. figure:: choose-fra1-3-ecis-portal.png
   :class: image-with-border

After that, the interface opens and displays the list of existing clusters in that region:

.. figure:: managed-kubernetes-clusters-ecis-portal.png
   :class: image-with-border

Clouds **R1** and **R2** are opened through the portal and use the EUMETSAT-branded login page.

Cloud **FRA1-3** may serve as an extension to R1 and/or R2 but is also a public CloudFerro cloud. Its Horizon interface is opened through the shared CloudFerro Horizon service at **horizon.cloudferro.com**, where you must first select youridentity provider and then choose the **FRA1-3** region.

R1 Cloud Panel
--------------

Clicking this option opens the following form:

.. figure:: eumetsat-login-ecis-r1.png
   :class: image-with-border

You are the admin of the account
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If you are an administrator of your account in the portal, click on button **Sign In** and proceed to the Horizon interface.

You are the user of the account
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If you are a user of the account (meaning the admin of that account has previously assigned you a **member** role) click **Keystone credentials** and select **Keystone Credential** from the drop-down list:

.. figure:: eumetsat-ecis-become-user.png
   :class: image-with-border

The form then changes as follows:

.. figure:: eumetsat-ecis-enter-user-data.png
   :class: image-with-border

Enter the **User Name** and **Password** that were allocated to you in order to continue to the **Horizon** interface for **R1** region. Then use EWC IAM identity provider to sign in

.. figure:: step-1-for-clouds-r1-and-r2.png
   :class: image-with-border

The next step is to enter the Horizon interface:

.. figure:: next-step-end-up-in-r1.png
   :class: image-with-border

In the upper left corner you can see the projects and regions present:

.. figure:: project-and-region-in-r1.png
   :class: image-with-border

R2 Cloud Panel
--------------

This option opens the **OpenStack Horizon** interface for region **R2**:

.. figure:: eumetsat-ecis-use-r2-form.png
   :class: image-with-border

The same logic applies for both the admin and the user/member of the **R2** account.

You will end up in Horizon interface for region **R2**:

.. figure:: cloud-and-region-for-r2.png
   :class: image-with-border


FRA1-3 Cloud Panel
------------------

This option opens the **OpenStack Horizon** interface for region **FRA1-3**:

.. figure:: eumetsat-ecis-enter-fra1-3-general.png
   :class: image-with-border

Note that you are logging in to one of the public clouds run by CloudFerro. First find ECIS in **Authenticate using** field

.. figure:: fra1-3-authenticate-using-ecis.png
   :class: image-with-border

and then find **FRA1-3** in **Region** fields:

.. figure:: region-fields-in-fra1-3.png
   :class: image-with-border

You should have this on the screen:

.. figure:: selected-region-and-auth-field-fra1-3.png
   :class: image-with-border

You should end up in Horizon interface:

.. figure:: cloudferro-upper-left-menu-projects-and-regions.png
   :class: image-with-border

What To Do Next
-------------------

It is possible to use **OpenStack** in combination with **Managed Kubernetes** and **Private storage**, see :doc:`/accountmanagement/Service-catalog/Service-catalog`.



