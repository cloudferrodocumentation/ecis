How to create a Linux VM and access it from Linux command line on |brand-name|
==============================================================================

Creating a virtual machine in a |brand-name| cloud allows you to perform computations without having to engage your own infrastructure. In this article you shall create a Linux based virtual machine and access it remotely from a Linux command line on a desktop or laptop.

.. jinja:: brand_names

   If you want to access Linux VM from a Windows based command line, follow this article instead: :doc:`/cloud/How-to-create-a-Linux-VM-and-access-it-from-Windows-desktop-on-{{ brand_name_hyphen }}`.

.. note::

   This article only covers the basics of creating a VM - it does not cover topics such as use of NVIDIA hardware or creating a volume during the creation of a VM.

What We Are Going To Cover
--------------------------

 * Creating a Linux virtual machine in |brand-name| cloud using command **Launch Instance** from Horizon Dashboard

You will enter the following required data into that window:

 * Instance name

 * Instance source (from an operating system image)

 * Instance flavor (the combination of CPU, memory and storage capacity)

 * Networks that the newly created VM will use

Then create elements later needed for SSH connection:

 * Security groups to control access to the machine and

 * A key pair for SSH access to the Linux based VM in the cloud

For external access

 * Attach a floating IP to the instance so that it can be found on the Internet and, finally,

 * Use SSH to connect to that virtual machine from another Linux based system

Prerequisites
-------------

No. 1 **Hosting**

You need a |brand-name| hosting account with Horizon interface |brand-name-site-link|.

No. 2 **Basic knowledge of Linux terminal**

You should have some experience with Linux command line interface.

No. 3 **Linux installed on your local computer**

A Linux distribution running on your computer. This article was written for Ubuntu 20.04 LTS so please adjust the commands to your version of Linux.

No. 4 **SSH client installed and configured on your local Linux computer**

.. jinja:: brand_names

   The SSH client must be installed and configured on your local Linux computer. Please see :doc:`/networking/Generating-a-SSH-keypair-in-Linux-on-{{ brand_name_hyphen }}`.

.. jinja:: brand_names

   If you already have an SSH key pair and an SSH client configured, you should import your public key to the Horizon dashboard. The following article contains information how to do it: :doc:`/networking/How-to-Import-SSH-Public-Key-to-OpenStack-Horizon-on-{{ brand_name_hyphen }}`.

Alternatively, you can also create a key pair directly in the Horizon:

.. jinja:: brand_names

   :doc:`/cloud/How-to-create-key-pair-in-OpenStack-Dashboard-on-{{ brand_name_hyphen }}`.

Options for creation of a Virtual Machine (VM)
----------------------------------------------

Creation of a virtual machine is divided into 11 sections, four of which are mandatory (denoted by an asterisk in the end of the name of the option). In addition to those four (**Details**, **Source**, **Flavor**, and **Networks**), we shall define **Security Groups** and **Key Pairs**. The rest of the options to launch an instance is out of scope of this article.

.. note::

   In OpenStack terminology, a *virtual machine* is also an *instance*. *Instance* is a broader term as not all instances need be virtual machines, it is also possible to use real hardware as an instance.

The window to create a virtual machine is called **Launch Instance**. You will enter all the data about an instance into that window and its options.

Step 1 Start the Launch Instance window and name the virtual machine
--------------------------------------------------------------------

In the Horizon dashboard go to **Compute** -> **Instances** and click **Launch Instance**. You should get the following window:

.. image:: create-linux-linux-04_creodias.png

Type the name for your virtual machine in the **Instance Name** text field.

Click **Next** or the **Source** option on the left side menu.

Step 2 Define the source of the virtual machine
-----------------------------------------------

The **Source** window appears:

.. image:: create-linux-linux-05_creodias.png

Make sure that from the drop-down menu **Select Boot Source** option **Image** is selected.

.. image:: boot_source.png

From the **Available** list choose Linux distribution that suits you best and click **↑** next to it. It should now be visible in the **Allocated** section:

.. image:: create-linux-linux-06_creodias.png

This image shows that a Ubuntu 20.04 LTS was selected; if you, however, chose CentOS 7, that is what would show here instead of Ubuntu 20.04 LTS.

If you change your mind, click **↓** to unselect a source and then choose a different one.

Images which have **NVIDIA** in their name contain NVIDIA hardware. This article does not cover their use. Therefore, make sure that you choose the image without it.

Also, make sure that in the section **Create New Volume** option **No** is selected.

Click **Next** or click on button **Flavor** to define the flavor of the instance.

Step 3 Define the flavor of the instance
----------------------------------------

