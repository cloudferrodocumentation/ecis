Can I change my password through RDP on |brand-name|?
=====================================================

In short: No, this is not possible. You have to be logged in when you want to change your password. Security measures requiring you to change your password on first login are not working with RDP and have to be disabled on administrative level.
This article will show you how to create and configure a new account which can access the VM using RDP without the need to immediately change the password.

What We Are Going To Cover
--------------------------

 * Creating an account on administrative level

 * Configuring the account for remote access

Prerequisites
-------------

No. 1 **Account**

You need a |brand-name| hosting account with access to the Horizon interface: |brand-name-site-auth-link|.

No. 2 **Windows VM**

You need a running Windows VM with Remote Access allowed, an Administrator account, and basic Windows knowledge.

Step 1: Microsoft Management Console (mmc)
------------------------------------------

Log in as administrator, click on the Windows icon and type "mmc".

.. jinja:: windows_images

   .. image:: {{ windows058 }}

Confirm the question with "Yes", select File -> Add/Remove Snap-in...

.. jinja:: windows_images

   .. image:: {{ windows059 }}

Chose the snap-in "Local Users and Groups", click "Add >", "Finish", and "OK" in the successive windows.

Step 2: Create and configure a user account
-------------------------------------------

Expand the snap-in and open the "Users" folder. There are already some default accounts available.
Right-click into the white area where the accounts are listed and select "New user..." from the menu.
Provide a user name and a password, full name and description are optional.
Deselect "User must change password at next logon" and click "Create".

.. jinja:: windows_images

   .. image:: {{ windows060 }}

Right-click on the newly created account and select "Properties".

.. jinja:: windows_images

   .. image:: {{ windows061 }}

Navigate to "Member Of" and click "Add..."

.. jinja:: windows_images

   .. image:: {{ windows062 }}

Click on "Advanced..." in the opening window, then "Find Now".
Select "Remote Desktop Users" in the search results, click "OK" twice.

.. jinja:: windows_images

   .. image:: {{ windows063 }}

If everything was done right, the selected group is now listed. Click "Apply", then "OK".

.. jinja:: windows_images

   .. image:: {{ windows064 }}

What To Do Next
---------------

You have successfully created a new user account and configured this account for remotely using the VM.
You can now forward the credentials and ask the user to change the password after logging in.