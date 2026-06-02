How to export a volume over NFS on |brand-name|
================================================

**Server configuration**

Update your system:

::

  sudo apt update && apt upgrade

Install necessary packages:

::

  sudo apt install nfs-kernel-server

Create a new folder, which will be exported by NFS, e.g.:

::

  sudo mkdir -p /mnt/<name of your folder>

Delete all access restrictions in the folder:

::

  sudo chown -R nobody:nogroup /mnt/<name of your folder>/

You can also replace permisssions of files in the folder with your own preferences.

e.g.

::

  sudo chmod 777 /mnt/<name of your folder>/


**Defining access permisions to NFS Server.**

In the file /etc/exports add the following line:

::

  /mnt/<name of your folder>  <IP address of allowed client>(rw,sync,no_subtree_check)

where <IP address> is the address of the server allowed to access the folder /mnt/<name of your folder>

e.g.

::

  # /etc/exports: the access control list for filesystems which may be exported

  #        to NFS clients.  See exports(5).

  #

  # Example for NFSv2 and NFSv3:

  # /srv/homes       hostname1(rw,sync,no_subtree_check) hostname2(ro,sync,no_subtree_check)

  #

  # Example for NFSv4:

  # /srv/nfs4        gss/krb5i(rw,sync,fsid=0,crossmnt,no_subtree_check)

  # /srv/nfs4/homes  gss/krb5i(rw,sync,no_subtree_check)

  #

  /mnt/<name of your folder>  <IP address of NFS server>(rw,sync,no_subtree_check)

You can also share your folder to more IP addresses:

::

  /mnt/<name of your folder>  <IP address 1>(rw,sync,no_subtree_check)
  /mnt/<name of your folder>  <IP address 2>(rw,sync,no_subtree_check)
  /mnt/<name of your folder>  <IP address 3>(rw,sync,no_subtree_check)

You can also share the folder to all servers in a Subnet (instead of adding every IP address separately) by adding following line to /etc/exports (e.g. servers in 192.168.0.0/24):

::

  /mnt/<name of your folder> 192.168.0.0/24(rw,sync,no_subtree_check)

When the configuration file /etc/exports is saved, invoke the following commands:

::

  sudo exportfs -a
  sudo systemctl restart nfs-kernel-server

**IT IS NECESSARY TO OPEN THE PORT 2049 IN A SECURITY GROUP!**


.. jinja:: brand_names

   (The FAQ about opening ports in a security group is available at :doc:`/networking/How-can-I-open-new-ports-port-80-for-http-for-my-service-or-instance-on-Eumetsat-Elasticity/How-can-I-open-new-ports-port-80-for-http-for-my-service-or-instance-on-Eumetsat-Elasticity`)

**Client Configuration**

Install required packages:

::

  sudo apt install nfs-common

Mount the NFS folder:

::

  sudo mount <IP address of your NFS server>:/mnt/<name of your folder in NFS server> <name of your folder in Client>/
