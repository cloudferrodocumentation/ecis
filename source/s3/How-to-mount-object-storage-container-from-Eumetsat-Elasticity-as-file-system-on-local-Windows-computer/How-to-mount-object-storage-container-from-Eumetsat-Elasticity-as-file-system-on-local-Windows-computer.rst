How to mount object storage container from |brand-name| as file system on local Windows computer
================================================================================================

This article describes how to configure direct access to object storage
containers from |brand-name| cloud in the **This PC** window on your local
Windows computer. Such containers will be mounted as network drives, for
example:

.. jinja:: s3_images

   .. image:: {{ s3074 }}

You will configure mounting using an account that can be elevated to
administrative privileges through User Account Control (UAC). After this
process, the mounted container should also be available to accounts that do
not have such administrative privileges.

Prerequisites
-------------

No. 1 **Account**

You need a |brand-name| hosting account with access to the Horizon interface:
|brand-name-site-link|.

No. 2 **Object storage container**

You need at least one object storage container on the |brand-name| cloud.

.. jinja:: doc_links

   If you do not have one yet, follow this article: :doc:`{{ object_storage }}`

No. 3 **Generated S3 credentials**

You need S3 credentials for your account.

.. jinja:: doc_links

   :doc:`{{ ec2_credentials }}`

If you want to generate credentials from Windows by using OpenStack CLI, you
need to install the OpenStack CLI client first.

.. jinja:: doc_links

   * :doc:`{{ openstackclient_windows }}`
   * :doc:`{{ openstackclient_windows_wsl }}`

Once you have installed OpenStack CLI on Windows, use it to perform the
credentials workflow from the S3 credentials article. Adjust the commands for
your Windows environment where needed.

No. 4 **A local computer running Microsoft Windows**

You need a local computer running Microsoft Windows. This article was written
for Windows 10 Pro.

You need access to an account that can be elevated to administrative
privileges through UAC. Such an account is usually created during a standard
installation of Microsoft Windows.

Other accounts, including accounts named **Administrator** on Windows Server,
are outside the scope of this article.

What we are going to cover
--------------------------

* Mounting an object storage container as a Windows drive using open source
  software
* Testing the connection to the container
* Tweaking the **--dir-cache-time** option
* Setting automatic mounting for a container
* Removing software used for mounting

Software tools used in this article
-----------------------------------

This article uses **Rclone**, **WinFsp**, and **NSSM**.

`Rclone <https://rclone.org/>`_ can manage files in cloud storage and sync
between file systems. In this article, you will use its
`rclone mount <https://rclone.org/commands/rclone_mount/>`__ command to mount
object storage on your Windows computer.

`WinFsp <https://winfsp.dev/>`_ enables access to custom file systems on
Microsoft Windows. In this workflow, it allows Rclone to mount S3 storage.

`NSSM <https://nssm.cc/>`_ is a service manager. Here, it is used to configure
automatic mounting of object storage. You will run it from the
`command line <https://nssm.cc/commands>`_.

How to use the Rclone configuration file
----------------------------------------

By default, Rclone creates and uses a configuration file in the
**\\.config\\rclone** folder in the home directory of the current user.

To streamline the configuration process, you will instead manually create a
configuration file called **rclone.conf** in the folder where the Rclone binary
is stored. Each time Rclone is executed, the location of that file will be
passed to it as a parameter.

.. warning::

   All users of your computer may be able to access and modify the
   configuration file. It contains access credentials written as plain text.

Step 1: Download and install the required software
------------------------------------------------------

.. note::

   Skip this step if these software tools are already configured.

Download and extract Rclone
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Start PowerShell normally, not as Administrator.

Use the following commands to create the directory in which Rclone will be
stored and navigate to it:

.. code-block:: powershell

   mkdir C:\rclone
   cd C:\rclone

Without closing PowerShell, open a web browser on your computer. Navigate to
the Rclone downloads page:

https://rclone.org/downloads

The page contains a table with links to different versions:

.. jinja:: s3_images

   .. image:: {{ s3075 }}

Download the version of Rclone for the **Intel/AMD - 64 Bit** platform for
Windows.

