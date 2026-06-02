Load Balancer as a Service - user documentation on |brand-name|
===========================================================================================

Load Balancer is a service that listens for requests, and then forwards those requests on to servers within a pool.
There are many reasons why you should take advantage of this functionality, but the most common situations are when you are trying to get a
high-availability architecture, and when you need more performance than a single server can provide.

The following figure presents the general concept of LBaaS service and its main components.

.. jinja:: networking_images

   .. figure:: {{ networking002 }}
      :class: with-border

The load balancer occupies Openstack neutron network port and has an IP address assigned from a subnet. Load balancers can listen for requests on multiple ports. Each one of those ports is specified by a listener. A pool holds a list of members that serve content through the load balancer. Members are servers that serve traffic behind a load balancer. Each member is specified by the IP address and port that it uses to serve traffic. Members may go offline from time to time and health monitors divert traffic away from members that are not responding properly. Health monitors are associated with pools.

**Basic Load Balancer configuration**

You can create new Load Balancer using one of two available methods

* by OpenStack Horizon dashboard
* using Octavia CLI extensions to OpenStack Client

**Types of Load Balancers in** |cloud-name| **Cloud**

For the cloud |cloud-name|, there are 6 types of flavors available that can be used when launching the load balancer.
3 of them are flavors designed for load balancers operating in HA (High Availability) mode and another 3 in non-HA mode.
We strongly recommend to run flavors in high availability mode, non-HA flavors should be used for testing purposes, because there is a danger to lose all traffic on them in case of Amphora agent failure. Load balancers in HA mode will automatically switch to another agent in such a case.

**Available flavor types**

.. jinja:: networking_images

   .. figure:: {{ networking003 }}
      :class: with-border

.. attention::

   Please note that the biggest flavor of load balancer will not necessarily result in the highest performance. The performance achieved depends on several factors. For example, the largest flavor will provide the best efficiency for simultaneous access to small files by a large number of users. Therefore, we recommend the user to carry out performance tests for their specific applications in order to choose the best load balance solution.

**Creating Load Balancer using OpenStack Horizon dashboard**

If you want to configure new Load Balancer using Openstack dashboard, navigate to Project **>** Network **>** Load Balancers tab and click on *Create Load Balancer* button.

Fill the required fields in Load Balancer Details tab, select flavor type and subnet for Load Balancer.
If flavor is not selected, the load balancer will be launched with the default flavor type: HA-large (2 CPU,2GB RAM)

.. jinja:: networking_images

   .. figure:: {{ networking004 }}
      :class: with-border

Now you should provide the details for the listener (listening endpoint of a load balanced service).
Choose from the list protocol as well as other protocol specific details that are attributes of the listener.
For HTTP protocol, you can choose whether to include headers into the request to the backend member as well.

.. jinja:: networking_images

   .. figure:: {{ networking005 }}
      :class: with-border

Provide details for the pool as well as pool members ( pool is the object representing the grouping of members to which the listener forwards client requests). Pool members can be also added after creation of Load Balancer.

.. jinja:: networking_images

   .. figure:: {{ networking006 }}
      :class: with-border

.. jinja:: networking_images

   .. figure:: {{ networking007 }}
      :class: with-border

Now you can define the detail for health monitor, which is an object that defines a check method for each member of the pool.

.. jinja:: networking_images

   .. figure:: {{ networking008 }}
      :class: with-border


Now you can click the “Create Load Balancer” button and create a load balancer in accordance to the previously entered configuration.

After creation Floating IP can be associated to Load Balancer, if such association is needed.

.. jinja:: networking_images

   .. figure:: {{ networking009 }}
      :class: with-border

**Python Octavia Client**

To operate with Load Balancers with CLI the Python Octavia Client (python-octaviaclient) is required.
It is a command-line client for the OpenStack Load Balancing service.

**Installation**

Install the load-balancer (Octavia) plugin:

.. code::

   pip install python-octaviaclient

Or, if you have virtualenvwrapper installed:

.. code::

   mkvirtualenv python-octaviaclient
   pip install python-octaviaclient


**Creating basic HTTP Load Balancer using CLI**

The way in which you can prepare the basic HTTP Load Balancer configuration using the Openstack CLI will be illustrated in the following example:

Description of the example scenario:

  * To ensure a high level of reliability and performance we need to configure three BackEnd servers using IP: 192.168.1.10, 192.168.1.11, 192.168.1.12 on subnet private-subnet, that have been configured with an HTTP application on TCP port 80.

  * Backend servers will be monitored by health check based on ping.

  * Neutron network public is a shared external network created by the cloud operator which is reachable from the internet.

  * We want to configure a basic load balancer that is accessible from the internet via Floating IP, which distributes web requests to the back-end servers, and which checks the servers with ping stream to ensure back-end member health.

List of steps that should be taken to achieve the goal described in the above scenario:

1. Create a new load balancer

.. code::

   openstack loadbalancer create --vip-subnet-id <subnet-id> --name <name>

2. Create HTTP listener for freshly created load balancer

.. code::

   openstack loadbalancer listener create --name <name for listener> --protocol HTTP --protocol-port 80 <load balancer name or id>

3. Create a new pool based on round-robin algorithm and set this pool as default for HTTP listener.

