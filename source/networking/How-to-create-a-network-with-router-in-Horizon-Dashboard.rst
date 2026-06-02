How to create a network with router in Horizon Dashboard on |brand-name|
========================================================================

When you create a new project in Horizon, its content is empty. You have to manually configure your private network. In order to complete this task, please follow those steps.



1. Log in to your OpenStack dashboard and choose **Network** tab, then choose **Networks** sub-label.

.. figure:: net1.png
   :class: with-border


2. Click on the **“Create Network”** button.

.. figure:: net2.png



3. Define your Network Name and tick two checkboxes: **Enable Admin State** and **Create Subnet**. Go to Next.

.. figure:: net3.png



4. Define your Subnet name. Assign a valid network address with mask presented as a prefix. (This number determines how many bytes are being destined for network address)

Define Gateway IP for your Router. Normally it’s the first available address in the subnet.

Go to Next.

.. figure:: net4.png



5. In Subnet Details you are able to turn on DHCP server, assign DNS servers to your network and set up basic routing. In the end, confirm the process with **“Create”** button.

.. figure:: net5.png



6. Click on the **Routers** tab.

.. figure:: net6.png



7. Click on the **“Create Router”** button.

.. figure:: net7.png



8. Name your device and assign the only available network → external. Finish by choosing **“Create Router”** blue button.

.. figure:: net8.png



9. Click on your newly created Router (e.g called “Router_1”).

.. figure:: net9.png




10. Choose **Interfaces**.

.. figure:: net10.png



11. Choose **+ Add Interface** button.


.. figure:: net11.png



12. Assign a proper subnet and fill in IP Address. (It’s the gateway for our network). Submit the process.


.. figure:: net12.png



13. The internal interface has been attached to the router.


.. figure:: net13.png
