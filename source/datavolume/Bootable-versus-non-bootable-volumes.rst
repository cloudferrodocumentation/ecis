Bootable versus non-bootable volumes on |brand-name|
====================================================

Each volume has an indicator called **bootable** which shows whether an operating system can be booted from it or not. That indicator can be set up manually at any time. If you set it up on a volume that does not contain a bootable operating system and later try to boot a VM from it, you will see an error as a response.

In this article we will

 * explain practical differences between **bootable** and **non-bootable** volumes and
 * provide procedures in Horizon and OpenStack CLI to check whether the volume **bootable** or not.

Bootable vs. non-bootable volumes
---------------------------------

Bootable and non-bootable volumes share the following similarities:

 * **Data storage**: both types can store data (regardless of being bootable or not)
 * **Persistance**: they can be retained even if an instance is removed
 * **Snapshots**: they allow you to create snapshots which represent state of a volume at a particular point in time.

From a snapshot, you can spawn additional volumes so volumes act as a means of both conserving data and transferring of the data.

Bootable volumes usually serve as a boot drive for a virtual machine while non-bootable volumes typically function as data storage only. Bootable volumes can also contain data but one part of capacity will be devoted to the operating system that they contain.

On the other hand, non-bootable volumes can

 * add more storage space to an instance (especially for applications which require lots of data) and
 * separate data from the operating system to make backups and data management easier.

What We Are Going To Cover
--------------------------

 * Which volumes appear when creating a virtual machine using Horizon dashboard?
 * Attempting to create a virtual machine from non-bootable volume using OpenStack CLI
 * Checking whether a volume is bootable
 * Checking whether a volume snapshot was created from a bootable volume
 * Modifying bootable status of a volume
 * What happens if you launch a virtual machine from a volume which does not have a functional operating system?

Prerequisites
-------------

No. 1 **Account**

You need a |brand-name| hosting account with access to the Horizon interface: |brand-name-site-link|.

No. 2 **OpenStack CLI client operational**

We assume you are familiar with OpenStack CLI client. If not, here are some articles to get you started:

.. jinja:: brand_names

    * :doc:`/openstackcli/How-to-install-OpenStackClient-for-Linux-on-Eumetsat-Elasticity/How-to-install-OpenStackClient-for-Linux-on-Eumetsat-Elasticity`

    * :doc:`/openstackcli/How-to-install-OpenStackClient-GitBash-or-Cygwin-for-Windows-on-Eumetsat-Elasticity/How-to-install-OpenStackClient-GitBash-or-Cygwin-for-Windows-on-Eumetsat-Elasticity`

    * :doc:`/openstackcli/How-to-install-OpenStackClient-on-Windows-using-Windows-Subsystem-for-Linux-on-Eumetsat-Elasticity-OpenStack-Hosting/How-to-install-OpenStackClient-on-Windows-using-Windows-Subsystem-for-Linux-on-Eumetsat-Elasticity-OpenStack-Hosting`

.. ifconfig:: brand_name in two_fa_activated

    .. jinja:: brand_names

       Once you have installed this piece of software, you need to authenticate to start using it: :doc:`/accountmanagement/How-to-activate-OpenStack-CLI-access-to-Eumetsat-Elasticity-cloud/How-to-activate-OpenStack-CLI-access-to-Eumetsat-Elasticity-cloud`

.. ifconfig:: brand_name not in two_fa_activated

    .. ifconfig:: brand_name!= 'WEkEO'

       .. jinja:: brand_names

          Once you have installed this piece of software, you need to authenticate to start using it: :doc:`/accountmanagement/How-to-activate-OpenStack-CLI-access-to-Eumetsat-Elasticity-cloud/How-to-activate-OpenStack-CLI-access-to-Eumetsat-Elasticity-cloud`

    .. ifconfig:: brand_name == 'WEkEO'

       Once you have installed this piece of software, you need to authenticate to start using it: :doc:`/accountmanagement/How-to-activate-OpenStack-CLI-access-to-WEkEO-cloud-using-Federated-IDP-authorization-and-application-credentials`

No. 3 **Familiarity with the process of creation of virtual machines within OpenStack**

When creating a new virtual machine in OpenStack environment, you can decide what storage should it use to boot the operating system. These are some of the available options:

