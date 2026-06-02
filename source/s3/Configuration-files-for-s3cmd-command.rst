Configuration files for s3cmd command on |brand-name|
=====================================================

`s3cmd <https://github.com/s3tools/s3cmd>`_ can access remote data using
the S3 protocol. This includes the **EODATA** repository and object storage
on the |brand-name| cloud.

To connect to S3 storage, **s3cmd** uses several parameters, such as an
access key, secret key, S3 endpoint, and others. During configuration, you can
enter this data interactively, and the command saves it into a configuration
file. This file can then be passed to **s3cmd** when issuing commands using
the connection described within.

If you want to use multiple connections from a single virtual machine, such
as connecting both to the **EODATA** repository and to object storage on the
|brand-name| cloud, you can create and store multiple configuration files,
one per connection.

This article provides examples of how to create and save these configuration
files under various circumstances and describes some potential problems you
may encounter.

The examples are not intended to be executed sequentially as part of a single
workflow. They illustrate different use cases of **s3cmd** operations.

.. contents:: What we are going to cover
   :depth: 2
   :local:
   :backlinks: none

Prerequisites
-------------

No. 1 **s3cmd installed**

To use **s3cmd**, it must first be installed.

.. jinja:: brand_names

   :doc:`/s3/How-to-install-s3cmd-on-Linux-on-{{ brand_name_hyphen }}/How-to-install-s3cmd-on-Linux-on-{{ brand_name_hyphen }}`

No. 2 **Knowledge of using s3cmd**

To run the examples later in this article, you need to know how to access
object storage from **s3cmd**.

.. jinja:: brand_names

   :doc:`/s3/How-to-access-object-storage-from-{{ brand_name_hyphen }}-using-s3cmd/How-to-access-object-storage-from-{{ brand_name_hyphen }}-using-s3cmd`

Initializing the configuration process
--------------------------------------

Saving an **s3cmd** configuration file is a two-part process:

* answering a series of interactive questions,
* saving the answers to a configuration file.

Execute this command:

.. code-block:: bash

   s3cmd -c eodata-config --configure

The command starts an interactive session. You enter the following data:

* **Access Key** -- your access key from Prerequisite No. 2.
* **Secret Key** -- your secret key from Prerequisite No. 2.
* **Default Region** -- use the value shown for your region in the tabbed
  example below.
* **S3 Endpoint** -- use the endpoint shown for your region in the tabbed
  example below.

For all other questions, keep pressing **Enter** to accept the default values.

The whole procedure looks like this on the screen:

.. jinja:: regional_clouds

   .. tabs::

      {% for region in regions %}
      .. tab:: {{ region.display_name }}

         .. code-block:: text

            Enter new values or accept defaults in brackets with Enter.
            Refer to user manual for detailed description of all options.

            Access key and Secret key are your identifiers for Amazon S3. Leave them empty for using the env variables.
            Access Key: <your S3 access key>
            Secret Key: <your S3 secret key>
            Default Region [US]: {{ region.s3cmd_region }}

            Use "s3.amazonaws.com" for S3 Endpoint and not modify it to the target Amazon S3.
            S3 Endpoint [s3.amazonaws.com]: {{ region.s3_host }}

            Use "%(bucket)s.s3.amazonaws.com" to the target Amazon S3. "%(bucket)s" and "%(location)s" vars can be used
            if the target S3 system supports dns based buckets.
            DNS-style bucket+hostname:port template for accessing a bucket [%(bucket)s.s3.amazonaws.com]:

            Encryption password is used to protect your files from reading
            by unauthorized persons while in transfer to S3
            Encryption password:
            Path to GPG program [/usr/bin/gpg]:

            When using secure HTTPS protocol all communication with Amazon S3
            servers is protected from 3rd party eavesdropping. This method is
            slower than plain HTTP, and can only be proxied with Python 2.7 or newer
            Use HTTPS protocol [Yes]:

            On some networks all internet access must go through a HTTP proxy.
            Try setting it here if you can't connect to S3 directly
            HTTP Proxy server name:

            New settings:
              Access Key: <your S3 access key>
              Secret Key: <your S3 secret key>
              Default Region: {{ region.s3cmd_region }}
              S3 Endpoint: {{ region.s3_host }}
              DNS-style bucket+hostname:port template for accessing a bucket: %(bucket)s.s3.amazonaws.com
              Encryption password:
              Path to GPG program: /usr/bin/gpg
              Use HTTPS protocol: True
              HTTP Proxy server name:
              HTTP Proxy server port: 0
            Test access with supplied credentials? [Y/n]
            Please wait, attempting to list all buckets...
            Success. Your access key and secret key worked fine :-)

            Now verifying that encryption works...
            Not configured. Never mind.

            Save settings? [y/N] y
            Configuration saved to 'eodata-config'

      {% endfor %}

