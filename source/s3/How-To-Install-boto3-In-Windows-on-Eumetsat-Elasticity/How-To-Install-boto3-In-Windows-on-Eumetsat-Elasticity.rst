How to install boto3 in Windows on |brand-name|
===============================================

Introduction
------------

.. ifconfig:: brand_name in brands_without_eodata

   The **boto3** library for Python can be used to list and download items
   from a specified S3 bucket. In this article, you will install **boto3** on a
   Windows system.

.. ifconfig:: brand_name not in brands_without_eodata

   The **boto3** library for Python can be used to list and download items
   from a specified S3 bucket or from the **EODATA** repository. In this
   article, you will install **boto3** on a Windows system.

Step 1: Ensure that Python 3 is preinstalled
--------------------------------------------

On a desktop Windows system
^^^^^^^^^^^^^^^^^^^^^^^^^^^

To run **boto3**, you need to have Python installed.

.. jinja:: doc_links

   If you are running Windows on a desktop computer, the first step of this
   article shows how to install Python: :doc:`{{ openstackclient_windows }}`.

On a virtual machine running in |brand-name| cloud
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Virtual machines created in the |brand-name| cloud usually have Python 3
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

   .. image:: {{ s3062 }}

Verify that you have an up-to-date Python installation:

.. code-block:: powershell

   python -V

.. jinja:: s3_images

   .. image:: {{ s3063 }}

Install **boto3** with the following command:

.. code-block:: powershell

   pip install boto3

.. jinja:: s3_images

   .. image:: {{ s3064 }}

Verify the installation:

.. code-block:: powershell

   pip show boto3

.. jinja:: s3_images

   .. image:: {{ s3065 }}

What to do next
---------------

.. jinja:: doc_links

   {% if eodata_boto3_access %}
   With the **boto3** library, you can download and list satellite images from
   buckets or from the **EODATA** repository.

   * :doc:`{{ eodata_boto3_access }}`
   {% endif %}

   {% if slurm_mpi_workflow %}
   You can also run larger processing workflows on a SLURM cluster.

   * :doc:`{{ slurm_mpi_workflow }}`
   {% endif %}