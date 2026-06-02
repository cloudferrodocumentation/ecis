Cannot ping VM on |brand-name|
======================================

If you have problems with access to your VM - ping is not responding. Try the following:


install the packages **net-tools** (to have the **ifconfig** command) and **arping**:

in CentOS:

.. code::

   sudo yum install net-tools arping

in Ubuntu:

.. code::

   sudo apt install net-tools arping

check the name of the interface connected to private network:

.. code::

   ifconfig

based on the response, find the number of  the interface of 192.168.x.x (eth<number> or ens<number>)

after that invoke the following commands:

in CentOS:

.. code::

   sudo arping -U -c 2 -I eth<number> $(ip -4 a show dev eth<number> | sed -n 's/.*inet \([0-9\.]\+\).*/\1/p')


in Ubuntu:

.. code::

   sudo arping -U -c 2 -I ens<number> $(ip -4 a show dev ens<number> | sed -n 's/.*inet \([0-9\.]\+\).*/\1/p')


Next ping your external ip address and check if it helped.

