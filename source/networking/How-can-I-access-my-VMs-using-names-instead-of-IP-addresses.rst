How can I access my VMs using names instead of IP addresses on |brand-name|
===========================================================================

The VMs are seen simultaneously in several networks, at least in your "private" LAN and in the public Internet. By default the public addresses (Floating IPs, 185.48.x.x) have no associated names. You may assign such names from your DNS domain or you may request a name from us (as an additional service). The names provided by us have the following format:

.. code::

   computer_name.users.creodias.eu

where **computer_name** is chosen by you.

If you need the name just to access the machine from your office workstation, the simplest way is to add its address and friendly name to **/etc/hosts**.

The VMs in a given project share a common "private" network – by default it is **10.0.0.0/24**. You may create additional private networks with any addresses you like. However, they will not be equipped with DNS. If the machines are expected to recognize each other by their names, either **/etc/hosts** needs to be created and copied to all machines, or a private DNS may be run on one of them. Moreover, although the addresses are dynamically assigned, they are constant which means they do not change from the moment of creation to the moment of deletion of your machine.