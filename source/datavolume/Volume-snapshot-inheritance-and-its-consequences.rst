Volume snapshot inheritance and its consequences on |brand-name|
================================================================

Performing a volume snapshot is a common form of securing your data against loss.
There is nothing wrong with that, but you should remember what the consequences are.

To illustrate the situation, we will present it on an example:
We have created a volume called "Volume A".

.. jinja:: datavolume_images

   .. figure:: {{ datavolume101 }}

Next we create an "SA" snapshot from the "VA" volume.

.. jinja:: datavolume_images

   .. figure:: {{ datavolume102 }}

From the OpenStack dashboard we can create new volumes "Volume B" and "Volume C" based on the previously created snapshot "Snapshot A".

.. jinja:: datavolume_images

   .. figure:: {{ datavolume103 }}

At the moment we have two new volumes which are based on the "Snapshot A" snapshot. Suppose we no longer need the volume called "Volume A" and we want to delete it.

.. jinja:: datavolume_images

   .. figure:: {{ datavolume104 }}

Unfortunately, its deletion will not be possible directly because to delete a given volume, we have to delete its snapshots.

.. jinja:: datavolume_images

   .. figure:: {{ datavolume105 }}

So we must first delete the snapshot "Snapshot A" and then the volume "Volume A".

However, this will also not be possible due to the fact that the "Snapshot A" snapshot is the source for 2 volumes "Volume B" and "Volume C".

To delete a volume from which snapshots volumes were created, we must also delete all snapshots of this volume.

In conclusion, when creating new volumes from a snapshot, remember about inheritance. Snapshot "Snapshot A" is a parent for the volumes (children) "Volume B" and "Volume C" and if we want to delete the volume "Volume A", we have to do it from the youngest generation (Volume B and Volume C).

.. jinja:: brand_names

   Backups are another solution and they do not create such bonds as snapshots and may exist even after the volume from which the backup was created has been deleted. Please see :doc:`/openstackcli/How-to-backup-an-instance-and-download-it-to-the-desktop-on-Eumetsat-Elasticity/How-to-backup-an-instance-and-download-it-to-the-desktop-on-Eumetsat-Elasticity`.