You should now see the following form:

.. image:: create-linux-linux-07_creodias.png

The standard definition of OpenStack *flavor* is the amount of resources available to the instance - like VCPU, memory and storage capacity.

Choose the one which suits you best and click **↑** next to it.

Make sure that you do **not** select one of the below flavors - they contain NVIDIA hardware and this article does not cover their use.

 * **vm.a6000.1**
 * **vm.a6000.2**
 * **vm.a6000.4**
 * **vm.a6000.8**

Sometimes, a flavor might be insufficient for source you chose in the previous step. If this is the case, you will see a yellow warning sign next to at least one of the values in the row for that flavor:

.. image:: yellow_triangles.png

To solve this issue, choose a flavor that supports your chosen source instead. In the image above, *vm.a6000.4* is not available but, say, *hm.large* is.

Another possible explanation might be that your quota is too low for creating a VM with your chosen flavor. You can see your quota in the **Compute -> Overview** section of your Horizon dashboard. If that is the case, you can either:

.. jinja:: brand_names

    * choose a different flavor or
    * contact the |brand-name| Support to request quota increase - :doc:`/accountmanagement/Help-Desk-And-Support`.

Click **Next** or click **Networks** to define networks.

Step 4 Define networks for the virtual machine
----------------------------------------------

You should now see the following window:

.. image:: create-linux-linux-08_creodias.png

Here you can select networks that will be attached to your virtual machine. They control the way your machine is connected to the Internet, to the other machines and to other resources as well.

.. ifconfig:: brand_name not in brands_without_eodata

   By default, you should have access to the following networks:

    * The network whose name starts with **cloud_** and which allows you to connect your machines together. It also has access to the **external** network which gives the instance access to the Internet.

    * The network whose name starts with **eodata_** which gives you access to the **eodata** repository.

   **eodata** is a repository of satellite images available on your |brand-name| cloud for download or processing.

.. ifconfig:: brand_name in brands_without_eodata

   By default, you should have access to the network whose name starts with **cloud_**, which allows you to connect your machines together. It also has access to the **external** network which gives the instance access to the Internet.

   Choose that network and also choose any other network that you want to access through the newly created VM.

These were the obligatory options. Since you want to access the instance through an SSH connection, you will need to define **Security Groups** and **Key Pair**.

Step 5 Define security groups for VM
------------------------------------

Security groups control network traffic to and from your virtual machine.

Click **Security Groups**. You should see the following form:

.. image:: create-linux-linux-09_creodias.png

By default, you have access to two groups:

 * **default** which blocks all incoming traffic and allows all outgoing traffic

 * **allow_ping_ssh_icmp_rdp** which allows incoming Ping, SSH, ICMP and RDP connections

Enable both of these rules. One of the open ports in **allow_ping_ssh_icmp_rdp** is 22, which is a prerequisite for SSH access.

Step 6 Create a key pair for SSH access
---------------------------------------

To use SSH to connect your local Linux computer to the cloud Linux "computer", you will need to provide one public and one secret key. (Keys are random strings, usually hundreds of characters long.)

Click **Key Pair**. You should now see the following window:

.. image:: create-linux-linux-10_creodias.png

In the image above, the key is called **test-key**. There are three ways to enter the keys into this window:

 * using option **Create Key Pair** -- create it on the spot,

 * using option **Import Key Pair** -- take the keys you already have and upload them to the cloud,

 * using one of the key pairs that were already existing within OpenStack cloud.

If you haven't created your key pair yet, please follow Prerequisite No. 4.

Anyways, make sure that your uploaded key is in the **Allocated** section.

.. removed this information, it is already in What To Do Next

Step 7 Create the instance
--------------------------

Once you have set everything up, click **Launch Instance**.

Your instance should now be in the **Instances** list. Initially, the instance will be in a state of "Spawning" as in this image:

.. image:: create-linux-linux-12_creodias.png

Spawning is the process of preparing the instance.

Wait up to a few minutes until your instance has finished spawning. The next state is **Running** label in the **Power State** column:

.. image:: create-linux-linux-13_creodias.png

It means that the instance is ready to use.

In Step 4 you have attached a network with the name that starts with **cloud_**. It allows the instance to send and receive data from other instances in the cloud and the Internet but does not automatically provide a static IP address. Such address is important if you want to host a website or access the instance via the SSH protocol.

Just like on the above screenshot, under header **IP Address**, you will see network addresses which both start with **10.**. It means that they are local network addresses. If you want to access your instance remotely, it must have a static IP address. The way to add it is to attach a so-called *floating IP* address to the instance.

