How to Back Up an Instance and Download it to the Desktop on |brand-name| OpenStack Hosting
=====================================================================================================

This article explains how to create a virtual machine using OpenStack CLI, create a snapshot of its boot volume, and prepare the backed-up disk for download to your desktop.

The article uses CLI commands only.

OpenStack instances can be created in different ways. If the instance is **booted from volume**, the **openstack server backup create** command is not supported. In that case, you must work with the attached boot volume instead.

Prerequisites
-------------

Before you start, make sure that the following requirements are met.

No. 1 **Account**

You need a |brand-name| hosting account with access to the Horizon interface: |brand-name-site-auth-link|.

No. 2 **OpenStack CLI client**

You need OpenStack CLI client installed. One of the following articles should help you:

.. jinja:: doc_links

   * :doc:`{{ openstackclient_linux }}`
   * :doc:`{{ openstackclient_windows }}`
   * :doc:`{{ openstackclient_windows_wsl }}`

   To use OpenStack CLI client to control |brand-name| cloud, you need to prove your identity: :doc:`{{ openstack_cli_auth }}`

No. 3 **OpenStack credentials**

You need an OpenStack RC file or an application credential RC file.

In this article, the file is named **app-cred-test-access-openrc.sh**. Use the name of your own RC file if it is different.


Prepare the CLI environment
---------------------------

Copy the RC file to your working directory and activate it.

.. code-block:: console

   cp /home/dusko/Downloads/app-cred-test-access-openrc.sh .
   source ./app-cred-test-access-openrc.sh

Verify that the OpenStack CLI client can communicate with the cloud.

.. code-block:: console

   openstack flavor list

Example output:

.. code-block:: text

   +------------------------------+------------------------------+---------+------+-----------+-------+-----------+
   | ID                           | Name                         |     RAM | Disk | Ephemeral | VCPUs | Is Public |
   +------------------------------+------------------------------+---------+------+-----------+-------+-----------+
   | 1cpu-1gbmem                  | 1cpu-1gbmem                  |    1024 |    0 |         0 |     1 | True      |
   | 2cpu-4gbmem                  | 2cpu-4gbmem                  |    4096 |    0 |         0 |     2 | True      |
   | 4cpu-4gbmem                  | 4cpu-4gbmem                  |    4096 |    0 |         0 |     4 | True      |
   | 4cpu-8gbmem                  | 4cpu-8gbmem                  |    8192 |    0 |         0 |     4 | True      |
   +------------------------------+------------------------------+---------+------+-----------+-------+-----------+


Choose the VM parameters
------------------------

Before creating the virtual machine, list the available images.

.. code-block:: console

   openstack image list

Choose the image that you want to use and save its ID in a variable.

.. code-block:: console

   IMAGE_ID=IMAGE_ID_FROM_THE_IMAGE_LIST

List the available networks.

.. code-block:: console

   openstack network list

Choose the network that should be attached to the instance and save its ID in a variable.

.. code-block:: console

   NETWORK_ID=NETWORK_ID_FROM_THE_NETWORK_LIST

List the available SSH key pairs.

.. code-block:: console

   openstack keypair list

Save the key pair name in a variable.

.. code-block:: console

   KEY_NAME=sshkey

List the available security groups.

.. code-block:: console

   openstack security group list

Save the security group name in a variable.

.. code-block:: console

   SECURITY_GROUP=default

Set the remaining variables used in this article.

.. code-block:: console

   SERVER_NAME=vm-john-01
   FLAVOR_NAME=4cpu-4gbmem
   BOOT_VOLUME_SIZE=5

   SNAPSHOT_NAME=backup-01-snapshot
   TEMP_VOLUME_NAME=backup-01-volume
   IMAGE_NAME=backup-01-image
   DOWNLOAD_FILE=backup-01-image.raw


Create the virtual machine
--------------------------

Create the virtual machine from an image and boot it from a volume.

.. code-block:: console

   openstack server create \
     --flavor "$FLAVOR_NAME" \
     --image "$IMAGE_ID" \
     --boot-from-volume "$BOOT_VOLUME_SIZE" \
     --network "$NETWORK_ID" \
     --key-name "$KEY_NAME" \
     --security-group "$SECURITY_GROUP" \
     "$SERVER_NAME"

Wait until the virtual machine becomes **ACTIVE**.

.. code-block:: console

   openstack server list

Example output:

.. code-block:: text

   +--------------------------------------+------------+--------+-------------------------------------------------+--------------------------+-------------+
   | ID                                   | Name       | Status | Networks                                        | Image                    | Flavor      |
   +--------------------------------------+------------+--------+-------------------------------------------------+--------------------------+-------------+
   | 1c344527-d2a5-4a10-906c-1bbf8878551f | vm-john-01 | ACTIVE | cf_cloud_mvp_dev_ecis_r1_with_sfs=192.168.168.2 | N/A (booted from volume) | 4cpu-4gbmem |
   |                                      |            |        | 40; sfs_network_638f4089d6ad470aaaeb70268529701 |                          |             |
   |                                      |            |        | 2=10.84.16.37                                   |                          |             |
   +--------------------------------------+------------+--------+-------------------------------------------------+--------------------------+-------------+

