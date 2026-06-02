Ephemeral vs Persistent storage option Create New Volume on |brand-name|
===============================================================================

.. jinja:: brand_names

   Volumes created in the **Volumes > Volumes** section are *persistent* storage. They can be attached to a virtual machine and then reattached to a different one. They survive the removal of the virtual machine to which they are connected. You can also clone them, which is a simple way of creating a backup. However, if you copy them, you might also be interested in :doc:`/datavolume/Volume-snapshot-inheritance-and-its-consequences-on-Eumetsat-Elasticity/Volume-snapshot-inheritance-and-its-consequences-on-Eumetsat-Elasticity`.

.. jinja:: brand_names

      If you follow the instructions in this article: :doc:`/cloud/VM-created-with-option-Create-New-Volume-Yes-on-Eumetsat-Elasticity/VM-created-with-option-Create-New-Volume-Yes-on-Eumetsat-Elasticity` and set **Delete Volume on Instance Delete** to **No**, the boot drive of such virtual machine will also be persistent storage. You can, for example, use this feature to perform various tests and experiments.

.. jinja:: brand_names

       If you do not need persistent storage, use *ephemeral* storage. It cannot be reattached to a different machine and will be removed if the machine is removed. See the article :doc:`/cloud/VM-created-with-option-Create-New-Volume-No-on-Eumetsat-Elasticity/VM-created-with-option-Create-New-Volume-No-on-Eumetsat-Elasticity` on how to create a virtual machine with this type of storage.

You may find more information regarding this topic in `the official OpenStack documentation on design storage concepts <https://docs.openstack.org/arch-design/design-storage/design-storage-concepts.html>`_.


