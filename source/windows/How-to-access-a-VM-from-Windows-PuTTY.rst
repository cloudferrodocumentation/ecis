How to access a VM from Windows PuTTY
=====================================

The link below shows how to generate and add rsa key pairs:

.. jinja:: brand_names

   :doc:`/windows/How-to-connect-to-a-virtual-machine-via-SSH-from-Windows-10-Command-Prompt`

In this tutorial key.pem is equivalent to the id_rsa file that we obtain in a zip package after the key generation process.

To connect via PuTTY, copy your Virtual Machine floating IP address and save it somewhere.

Open PuTTYGen to converse the private key file to ppk format. (This format is being ussed by the PuTTY client). Click on the "Load" button.


.. jinja:: windows_images

   .. figure:: /windows/How-to-access-a-VM-from-Windows-PuTTY/{{ windows099 }}
      :alt: How to access a VM from Windows PuTTY
      :class: with-border

Choose the key file. Make sure that you have set the visibility to "All files".


.. jinja:: windows_images

   .. figure:: /windows/How-to-access-a-VM-from-Windows-PuTTY/{{ windows100 }}
      :alt: How to access a VM from Windows PuTTY
      :class: with-border

A prompt window informing you about succesful import will appear.


.. jinja:: windows_images

   .. figure:: /windows/How-to-access-a-VM-from-Windows-PuTTY/{{ windows101 }}
      :alt: How to access a VM from Windows PuTTY
      :class: with-border

Save your imported private key in the ppk format.

.. jinja:: windows_images

   .. figure:: /windows/How-to-access-a-VM-from-Windows-PuTTY/{{ windows102 }}
      :alt: How to access a VM from Windows PuTTY
      :class: with-border

.. jinja:: windows_images

   .. figure:: /windows/How-to-access-a-VM-from-Windows-PuTTY/{{ windows103 }}
      :alt: How to access a VM from Windows PuTTY
      :class: with-border

Open PuTTY Configuration tool and focus on the marked labels:

.. jinja:: windows_images

   .. figure:: /windows/How-to-access-a-VM-from-Windows-PuTTY/{{ windows104 }}
      :alt: How to access a VM from Windows PuTTY
      :class: with-border

**Description:**

1) Host Name( or IP address) → Write down the floating IP address that you may find in the Horizon Panel

2) Port → Assign a SSH service port, by default it is set up on 22

3) Connection type → Check SSH

Configuration has been set up. Enroll the SSH branch.

.. jinja:: windows_images

   .. figure:: /windows/How-to-access-a-VM-from-Windows-PuTTY/{{ windows105 }}
      :alt: How to access a VM from Windows PuTTY
      :class: with-border

Enroll the Auth branch and provide a private key file by clicking "Browse", selecting your key and clicking "Open".

.. jinja:: windows_images

   .. figure:: /windows/How-to-access-a-VM-from-Windows-PuTTY/{{ windows106 }}
      :alt: How to access a VM from Windows PuTTY
      :class: with-border

.. jinja:: windows_images

   .. figure:: /windows/How-to-access-a-VM-from-Windows-PuTTY/{{ windows107 }}
      :alt: How to access a VM from Windows PuTTY
      :class: with-border

(Optionally) Expand the "Connection" list and click on the "Data".

Set Auto-login username: eouser.

.. jinja:: windows_images

   .. figure:: /windows/How-to-access-a-VM-from-Windows-PuTTY/{{ windows108 }}
      :alt: How to access a VM from Windows PuTTY
      :class: with-border

For your comfort you can save the session for future use by naming it and saving changes.

.. jinja:: windows_images

   .. figure:: /windows/How-to-access-a-VM-from-Windows-PuTTY/{{ windows109 }}
      :alt: How to access a VM from Windows PuTTY
      :class: with-border

Choose the proper session and click on the "Open" button to commence the ssh session:

.. jinja:: windows_images

   .. figure:: /windows/How-to-access-a-VM-from-Windows-PuTTY/{{ windows110 }}
      :alt: How to access a VM from Windows PuTTY
      :class: with-border

If you are connecting to your VM via PuTTY for the first time, we recommend that you save the rsa key fingerprint by choosing Yes (Tak) for future connections from your computer.

.. jinja:: windows_images

   .. figure:: /windows/How-to-access-a-VM-from-Windows-PuTTY/{{ windows111 }}
      :alt: How to access a VM from Windows PuTTY
      :class: with-border

If you logged in correctly you should see the following at the bottom of the screen:

.. code::

   eouser@yourInstanceName:~$

You are now correctly logged into your VM via SSH from another host.

.. jinja:: windows_images

   .. figure:: /windows/How-to-access-a-VM-from-Windows-PuTTY/{{ windows112 }}
      :alt: How to access a VM from Windows PuTTY
      :class: with-border

If you would like to learn more about **PuTTYgen**, its installation and usage, visit the website https://www.puttygen.com.