The **Image** column shows **N/A (booted from volume)**. This means that the virtual machine uses a Cinder volume as its root disk.


Why server backup is not used
-----------------------------

The **openstack server backup create** command is not supported for volume-backed instances.

If you try to use it for this type of virtual machine, the command fails.

.. code-block:: console

   openstack server backup create \
     --name backup-01 \
     1c344527-d2a5-4a10-906c-1bbf8878551f

Example output:

.. code-block:: text

   BadRequestException: 400: Client Error for url: https://nova.api.r1.cloud.eumetsat.int/v2.1/servers/1c344527-d2a5-4a10-906c-1bbf8878551f/action, Backup is not supported for volume-backed instances.

For a volume-backed virtual machine, use the boot volume workflow described in the following sections.


Find the boot volume
--------------------

Show the volumes attached to the virtual machine.

.. code-block:: console

   openstack server show "$SERVER_NAME" \
     -c volumes_attached \
     -f yaml

Example output:

.. code-block:: yaml

   volumes_attached:
   - delete_on_termination: false
     id: 4ee0a54d-3742-48e6-a665-43028f27462f

Save the boot volume ID in a variable.

.. code-block:: console

   BOOT_VOLUME_ID=4ee0a54d-3742-48e6-a665-43028f27462f

Check the boot volume.

.. code-block:: console

   openstack volume show "$BOOT_VOLUME_ID"


Create a snapshot of the boot volume
------------------------------------

Create a snapshot of the boot volume.

.. code-block:: console

   openstack volume snapshot create \
     --force \
     --volume "$BOOT_VOLUME_ID" \
     "$SNAPSHOT_NAME"

Example output:

.. code-block:: text

   +-------------+--------------------------------------+
   | Field       | Value                                |
   +-------------+--------------------------------------+
   | created_at  | 2026-05-29T21:17:52.306655           |
   | description | None                                 |
   | id          | d092e03d-6b97-4ba0-ad07-4a6d239ca55a |
   | name        | backup-01-snapshot                   |
   | properties  |                                      |
   | size        | 5                                    |
   | status      | creating                             |
   | updated_at  | None                                 |
   | volume_id   | 4ee0a54d-3742-48e6-a665-43028f27462f |
   +-------------+--------------------------------------+

Check the snapshot status.

.. code-block:: console

   openstack volume snapshot list

Example output:

.. code-block:: text

   +--------------------------------------+--------------------+-------------+-----------+------+
   | ID                                   | Name               | Description | Status    | Size |
   +--------------------------------------+--------------------+-------------+-----------+------+
   | d092e03d-6b97-4ba0-ad07-4a6d239ca55a | backup-01-snapshot | None        | available |    5 |
   +--------------------------------------+--------------------+-------------+-----------+------+

Continue only after the snapshot status becomes **available**.


Create a temporary volume from the snapshot
-------------------------------------------

Create a temporary volume from the snapshot.

.. code-block:: console

   openstack volume create \
     --snapshot "$SNAPSHOT_NAME" \
     "$TEMP_VOLUME_NAME"

Check the temporary volume status.

.. code-block:: console

   openstack volume show "$TEMP_VOLUME_NAME" \
     -c status \
     -f value

Continue only after the temporary volume status becomes **available**.


Upload the temporary volume to the Image service
------------------------------------------------

Upload the temporary volume to the OpenStack Image service.

.. code-block:: console

   openstack image create \
     --volume "$TEMP_VOLUME_NAME" \
     "$IMAGE_NAME"

Check the image status.

.. code-block:: console

   openstack image show "$IMAGE_NAME" \
     -c status \
     -f value

Continue only after the image status becomes **active**.


Download the image to your desktop
----------------------------------

Download the image file to your current working directory.

.. code-block:: console

   openstack image save \
     --file "$DOWNLOAD_FILE" \
     "$IMAGE_NAME"

Check that the file was downloaded.

.. code-block:: console

   ls -lh "$DOWNLOAD_FILE"


Clean up temporary resources
----------------------------

After downloading the image, remove the temporary OpenStack resources that you no longer need.

Delete the temporary image.

.. code-block:: console

   openstack image delete "$IMAGE_NAME"

Delete the temporary volume.

.. code-block:: console

   openstack volume delete "$TEMP_VOLUME_NAME"

Keep the snapshot if you still need it. To delete it, run:

.. code-block:: console

   openstack volume snapshot delete "$SNAPSHOT_NAME"