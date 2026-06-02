.. meta::
   :description: What if i forgot to add the ssh key to my vm - or deleted it?
   :keywords: EO-Lab, forgot, deleted

What if I Forgot to Add the SSH Key to my VM - or Deleted it?
=============================================================

OpenStack only allows to add a SSH key to your VM during its creation, so if you forgot to add an SSH key to your VM at the start you may consider following options:

.. jinja:: brand_names

   1) You can try logging in using OpenStack Console in Horizon (see: :doc:`/cloud/How-to-access-the-VM-from-OpenStack-console-on-{{ brand_name_hyphen }}/How-to-access-the-VM-from-OpenStack-console-on-{{ brand_name_hyphen }}`) and add SSH key as per this article: :doc:`/networking/How-to-add-SSH-key-from-Horizon-web-console-on-{{ brand_name_hyphen }}/How-to-add-SSH-key-from-Horizon-web-console-on-{{ brand_name_hyphen }}`.

2) If your VM is new and doesn't have any important data, or attached Volumes with data, you can just delete it and create a new one.

3) If the VM has attached a Volume, you can detach the Volume, delete the VM, create a new VM and attach the volume again.

4) If you have important data and you have accidentally deleted your SSH key (either from the computer you connect from or from the VM itself) you may:

 * Create a Snapshot of your VM

 * Shelve your old VM

 * Run new VM from Snapshot. If all works you may delete the old VM.

When you start new VM from Snapshot you will have all starting options available (like Security Rules and SSH keys). If you have no SSH keys available just create a new one in **Project** → **Compute** → **Key pairs**.