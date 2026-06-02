How to connect to a virtual machine via SSH from Windows 10 Command Prompt on |brand-name|
=============================================================================================

Requirements
----------------

.. jinja:: brand_names

   The private and public keys were created and saved on the local disk of your computer. (:doc:`/cloud/How-to-create-key-pair-in-OpenStack-Dashboard-on-{{ brand_name_hyphen }}/How-to-create-key-pair-in-OpenStack-Dashboard-on-{{ brand_name_hyphen }}`)

.. jinja:: brand_names

   During the virtual machine creation procedure, the generated key was attached. (:doc:`/cloud/How-to-create-new-Linux-VM-in-OpenStack-Dashboard-Horizon-on-{{ brand_name_hyphen }}/How-to-create-new-Linux-VM-in-OpenStack-Dashboard-Horizon-on-{{ brand_name_hyphen }}`)

.. jinja:: brand_names

   A floating IP was assigned to your VM. (:doc:`/networking/How-to-Add-or-Remove-Floating-IPs-to-your-VM-on-{{ brand_name_hyphen }}/How-to-Add-or-Remove-Floating-IPs-to-your-VM-on-{{ brand_name_hyphen }}`)

Check in "Installed features" if the OpenSSH client is installed, if not click **Add a feature**, search for **OpenSSH client** and install it.

.. jinja:: windows_images

   .. figure:: {{ windows113 }}
      :class: with-border

Step 1 Go to the folder containing your SSH keys
--------------------------------------------------

Run the Command Prompt and change the current folder to the folder where you store your keys.

For example:

.. code::

   cd c:\Users\wikit\sshkeys


Step 2 Connect to your VM using SSH
--------------------------------------------

If the name of your key is **id_rsa** and the floating IP of your virtual machine is **64.225.129.203**, type the following command:

.. code::

   ssh -i id_rsa eouser@64.225.129.203

If the text before the cursor changed to eouser@test (assuming the name of your virtual machine is **test**), the connection was successfully established. Before that, you may get the message that the authenticity of the host can't be established and the following question:

.. code::

   Are you sure you want to continue connecting (yes/no/[fingerprint])?

If you got that message, it typically means that your computer has never connected to your VM via SSH before and you should confirm that you are willing to connect by typing "yes" and pressing Enter.

You should now be able to issue commands to your VM:

.. jinja:: windows_images

   .. figure:: {{ windows114 }}
      :class: with-border