.. jinja:: brand_names

    * **ephemeral** storage: :doc:`/datavolume/Ephemeral-vs-Persistent-storage-option-Create-New-Volume-on-Eumetsat-Elasticity/Ephemeral-vs-Persistent-storage-option-Create-New-Volume-on-Eumetsat-Elasticity`

    * an exisiting volume

    * an existing volume snapshot

    * a volume being created while creating a virtual machine

.. jinja:: brand_names

   Article :doc:`/cloud/How-to-create-new-Linux-VM-in-OpenStack-Dashboard-Horizon-on-Eumetsat-Elasticity/How-to-create-new-Linux-VM-in-OpenStack-Dashboard-Horizon-on-Eumetsat-Elasticity` shows the general procedure for creating a VM while articles :doc:`/cloud/VM-created-with-option-Create-New-Volume-Yes-on-Eumetsat-Elasticity/VM-created-with-option-Create-New-Volume-Yes-on-Eumetsat-Elasticity` and :doc:`/cloud/VM-created-with-option-Create-New-Volume-No-on-Eumetsat-Elasticity/VM-created-with-option-Create-New-Volume-No-on-Eumetsat-Elasticity` discuss various options in connection to volumes.

If you create a virtual machine with option **Create New Volume** set to **Yes**, a **bootable** volume will be added to a list of your volumes.

Which volumes appear when creating a virtual machine using Horizon dashboard?
-----------------------------------------------------------------------------

Only bootable volumes appear while creating a virtual machine using Horizon dashboard.

Let's assume we have two volumes called **first-volume** and **second-volume** and let us say the former is non-bootable while the latter, **second-volume**, is bootable.

This is how they look like in Horizon dashboard:

.. jinja:: datavolume_images

   .. image:: {{ datavolume002 }}

When creating an instance, if we choose **Volume** from drop-down menu **Select Boot Source**, only **second-volume** will be visible because it is bootable.

.. jinja:: datavolume_images

   .. image:: {{ datavolume003 }}

Attempting to create a virtual machine from non-bootable volume using OpenStack CLI
-----------------------------------------------------------------------------------

OpenStack CLI client will also block an attempt of creating an instance from a non-bootable volume. If this happens, it will return a message similar to this as output:

.. code::

   Block Device cf3143bf-d227-4fa3-9224-c078f1ebdbad is not bootable. (HTTP 400) (Request-ID: req-d15e8fd6-028f-4d6b-904f-32dc78ccc3ad)

Checking whether a volume is bootable
-------------------------------------

Checking whether a volume is bootable using Horizon dashboard
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Navigate to **Volumes -> Volumes** of the Horizon dashboard. You should see the list of your volumes:

.. jinja:: datavolume_images

   .. image:: {{ datavolume004 }}

On this screen, in the row containing the volume you want to modify, check the value of column **Bootable**. On screenshot above, **bootable** status for volume **my-volume** was highlighted using the blue rectangle. It shows that that volume is indeed **bootable**.

Checking whether a volume is bootable using OpenStack CLI client
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Execute the following command to list volumes:

.. code::

   openstack volume list

You should get output similar to this:

.. jinja:: datavolume_images

   .. image:: {{ datavolume005 }}

This contains information about your volumes, such as their IDs, names and sizes. To check whether a volume is **bootable**, execute the command below:

.. code::

   openstack volume show -c bootable <<volume_id>>

You should get information whether the volume is **bootable**:

.. jinja:: datavolume_images

   .. image:: {{ datavolume006 }}

Checking whether a volume snapshot was created from a bootable volume
---------------------------------------------------------------------

If you want to create a virtual machine from a volume snapshot, make sure that a volume from which that volume snapshot was created is bootable.

Checking whether a volume snapshot was created from a bootable volume using Horizon dashboard
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Navigate to section **Volume -> Snapshots** of the Horizon dashboard. You should see a list of volume snapshots:

.. jinja:: datavolume_images

   .. image:: {{ datavolume007 }}

Click on the name of volume snapshot from which you want to create a virtual machine:

.. jinja:: datavolume_images

   .. image:: {{ datavolume008 }}

You should see the information about the volume snapshot. Click on the name of the volume from which the snapshot was created:

.. jinja:: datavolume_images

   .. image:: {{ datavolume009 }}