.. code::

   openstack loadbalancer pool create --name <name for pool> --lb-algorithm ROUND_ROBIN --listener <listener name or id> --protocol HTTP --session-persistence type=APP_COOKIE,cookie_name=PHPSESSIONID

4. Create a health monitor based on ping.

.. code::

   openstack loadbalancer healthmonitor create --name <name for health monitor> --delay 5 --max-retries 4 --timeout 10 --type PING <pool name or id>

5. Add members to the pool

.. code::

   openstack loadbalancer member create --subnet-id subnet --address 192.168.1.10 --protocol-port 80 <pool name or id>
   openstack loadbalancer member create --subnet-id subnet --address 192.168.1.11 --protocol-port 80 <pool name or id>
   openstack loadbalancer member create --subnet-id subnet --address 192.168.1.12 --protocol-port 80 <pool name or id>

6. Allocate a floating IP address to the project.

.. code::

   openstack floating ip create external

7. Associate this floating IP with the load balancer VIP port. The following IDs should be visible in the output of previous commands.

.. code::

   openstack floating ip set --port <load balancer vip_port_id> <floating IP id>


**Glossary**

*Amphora*

Virtual machine, container, dedicated hardware, appliance or device that actually performs the task of load balancing in the Octavia system. More specifically, an amphora takes requests from clients on the front-end and distributes these to back-end systems. Amphorae communicate with their controllers over the LB Network through a driver interface on the controller.

*Apolocation*

Term used to describe when two or more amphorae are not colocated on the same physical hardware (which is often essential in HA topologies). May also be used to describe two or more loadbalancers which are not colocated on the same amphora.

*Controller*

Daemon with access to both the LB Network and OpenStack components which coordinates and manages the overall activity of the Octavia load balancing system. Controllers will usually use an abstracted driver interface (usually a base class) for communicating with various other components in the OpenStack environment in order to facilitate loose coupling with these other components. These are the “brains” of the Octavia system.

*HAProxy*

Load balancing software used in the reference implementation for Octavia. (See http://www.haproxy.org/ ). HAProxy processes run on amphorae and actually accomplish the task of delivering the load balancing service.

*Health Monitor*

An object that defines a check method for each member of the pool. The health monitor itself is a pure-db object which describes the method the load balancing software on the amphora should use to monitor the health of back-end members of the pool with which the health monitor is associated.

*LB Network*

Load Balancer Network. The network over which the controller(s) and amphorae communicate. The LB network itself will usually be a nova or neutron network to which both the controller and amphorae have access, but is not associated with any one tenant. The LB Network is generally also not part of the undercloud and should not be directly exposed to any OpenStack core components other than the Octavia Controller.

*Listener*

Object representing the listening endpoint of a load balanced service. TCP / UDP port, as well as protocol information and other protocol- specific details are attributes of the listener. Notably, though, the IP address is not.

*Load Balancer*

Object describing a logical grouping of listeners on one or more VIPs and associated with one or more amphorae. (Our “Loadbalancer” most closely resembles a Virtual IP address in other load balancing implementations.) Whether the load balancer exists on more than one amphora depends on the topology used. The load balancer is also often the root object used in various Octavia APIs.

*Load Balancing*

The process of taking client requests on a front-end interface and distributing these to a number of back-end servers according to various rules. Load balancing allows for many servers to participate in delivering some kind TCP or UDP service to clients in an effectively transparent and often highly-available and scalable way (from the client’s perspective).

*Member*

Object representing a single back-end server or system that is a part of a pool. A member is associated with only one pool.

*Octavia*

Octavia is an operator-grade open source load balancing solution. Also known as the Octavia system or Octavia Openstack project. The term by itself should be used to refer to the system as a whole and not any individual component within the Octavia load balancing system.

*Pool*

Object representing the grouping of members to which the listener forwards client requests. Note that a pool is associated with only one listener, but a listener might refer to several pools (and switch between them using layer 7 policies).

*TLS Termination*

Transport Layer Security Termination - type of load balancing protocol where HTTPS sessions are terminated (decrypted) on the amphora as opposed to encrypted packets being forwarded on to back-end servers without being decrypted on the amphora. Also known as SSL termination. The main advantages to this type of load balancing are that the payload can be read and / or manipulated by the amphora, and that the expensive tasks of handling the encryption are off-loaded from the back-end servers. This is particularly useful if layer 7 switching is employed in the same listener configuration.

*VIP*

Virtual IP Address - single service IP address which is associated with a load balancer. In a highly available load balancing topology in Octavia, the VIP might be assigned to several amphorae, and a layer-2 protocol like CARP, VRRP, or HSRP (or something unique to the networking infrastructure) might be used to maintain its availability. In layer-3 (routed) topologies, the VIP address might be assigned to an upstream networking device which routes packets to amphorae, which then load balance requests to back-end members.

**Additional documentation and useful links**

`Openstack Octavia documentation: <https://docs.openstack.org/octavia/queens/user/>`_

`Openstack LBaaS Octavia Command Line Interface Reference: <https://docs.openstack.org/python-octaviaclient/latest/cli/index.html>`_

`OpenStack Octavia v2 ReSTful HTTP API <https://developer.openstack.org/api-ref/load-balancer/v2/index.html>`_

`Openstack LBaaS Octavia HAProxy Amphora API <https://docs.openstack.org/octavia/queens/contributor/api/haproxy-amphora-api.html>`_
