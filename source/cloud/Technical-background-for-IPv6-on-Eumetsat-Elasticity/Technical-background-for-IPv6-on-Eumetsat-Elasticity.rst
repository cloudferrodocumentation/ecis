Understand IPv6 on |brand-name|
===============================

This article explains the technical background for IPv6 on |brand-name|.

If you want to create an IPv6-enabled tenant network first, follow the companion article:

.. jinja:: brand_names

   * :doc:`/cloud/Create-an-IPv6-network-on-{{ brand_name_hyphen }}/Create-an-IPv6-network-on-{{ brand_name_hyphen }}`

This follow-up article is for readers who want to understand why the recommended settings are used, how IPv6 behaves in practice, and which limitations are important in everyday work.

.. raw:: html

   <h2>What we are going to cover</h2>

.. contents::
   :depth: 2
   :local:
   :backlinks: none

IPv6 use cases -- a technical overview
--------------------------------------

Any network, including pre-created tenant networks, can have an IPv6 subnet attached just as an IPv4 subnet would be.

For most tenant users, the main question is not whether IPv6 works, but which type of IPv6 setup is appropriate for the intended workload.

Private networks
^^^^^^^^^^^^^^^^

.. role:: under

The private IPv6 address range spans **fc00::/7**, which makes any **/64** subnet within this range a very good and generally recommended choice for local network prefixes.

For example, a network can be configured with a mnemonic address like :under:`fc00:abcd:1234:1::/64`.

In this example:

* **fc00** places the subnet in the private IPv6 range
* **abcd:1234** are example hexadecimal blocks within your private addressing plan
* **1** identifies one particular subnet within that plan
* **::** shortens the remaining zero blocks
* **/64** defines the network prefix length

Typically, the network gateway is located at the first address of the subnet, at **:1**. It is important to keep this gateway active to support automatic address assignment methods such as SLAAC.

Although it is possible to use other IPv6 prefixes, including publicly routable ones, inside private networks, such addresses will not normally be reachable from the Internet in this setup. As a result, a private IPv6 network should be treated as not having direct Internet access.

Public networks
^^^^^^^^^^^^^^^

To establish a public IPv6 network, use addresses from the provided subnet pool, which can be selected by using the :under:`--subnet-pool` option in the command-line interface (CLI).

After selecting the appropriate subnet, create a tenant network and connect it to a router that has a gateway in one of the external networks.

It is important to note that IPv6 networks with Internet access are publicly reachable. Therefore, avoid connecting servers with permissive access groups to public networks unless this is really required.

Single-stack and dual-stack
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Although single-stack IPv6 is supported, it is recommended to attach an IPv4 network during setup and throughout the lifecycle of a virtual machine.

This improves compatibility and helps services such as cloud-init work more reliably.

In practice, dual-stack is often the easier option because it avoids some image-specific and DNS-related edge cases that can appear in IPv6-only deployments.

Security groups
^^^^^^^^^^^^^^^

IPv6 security groups are fully supported, but they require additional rules compared to IPv4, including the "**Any host**" rule set to **::/0** to cover all IPv6 addresses.

When adding interfaces to a server, pay attention to the security groups assigned to each port, as a new port may not inherit all the security groups from the server itself.

For most tenant users, this becomes relevant as soon as an instance should be reachable over public IPv6. If traffic does not reach the instance, check the security group rules first.

Address assignment
^^^^^^^^^^^^^^^^^^

The recommended setting for address assignment is SLAAC using the EUI-64 format. This setting :under:`MUST` be configured explicitly; otherwise, it will default to "**None**".

The following modes are available:

SLAAC (eui-64) RECOMMENDED
   The gateway router sends router advertisements containing the network prefix so that virtual machines can compute their addresses statelessly by using the EUI-64 algorithm.

   It is important to note that other address generation methods, including privacy extensions, may not work correctly in this setup. For best compatibility, use plain EUI-64 without privacy extensions.

SLAAC (external)
   Exists for specific use cases outside the scope of this document.

DHCPv6 stateful
   Classic DHCP. This mode is not supported by many images as a default option.

DHCPv6 stateless
   A mix of SLAAC and DHCP: the router provides the prefix, while DHCP provides extended options such as DNS.

Why SLAAC with EUI-64 is recommended
------------------------------------

For normal tenant usage, SLAAC with EUI-64 is the safest and most compatible option.

The main reason is consistency. In this setup, the address that the instance uses is expected to match the address visible from OpenStack. This matters for port security and for services that expect the addressing model to remain predictable.

If a different address generation method is used, especially one that relies on privacy extensions, the instance may behave in ways that are harder to reconcile with the expected network state. This is why plain EUI-64 is recommended for normal use.

Load balancers and dual stack
-----------------------------

Load balancers in OpenStack cannot support dual-stack Virtual IPs on a single instance.

If IPv4 and IPv6 frontends are needed, two separate load balancers are required, each connected to its respective subnet.

Additionally, in dual-stack networks, load balancers can handle pool members using both IPv4 and IPv6. They can also include pool members from external networks that are routable.

Important considerations
------------------------

Before relying on IPv6 in production workloads, note the following:

#. **HTTP(s) addresses**

   When an IPv6 address is used in a URL, it must be enclosed in square brackets to distinguish the address from the port number.

   .. code::

      http://[fd00:dead:beef:64:34::2]:80

#. **Link-local addresses**

   Every interface in an IPv6 network is automatically assigned a link-local address in the **fe80::** range. These addresses are important for local communication, and it is often necessary to specify the interface when using them.

   .. code::

      fe80::a9fe:a9fe%eth0

#. **Subnet size**

   Use **/64** networks for your subnets unless you have a strong reason not to do so. This is the standard choice for IPv6 functionality and compatibility.

#. **SLAAC behavior**

   EUI-64 without privacy extensions is the recommended SLAAC mode in this setup. Other methods may not work correctly, because the address is expected to match what OpenStack shows in **server show**. This is related to port security behavior.

#. **Port security and Metadata6**

   Disabling port security can disrupt the Metadata6 service. This service listens on the link-local address :under:`fe80::a9fe:a9fe%interface`, which requires the correct interface to be specified. It is important for cloud-init compatibility with the OpenStack source, although it does not function for the EC2 source.

#. **DNS in single-stack IPv6**

   In single-stack IPv6 implementations, manual DNS configuration on instances may be required to ensure proper name resolution.

#. **Dual-stack recommendation**

   Dual-stack deployments are strongly recommended, even with a small private IPv4 subnet. In practice, dual-stack usually offers simpler configuration and better compatibility with different image types.

#. **Default security groups**

   At present, default security groups do not allow incoming IPv6 traffic. Make sure that your security group rules are adjusted appropriately for your IPv6 requirements.

What to do next
---------------

After reading this article, you may want to continue with one of the following tasks:

* create and test an IPv6-enabled tenant network
* review your security groups for public IPv6 access
* decide whether a workload should use single-stack IPv6 or dual-stack
* verify how a load-balanced service should be exposed over IPv4 and IPv6

.. jinja:: brand_names

   See also:

   * :doc:`/cloud/Create-an-IPv6-network-on-{{ brand_name_hyphen }}/Create-an-IPv6-network-on-{{ brand_name_hyphen }}`