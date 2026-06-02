How to access object storage from |brand-name| using s3cmd
==========================================================

In this article, you will learn how to access object storage from |brand-name|
on Linux using `s3cmd <https://github.com/s3tools/s3cmd>`_, without mounting
it as a file system.

You can run these commands on a virtual machine hosted on |brand-name| cloud or
on a local Linux computer.

What we are going to cover
--------------------------

* Object storage and standard file systems
* Terminology: containers and buckets
* Configuring **s3cmd**
* S3 paths in **s3cmd**
* Listing buckets
* Choosing a bucket for the examples
* Creating a bucket, if needed
* Uploading a file to a bucket
* Listing files and directories in a bucket
* Removing a file from a bucket
* Downloading a file from a bucket
* Checking how much storage is used by a bucket
* Removing a bucket

Prerequisites
-------------

No. 1 **Account**

You need a |brand-name| hosting account with access to the Horizon interface:
|brand-name-site-link|.

No. 2 **Generated S3 credentials**

You need to generate S3 credentials.

.. jinja:: doc_links

   :doc:`{{ ec2_credentials }}`

No. 3 **A Linux computer or virtual machine**

You need a Linux virtual machine or a local Linux computer. This article was
written for Ubuntu 22.04. Other operating systems might work, but are out of
scope of this article and might require you to adjust the commands.

If you want to use a virtual machine hosted on |brand-name| cloud and you do
not have one yet, one of these articles can help:

.. jinja:: doc_links

   * :doc:`{{ linux_vm_from_windows }}`
   * :doc:`{{ linux_vm_from_linux }}`

No. 4 **s3cmd installed**

You need to have **s3cmd** installed on your virtual machine or local computer.

.. jinja:: doc_links

   :doc:`{{ s3cmd_install }}`

No. 5 **Understanding how s3cmd handles its configuration file**

**s3cmd** stores connection data in configuration files. One configuration file
can describe one connection. You need to decide where you want to keep the
connection data for object storage.

.. jinja:: doc_links

   :doc:`{{ s3cmd_config }}`

Object storage and standard file systems
----------------------------------------

Object storage uses objects, not files and folders in the conventional file
system sense. To make navigation easier, the Horizon dashboard presents objects
as files and folders in **Object Store** -> **Containers**.

This representation is convenient, but object storage behaves differently from
a standard file system.

For example, in a conventional file system, you usually cannot have a file and
a folder with the same name in the same location. In object storage, however,
one path can contain both an object named **something/** and an object named
**something**. Horizon may show the first one as a folder named **something**
and the second one as a downloadable file named **something**.

Terminology: containers and buckets
-----------------------------------

There are two object storage interfaces:

* **Swift / Horizon** -- the Horizon dashboard uses the Swift API, where the
  top-level namespaces are called **containers**.

* **S3 / s3cmd** -- the S3-compatible endpoint, used by **s3cmd** and other S3
  tools, uses **buckets** as the top-level namespaces.

In this article, we use **bucket** when describing commands issued with
**s3cmd**. If you are comparing the result with Horizon, the corresponding
top-level item may be shown as a **container**.

Configuring s3cmd
-----------------

Throughout this article, we use file **/home/eouser/storage-access** as an
example **s3cmd** configuration file. You can use another file name or another
location if needed.

Start the configuration process:

.. code-block:: bash

   s3cmd -c /home/eouser/storage-access --configure

A series of questions appears. Replace **access_key** and **secret_key** with
the access and secret keys obtained in Prerequisite No. 2.

When asked for endpoint and region values, use the tab for the cloud region
you are working with.

.. jinja:: regional_clouds

   .. tabs::

      {% for region in regions %}
      .. tab:: {{ region.display_name }}

         .. code-block:: text

            New settings:
            Access Key: access_key
            Secret Key: secret_key
            Default Region: {{ region.s3cmd_region }}
            S3 Endpoint: {{ region.s3_host }}
            DNS-style bucket+hostname:port template for accessing a bucket: %(bucket)s.{{ region.s3_host }}
            Encryption password:
            Path to GPG program: /usr/bin/gpg
            Use HTTPS protocol: Yes
            HTTP Proxy server name:
            HTTP Proxy server port: 0

      {% endfor %}

When **s3cmd** asks whether to test access with the supplied credentials, answer
with **Y** and press **Enter**:

.. code-block:: text

   Test access with supplied credentials? [Y/n]

Wait until testing is completed. It should take no more than a couple of
seconds. If the process is successful, you should get output similar to this:

.. code-block:: text

   Please wait, attempting to list all buckets...
   Success. Your access key and secret key worked fine :-)

   Now verifying that encryption works...
   Success. Encryption and decryption worked fine :-)

   Save settings? [y/N]

Answer with **Y** and press **Enter**.

You should get a confirmation similar to this:

