VM created with option Create New Volume Yes on |brand-name|
===============================================================

.. note::

   While creating a new Virtual Machine, you have to choose the source from which the VM will be built:

.. figure:: /cloud/VM-created-with-option-Create-New-Volume-Yes-on-Eumetsat-Elasticity/volyes1.png

|

If you choose "Image", you can choose the option "Create New Volume": Yes or No.

By default the option "No" is chosen.

**Option: Create New Volume - Yes**

This option allows you to choose the system volume different from that defined in the flavor:

.. figure:: /cloud/VM-created-with-option-Create-New-Volume-Yes-on-Eumetsat-Elasticity/volyes2.png

|

Now you can choose the Volume Size.

In the example below we will choose the volume 15 GB and apply it to the flavor eo1.xsmall.

Default size of the system disk for flavor eo1.xsmall is 8 GB:

.. figure:: /cloud/VM-created-with-option-Create-New-Volume-Yes-on-Eumetsat-Elasticity/volyes3.png

|

After choosing the other parameters (Details, Flavor, Networks, Security Group and Key Pair) you can launch the instance:

.. figure:: /cloud/VM-created-with-option-Create-New-Volume-Yes-on-Eumetsat-Elasticity/volyes4.png

|

You can see the VM created:

.. figure:: /cloud/VM-created-with-option-Create-New-Volume-Yes-on-Eumetsat-Elasticity/volyes5.png

|

If you go to Volumes -> Volumes pane you can see the system volume which the new VM is built on:

.. figure:: /cloud/VM-created-with-option-Create-New-Volume-Yes-on-Eumetsat-Elasticity/volyes6.png

|

If you click on "Edit Volume" button, you will see that the volume is bootable:

.. figure:: /cloud/VM-created-with-option-Create-New-Volume-Yes-on-Eumetsat-Elasticity/volyes7.png

|

If you previously have chosen "Delete Volume on Instance Delete": No

.. figure:: /cloud/VM-created-with-option-Create-New-Volume-Yes-on-Eumetsat-Elasticity/volyes8.png

|

and now you will delete the VM:

.. figure:: /cloud/VM-created-with-option-Create-New-Volume-Yes-on-Eumetsat-Elasticity/volyes9.png

|

then the volume will remain (not attached to any instance):

.. figure:: /cloud/VM-created-with-option-Create-New-Volume-Yes-on-Eumetsat-Elasticity/volyes10.png

|

You can now create a new VM from the volume choosing "Launch as Instance":

.. figure:: /cloud/VM-created-with-option-Create-New-Volume-Yes-on-Eumetsat-Elasticity/volyes11.png

.. figure:: /cloud/VM-created-with-option-Create-New-Volume-Yes-on-Eumetsat-Elasticity/volyes12.png

.. figure:: /cloud/VM-created-with-option-Create-New-Volume-Yes-on-Eumetsat-Elasticity/volyes13.png

|

you can choose different new flavor (eg. eo1.xmedium) than original (eo1.xsmall):

.. figure:: /cloud/VM-created-with-option-Create-New-Volume-Yes-on-Eumetsat-Elasticity/volyes14.png

|

After choosing other parameters (Details, Networks, Security Group and Key Pair) you can launch the instance.

.. figure:: /cloud/VM-created-with-option-Create-New-Volume-Yes-on-Eumetsat-Elasticity/volyes15.png

.. figure:: /cloud/VM-created-with-option-Create-New-Volume-Yes-on-Eumetsat-Elasticity/volyes16.png
