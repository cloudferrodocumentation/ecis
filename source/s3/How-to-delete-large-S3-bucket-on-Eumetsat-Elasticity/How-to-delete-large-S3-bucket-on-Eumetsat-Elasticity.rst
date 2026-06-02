How to delete a large S3 bucket on |brand-name|
===============================================

Introduction
------------

In some cases, deleting a large object storage bucket through OpenStack CLI may
fail. This can happen when the bucket contains a large number of objects.

For example, removing a bucket with more than 10 000 objects may fail when
using the following command:

.. code-block:: bash

   openstack container delete --recursive <bucket_name>

The command may return an error similar to this:

.. code-block:: text

   Conflict (HTTP 409) (Request-ID: tx00000000000001bb5e8e5-006135c488-35bc5d520-dias_default) clean_up DeleteContainer: Conflict (HTTP 409) (Request-ID:)

The recommended solution is to use **s3cmd** and remove the bucket
recursively through the S3 interface.

Prerequisites
-------------

No. 1 **Generated  credentials**

You need S3 credentials for accessing object storage through S3-compatible
tools.

.. jinja:: doc_links

   :doc:`{{ ec2_credentials }}`

No. 2 **s3cmd configured for object storage**

You also need **s3cmd** configured for access to your object storage buckets.

.. jinja:: doc_links

   :doc:`{{ s3cmd_access }}`

After **s3cmd** is configured, you should be able to list and access your
object storage buckets.

List buckets
------------

Start by listing buckets visible to your credentials:

.. code-block:: bash

   s3cmd ls

If your **s3cmd** configuration is stored in a custom file, use the **-c**
option. For example:

.. code-block:: bash

   s3cmd -c /home/eouser/storage-access ls

The output should list the buckets available to your credentials. For example:

.. code-block:: text

   2022-02-02 22:22  s3://large-bucket

Choose the bucket that you want to remove.

Delete the bucket recursively
-----------------------------

To delete a large bucket and all objects inside it, use **s3cmd rb** with the
**-r** option.

The **-r** option means recursive removal.

.. important::

   This is a destructive operation. The bucket and all objects inside it will
   be removed. Make sure that you selected the correct bucket before running
   the command.

Run the following command, replacing **large-bucket** with the name of your
bucket:

.. code-block:: bash

   s3cmd rb -r s3://large-bucket

If your **s3cmd** configuration is stored in a custom file, use:

.. code-block:: bash

   s3cmd -c /home/eouser/storage-access rb -r s3://large-bucket

The command removes all objects from the bucket first, and then removes the
bucket itself.

Example output:

.. code-block:: text

   WARNING: Bucket is not empty. Removing all the objects from it first. This may take some time...
   delete: 's3://large-bucket/example_file.jpg'
   delete: 's3://large-bucket/example_file.txt'
   delete: 's3://large-bucket/example_file.png'
   ...
   ...
   ...
   Bucket 's3://large-bucket/' removed

Verify that the bucket was removed
----------------------------------

After the command finishes, list buckets again:

.. code-block:: bash

   s3cmd ls

Or, if you use a custom configuration file:

.. code-block:: bash

   s3cmd -c /home/eouser/storage-access ls

If the removed bucket was the only bucket available to your credentials, the
output should be empty:

.. code-block:: text

   eouser@vm01:$ s3cmd ls
   eouser@vm01:$

If other buckets exist, they will still be listed.

Troubleshooting
---------------

**Bucket does not exist**

If the bucket name is wrong or the bucket is not visible to your credentials,
the command may fail. List your buckets again and verify the exact bucket name:

.. code-block:: bash

   s3cmd ls

**Access denied**

If your S3 credentials do not have permission to remove the bucket or objects
inside it, the command may fail with an access-related error. In that case,
use credentials with the required permissions or ask the project administrator
to remove the bucket.

**The operation takes a long time**

Recursive deletion of a large bucket may take some time because **s3cmd** has
to remove the objects first. Wait for the command to finish before checking
the result.

What to do next
---------------

You can continue working with object storage by creating or using another
bucket.

.. jinja:: doc_links

   :doc:`{{ s3cmd_access }}`