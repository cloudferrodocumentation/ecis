How To Attach Volume To Windows VM On |brand-name|
==================================================

In this tutorial, you will attach a volume to your Windows virtual machine. It increases the storage available for your files.

What We Are Going To Cover
--------------------------

 * Creating a new volume

 * Attaching the new volume to a VM

 * Preparing the volume to use with a VM

Prerequisites
-------------

No. 1 **Hosting**

You need a |brand-name| hosting account with Horizon interface |brand-name-site-link|.

No. 2 **Windows VM**

.. jinja:: brand_names

   You must operate a Microsoft Windows virtual machine running on |brand-name| |cloud-name| cloud. You can access it using the webconsole (:doc:`/cloud/How-to-access-the-VM-from-OpenStack-console-on-Eumetsat-Elasticity/How-to-access-the-VM-from-OpenStack-console-on-Eumetsat-Elasticity`) or through RDP. If you are using RDP, we strongly recommend using a bastion host for your security: :doc:`/windows/Connecting-to-a-Windows-VM-via-RDP-through-a-Linux-bastion-host-port-forwarding-on-Eumetsat-Elasticity/Connecting-to-a-Windows-VM-via-RDP-through-a-Linux-bastion-host-port-forwarding-on-Eumetsat-Elasticity`.

Step 1: Create a New Volume
---------------------------

Login to the Horizon panel available at |brand-name-site-link|.

Go to the section **Volumes -> Volumes**:

.. jinja:: datavolume_images

   .. image:: {{ datavolume019 }}

Click **Create Volume**.

The following window should appear:

.. jinja:: datavolume_images

   .. image:: {{ datavolume020 }}

In it provide the **Volume Name** of your choice.

Choose the **Type** of your volume - SSD or HDD.

Enter the size of your volume in gigabytes.

When you're done, click **Create Volume**.

You should now see the volume you just created. In our case it is called **data**:

.. jinja:: datavolume_images

   .. image:: {{ datavolume021 }}

Step 2: Attach the Volume to VM
-------------------------------

Now that you have created your volume, you can use it as storage for one of your VMs. To do that, attach the volume to a VM.

Shut down your VM if it is running.

In the **Actions** menu for that volume select the option **Manage Attachments**:

.. jinja:: datavolume_images

   .. image:: {{ datavolume022 }}

You should now see the following window:

.. jinja:: datavolume_images

   .. image:: {{ datavolume023 }}

Select the virtual machine to which the volume should be attached from the drop-down menu **Attach to Instance** and click **Attach Volume**.

Your volume should now be attached to the virtual machine:

.. jinja:: datavolume_images

   .. image:: {{ datavolume024 }}

Step 3: Format the Drive
------------------------

Start your VM and access it using RDP or the webconsole (see Prerequisite 2). Right-click the Start button and from the context menu select **Disk Management**. You should receive the following window:

.. jinja:: datavolume_images

   .. image:: {{ datavolume025 }}

In its lower section are the drives currently connected to your virtual machine:

.. jinja:: datavolume_images

   .. image:: {{ datavolume026 }}

In this case (on the screenshot above), there are two drives:

 * the system drive with 32 GB space
 * the attached volume with 2 GB of unallocated space

Right-click the section of the window in which the label **Not Initialized** exists:

.. jinja:: datavolume_images

   .. image:: {{ datavolume027 }}

From the context menu select **Initialize Disk**. You should receive the following window:

.. jinja:: datavolume_images

   .. image:: {{ datavolume028 }}

In this window you are asked which partition style do you want to use: MBR or GPT. If your volume has 2 TB or less space and you intend to use 4 primary partitions or less, you can use MBR, but if your requirements are higher, you should use GPT.

Choose either of these options and click **OK**.

Right-click the **Unallocated** space:

.. jinja:: datavolume_images

   .. image:: {{ datavolume029 }}

Choose **New Simple Volume**.

You should receive the following window:

.. jinja:: datavolume_images

   .. image:: {{ datavolume030 }}

Click **Next >**. The following window should appear:

.. jinja:: datavolume_images

   .. image:: {{ datavolume031 }}

If you want your volume to have only one partition, leave the default value in the text field. Otherwise, enter the size of the first partition of your volume.

You can choose to either assign a drive letter to your drive or mount it in an empty folder.

* If you want to assign a drive letter to that volume, choose the **Assign the following drive letter:** radio button. From the drop-down menu to its right choose a letter to which you wish to attach your volume. Confirm your choice by clicking **OK**.
* If you want to mount the volume to an NTFS folder on your drive, choose **Mount in the following empty NTFS folder:**. Click **Browse...** and in the **Browse for Drive Path** window choose an empty folder in which you wish to mount it. Confirm your choice by clicking **OK**.

The following window should now appear:

.. jinja:: datavolume_images

   .. image:: {{ datavolume032 }}

Here you can choose the formatting settings. Keep the radio button **Format this drive with the following settings:** selected. You can now enter the name which Windows will show for your new volume - it can be different then the one you typed in **Step 1**. Keep **Perform a quick format** checkbox selected. Click **Next >**. You should get the following window containing the summary of your chosen settings:

.. jinja:: datavolume_images

   .. image:: {{ datavolume033 }}

Click **Finish**.

Once the formatting process is complete, you should see appropriate information about your volume in the **Disk Management** window:

.. jinja:: datavolume_images

   .. image:: {{ datavolume034 }}

Your volume should now be mounted. If you chose to assign a drive letter, it should be visible in the **This PC** window:

.. jinja:: datavolume_images

   .. image:: {{ datavolume035 }}

If you want to create more partitions, repeat right-clicking the **Unallocated** space and completing the wizard as previously explained.

What To Do Next
---------------

Once you have gathered some data on your volume, you can create its backup, as explained in this article:

.. jinja:: brand_names

   :doc:`/datavolume/How-To-Create-Backup-Of-Your-Volume-From-Windows-Machine-on-Eumetsat-Elasticity/How-To-Create-Backup-Of-Your-Volume-From-Windows-Machine-on-Eumetsat-Elasticity`