How to mount object storage in Linux on |brand-name|
======================================================================

S3 is a protocol for storing and retrieving data on and from remote servers. The user has their own S3 account and is identified by a pair of identifiers, which are called Access Key and Secret Key. These keys act as a username and password for your S3 account.

Usually, for desktop computers we refer to files within a directory. In S3 terminology, file is called "object" and its name is called "key". The S3 term for directory (or folder) is "bucket". To mount object storage in your Linux computer, you will use command **s3fs**.

Prerequisites
----------------------

Prerequisite No. 1 **Hosting**

To use s3 protocol, you need a |brand-name| hosting account. It comes with graphical user interface called Horizon: |brand-name-site-link| but you can also use s3 commands from terminal in various operating systems.

Prerequisite No. 2 **Valid EC2 credentials**

The Access Key and Secret Key for access to an s3 account are also called the "EC2 credentials". See article

.. jinja:: brand_names

   :doc:`/cloud/How-to-generate-ec2-credentials-on-Eumetsat-Elasticity/How-to-generate-ec2-credentials-on-Eumetsat-Elasticity`

At this point, you should have access to the cloud environment, using the OpenStack CLI client. It means that the command **openstack** is operational.

Check your credentials and save them in a file
----------------------------------------------------

Check your credentials with the following command:

.. code::

   openstack ec2 credentials list

where Access token and Secret token will be used in s3fs configuration:

.. code::

  echo Access_token:Secret_token > ~/.passwd-s3fs

That command will store the credentials into a file called *passwd-s3fs*. Since it starts with a dot, it will be invisible to the usual searches under Linux.

The file will be created in the present directory, but you can also create it anywhere else, for instance, in /etc/ folder and the like.

Change permissions of the newly created file

.. code::

  chmod 600 .passwd-s3fs

Code **600** means you can read and write the file or directory but that none of the other users on the local host will have access to it.

Enable 3fs
--------------------

Uncomment "user_allow_other" in *fuse.conf* file as root

.. code::

  sudo nano /etc/fuse.conf

Now you are ready to mount your object storage to your Linux system. The command looks like:

.. code::

   s3fs w-container-1 /local/mount/point - passwd_file=~/.passwd-s3fs -o url=https://s3.waw3-1.cloudferro.com -o use_path_request_style -o umask=0002 -o allow_other

What To Do Next
-----------------------

If you want to access s3 files without mounting to the local computer, use command **s3cmd**.

.. jinja:: brand_names

