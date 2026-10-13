VM created with option Create New Volume No
===========================================

During creation of a VM you can select a source. If you choose “Image”, you can then choose **Yes** or **No** for the option “**Create New Volume**”.

.. figure:: /cloud/VM-created-with-option-Create-New-Volume-No/volno1.png


By default **No** is selected:

.. figure:: /cloud/VM-created-with-option-Create-New-Volume-No/volno2.png

The new Virtual Machine will be created with the System Volume (Root Disk) size as defined in the flavor.

.. figure:: /cloud/VM-created-with-option-Create-New-Volume-No/volno3.png

.. jinja:: brand_names

   If you want to select a different size for the System Volume (Root Disk) please read article :doc:`/cloud/VM-created-with-option-Create-New-Volume-Yes`.

.. figure:: /cloud/VM-created-with-option-Create-New-Volume-No/volno4.png

In contrast to a VM created when choosing **Yes**, when choosing **No** the system disk is “ephemeral” and will not be visible in the Volumes view.

.. figure:: /cloud/VM-created-with-option-Create-New-Volume-No/volno5.png