If this is the first time you are issuing this command for file
**eodata-config**, there will be no default data in the interactive session.

To cancel the configuration process, press **CTRL+C**.

Explanation of parameters
^^^^^^^^^^^^^^^^^^^^^^^^^

The most often used **s3cmd** parameters are:

-c
   Specifies the name and/or location of the configuration file. Note that
   this option uses a single dash.

\-\-config
   Alternative to **-c**. Note that this option uses two dashes.

\-\-configure
   Initiates the on-screen question session and saves the answers to the file.

You can use **-c** or **\-\-config** together with **\-\-configure**.

Ensure that you pass the file path correctly to the shell, paying attention
to spaces, quotation marks, and escape characters.

Destination: default file
^^^^^^^^^^^^^^^^^^^^^^^^^

The default location for the **s3cmd** configuration file is a hidden file
named **.s3cfg** located in your home directory.

To check your home directory, use:

.. code-block:: bash

   echo $HOME

On Linux, the home directory is usually **/home/<username>**.

On a VM hosted by |brand-name|, it will typically be **/home/eouser**. Thus,
the configuration file will be **/home/eouser/.s3cfg**.

To initialize the configuration process using the default location, run:

.. code-block:: bash

   s3cmd --configure

Securing the configuration file
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

After the configuration file is created, it is highly recommended to protect
it by setting appropriate permissions. This ensures that your access and
secret keys are not readable by unauthorized users.

Example command for securing the default configuration file:

.. code-block:: bash

   chmod 600 ~/.s3cfg

This command makes the file readable and writable only by your user.

Destination: custom file
^^^^^^^^^^^^^^^^^^^^^^^^

If your destination of choice is a custom file, pass its name and/or location
to the command using the **-c** parameter. Finish the command with
**\-\-configure** to instruct **s3cmd** to create the file.

Examples:

**File named object-storage-access in your current working directory**

.. code-block:: bash

   s3cmd -c object-storage-access --configure

**File named eodata-access in /home/eouser/ directory**

.. code-block:: bash

   s3cmd -c /home/eouser/eodata-access --configure

**File named object-storage-access located in the parent directory of your
current working directory**

.. code-block:: bash

   s3cmd -c../object-storage-access --configure

Again, if you save the configuration file outside the default location, for
example as **/home/eouser/eodata-access**, set proper file permissions to
protect it.

Example command:

.. code-block:: bash

   chmod 600 /home/eouser/eodata-access

This ensures your access and secret keys remain secure, just like with the
default **.s3cfg** file.

Using \-\-configure on an existing file
---------------------------------------

When you use **\-\-configure**, **s3cmd** operates on a configuration file:

* If **-c** or **\-\-config** are omitted, it uses the default location.
* If **-c** or **\-\-config** are specified, it uses the given file.

If the configuration file, such as **eodata-config**, already exists, the
application offers you default values and accepts them if you press **Enter**.

Existing and valid s3cmd configuration file
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If you:

* pass an existing valid **s3cmd** configuration file,
* use **\-\-configure**,
* approve saving after finishing the session,

then the answers update the existing configuration.

If you cancel before saving, the original configuration remains unchanged.

Existing file but not a valid s3cmd configuration file
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If you:

* pass an existing file that is not a valid **s3cmd** configuration file,
* use **\-\-configure**,

it may lead to unexpected results.

Double-check that the correct file path is specified.

Executing S3 commands
---------------------

Once you have a valid configuration file, you can use **s3cmd** commands with
it. Get S3 credentials first by using Prerequisite No. 2.

In this article, we focus only on the **ls** command, which lists available
buckets.

Existing and valid configuration file — non-default location
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To execute S3 commands using a non-default config file:

.. code-block:: bash

   s3cmd -c eodata-config ls

Example output:

