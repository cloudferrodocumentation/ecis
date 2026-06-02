Deep dive into using s3cmd to access object storage
===================================================

Object storage can be used to store your files in *containers*. In this article, you will create a basic object storage container and perform common object storage operations with **s3cmd**.

.. raw:: html

   <h2>What we are going to cover</h2>

* Creating a new object storage container
* Uploading files
* Listing files and folder-like prefixes
* Deleting files from a container
* Removing storage containers
* Enabling or disabling public access to object storage containers
* Testing public access from the command line

Prerequisites
-------------

Before starting, make sure that:

1. You have an admin hosting account with access to the EUMETSAT cloud interface:

   `my.cloud.eumetsat.int <http://my.cloud.eumetsat.int>`__

2. You can sign in to the portal and open the service catalog. For more information, see :doc:`/accountmanagement/Service-catalog/Service-catalog`

3. You have S3 API keys for Object Storage.

   To create and manage S3 keys, see:

   :doc:`/accountmanagement/S3-keys/S3-keys`

4. You have access to a virtual machine or local terminal.

   You can create a Linux virtual machine by following one of these articles:

   .. jinja:: brand_names

      * :doc:`/cloud/How-to-create-a-Linux-VM-and-access-it-from-Windows-desktop-on-{{ brand_name_hyphen }}/How-to-create-a-Linux-VM-and-access-it-from-Windows-desktop-on-{{ brand_name_hyphen }}`
      * :doc:`/cloud/How-to-create-a-Linux-VM-and-access-it-from-Linux-command-line-on-{{ brand_name_hyphen }}/How-to-create-a-Linux-VM-and-access-it-from-Linux-command-line-on-{{ brand_name_hyphen }}`

5. **s3cmd** is installed and configured for the Object Storage endpoint of the region where you want to work.

   For configuration instructions, see:

   .. jinja:: brand_names

      * :doc:`/s3/How-to-install-s3cmd-on-Linux-on-{{ brand_name_hyphen }}/How-to-install-s3cmd-on-Linux-on-{{ brand_name_hyphen }}`
      * :doc:`/s3/Configuration-files-for-s3cmd-command-on-{{ brand_name_hyphen }}/Configuration-files-for-s3cmd-command-on-{{ brand_name_hyphen }}`
      * :doc:`/s3/How-to-access-object-storage-from-{{ brand_name_hyphen }}-using-s3cmd/How-to-access-object-storage-from-{{ brand_name_hyphen }}-using-s3cmd`

6. To test public object download from the terminal, you can use **wget** which comes preinstalled on most modern operating systems.

   The article uses **wget** only in the section about public object storage containers.

7. You have a test file available in your working directory, for example **file.txt**.

   The upload examples in this article use **file.txt**, **file2.txt**, and **folder-to-upload** as sample local files and directories.

8. You have permission to create, modify, and delete object storage containers.

9. The bucket names used in this article are examples.

   Replace names such as **example-bucket**, **example-default-placement-bucket**, and **example-cold-placement-bucket** with unique bucket names in your own environment.

Creating a new object storage container
---------------------------------------

To create a new storage container, you need an S3 client. In this example, you will use **s3cmd**.

To create a new S3 bucket, use the following command:

.. code-block:: bash

   s3cmd mb s3://example-bucket

The result is:

.. code-block:: bash

   Bucket 's3://example-bucket/' created

While creating the bucket, you can use the **--region** argument to specify where it should be stored. Currently, there are two available placements:

:default-placement:
   Default storage space with replicated storage backend.

:cold-placement:
   Slower, more space-efficient erasure-coded storage backend.

The colon before the placement name is **required**.

To create a bucket in the default placement, use:

.. code-block:: bash

   s3cmd mb s3://example-default-placement-bucket --region=':default-placement'

The result is:

.. code-block:: bash

   Bucket 's3://example-default-placement-bucket/' created

For cold placement, use:

.. code-block:: bash

   s3cmd mb s3://example-cold-placement-bucket --region=':cold-placement'

The result is:

.. code-block:: bash

   Bucket 's3://example-cold-placement-bucket/' created

