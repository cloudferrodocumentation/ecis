How to install s3cmd on Linux
=============================

In this article, you will learn how to install
`s3cmd <https://github.com/s3tools/s3cmd>`_ on Linux.

**s3cmd** is a command-line tool for working with S3-compatible object storage from a terminal. After installing it, you can use commands to list buckets, upload files, download files, synchronize directories, and automate storage tasks in scripts.

On |brand-name|, you can use **s3cmd** when you want to work with object storage directly from the command line instead of mounting storage as a local file system.

What we are going to cover
--------------------------

* Installing **s3cmd** using **apt**
* Checking the installed version
* Uninstalling **s3cmd**

Prerequisites
-------------

No. 1 **Account**

You need a |brand-name| hosting account with access to the Horizon interface:
|brand-name-site-link|.

No. 2 **A virtual machine or local computer**

These instructions are written for Ubuntu 22.04, either on a local computer or
on a virtual machine hosted on the cloud.

Other operating systems and environments are outside the scope of this article
and may require adjusted commands.

If you want to install **s3cmd** on a virtual machine hosted on |brand-name|
cloud, follow one of these articles:

.. jinja:: doc_links

   * :doc:`{{ linux_vm_from_windows }}`
   * :doc:`{{ linux_vm_from_linux }}`

Object storage from |brand-name| is available both from a virtual machine
hosted on the cloud and from a local Linux computer.

Installing s3cmd using apt
--------------------------

Update the packages on your system:

.. code-block:: bash

   sudo apt update && sudo apt -y upgrade

.. note::

   When executing **sudo**, you may be prompted for a password. If that
   happens, enter the local user account password and press **Enter**.

Install **s3cmd**:

.. code-block:: bash

   sudo apt -y install s3cmd

After installation, **s3cmd** is available as a command in the terminal.

Check whether the installation was successful:

.. code-block:: bash

   s3cmd --version

You should get the version of **s3cmd** installed on your computer. For
example:

.. code-block:: text

   s3cmd version 2.2.0

.. jinja:: s3_images

   .. image:: /s3/How-to-install-s3cmd-on-Linux/{{ s3068 }}
      :alt: Installing s3cmd using apt

Uninstalling s3cmd using apt
----------------------------

If you installed **s3cmd** using **apt**, remove it using the same package
manager:

.. code-block:: bash

   sudo apt -y remove s3cmd

To remove packages that were installed as dependencies of **s3cmd**, or other
packages that were later removed and are no longer needed, run:

.. code-block:: bash

   sudo apt autoremove

This may affect software not directly related to **s3cmd**. The command will
show you which packages are to be removed before proceeding.

.. jinja:: s3_images

   .. image:: /s3/How-to-install-s3cmd-on-Linux/{{ s3069 }}
      :alt: Uninstalling s3cmd using apt

You should get the following question:

.. code-block:: text

   Do you want to continue? [Y/n]

If you want to remove these packages, answer with **Y** and press **Enter**.

If you do not want to remove them, answer with **n** and press **Enter**.

What to do next
---------------

To access object storage buckets from the cloud on a virtual machine
hosted on the cloud or on a local Linux computer, follow this article:

.. jinja:: doc_links

   :doc:`{{ s3cmd_access }}`