Download the zip archive. In Microsoft Edge, it should look like this:

.. jinja:: s3_images

   .. image:: {{ s3076 }}

Enter the zip archive. It should contain one directory. Double-click to enter
it. Its content should look like this:

.. jinja:: s3_images

   .. image:: {{ s3077 }}

Copy the content of that directory to the **C:\\rclone** folder that you
created previously using PowerShell.

Download and install WinFsp
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Return to the browser and navigate to:

https://winfsp.dev/rel/

Click **Download WinFsp Installer**:

.. jinja:: s3_images

   .. image:: {{ s3078 }}

Run the downloaded installer. The installation process is similar to installing
other Windows programs. The **Custom Setup** step requires you to make a
choice:

.. jinja:: s3_images

   .. image:: {{ s3079 }}

Leave the default values intact to install only the **Core** section and click
**Next**. Complete the installation.

Download and extract NSSM
^^^^^^^^^^^^^^^^^^^^^^^^^

Navigate to:

https://nssm.cc/download

Click the link in the **Latest release** section:

.. jinja:: s3_images

   .. image:: {{ s3080 }}

A zip file should be downloaded. It should contain one folder. The content of
that folder should look like this:

.. jinja:: s3_images

   .. image:: {{ s3081 }}

Navigate to the **win64** folder. It should contain one executable file called
**nssm**:

.. jinja:: s3_images

   .. image:: {{ s3082 }}

Copy that file to **C:\\rclone**.

Step 2: Enter the connection data
---------------------------------

Open the **C:\\rclone** folder using Windows File Explorer.

The **rclone.conf** file in that folder will store connection data for object
storage. If the file does not exist, create it. Open it using Notepad.

Each section containing object storage connection data starts with a line
containing its name in square brackets. Below it, there are lines containing
different parameters used to connect to object storage.

A single section provides access to all object storage containers available to
the same access key and secret key pair. This means that you do not need to
create separate sections for different containers that use the same
credentials.

Add the following section to the end of the file.

.. jinja:: regional_clouds

   .. tabs::

      {% for region in regions %}
      .. tab:: {{ region.display_name }}

         .. code-block:: ini

            [remote-config]
            type = s3
            provider = Other
            access_key_id = 1234
            secret_access_key = 4321
            endpoint = {{ region.s3_host }}

      {% endfor %}

In the above block, replace **1234** and **4321** with the access key and
secret key obtained in Prerequisite No. 3.

This code creates a connection called **remote-config**. If you want to use a
different name for your connection, replace **remote-config** in the
configuration block. This name does not have to be the same as the name of one
of your containers.

If you want to access other object storage containers using different
credentials on your computer, create a separate section with a different name
for each key pair.

Step 3: Perform a test mount
----------------------------

In this step, you will perform a test mount to make sure that the
configuration was successful and **Rclone** can mount your object storage
container.

Return to the PowerShell window you opened in Step 1. If you closed it, open
PowerShell again as a normal user, not as Administrator, and navigate to the
**C:\\rclone** directory.

Execute the command below. Replace **remote-config** with the name of the
connection you configured.

.. code-block:: powershell

   .\rclone.exe --config "C:\rclone\rclone.conf" lsd remote-config:

You should see the list of object storage containers associated with your
credentials. For example:

.. code-block:: text

             -1 2023-01-18 12:53:14        -1 second-test-container
             -1 2023-01-16 13:23:03        -1 test-container

Repeat this process for each key pair you added in Step 2.

To test mounting one of your containers, execute the command below without
leaving PowerShell. Replace:

* **remote-config** with the name of your connection,
* **test-container** with the name of your container,
* **E:** with the drive letter under which you want to mount it.

.. code-block:: powershell

   .\rclone.exe mount --config "C:\rclone\rclone.conf" --network-mode remote-config:test-container E: --vfs-cache-mode full --dir-cache-time 1m0s

.. note::

   If you enter the name of a non-existing object storage container by
   mistake, the command may attempt to create and mount it, subject to
   permissions, bucket quota, and other constraints.

The option **--vfs-cache-mode full** makes the mount support standard file
system operations.