Step 8 Attach a Floating IP to the instance
-------------------------------------------

.. jinja:: brand_names

   Here is how to create and attach a floating IP to your instance: :doc:`/networking/How-to-Add-or-Remove-Floating-IPs-to-your-VM-on-{{ brand_name_hyphen }}`.

Once you have added the floating IP, you will see it in the Horizon dashboard under header **IP Address** - just like in the last image from that article:

.. image:: ip_address_from_article.png

The floating IP address in that article is **64.225.132.0**. Your address will vary.

Step 9 Connecting to your virtual machine using SSH
---------------------------------------------------

.. jinja:: brand_names

   The following article has information about connecting to a virtual machine using SSH: :doc:`/networking/How-to-connect-to-your-virtual-machine-via-SSH-in-Linux-on-{{ brand_name_hyphen }}`.

The last command in that article was:

.. code::

   ssh eouser@64.225.132.99

The IP address in that article is **64.225.132.99** and is different from the address from the previous article. Instead of IP addresses used in these articles (**64.225.132.99** and **64.225.132.0**), enter the IP address of your instance which you saw after doing Step 8.

What To Do Next
---------------

|brand-name| cloud can be used for general hosting needs, such as

 * installing LAMP servers,

 * installing and using WordPress servers,

 * email servers,

 * Kubernetes and SLURM clusters and so on.

.. ifconfig:: brand_name not in brands_without_eodata

    You can also take advantage of its access to the **eodata** repository, where "eodata" stands for "Earth Observation Data" from satellites.

    .. jinja:: brand_names

       :doc:`/eodata/How-to-mount-eodata-using-S3FS-in-Linux-on-{{ brand_name_hyphen }}`

    .. jinja:: brand_names

       :doc:`/eodata/How-to-mount-eodata-as-a-filesystem-using-Goofys-in-Linux-on-{{ brand_name_hyphen }}`

    .. jinja:: brand_names

       :doc:`/eodata/How-to-download-EODATA-files-using-s3cmd-on-{{ brand_name_hyphen }}`.

    .. jinja:: brand_names

       :doc:`/eodata/How-to-access-EODATA-using-boto3-on-{{ brand_name_hyphen }}`.

        If you need more performance for purposes such as deep learning, you can use VMs with NVIDIA hardware. The following article covers the creation of such VM:

        .. jinja:: brand_names

           :doc:`/cloud/How-To-Create-a-New-Linux-VM-With-NVIDIA-Virtual-GPU-in-the-OpenStack-Dashboard-Horizon-on-{{ brand_name_hyphen }}`

        For a cutting edge example of using **eodata** and deep learning algorithms, please see:

        .. jinja:: brand_names

           :doc:`/cuttingedge/Sample-Deep-Learning-workflow-using-vGPU-and-EO-DATA-on-{{ brand_name_hyphen }}`.

To create a *cluster* of instances, see the series of articles on Kubernetes:

.. jinja:: brand_names

   :doc:`/kubernetes/How-to-Create-a-Kubernetes-Cluster-Using-{{ brand_name_hyphen }}-OpenStack-Magnum`.

If you find yourself unable to connect to your virtual machine using SSH, you can use the web console for troubleshooting and other purposes. Here's how to do it:

.. jinja:: brand_names

   :doc:`/cloud/How-to-access-the-VM-from-OpenStack-console-on-{{ brand_name_hyphen }}`

.. jinja:: brand_names

If you don't want the storage of your instance to be deleted while the VM is removed, you can choose to use a volume during instance creation. Please see the following articles:

.. jinja:: brand_names

   :doc:`/cloud/VM-created-with-option-Create-New-Volume-No-on-{{ brand_name_hyphen }}`

.. jinja:: brand_names

   :doc:`/cloud/VM-created-with-option-Create-New-Volume-Yes-on-{{ brand_name_hyphen }}`.

.. the user might not know what a web console is

You can't apply the SSH keys uploaded to the Horizon dashboard directly to a VM after its creation. The following article presents a walkaround to this problem:

.. jinja:: brand_names

   :doc:`/networking/How-to-add-SSH-key-from-Horizon-web-console-on-{{ brand_name_hyphen }}`.

.. jinja:: brand_names

   If you find that the storage of your VM is insufficient for your needs, you can attach the volume to it after its creation. The following articles contain appropriate instructions: :doc:`/datavolume/How-to-attach-a-volume-to-VM-less-than-2TB-on-Linux-on-{{ brand_name_hyphen }}` and :doc:`/datavolume/How-to-attach-a-volume-to-VM-more-than-2TB-on-Linux-on-{{ brand_name_hyphen }}`.