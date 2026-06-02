How is my VM visible in the internet with no Floating IP attached on |brand-name|
==================================================================================

This article is written for clarification how an instance without a floating IP address would respond if we were to search for it it from an external machine.

How to find out what IP address is attached to VM?
-------------------------------------------------------

In Linux you can easily see your IP by executing command:

::

   curl ifconfig.me

In Windows, the easiest way is visiting website that shows us our public and private IP address, for example: `whatismyipaddress.com/ <https://whatismyipaddress.com//>`_



Is my VM visible from Internet without floating IP assigned?
------------------------------------------------------------------

No. If we don’t associate a Floating IP to the VM, it won't be routable from the internet. By setting an IP address using the process mentioned above, we will only see the interface address of the router attached to the private network (by default 192.168.0.1)


Can I send data from my VM without a floating IP?
-----------------------------------------------------------

Yes. If you want to send data from your VM to an external server, you should also allow receiving packets from 192.168.0.1 in your firewall configuration.

Is my VM accessible from the outside without floating IP?
------------------------------------------------------------------

.. jinja:: brand_names

   No. If a VM needs to be accessible from the Internet, a floating IP address must be attached to the instance. For more information on assigning Floating IPs to the instance, please see the following article: :doc:`/networking/How-to-Add-or-Remove-Floating-IPs-to-your-VM-on-{{ brand_name_hyphen }}/How-to-Add-or-Remove-Floating-IPs-to-your-VM-on-{{ brand_name_hyphen }}`.