.. warning::

   Bucket names must be unique.

   Bucket names cannot be formatted as IP addresses.

   Bucket names can be between 3 and 63 characters long.

   Bucket names must not contain uppercase characters or underscores.

   Bucket names must start with a lowercase letter or number.

   Bucket names must be a series of one or more labels. Adjacent labels are separated by a single period (**.**). Bucket names can contain lowercase letters, numbers, and hyphens. Each label must start and end with a lowercase letter or a number.

   Bucket names cannot contain forward slashes (**/**).

In this cloud environment, **single tenancy** is enabled. This means that two object storage containers cannot have the same name. Avoid common names such as **storage** or **files**.

Uploading a file
----------------

To upload a file to a storage bucket, use **s3cmd put**:

.. code-block:: bash

   s3cmd put file.txt s3://example-bucket/

The result is:

.. code-block:: bash

   upload: 'file.txt' -> 's3://example-bucket/file.txt'  [1 of 1]
    0 of 0     0% in    0s     0.00 B/s  done

To verify that the file was uploaded, list the contents of the bucket:

.. code-block:: bash

   s3cmd ls s3://example-bucket/

The result is:

.. code-block:: bash

   2026-04-24 14:51            0  s3://example-bucket/file.txt

This uploads the file to the root of the bucket.

Uploading a file into a prefix
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Object Storage does not use real folders. Folder-like paths are prefixes in object names.

To upload a file into a specific prefix, include the prefix in the object path:

.. code-block:: bash

   s3cmd put file.txt s3://example-bucket/directory1/directory1/

The result is:

.. code-block:: bash

   upload: 'file.txt' -> 's3://example-bucket/directory1/directory1/file.txt'  [1 of 1]
    0 of 0     0% in    0s     0.00 B/s  done

List the root of the bucket:

.. code-block:: bash

   s3cmd ls s3://example-bucket/

The result is:

.. code-block:: bash

                             DIR  s3://example-bucket/directory1/
   2026-04-24 14:51            0  s3://example-bucket/file.txt

List the contents of the prefix:

.. code-block:: bash

   s3cmd ls s3://example-bucket/directory1/directory1/

The result is:

.. code-block:: bash

   2026-04-24 14:53            0  s3://example-bucket/directory1/directory1/file.txt

Uploading multiple files
^^^^^^^^^^^^^^^^^^^^^^^^

You can upload multiple files at once:

.. code-block:: bash

   s3cmd put file.txt file2.txt s3://example-bucket/multiple-file-upload/

The result is:

.. code-block:: bash

   upload: 'file.txt' -> 's3://example-bucket/multiple-file-upload/file.txt'  [1 of 2]
    0 of 0     0% in    0s     0.00 B/s  done
   upload: 'file2.txt' -> 's3://example-bucket/multiple-file-upload/file2.txt'  [2 of 2]
    0 of 0     0% in    0s     0.00 B/s  done

To verify the upload, use:

.. code-block:: bash

   s3cmd ls s3://example-bucket/multiple-file-upload/

The result is:

.. code-block:: bash

   2026-04-24 14:54            0  s3://example-bucket/multiple-file-upload/file.txt
   2026-04-24 14:54            0  s3://example-bucket/multiple-file-upload/file2.txt

Uploading a directory recursively
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To upload an entire directory recursively, use **--recursive**:

.. code-block:: bash

   s3cmd put --recursive folder-to-upload s3://example-bucket/

The result is:

.. code-block:: bash

   upload: 'folder-to-upload/file.txt' -> 's3://example-bucket/folder-to-upload/file.txt'  [1 of 2]
    0 of 0     0% in    0s     0.00 B/s  done
   upload: 'folder-to-upload/file2.txt' -> 's3://example-bucket/folder-to-upload/file2.txt'  [2 of 2]
    0 of 0     0% in    0s     0.00 B/s  done

To verify the upload, use:

.. code-block:: bash

   s3cmd ls s3://example-bucket/folder-to-upload/

The result is:

.. code-block:: bash

   2026-04-24 14:56            0  s3://example-bucket/folder-to-upload/file.txt
   2026-04-24 14:56            0  s3://example-bucket/folder-to-upload/file2.txt

Deleting files from a container
-------------------------------

To delete a single file from a bucket, use:

.. code-block:: bash

   s3cmd del s3://example-bucket/file.txt

The result is:

.. code-block:: bash

   delete: 's3://example-bucket/file.txt'

To delete multiple files, specify them one by one:

.. code-block:: bash

   s3cmd del s3://example-bucket/multiple-file-upload/file.txt s3://example-bucket/multiple-file-upload/file2.txt

The result is:

.. code-block:: bash

   delete: 's3://example-bucket/multiple-file-upload/file.txt'
   delete: 's3://example-bucket/multiple-file-upload/file2.txt'

Deleting folders (prefixes)
^^^^^^^^^^^^^^^^^^^^^^^^^^^

As Object Storage does not support real folders, folder-like paths are prefixes in object names.

To delete a prefix and all objects under it, use **--recursive**:

.. code-block:: bash

   s3cmd del --recursive s3://example-bucket/folder-to-upload/

The result is:

.. code-block:: bash

   delete: 's3://example-bucket/folder-to-upload/file.txt'
   delete: 's3://example-bucket/folder-to-upload/file2.txt'

This removes all objects that start with the specified prefix.

Important notes
^^^^^^^^^^^^^^^

* Deletions are permanent and cannot be undone.
* Make sure you are targeting the correct bucket and prefix before using **--recursive**.

Removing storage containers
---------------------------

To remove an empty container, use **s3cmd rb**:

.. code-block:: bash

   s3cmd rb s3://example-cold-placement-bucket

The result is:

.. code-block:: bash

   Bucket 's3://example-cold-placement-bucket/' removed

The bucket must be empty before it can be removed.

If you try to remove a bucket that still contains objects, the command fails:

.. code-block:: bash

   s3cmd rb s3://example-bucket

The result is:

.. code-block:: bash

   ERROR: S3 error: 409 (BucketNotEmpty)

If the bucket contains data, you can remove the bucket together with all objects by using **--recursive**:

.. code-block:: bash

   s3cmd rb --recursive s3://example-bucket

The result is:

.. code-block:: bash

   WARNING: Bucket is not empty. Removing all the objects from it first. This may take some time...
   delete: 's3://example-bucket/directory1/directory1/file.txt'
   Bucket 's3://example-bucket/' removed

Use this option with caution, as it permanently deletes all data stored in the bucket.

Recommended number of files in your object storage containers
-------------------------------------------------------------

It is recommended that you do not have more than 1 000 000 (one million) files and folders in one object storage container, as listing them may become inefficient.

If you want to store a large number of files, use multiple object storage containers.

Working with public object storage containers
---------------------------------------------

Enabling or disabling public access to object storage containers
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

By default, object storage containers are **private**.

If you want to change access permissions after the container has been created, you can modify its ACL (Access Control List) using **s3cmd**.

To make a single object public, use:

.. code-block:: bash

   s3cmd setacl s3://example-bucket/folder-to-upload/file2.txt --acl-public

To make all objects under a prefix public, use **--recursive**:

.. code-block:: bash

   s3cmd setacl --recursive s3://example-bucket/folder-to-upload/ --acl-public

The result is:

.. code-block:: bash

   s3://example-bucket/folder-to-upload/file.txt: ACL set to Public  [1 of 2]
   s3://example-bucket/folder-to-upload/file2.txt: ACL set to Public  [2 of 2]

You can also change the ACL of the bucket itself:

.. code-block:: bash

   s3cmd setacl s3://example-bucket --acl-public

Use this option carefully. In most cases, it is safer to make only the required object or prefix public.

Object Storage endpoint depends on the region where the bucket was created. Use the endpoint that belongs to your region when creating public object URLs.

.. tabs::

   .. tab:: R1

      .. code-block:: text

         https://s3.r1.cloud.eumetsat.int

   .. tab:: R2

      .. code-block:: text

         https://s3.r2.cloud.eumetsat.int

   .. tab:: FRA1-3

      .. code-block:: text

         https://s3.fra1-3.cloudferro.com

Testing public access from the command line
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

After you make an object public, you do not need to open it in a browser. You can verify access directly from the command line.

First, list the objects in the bucket with **s3cmd**:

.. code-block:: bash

   s3cmd ls s3://example-bucket/

The result should show the objects stored in the bucket, for example:

.. code-block:: bash

   2026-04-24 14:51            0  s3://example-bucket/file.txt
                             DIR  s3://example-bucket/folder-to-upload/

To list objects inside a folder-like prefix, add the prefix to the path:

.. code-block:: bash

   s3cmd ls s3://example-bucket/folder-to-upload/

The result should show the objects under that prefix:

.. code-block:: bash

   2026-04-24 14:56            0  s3://example-bucket/folder-to-upload/file.txt
   2026-04-24 14:56            0  s3://example-bucket/folder-to-upload/file2.txt

The public URL of an object consists of the Object Storage endpoint, the bucket name, and the full object path.

For example, this object:

.. code-block:: text

   s3://example-bucket/folder-to-upload/file2.txt

can be accessed through the following public URL in the FRA1-3 region:

.. code-block:: text

   https://s3.fra1-3.cloudferro.com/example-bucket/folder-to-upload/file2.txt

Use the endpoint that belongs to the region where your bucket was created.

.. tabs::

   .. tab:: R1

      .. code-block:: bash

         wget https://s3.r1.cloud.eumetsat.int/example-bucket/folder-to-upload/file2.txt

   .. tab:: R2

      .. code-block:: bash

         wget https://s3.r2.cloud.eumetsat.int/example-bucket/folder-to-upload/file2.txt

   .. tab:: FRA1-3

      .. code-block:: bash

         wget https://s3.fra1-3.cloudferro.com/example-bucket/folder-to-upload/file2.txt

Example output:

.. code-block:: bash

   --2026-04-24 17:47:44--  https://s3.fra1-3.cloudferro.com/example-bucket/folder-to-upload/file2.txt
   Resolving s3.fra1-3.cloudferro.com (s3.fra1-3.cloudferro.com)... 74.63.12.97, 2a01:9aa0:45:1::100
   Connecting to s3.fra1-3.cloudferro.com (s3.fra1-3.cloudferro.com)|74.63.12.97|:443... connected.
   HTTP request sent, awaiting response... 200 OK
   Length: 0 [inode/x-empty]
   Saving to: 'file2.txt'

   file2.txt                 [ <=>                           ]       0  --.-KB/s    in 0s

   2026-04-24 17:47:44 (0.00 B/s) - 'file2.txt' saved [0/0]

You can also save the downloaded object under a different local file name:

.. code-block:: bash

   wget -O downloaded-file2.txt https://s3.fra1-3.cloudferro.com/example-bucket/folder-to-upload/file2.txt

If the object is not public, the download will fail with an access error, for example:

.. code-block:: bash

   ERROR 403: Forbidden.

In that case, check whether you made the correct object or prefix public:

.. code-block:: bash

   s3cmd info s3://example-bucket/folder-to-upload/file2.txt

To make the object public, use:

.. code-block:: bash

   s3cmd setacl s3://example-bucket/folder-to-upload/file2.txt --acl-public

To make all objects under a prefix public, use:

.. code-block:: bash

   s3cmd setacl --recursive s3://example-bucket/folder-to-upload/ --acl-public

To remove public access from one object again, use:

.. code-block:: bash

   s3cmd setacl s3://example-bucket/folder-to-upload/file2.txt --acl-private

To remove public access from all objects under a prefix, use:

.. code-block:: bash

   s3cmd setacl --recursive s3://example-bucket/folder-to-upload/ --acl-private

If you changed the ACL of the bucket itself, make the bucket private again with:

.. code-block:: bash

   s3cmd setacl s3://example-bucket --acl-private

.. note::

   Object Storage does not use real folders. Folder-like paths are prefixes in object names.

   You can download individual objects, but you cannot download a folder by adding a folder path to the public URL.

.. warning::

   Public access should be enabled only for objects that are intended to be shared.

   If you make a whole bucket or prefix public, other users may be able to access all public objects under that bucket or prefix if they know or can construct the object URLs.

What To Do Next
---------------

Now that you have created your object storage container, you can mount it on the platform of your choice for easier access. There are many ways to do that, for instance:

.. jinja:: brand_names

   * :doc:`/s3/How-to-mount-object-storage-container-as-a-file-system-in-Linux-using-s3fs-on-{{ brand_name_hyphen }}/How-to-mount-object-storage-container-as-a-file-system-in-Linux-using-s3fs-on-{{ brand_name_hyphen }}`

   * :doc:`/s3/How-to-mount-object-storage-container-from-{{ brand_name_hyphen }}-as-file-system-on-local-Windows-computer/How-to-mount-object-storage-container-from-{{ brand_name_hyphen }}-as-file-system-on-local-Windows-computer`
