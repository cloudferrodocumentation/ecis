How to mount an NFS Share on a Linux VM
=======================================

.. note::

   **Shares** functionality is present only in regions **R1** and **R2**.

A share created in Horizon does not appear automatically as a folder inside a virtual machine. Even after the share is created and the access rule is active, the Linux operating system still has to mount the NFS export before applications can use it.

This article shows how to connect a Linux VM to an OpenStack **NFS** share. You will copy the preferred export location from Horizon, connect to the VM over SSH, install the required NFS client tools if they are missing, create a local mount point, and mount the share as a directory in the VM.

After the share is mounted, the VM can use it like a normal filesystem path. This makes the share suitable for common files, project data, processing input and output, application directories, or any workflow where data must remain outside the VM disk and be available through shared storage.

Prerequisites
-------------

Before you mount an NFS share on a Linux VM, make sure that the share and VM are already prepared.

1. You need a |brand-name| hosting account with access to the Horizon interface:

   .. jinja:: horizon_interfaces

      .. tabs::

         {% for item in horizon_interfaces %}
         .. tab:: {{ item.label }}

            {{ item.url }}

            {% if item.note %}
            {{ item.note }}
            {% endif %}

         {% endfor %}

2. You have selected the correct project in Horizon.

   The share, access rule, and VM must belong to the project in which you are working.

3. You have created an NFS share and allowed access to it.

   The share must have the **Available** status, and an active access rule must already allow the VM's internal OpenStack IP address or private subnet.

   To prepare the share and access rule, use the previous articles in this series:

   * :doc:`/shares/How-to-create-a-Share-using-Horizon/How-to-create-a-Share-using-Horizon`
   * :doc:`/shares/How-to-allow-access-to-a-Share/How-to-allow-access-to-a-Share`

4. You have copied the preferred NFS export location from Horizon.

   The export location is the NFS path used in the mount command. It usually has this form:

   .. code::

      share-server-address:/share-path

   To find it, open:

   **Project** → **Share** → **Shares** → **share-name**

   .. jinja:: shares_images

      .. figure:: {{ shares038 }}
         :class: image-with-border
         :align: center

      Export location of the NFS share.

   Horizon marks one export location as **Preferred: True**. Copy it exactly as shown in Horizon and use as the location in the **mount** command.

5. You have SSH access to the Linux VM and **sudo** privileges.

   The mount operation is performed inside the VM. Make sure that you can log in to the VM over SSH and run commands with **sudo**.

   This article also uses **nano** to edit **/etc/fstab**. If **nano** is not installed on the VM, install it together with the NFS client tools in the installation step, or use another text editor already available on the VM.

Connect to the Linux VM
-----------------------

Connect to the Linux virtual machine that will mount the share.

Use the normal SSH method for your environment.

.. code::

   ssh username@vm-floating-ip-address

Replace **username** and **vm-floating-ip-address** with the values for your virtual machine.

Install NFS client tools
------------------------

The Linux VM must have NFS client tools installed before it can mount the share. This article also uses **nano** to edit **/etc/fstab**, so install it if it is not already present.

.. tabs::

   .. tab:: Ubuntu or Debian

      On Ubuntu or Debian, install the **nfs-common** and **nano** packages:

      .. code::

         sudo apt update
         sudo apt install nfs-common nano

   .. tab:: AlmaLinux, Rocky Linux, CentOS Stream, or RHEL-compatible distributions

      On AlmaLinux, Rocky Linux, CentOS Stream, or another RHEL-compatible distribution, install the **nfs-utils** and **nano** packages:

      .. code::

         sudo dnf install nfs-utils nano

After installation, the VM can mount NFS shares and you can edit **/etc/fstab** with **nano**.

Mount the NFS share
-------------------

Mount the share using the **preferred export location** copied from the share details page in Horizon.

The export location is the NFS address of the share. It tells the Linux VM which share server and share path to mount. In this example, the preferred export location is:

.. code::

   10.214.37.122:/share_a6c0751e_072c_4dc5_8b53_9f69a9b0433a

Create the local mount directory:

.. code::

   sudo mkdir -p /mnt/share1

Mount the share:

.. code::

   sudo mount -t nfs 10.214.37.122:/share_a6c0751e_072c_4dc5_8b53_9f69a9b0433a /mnt/share1

Test writing to the share
-------------------------

Create a test file:

.. code::

   echo "NFS share test" | sudo tee /mnt/share1/test-file.txt

List the directory contents:

.. code::

   ls -l /mnt/share1

If the file appears, the share is mounted and writable.

Here is what the entire process looks like in Terminal window:

.. jinja:: shares_images

   .. figure:: {{ shares039 }}
      :class: image-with-border
      :align: center

  Create a mounted NFS share

If you configured the share access rule as **read-only**, the write test will fail. In that case, use a read-only test instead.

Optional: mount the share automatically after reboot
----------------------------------------------------

To mount the share automatically after reboot, add it to **/etc/fstab**.

First, create a backup of the file:

.. code::

   sudo cp /etc/fstab /etc/fstab.backup

Then open **/etc/fstab** with a text editor:

.. code::

   sudo nano /etc/fstab

Add a line similar to this:

.. code::

   share-server-address:/share-path /mnt/share1 nfs defaults,_netdev 0 0

Replace **share-server-address:/share-path** with the preferred export location copied from Horizon.

For example, using the export location from this article:

.. code::

   10.214.37.122:/share_a6c0751e_072c_4dc5_8b53_9f69a9b0433a /mnt/share1 nfs defaults,_netdev 0 0
Test the **/etc/fstab** entry before rebooting:

.. code::

   sudo umount /mnt/share1
   sudo mount -a
   df -h /mnt/share1

If **mount -a** completes without errors and the share appears in **df -h**, the automatic mount configuration is working.

Troubleshooting
---------------

If the mount command fails, check the following:

* The share has the **Available** status in Horizon.
* The access rule has been added to the share.
* The access rule allows the correct IP address or network.
* The Linux VM can reach the share network endpoint.
* NFS client tools are installed.
* Security groups and network routes allow the required NFS traffic.
* You copied the export location exactly as shown in Horizon.

User messages for debugging
^^^^^^^^^^^^^^^^^^^^^^^^^^^

You can also check user messages in Horizon, via the following chain of commands:

**Project** → **Share** → **User Messages**

.. jinja:: shares_images

   .. figure:: {{ shares040 }}
      :class: image-with-border
      :align: center

   User Messages page for share-related errors.

The **User Messages** page may provide more information if the share operation failed or if the service reported an error.

What to do next
---------------

After mounting the share, you can use it as a shared directory for files, datasets, application data, or processing results.