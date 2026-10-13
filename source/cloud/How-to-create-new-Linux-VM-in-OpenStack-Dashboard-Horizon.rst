How to create new Linux VM in OpenStack Dashboard Horizon
=========================================================

Go to **Project → Compute → Instances**.

.. figure:: /cloud/How-to-create-new-Linux-VM-in-OpenStack-Dashboard-Horizon/newvm1.png

Click **"Launch Instance"**.

Insert the name of the Instance (eg. "vm01") and click Next button.

.. figure:: /cloud/How-to-create-new-Linux-VM-in-OpenStack-Dashboard-Horizon/newvm2.png

Select Instance Boot Source (eg. "Image"), and choose desired image (eg. "Ubuntu 20.04 LTS") by clicking on arrow.

.. note::

   If you do not need to have the system disk bigger than the size defined in a chosen flavor, we recommend setting "Create New Volume" feature to "No" state.

.. figure:: /cloud/How-to-create-new-Linux-VM-in-OpenStack-Dashboard-Horizon/newvm3.png

Choose Flavor (eg. eo1.xsmall).

.. figure:: /cloud/How-to-create-new-Linux-VM-in-OpenStack-Dashboard-Horizon/newvm4.png

Click **"Networks"** and then choose desired networks.

.. figure:: /cloud/How-to-create-new-Linux-VM-in-OpenStack-Dashboard-Horizon/newvm5.png

Open **"Security Groups"** After that, choose "default" and "allow_ping_ssh_icmp_rdp" groups.

.. figure:: /cloud/How-to-create-new-Linux-VM-in-OpenStack-Dashboard-Horizon/newvm6.png

.. jinja:: brand_names

   Choose or generate SSH keypair :doc:`/cloud/How-to-create-key-pair-in-OpenStack-Dashboard` for your VM. Next, launch your instance by clicking on blue button.

.. figure:: /cloud/How-to-create-new-Linux-VM-in-OpenStack-Dashboard-Horizon/newvm7.png

You will see **"Instances"** menu with your newly created VM.

.. figure:: /cloud/How-to-create-new-Linux-VM-in-OpenStack-Dashboard-Horizon/newvm8.png

Open the drop-down menu and choose **"Console"**.

.. figure:: /cloud/How-to-create-new-Linux-VM-in-OpenStack-Dashboard-Horizon/newvm9.png

 Click on the black terminal area (to activate access to the console). Type: **eoconsole** and hit Enter.

.. figure:: /cloud/How-to-create-new-Linux-VM-in-OpenStack-Dashboard-Horizon/newvm10.png

Insert and retype new password.

.. figure:: /cloud/How-to-create-new-Linux-VM-in-OpenStack-Dashboard-Horizon/newvm11.png

Now you can type commands.

.. figure:: /cloud/How-to-create-new-Linux-VM-in-OpenStack-Dashboard-Horizon/newvm12.png

After you finish, type "exit".

.. figure:: /cloud/How-to-create-new-Linux-VM-in-OpenStack-Dashboard-Horizon/newvm13.png

This will close the session.

.. jinja:: brand_names

   If you want to make your VM accessible from the Internet check :doc:`/networking/How-to-Add-or-Remove-Floating-IPs-to-your-VM`.