.. code-block:: text

   Configuration saved to '/home/eouser/storage-access'

You are now ready to use **s3cmd** with this configuration file.

S3 paths in s3cmd
-----------------

When accessing object storage with **s3cmd**, paths start with **s3://**,
followed by the bucket name and, optionally, an object path.

For example, what Horizon may show as a file named **my-file.txt** in a folder
named **my-folder** in a container named **my-container** is referred to by
**s3cmd** as:

.. code-block:: text

   s3://my-container/my-folder/my-file.txt

Listing buckets
---------------

Start by listing buckets visible to your S3 credentials. This tells you
whether you already have a bucket that can be used in the remaining examples.

To list your buckets, execute:

.. code-block:: bash

   s3cmd -c /home/eouser/storage-access ls

If you do not have any buckets, the output of the command should be empty.

If you have buckets, you should get their list. For example:

.. code-block:: text

   2026-04-30 12:03  s3://cf-s3-test
   2026-04-30 12:53  s3://cf-s3-test-1

.. note::

   If the output already shows a bucket that you can use, use that bucket in
   the remaining examples. In the commands below, replace example bucket names
   such as **my-bucket** or **my-files** with the bucket returned by this
   command.

   In some environments, a project may have no more than two S3 buckets at the
   same time. If the bucket quota is already full, creating another bucket will
   fail.

Choosing a bucket for the examples
----------------------------------

Before running the remaining examples, choose which bucket you will use.

You have two options:

* use an existing bucket returned by the **Listing buckets** example, or
* create a new bucket, if your project bucket quota allows it.

In the commands below, replace example bucket names such as **my-bucket**,
**my-files**, or **cf-s3-test** with the bucket name you selected.

.. important::

   A project may have a strict bucket quota. In some environments, no more
   than two S3 buckets may exist at the same time. If your project already has
   the maximum number of buckets, bucket creation will fail even when your
   credentials and endpoint are correct.

Creating a bucket, if needed
----------------------------

Create a new bucket only if you do not already have a suitable bucket and your
project bucket quota allows another bucket to be created.

To create a bucket, execute the command below. Replace **my-bucket** with the
name you want to use for your bucket.

.. code-block:: bash

   s3cmd -c /home/eouser/storage-access mb s3://my-bucket

If the process is successful, you should get output similar to this:

.. code-block:: text

   Bucket 's3://my-bucket/' created

Your bucket should now be visible after using the **s3cmd ls** command:

.. code-block:: bash

   s3cmd -c /home/eouser/storage-access ls

Troubleshooting creating a bucket
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Bucket already exists**

If you receive output similar to this:

.. code-block:: text

   ERROR: Bucket 'my-bucket' already exists
   ERROR: S3 error: 409 (BucketAlreadyExists)

choose a different bucket name and try again.

**Too many buckets**

If bucket creation fails because the bucket quota has been reached, the error
message may indicate that too many buckets already exist in the project.

In some environments, no more than two S3 buckets may exist at the same time.

To continue with the examples, use one of the buckets returned by the
**Listing buckets** example, remove an unused bucket, or contact support to ask
whether the bucket quota can be increased.

**Using unsupported characters in bucket name**

If you attempt to create a bucket with unsupported characters in its name, you
should get output similar to this:

.. code-block:: text

   ERROR: Parameter problem: Bucket name 'my_bucket' contains disallowed character '_'. The only supported ones are: lowercase us-ascii letters (a-z), digits (0-9), dot (.) and hyphen (-).

In this case, use only supported characters.

Uploading a file to a bucket
----------------------------

To upload a file into a bucket, use **s3cmd put**.

Replace **/home/eouser/my-file.txt** with the file you want to upload. Replace
**cf-s3-test/my-directory** with the bucket and path where you want to upload
the file.

.. code-block:: bash

   s3cmd -c /home/eouser/storage-access put /home/eouser/my-file.txt s3://cf-s3-test/my-directory/

Finish the destination path with a slash if you want to upload the file into a
directory-like prefix. If you skip the slash, the object may be uploaded under
a different object key than you expected.

To upload a file directly to the root of the bucket, use only the bucket name
as the destination path:

.. code-block:: bash

   s3cmd -c /home/eouser/storage-access put /home/eouser/my-file.txt s3://cf-s3-test/

The output should show the upload process. Once it is successful, you should
be returned to the command prompt.

Listing files and folders in the root of a bucket
-------------------------------------------------

To list files and folders in the root of a bucket, execute **s3cmd ls** on the
bucket path preceded by **s3://**.

For example, to list the content of bucket **cf-s3-test**, execute:

.. code-block:: bash

   s3cmd -c /home/eouser/storage-access ls s3://cf-s3-test

The following command, ending with a slash, should also work:

.. code-block:: bash

   s3cmd -c /home/eouser/storage-access ls s3://cf-s3-test/

