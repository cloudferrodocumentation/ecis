
You can move your instances and volumes between project and domains, however:

 * Openstack does not support moving IP addresses together with Instances, so you will need to Allocate and Associate new Floating IP.

 * If your instance had any Volimes attached as additional storage they will need to be moved separately. If there is more then one volume it is good to write down all device names (like /dev/vdb, /dev/vdc) together with their names or Volume ID's (in case names are identical). It will be needed later to re-attach them correctly, that is match the names or Volume ID's with device names.

As the procedure is easier to understand with Volumes, let's start with Volumes.

Transferring a Volume to new project/domain
-------------------------------------------------

Detach the Volume from any running instance before moving it to another domain or project.
After detaching you will have "Create Transfer" option avaliable.

Name your tranfer with any name, this is not important, but next thing is  - Transfer ID and Authorization Key - copy it to some text file.
Your Volume will be in "Awaiting Transfer" state until you finish.
Go to your destination project and/or domain then click "Accept transfer" in Volumes menu.
Paste your Transfer ID and Authorization Key.
Your Volume will now appear in new project/domain.


Transferring a Virtual Machine to new project/domain
--------------------------------------------------------

Create a snapshot of your VM by clicking "Create Snapshot" button in Instances menu in Horizon.
Convert Snapshot into a Volume. Only that way you can move it to new project and/or domain.
After converting Snapshot into a Volume you will have "Create Transfer" option avaliable and then you can proceed exactly the same way as with Volume transfer.

After you complete, launch Instance from that transferred Volume.
You will need to attach new Floating IP.

.. IMPORTANT::

   Running your new VM that had storage Volume(s) attached may result in an error and it will boot in Rescue Mode. This is normal and unavoidable, because to re-attach your storage volumes you need running Virtual Machine first.

   To fix that, just attach your newly transferred storage Volume(s) that were attached to the Instance before transferring it to new project/domain. If there is more then one the device, matching names (or Volume ID's if the names were identical)  with device names are important - that's why writing them down was needed.

   After attaching all Volumes just reboot your Instance, it will boot normaly next time.