In section **Specs**, check the value called **Bootable**. Here, it is highlighted with a red rectangle:

.. jinja:: datavolume_images

   .. image:: {{ datavolume010 }}

Checking whether a volume snapshot was created from a bootable volume using OpenStack CLI client
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Execute the following command to list volume snapshots:

.. code::

   openstack volume snapshot list

A list of volume snapshots, similar to this, will appear:

.. jinja:: datavolume_images

   .. image:: {{ datavolume011 }}

To see concrete data about a volume, execute this command:

.. code::

   openstack volume snapshot show <<volume_snapshot_id>>

and replace **<<volume_snapshot_id>>** with the ID of the volume you want to create.

In this example, this ID is **cd101818-d690-4905-8b4c-465d868cc07f**. Therefore, this is how viewing more information about this volume would look like:

.. jinja:: datavolume_images

   .. image:: {{ datavolume012 }}

Field **volume_id** contains the ID of the volume from which the volume snapshot was created. The following command will provide information about this volume (replace **<<volume_id>>** with that ID of the volume):

.. code::

   openstack volume show -c bootable <<volume_id>>

You should get information whether the volume is **bootable**:

.. jinja:: datavolume_images

   .. image:: {{ datavolume006 }}

Modifying bootable status of a volume
-------------------------------------

Modifying bootable status of a volume using the Horizon dashboard
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Perform what was described in section **Checking if a volume is bootable**, method **Using the Horizon dashboard** - access the list of your volumes in the Horizon dashboard.

If you want to change the **bootable** status of a volume, navigate to the row containing information about that volume. There, in the **Actions** column choose **Edit Volume**:

.. jinja:: datavolume_images

   .. image:: {{ datavolume013 }}

You should see the following window:

.. jinja:: datavolume_images

   .. image:: {{ datavolume014 }}

To change the **bootable** status, simply check or uncheck (depending on what you want to achieve) the checkbox **Bootable** and click **Submit**.

In example above, the volume named **my-volume** had **bootable** status turned on. If we want to turn it off, we can uncheck the **Bootable** checkbox:

.. jinja:: datavolume_images

   .. image:: {{ datavolume015 }}

and click **Submit**.

The following message should appear next to top right corner of the Horizon dashboard:

.. jinja:: datavolume_images

   .. image:: {{ datavolume016 }}

And the value of column **Bootable** should also change:

.. jinja:: datavolume_images

   .. image:: {{ datavolume017 }}

Modifying bootable status of a volume using OpenStack CLI client
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Obtain ID and **bootable** status of the volume which you want to modify by following section **Checking if a volume is bootable**, method **Using OpenStack CLI client**.

**Non-bootable to bootable**

If your volume is currently **not bootable** and you want to make it **bootable**, execute the command below. In it, replace **<<volume_id>>** with the ID of the volume which you want to modify:

.. code::

   openstack volume set --bootable <<volume_id>>

If the command was successful, the output should be empty. You can now once again check the status of the volume as explained in section **Checking if a volume is bootable**.

**Bootable to non-bootable**

If, on the other hand, your volume is currently **bootable** and you want to make it **non-bootable**, execute the command below. In it, replace **<<volume_id>>** with the ID of the volume which you want to modify:

.. code::

   openstack volume set --non-bootable <<volume_id>>

If the command was successful, the output should be empty. You can now once again check the status of the volume as explained in section **Checking if a volume is bootable**.

What happens if you launch a virtual machine from a volume which does not have a functional operating system?
-------------------------------------------------------------------------------------------------------------

It is technically possible to launch a virtual machine from a volume which has status set to **bootable** but that does not contain an operating system which can be launched.

In this case, the virtual machine should still be spawned, but its BIOS will not detect a **bootable** operating system. On its web console, you should see that BIOS is displaying an appropriate message, similar to this:

.. jinja:: datavolume_images

   .. image:: {{ datavolume018 }}

.. TODO

    What To Do Next
    ---------------

    .. jinja:: brand_names

       To learn how to create a virtual machine from a volume snapshot, see :doc:`/cloud/How-to-create-a-VM-from-volume-snapshot-using-Horizon-dashboard-on-Eumetsat-Elasticity/How-to-create-a-VM-from-volume-snapshot-using-Horizon-dashboard-on-Eumetsat-Elasticity`
