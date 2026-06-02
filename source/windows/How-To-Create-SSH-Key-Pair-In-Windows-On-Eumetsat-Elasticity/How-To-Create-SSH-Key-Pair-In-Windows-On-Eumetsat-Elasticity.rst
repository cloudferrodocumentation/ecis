How to Create SSH Key Pair in Windows 10 On |brand-name|
===================================================================

This guide will show you how to generate an SSH key pair in Windows 10 using OpenSSH.

Prerequisites
---------------

 * System running Windows 10 or Windows Server 2016-2022
 * User account with administrative privileges
 * Access to Windows command prompt

Step 1: Verify if OpenSSH Client is Installed
---------------------------------------------

First, check to see if you have the OpenSSH client installed:

1. Open the **Settings** panel, then click **Apps**.

2. Under the *Apps and Features* heading, click **Manage optional Features**.

.. jinja:: windows_images

   .. image:: {{ windows092 }}

3. Scroll down the list to see if OpenSSH Client is listed.

- If it’s not, click the plus-sign next to Add a feature.
- Scroll through the list to find and select OpenSSH Client.
- Finally, click Install.

.. jinja:: windows_images

   .. image:: {{ windows093 }}

This will install app called **ssh-keygen**.

Step 2: Open Command Prompt
---------------------------

**ssh-keygen** runs from Windows Command Prompt, so the next step is to open it.

1. Press the Windows key.

2. Type **cmd**.

3. Under **Best Match**, right-click **Command Prompt**.

4. Click Run as Administrator.

.. jinja:: windows_images

   .. image:: {{ windows094 }}

Step 3: Use OpenSSH to Generate an SSH Key Pair
-----------------------------------------------

Finally, run **ssh-keygen** to generate the public and private keys for SSH access to the |brand-name| server.

1. In command prompt, type the following:

.. code::

	ssh-keygen

.. jinja:: windows_images

   .. image:: {{ windows095 }}

Press **ENTER** three times. This will

 * create folder **/.ssh** for the keys as well as

 * file **id_rsa** for secret key and

 * file **id_rsa.pub** for public key.

These are the default values.

.. warning::

   If you have created other keys in those same locations, you can define other folder and files instead of just pressing Enter three times.

.. jinja:: windows_images

   .. image:: {{ windows096 }}

To see the generated files, navigate to **C:/Users/<Your_User_Name>/.ssh** with your file explorer.

.. jinja:: windows_images

   .. image:: {{ windows097 }}

The image shows default values of files for private and public keys, in files **id_rsa** and **id_rsa.pub**, respectively.

What To Do Next
-----------------

.. jinja:: brand_names

   For Windows 11, see this guide: :doc:`/windows/How-To-Create-SSH-Key-Pair-In-Windows-11-On-{{ brand_name_hyphen }}/How-To-Create-SSH-Key-Pair-In-Windows-11-On-{{ brand_name_hyphen }}`

Put your public key on remote server and use your private key to authorize to your VM. To add the public key to remote server see

.. jinja:: brand_names

   :doc:`/networking/How-to-add-SSH-key-from-Horizon-web-console-on-{{ brand_name_hyphen }}`

To connect to the server from Windows:

.. jinja:: brand_names

   :doc:`/windows/How-to-connect-to-a-virtual-machine-via-SSH-from-Windows-10-Command-Prompt-on-{{ brand_name_hyphen }}`

   :doc:`/windows/How-to-access-a-VM-from-Windows-PuTTY-on-{{ brand_name_hyphen }}`