Assume that the location contains a directory-like prefix named
**some-directory** and a file named **text-file.txt**. In this case, the output
can look like this:

.. code-block:: text

                             DIR  s3://cf-s3-test/some-directory/
   2026-04-30 14:39           10  s3://cf-s3-test/text-file.txt

Listing files and folders below a prefix
----------------------------------------

To list files inside what Horizon shows as folders, use the full path separated
by slashes. End the path with a slash.

For example, to list the content of **some-directory/some-other-directory/**
inside bucket **cf-s3-test**, execute:

.. code-block:: bash

   s3cmd -c /home/eouser/storage-access ls s3://cf-s3-test/some-directory/some-other-directory/

The output should contain the list of objects located there. For example:

.. code-block:: text

   2026-04-30 14:30            0  s3://cf-s3-test/some-directory/some-other-directory/
   2026-04-30 14:32           19  s3://cf-s3-test/some-directory/some-other-directory/some-other-file.txt
   2026-04-30 14:31           19  s3://cf-s3-test/some-directory/some-other-directory/yet-another-file.txt

Ending paths with slash while using s3cmd ls
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

When listing the contents of directory-like prefixes with **s3cmd ls**, finish
the path with a slash.

For example, list files under **some-directory/** in bucket **cf-s3-test** like
this:

.. code-block:: bash

   s3cmd -c /home/eouser/storage-access ls s3://cf-s3-test/some-directory/

In this case, the output should be correct:

.. code-block:: text

                             DIR  s3://cf-s3-test/some-directory/some-other-directory/
   2026-04-30 14:25            0  s3://cf-s3-test/some-directory/
   2026-04-30 14:27           15  s3://cf-s3-test/some-directory/another-file.txt
   2026-04-30 14:28           23  s3://cf-s3-test/some-directory/first-file.txt

If you omit the slash at the end:

.. code-block:: bash

   s3cmd -c /home/eouser/storage-access ls s3://cf-s3-test/some-directory

your output may only contain the same path with a slash added at the end:

.. code-block:: text

                             DIR  s3://cf-s3-test/some-directory/

Removing a file from a bucket
-----------------------------

To delete a file from a bucket, execute **s3cmd rm** with the path of the file
you want to remove.

Example:

.. code-block:: bash

   s3cmd -c /home/eouser/storage-access rm s3://cf-s3-test/my-folder/my-file.txt

You should get a confirmation similar to this:

.. code-block:: text

   delete: 's3://cf-s3-test/my-folder/my-file.txt'

Downloading a file from a bucket
--------------------------------

To download a file from a bucket to your local computer, execute **s3cmd get**
with the full path to the object you want to download.

Example:

.. code-block:: bash

   s3cmd -c /home/eouser/storage-access get s3://cf-s3-test/my-folder/my-file.txt

The download process to the current working directory should begin.

Troubleshooting downloading a file
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If the file already exists in the current working directory, you should get
output similar to this:

.. code-block:: text

   ERROR: Parameter problem: File ./my-file.txt already exists. Use either of --force / --continue / --skip-existing or give it a new name.

If you use **--force**, the file detected by **s3cmd** will be overwritten.

The **\-\-continue** parameter can be used to resume an interrupted download.

If you want to save the downloaded file under another name, put the new name
after the S3 path, separated by a space:

.. code-block:: bash

   s3cmd -c /home/eouser/storage-access get s3://cf-s3-test/my-folder/my-file.txt another-name.txt

Checking how much storage is used by a bucket
---------------------------------------------

To check how much space is used by a particular path, use **s3cmd du**.

If you want human-readable values, use the **-H** parameter.

Example:

.. code-block:: bash

   s3cmd -c /home/eouser/storage-access du -H s3://cf-s3-test

The output should look similar to this:

.. code-block:: text

   318M       2 objects s3://cf-s3-test/

Removing a bucket
-----------------

You can use **s3cmd** to delete a bucket. The bucket must be empty before it
can be removed.

.. important::

   Remove a bucket only when you are sure that it is no longer needed. This is
   a destructive operation.

Execute **s3cmd rb**, followed by the bucket path. For example, to remove
bucket **cf-s3-test**, execute:

.. code-block:: bash

   s3cmd -c /home/eouser/storage-access rb s3://cf-s3-test

If the process is successful, you should get confirmation similar to this:

.. code-block:: text

   Bucket 's3://cf-s3-test/' removed

What to do next
---------------

You can use **s3cmd** to share your bucket outside of your project by applying
a sharing policy.

.. jinja:: doc_links

   :doc:`{{ bucket_policy }}`

.. ifconfig:: brand_name not in brands_without_eodata

   **s3cmd** can also be used to access the **EODATA** repository.

   .. jinja:: doc_links

      :doc:`{{ eodata_s3cmd_access }}`