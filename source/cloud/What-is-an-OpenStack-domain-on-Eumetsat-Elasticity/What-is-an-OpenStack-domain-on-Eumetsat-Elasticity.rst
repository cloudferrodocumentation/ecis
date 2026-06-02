What is an OpenStack domain on |brand-name|
============================================

**Domain**

Intention of providing a domain in cloud environment is to define boundaries for management. OpenStack domain is a type of a container for projects, users and groups.
One crucial benefit is separating overlapping resource names for different domains.
Furthermore, permissions in the project and domain are two not related things, hereby customization for administrator is made up much easier.

Current domain name is **visible** beside the project that is currently selected in the Horizon panel.

.. jinja:: openstack_domain

   .. image:: {{ openstack_domain }}

The name of the domain is grayed out, denoting that you can use only the domain that has been allocated to you by the system.

You cannot create a new domain.

**Service relation**

|brand-name| account is linked to your main account in particular domain, hence it allows you to login to the OpenStack dashboard without any need to deliver keystone credentials.

This type of facility is due to a proper implementation of KeyCloak and KeyStone relation.

**Docs**

Click here if you want to see official `OpenStack documentation for domains <https://docs.openstack.org/security-guide/identity/domains.html>`_.

