How to restore volume from snapshot on |brand-name|
===================================================

In this article, you will learn how to restore volume from volume snapshot using Horizon dashboard or OpenStack CLI client.

This can be achieved by creating a new volume from existing snapshot. You can then delete the previous snapshot and, optionally, previous volume.

Prerequisites
-------------

No. 1 **Hosting**

You need a |brand-name| hosting account with access to Horizon interface: |brand-name-site-link|

No. 2 **A volume snapshot**

You need to have a volume snapshot which you want to restore.

No. 3 **OpenStack CLI client**

If you want to interact with |brand-name| cloud using the OpenStack CLI client, you need to have it installed. Check one of these articles:

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


What We Are Going To Cover
--------------------------

 * Restoring volume snapshot using Horizon dashboard
 * Restoring volume snapshot using OpenStack CLI client

Restoring volume snapshot using Horizon dashboard
-------------------------------------------------

Navigate to the **Volumes -> Snapshots** section of the Horizon dashboard:

.. jinja:: datavolume_images

   .. image:: {{ datavolume094 }}

From the row representing the snapshot you want to restore, in the **Actions** column choose **Create Volume**:

.. jinja:: datavolume_images

   .. image:: {{ datavolume095 }}

You should get the window similar to this:

.. jinja:: datavolume_images

   .. image:: {{ datavolume096 }}

If you want your new volume to have a different name than your snapshot, enter the name of your choice in text field **Volume Name**.

In this example, we will name our new volume **my-restored-volume**.

Click **Create Volume**.

You should now be transferred to section **Volumes -> Volumes** of the Horizon dashboard. Your newly created volume should be there (in this example, its name was marked with a blue rectangle):

.. jinja:: datavolume_images

   .. image:: {{ datavolume097 }}

Make sure that the volume has the following **Status**: **Available**.

Restoring volume snapshot using OpenStack CLI client
----------------------------------------------------

Execute the following command:

.. code::

   openstack volume snapshot list

You should see the list of snapshots of your volumes:

.. jinja:: datavolume_images

   .. image:: {{ datavolume098 }}

Write somewhere down the ID of the snapshot from which you want to create a volume:

In this example, we want to restore the snapshot called **my-snapshot**. Its ID, marked on screenshot above with a blue rectangle, is **d0f384be-3e61-49a4-8742-70929d22032e**

To create a volume from your snapshot, execute command below, after replacing values as instructed.

.. code::

   openstack volume create --snapshot d0f384be-3e61-49a4-8742-70929d22032e my-restored-volume

Replace:

 * **d0f384be-3e61-49a4-8742-70929d22032e** with the ID of your volume snapshot
 * **my-restored-volume** with the name you want to give to your new volume

You should get output similar to this:

.. jinja:: datavolume_images

   .. image:: {{ datavolume099 }}

List volumes:

.. code::

   openstack volume list

Your new volume should now be on the list:

.. jinja:: datavolume_images

   .. image:: {{ datavolume100 }}

Make sure that newly created volume has the following **Status**: **available**.

What To Do Next
---------------

You can now connect your new volume to a virtual machine and/or delete the previous one.

.. jinja:: brand_names

   The following article includes information how to connect a volume to a virtual machine: :doc:`/openstackcli/How-to-move-data-volume-between-two-VMs-using-OpenStack-CLI-on-Eumetsat-Elasticity/How-to-move-data-volume-between-two-VMs-using-OpenStack-CLI-on-Eumetsat-Elasticity`

.. jinja:: brand_names

   To learn how to delete a volume snapshot, see this article :doc:`/datavolume/How-to-create-or-delete-volume-snapshot-on-Eumetsat-Elasticity/How-to-create-or-delete-volume-snapshot-on-Eumetsat-Elasticity`

Volume you've just created can also be migrated to another project on the same cloud. This can be done by following one of these articles:

.. jinja:: brand_names

    * :doc:`/cloud/How-to-transfer-volumes-between-domains-and-projects-using-Horizon-dashboard-on-Eumetsat-Elasticity/How-to-transfer-volumes-between-domains-and-projects-using-Horizon-dashboard-on-Eumetsat-Elasticity`
    * :doc:`/openstackcli/How-to-transfer-volumes-between-domains-and-projects-using-OpenStack-CLI-client-on-Eumetsat-Elasticity/How-to-transfer-volumes-between-domains-and-projects-using-OpenStack-CLI-client-on-Eumetsat-Elasticity`
