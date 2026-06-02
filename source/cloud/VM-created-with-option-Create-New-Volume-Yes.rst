VM created with option Create New Volume Yes on |brand-name|
============================================================

.. note::

   While creating a new Virtual Machine, you have to choose the source from which the VM will be built:

.. figure:: volyes1.png

|

If you choose "Image", you can choose the option "Create New Volume": Yes or No.

By default the option "No" is chosen.

**Option: Create New Volume - Yes**

This option allows you to choose the system volume different from that defined in the flavor:

.. figure:: volyes2.png

|

Now you can choose the Volume Size.

In the example below we will choose the volume 15 GB and apply it to the flavor eo1.xsmall.

Default size of the system disk for flavor eo1.xsmall is 8 GB:

.. figure:: volyes3.png

|

After choosing the other parameters (Details, Flavor, Networks, Security Group and Key Pair) you can launch the instance:

.. figure:: volyes4.png

|

You can see the VM created:

.. figure:: volyes5.png

|

If you go to Volumes -> Volumes pane you can see the system volume which the new VM is built on:

.. figure:: volyes6.png

|

If you click on "Edit Volume" button, you will see that the volume is bootable:

.. figure:: volyes7.png

|

If you previously have chosen "Delete Volume on Instance Delete": No

.. figure:: volyes8.png

|

and now you will delete the VM:

.. figure:: volyes9.png

|

then the volume will remain (not attached to any instance):

.. figure:: volyes10.png

|

You can now create a new VM from the volume choosing "Launch as Instance":

.. figure:: volyes11.png

.. figure:: volyes12.png

.. figure:: volyes13.png

|

you can choose different new flavor (eg. eo1.xmedium) than original (eo1.xsmall):

.. figure:: volyes14.png

|

After choosing other parameters (Details, Networks, Security Group and Key Pair) you can launch the instance.

.. figure:: volyes15.png

.. figure:: volyes16.png