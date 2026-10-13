How to install boto3 in Windows
===============================

Introduction
------------

.. ifconfig:: brand_name in brands_without_eodata

   The **boto3** library for Python can be used to list and download items
   from a specified S3 bucket. In this article, you will install **boto3** on a
   Windows system.

Step 1: Ensure that Python 3 is preinstalled
--------------------------------------------

On a desktop Windows system
^^^^^^^^^^^^^^^^^^^^^^^^^^^

To run **boto3**, you need to have Python installed.

.. jinja:: doc_links

   If you are running Windows on a desktop computer, the first step of this
   article shows how to install Python: :doc:`{{ openstackclient_windows }}`.

On a virtual machine running
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Virtual machines created in the cloud usually have Python 3
already preinstalled.

If you want to create your own Windows VM, two steps are involved:

#. Log in to your |brand-name| hosting account with access to the Horizon
   interface: |brand-name-site-link|.

#. Use an existing Windows instance or create a new one.

.. jinja:: doc_links

   For more information, see :doc:`{{ windows_vm_rdp_bastion }}`.

Step 2: Install boto3 on Windows
--------------------------------

To install **boto3** on Windows:

#. Log in as administrator.

#. Click the Windows icon in the bottom-left corner of your desktop.

#. Find **Command Prompt** by entering **cmd**.

.. jinja:: s3_images

   .. image:: /s3/How-To-Install-boto3-In-Windows/{{ s3062 }}
      :alt: Step 2: Install boto3 on Windows

Verify that you have an up-to-date Python installation:

.. code-block:: powershell

   python -V

.. jinja:: s3_images

   .. image:: /s3/How-To-Install-boto3-In-Windows/{{ s3063 }}
      :alt: Step 2: Install boto3 on Windows

Install **boto3** with the following command:

.. code-block:: powershell

   pip install boto3

.. jinja:: s3_images

   .. image:: /s3/How-To-Install-boto3-In-Windows/{{ s3064 }}
      :alt: Step 2: Install boto3 on Windows

Verify the installation:

.. code-block:: powershell

   pip show boto3

.. jinja:: s3_images

   .. image:: /s3/How-To-Install-boto3-In-Windows/{{ s3065 }}
      :alt: Step 2: Install boto3 on Windows

What to do next
---------------

Use the installed library to access your buckets:

* :doc:`/s3/How-to-access-object-storage-using-boto3/How-to-access-object-storage-using-boto3`