The option **--dir-cache-time 1m0s** is explained in the next step.

The option **--network-mode** is optional. It was added so that the mounted
container is visually represented as a network drive in **This PC**. Removing
it causes the container to be represented as a normal drive and may solve some
mounting-related problems.

You should now get the following output:

.. code-block:: text

   The service rclone has been started.

Go to the **This PC** window. You should see the mounted container there:

.. jinja:: s3_images

   .. image:: {{ s3083 }}

Enter it. You should see its content:

.. jinja:: s3_images

   .. image:: {{ s3084 }}

To stop the test mount, press **CTRL+C** in PowerShell. You should get the
following output:

.. code-block:: text

   The service rclone has been stopped.

The container should no longer be visible in the **This PC** window.

If pressing **CTRL+C** does not stop the test mount, make sure that the
PowerShell window is focused by left-clicking it. Press a letter on your
keyboard, for example **A**, and try pressing **CTRL+C** again.

You can perform such tests for all object storage containers you want to use
on your computer.

Do not close PowerShell yet.

Step 4: Tweak the --dir-cache-time option
-----------------------------------------

In Step 3, you performed a test mount of your object storage container using
a command similar to this:

.. code-block:: powershell

   .\rclone.exe mount --network-mode remote-config:test-container E: --vfs-cache-mode full --dir-cache-time 1m0s

Tweaking the **--dir-cache-time** option is important especially if you intend
to use your container on multiple physical or virtual machines. This includes
using the container from your Windows computer and from the Horizon dashboard.

You may discover that changes made to the bucket from another computer do not
appear immediately on your Windows computer. Using the **Refresh** option in
Windows File Explorer might not synchronize that change either.

This happens because **Refresh** may read from the local cache instead of
pulling changes directly from object storage. If **--dir-cache-time** is not
specified during mounting, the cache is automatically synchronized every 5
minutes. Therefore, if you rename a folder from another device, it may take up
to about 5 minutes to become visible.

Specifying **--dir-cache-time** overwrites the default value. In this example,
the automatic cache refresh interval was set to 1 minute: **1m0s**. You can
also set it to a lower value, for example 1 second: **1s**.

You can perform several test mounts as explained in Step 3 and choose the
**--dir-cache-time** value that suits your workflow.

Step 5: Configure automatic mounting of your container
------------------------------------------------------

Open **PowerShell** as Administrator and navigate to the **C:\\rclone**
directory:

.. code-block:: powershell

   cd C:\rclone

Start the NSSM service installer:

.. code-block:: powershell

   .\nssm.exe install

You should get the following window:

.. jinja:: s3_images

   .. image:: {{ s3085 }}

Click the **...** button next to the **Path:** text field.

Choose the location of Rclone. If you followed this tutorial, this location is:

.. code-block:: text

   C:\rclone\rclone.exe

In the **Arguments** text field, enter the following code. Replace
**remote-config** with the name of your connection, **test-container** with the
name of your container, **E:** with the drive letter under which you want to
mount it, and **1m0s** with the value chosen in Step 4.

.. code-block:: text

   mount --config "C:\rclone\rclone.conf" --network-mode remote-config:test-container E: --vfs-cache-mode full --dir-cache-time 1m0s

.. warning::

   Make sure that nothing is already mounted under the drive letter you choose.

In the **Service name:** text field, enter the name for your mounting service.
It can be different from the name of your connection and from the name of your
S3 container. In this example, the name **mounting-service** is used.

Navigate to the **Log on** tab. Make sure that **Local System account** is
selected.

Click **Install service**. You should get the following message:

.. jinja:: s3_images

   .. image:: {{ s3086 }}

Restart your computer and check whether the drive is automatically mounted in
the **This PC** window. If it is, the service works as intended.

You should now be able to work with your files.

Add a separate service with a different name for each object storage container
you want to have automatically mounted on your computer. Save the service
names so that you can stop and remove them later if needed.

If you cannot delete files or folders from the mounted object storage, you can
remove them from **Object Store** -> **Containers** in the Horizon dashboard:

.. jinja:: s3_images

   .. image:: {{ s3087 }}