.. code-block:: text

   2017-11-15 10:40 s3://eodata
   2017-11-15 10:40 s3://eodata

Existing and valid configuration file — default location
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If your configuration file is saved at the default location:

.. code-block:: bash

   s3cmd ls

No **-c** parameter is needed.

Non-existent configuration file
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If you:

* pass a non-existent file path,
* do not use **\-\-configure**,

you will get an error.

Example:

.. code-block:: bash

   s3cmd -c /home/eouser/nonexistentfile ls

Error output:

.. code-block:: text

   ERROR: /home/eouser/nonexistentfile: None
   ERROR: Configuration file not available.
   ERROR: Consider using --configure parameter to create one.

Existing file that is not a valid s3cmd configuration file
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If you:

* pass a file that exists,
* the file is not a valid **s3cmd** configuration file,
* do not use **\-\-configure**,

then unexpected results may occur.

This warning also applies if the default configuration file is invalid.

Creating a minimal configuration file manually
----------------------------------------------

Instead of using the interactive **\-\-configure** process, you can create a
minimal **s3cmd** configuration file manually.

This is useful when you are:

* scripting or working in automated environments,
* quickly setting up access using an editor.

Minimal content required
^^^^^^^^^^^^^^^^^^^^^^^^

Below is the minimum content required for a valid configuration file that
connects to object storage on the |brand-name| cloud:

.. jinja:: regional_clouds

   .. tabs::

      {% for region in regions %}
      .. tab:: {{ region.display_name }}

         .. code-block:: ini

            [default]
            access_key = <your S3 access key>
            secret_key = <your S3 secret key>
            host_base = {{ region.s3_host }}
            host_bucket = %(bucket)s.{{ region.s3_host }}
            bucket_location = {{ region.s3cmd_region }}
            signature_v2 = False
            use_https = True

      {% endfor %}

Use Prerequisite No. 2 to obtain **<your S3 access key>** and
**<your S3 secret key>**, and use them as your actual credentials.

Creating the file using nano
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To create a configuration file manually using the **nano** text editor, run:

.. code-block:: bash

   nano ~/.s3cfg

Paste the configuration content into the editor.

Save and exit the file with:

* **CTRL+O** to write the file,
* **ENTER** to confirm the filename,
* **CTRL+X** to exit the editor.

To protect the file, set secure permissions:

.. code-block:: bash

   chmod 600 ~/.s3cfg

Using a custom configuration path
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

You can also save the configuration file to a custom location:

.. code-block:: bash

   nano ~/my-s3cfg-file

Once saved, you can use it with the **-c** option:

.. code-block:: bash

   s3cmd -c ~/my-s3cfg-file ls

The **[default]** section header is required. **s3cmd** will not recognize the
file as valid without it, and commands may fail silently or with cryptic
errors.

Maintaining separate s3cmd configuration files
----------------------------------------------

When developing in Python and **s3cmd**, the best practice is to maintain
separate configuration files and have separate environments, for example:

* production,
* testing,
* development.

By way of example, let us concentrate only on production and testing
environments.

The benefits of separating **s3cmd** config files are that:

* you do not accidentally upload or delete data in production while testing,
* each environment can use a different set of credentials, endpoints, or
  permissions,
* you retain clarity and control over which connection is active.

Example setup for production and testing environments
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Create two separate files in your home directory:

.. code-block:: bash

   nano ~/s3cfg-prod
   nano ~/s3cfg-test

Each file should contain the required configuration, with the correct
credentials for its environment.

You can then run **s3cmd** with the appropriate file using the **-c** flag:

.. code-block:: bash

   # For production
   s3cmd -c ~/s3cfg-prod ls

   # For testing
   s3cmd -c ~/s3cfg-test ls

To prevent accidental edits or exposure, restrict permissions on each file:

.. code-block:: bash

   chmod 600 ~/s3cfg-prod ~/s3cfg-test

.. tip::

   Use meaningful names such as **s3cfg-prod** and **s3cfg-test** to
   distinguish environments clearly in scripts and commands.

What to do next
---------------

You can use **s3cmd** for several common tasks:

.. ifconfig:: brand_name not in brands_without_eodata

   .. jinja:: doc_links

      * :doc:`{{ eodata_s3cmd_access }}`

.. jinja:: doc_links

   * :doc:`{{ s3cmd_access }}`