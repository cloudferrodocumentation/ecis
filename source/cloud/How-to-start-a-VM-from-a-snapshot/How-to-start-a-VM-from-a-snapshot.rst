How to start a VM from a snapshot
=================================


a) Volume Snapshot
------------------

1. Choose the desired virtual machine (booted from Volume) and click on the “Create snapshot” button.

.. figure:: /cloud/How-to-start-a-VM-from-a-snapshot/snap00.png



2. Name the snapshot. The decision is up to you to improve the personal navigation throughout image or volume snapshot repository. Confirm with the blue button.

.. figure:: /cloud/How-to-start-a-VM-from-a-snapshot/snap01.png



3. Go to Volumes tab and press Snapshots.

.. figure:: /cloud/How-to-start-a-VM-from-a-snapshot/snap3.png



4. Your volume snapshot is being stored in this place. To start a virtual machine from this type of snapshot, press on the arrow beside “Create Volume”.

.. figure:: /cloud/How-to-start-a-VM-from-a-snapshot/snap4.png



5. Choose “Launch as Instance”.

.. figure:: /cloud/How-to-start-a-VM-from-a-snapshot/snap5.png


6. Define Instance name and change  bookmark to “Source”.

.. figure:: /cloud/How-to-start-a-VM-from-a-snapshot/snap6.png

7. Set Boot Source on “Volume Snapshot” and assign previously created snapshot by clicking on the arrow.

.. figure:: /cloud/How-to-start-a-VM-from-a-snapshot/snap7.png

.. jinja:: brand_names

   8. The rest of procedure is the same: :doc:`/cloud/How-to-create-new-Linux-VM-in-OpenStack-Dashboard-Horizon/How-to-create-new-Linux-VM-in-OpenStack-Dashboard-Horizon`.

9. Newly created machine is visible in the Instances list.

.. figure:: /cloud/How-to-start-a-VM-from-a-snapshot/snap8.png

b) Image Snapshot
-----------------

1.Choose the desired virtual machine (booted from Glance image) and click on the “Create snapshot” button.

.. figure:: /cloud/How-to-start-a-VM-from-a-snapshot/snap1.png

2. Name the snapshot. The decision is up to you to improve the personal navigation throughout image or volume snapshot repository. Confirm with the blue button.

.. figure:: /cloud/How-to-start-a-VM-from-a-snapshot/snap2.png

3. Go to Compute tab and press Images.

.. figure:: /cloud/How-to-start-a-VM-from-a-snapshot/snap3.png

4. Scroll down and find your snapshot. Click on the “Launch”.

.. figure:: /cloud/How-to-start-a-VM-from-a-snapshot/snap4.png

.. attention::

   Image snapshot is in RAW format and its size is equivalent to the image that VM was booted from.
   In the “Images” you may also find symbolic links to the volume snapshots.(i.e. snapshot-virtual-machine-01 from a) scenario). This type of snapshot is in format QCOW2 and its size is set on 0 bytes.

5. Name your virtual machine and go to “Source.” Set Boot Source on “Instance snapshot" and choose previously created Snapshot in RAW format.

.. figure:: /cloud/How-to-start-a-VM-from-a-snapshot/snap5.png

.. jinja:: brand_names

   6. The rest of procedure is the same: :doc:`/cloud/How-to-create-new-Linux-VM-in-OpenStack-Dashboard-Horizon/How-to-create-new-Linux-VM-in-OpenStack-Dashboard-Horizon`.

7. Virtual machine has been created.

.. figure:: /cloud/How-to-start-a-VM-from-a-snapshot/snap6.png
