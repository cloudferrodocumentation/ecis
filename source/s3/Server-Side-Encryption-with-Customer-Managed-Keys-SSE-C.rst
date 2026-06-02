Server-Side Encryption with Customer-Managed Keys (SSE-C) on |brand-name|
=========================================================================

Introduction
------------

This guide explains how to encrypt your objects server-side with SSE-C.

Server-side encryption protects data at rest. It encrypts the object data
stored in Object Storage. Server-side encryption with customer-provided
encryption keys (SSE-C) lets you provide your own encryption key for an
object. The server uses that key to encrypt the object while writing it to
disk and to decrypt it when you access the object again.

With SSE-C, you are responsible for managing the encryption key. The server
does not store the key. It uses the key only during the request and removes it
from memory after the operation is complete.

When you upload an object with SSE-C, the server applies AES-256 encryption by
using the key you provide. To access the object later, you must provide the
same key again. The server verifies that the provided key matches the object
and then decrypts the object before returning it to you.

Requirements
------------

* A bucket.

  .. jinja:: doc_links

     :doc:`{{ object_storage }}`

* A user with the required access rights on the bucket.

* S3 credentials.

  .. jinja:: doc_links

     :doc:`{{ ec2_credentials }}`

* The AWS CLI installed and configured.

If you have not used the AWS CLI before, install it first:

.. code-block:: bash

   sudo apt install awscli

Then configure it:

.. code-block:: bash

   aws configure

   AWS Access Key ID [None]: <your S3 Access Key>
   AWS Secret Access Key [None]: <your S3 Secret Key>
   Default region name [None]: <enter>
   Default output format [None]: <enter>

SSE-C at a glance
-----------------

* S3 rejects SSE-C requests sent over HTTP. Use HTTPS only.

* If you accidentally send an SSE-C request over HTTP, discard the key and
  rotate it as appropriate.

* The ETag in the response is not the MD5 hash of the object data.

* You are responsible for managing encryption keys and keeping track of which
  key was used for which object.

* If bucket versioning is enabled, each object version can have its own
  encryption key.

.. attention::

   If you lose the encryption key, the object is also lost. The server does
   not store SSE-C encryption keys, so it is not possible to access the data
   again without the original key.

REST API
--------

To encrypt or decrypt objects in SSE-C mode, the following headers are
required:

.. jinja:: caption_colors

   .. list-table::
      :widths: 50 25 50
      :header-rows: 1

      * - :{{ header }}:`Header`
        - :{{ header }}:`Type`
        - :{{ header }}:`Description`
      * - x-amz-server-side-encryption-customer-algorithm
        - string
        - Encryption algorithm. Must be set to **AES256**.
      * - x-amz-server-side-encryption-customer-key
        - string
        - 256-bit base64-encoded encryption key used in the server-side
          encryption process.
      * - x-amz-server-side-encryption-customer-key-MD5
        - string
        - Base64-encoded 128-bit MD5 digest of the encryption key according to
          `RFC 1321 <https://www.rfc-editor.org/rfc/rfc1321>`_. It is used to
          verify that the encryption key was not corrupted during transport and
          encoding.

.. note::

   Calculate the MD5 digest of the key before base64 encoding.

These headers apply to the following API operations:

* PutObject
* PostObject
* CopyObject, for target objects
* HeadObject
* GetObject
* InitiateMultipartUpload
* UploadPart
* UploadPart-Copy, for target parts

Example No. 1: Generate header values
-------------------------------------

You can define the encryption key directly:

.. code-block:: bash

   secret="32bytesOfTotallyRandomCharacters"
   key=$(echo -n "$secret" | base64)
   keymd5=$(echo -n "$secret" | openssl dgst -md5 -binary | base64)

Alternatively, you can generate the key and store it in a file:

.. code-block:: bash

   openssl rand 32 > sse-c.key
   key=$(cat sse-c.key | base64)
   keymd5=$(cat sse-c.key | openssl dgst -md5 -binary | base64)

Example No. 2: Upload an object with aws-cli s3api
--------------------------------------------------

Use the following command to upload an object with SSE-C encryption enabled.

.. jinja:: regional_clouds

   .. tabs::

      {% for region in regions %}
      .. tab:: {{ region.display_name }}

         .. code-block:: bash

            aws s3api put-object \
              --bucket bucket-name \
              --key object-name \
              --body contents.txt \
              --sse-customer-algorithm AES256 \
              --sse-customer-key "$key" \
              --sse-customer-key-md5 "$keymd5" \
              --endpoint-url {{ region.s3_endpoint }}

      {% endfor %}

Example No. 3: Upload an object with aws-cli s3
-----------------------------------------------

You can also upload the object with the high-level **aws s3** command.

.. jinja:: regional_clouds

   .. tabs::

      {% for region in regions %}
      .. tab:: {{ region.display_name }}

         .. code-block:: bash

            aws s3 cp file.txt s3://bucket-name/ \
              --sse-c-key "$secret" \
              --sse-c AES256 \
              --endpoint-url {{ region.s3_endpoint }}

      {% endfor %}

Example No. 4: Upload an object with a key file
-----------------------------------------------

If the encryption key is stored in a file, use the **fileb://** prefix.

.. jinja:: regional_clouds

   .. tabs::

      {% for region in regions %}
      .. tab:: {{ region.display_name }}

         .. code-block:: bash

            aws s3 cp file.txt s3://bucket/ \
              --sse-c-key fileb://sse-c.key \
              --sse-c AES256 \
              --endpoint-url {{ region.s3_endpoint }}

      {% endfor %}

.. note::

   This article uses **AWS CLI** for SSE-C operations. The documented
      **s3cmd** options do not currently provide the same SSE-C workflow as AWS
      CLI options such as **--sse-c**, **--sse-c-key**, and the corresponding
      **s3api** SSE-C parameters.

Download the encrypted object
-----------------------------

To download an object encrypted with SSE-C, provide the same encryption key
that was used during upload.

Use this form if the key is stored in the **secret** variable:

.. jinja:: regional_clouds

   .. tabs::

      {% for region in regions %}
      .. tab:: {{ region.display_name }}

         .. code-block:: bash

            aws s3api get-object \
              --bucket <bucket_name> \
              --key <object_key> \
              --sse-customer-key "$secret" \
              --sse-customer-algorithm AES256 \
              --endpoint-url {{ region.s3_endpoint }} \
             <file_name>

      {% endfor %}

Use this form if the key is stored in a file:

.. jinja:: regional_clouds

   .. tabs::

      {% for region in regions %}
      .. tab:: {{ region.display_name }}

         .. code-block:: bash

            aws s3api get-object \
              --bucket <bucket_name> \
              --key <object_key> \
              --sse-customer-key fileb://<key_name> \
              --sse-customer-algorithm AES256 \
              --endpoint-url {{ region.s3_endpoint }} \
             <file_name>

      {% endfor %}