Removing software responsible for automatic mounting of object storage
----------------------------------------------------------------------

If you no longer want to access object storage containers from |brand-name| on
a particular machine, you can remove the configuration and software.

.. ifconfig:: brand_name == 'Creodias'

   The software stack described here might also be used for mounting the
   EODATA repository using the Remote Transfer for EODATA service. If you
   follow this section correctly, that configuration will also be removed.

The whole procedure is covered in this section:

* removing automatic mounting created in NSSM,
* removing saved object storage configuration in Rclone,
* uninstalling WinFsp,
* removing the **C:\\rclone** folder containing Rclone and NSSM.

Open PowerShell as Administrator. Navigate to the **C:\\rclone** directory:

.. code-block:: powershell

   cd C:\rclone

To check the status of your automatic mounting service, execute the following
command. Replace **mounting-service** with the name of your automatic mounting
service:

.. code-block:: powershell

   .\nssm.exe status mounting-service

You should get the following output:

.. code-block:: text

   SERVICE_RUNNING

To stop automatic mounting of your container, execute the command below.
Replace **mounting-service** as previously:

.. code-block:: powershell

   .\nssm.exe stop mounting-service

Delete the service:

.. code-block:: powershell

   .\nssm.exe remove mounting-service confirm

You should get output similar to this:

.. code-block:: text

   Service "mounting-service" removed successfully.

.. ifconfig:: brand_name == 'Creodias'

   If you have used this Rclone installation to mount other object storage
   containers from |brand-name| or the EODATA repository using the Remote
   Transfer for EODATA service, remove their services using NSSM in the same
   way.

.. ifconfig:: brand_name != 'Creodias'

   If you have used this Rclone installation to mount other object storage
   containers from |brand-name|, remove their services using NSSM in the same
   way.

Delete the **C:\\rclone** folder you created.

Click the **Start** menu and type **control panel**.

You should see the following search result:

.. jinja:: s3_images

   .. image:: {{ s3088 }}

Click it to enter Control Panel.

Make sure that the **View by** drop-down menu is set to **Category**.

In the **Programs** section, select **Uninstall a program**.

.. jinja:: s3_images

   .. image:: {{ s3089 }}

In the list that appears, find the **WinFsp** entry:

.. jinja:: s3_images

   .. image:: {{ s3090 }}

Right-click it and choose **Uninstall**:

.. jinja:: s3_images

   .. image:: {{ s3091 }}

You will get the following question:

.. jinja:: s3_images

   .. image:: {{ s3092 }}

Click **Yes**. You should get the following window:

.. jinja:: s3_images

   .. image:: {{ s3093 }}

Close all open programs and File Explorer windows, for example **This PC** or
**Documents** windows. Make sure that **Automatically close applications and
attempt to restart them after setup is complete.** is selected and click
**OK**.

You will be prompted to reboot your computer:

.. jinja:: s3_images

   .. image:: {{ s3094 }}

Make sure that it is safe to reboot, including that you have:

* saved your work,
* closed the programs.

After that, click **Yes** in the prompt shown above.

Your computer should now reboot.

Once you have logged in again, open **This PC**.

Enter your **C:** drive.

Remove the **rclone** folder. You may need administrative privileges for it.

Rclone and other software used for mounting object storage should now be
removed.

What to do next
---------------

Object storage containers on the |brand-name| cloud can be mounted both on
physical and virtual machines running Windows and Linux.

To mount an object storage container on a different platform, follow one of
the articles below:

.. jinja:: doc_links

   {% if object_storage_windows_vm_mount %}
   :doc:`{{ object_storage_windows_vm_mount }}`
   {% endif %}

   {% if s3fs_linux_mount %}
   :doc:`{{ s3fs_linux_mount }}`
   {% endif %}

   {% if s3_private_access %}
   :doc:`{{ s3_private_access }}`
   {% endif %}

   {% if remote_transfer_eodata %}
   You can also mount the EODATA repository onto your local computer using the
   Remote Transfer for EODATA service.

   :doc:`{{ remote_transfer_eodata }}`
   {% endif %}