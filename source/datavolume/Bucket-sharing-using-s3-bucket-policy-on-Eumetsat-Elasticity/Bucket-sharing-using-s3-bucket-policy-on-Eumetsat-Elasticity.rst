Bucket sharing using s3 bucket policy on |brand-name|
=========================================================

S3 bucket policy
-----------------------------------

**Ceph** - the Software Defined Storage used in |brand-name| cloud, providing object storage compatibility with a subset of Amazon S3 API. Bucket policy in Ceph is part of the S3 API and allows for a selective access sharing to object storage buckets between users of different projects, in the same cloud.

Naming conventions used in this document
-----------------------------------------------

Bucket Owner
   OpenStack tenant who created an object storage bucket in their project, intending to share to their bucket or a subset of objects in the bucket to another tenant in the same cloud.

Bucket User
   OpenStack tenant who wants to gain access to a Bucket Owner's object storage bucket.

Bucket Owner's Project
   A project in which a shared bucket is created.

Bucket User's Project
   A project which gets access to Bucket Owner's object storage bucket.

Tenant Admin
   A tenant's administrator user who can create OpenStack projects and manage users and roles within their domain.

In code examples, values typed in all-capital letters, such as BUCKET_OWNER_PROJECT_ID, are placeholders which should be replaced with actual values matching your use-case.

Limitations
---------------------------

It is possible to grant access at the project level only, not at the user level. In order to grant access to an individual user,
Bucket User's Tenant Admin must create a separate project within their domain, which only selected users will be granted access to.

Ceph S3 implementation

 * supports the following S3 actions by setting bucket policy but

 * does not support user, role or group policies.

S3cmd CONFIGURATION
----------------------------

.. jinja:: doc_links

   To share bucket using S3 bucket policy you have to configure s3cmd first using this tutorial :doc:`{{ s3cmd_access }}`

Declaring bucket policy
------------------------------------



.. important::

   The code in this article will work only if the value of **Version** parameter is

   .. code::

      "Version":  "2012-10-17",

Policy JSON file's sections
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Bucket policy is declared using a JSON file. It can be created using editors such as **vim** or **nano**. Here is an example policy JSON template:

.. code::

   {
       "Id":  "POLICY_ID",
       "Version":  "2012-10-17",
       "Statement":  [
         {
           "Sid":  "STATEMENT_NAME",
           "Action":  [
             "s3:ACTION_1",
             "s3:ACTION_2"
           ],
           "Effect":  "EFFECT",
           "Resource":  "arn:aws:s3:::KEY_SPECIFICATION",
           "Condition":  {
             "CONDITION_1": {
             }
           },
           "Principal":  {
             "AWS":  [
               "arn:aws:iam::PROJECT_ID:root"
             ]
           }
         }
       ]
     }


POLICY_ID
   ID of your policy.

STATEMENT_NAME
   Name of your statement.

ACTION
   Actions that you grant access to bucket user to perform on the bucket.

PROJECT_ID
   |cloud-name| Project ID

List of actions
^^^^^^^^^^^^^^^^^^^^^^^^^

.. code::

   s3:AbortMultipartUpload
   s3:CreateBucket
   s3:DeleteBucketPolicy
   s3:DeleteBucket
   s3:DeleteBucketWebsite
   s3:DeleteObject
   s3:DeleteObjectVersion
   s3:GetBucketAcl
   s3:GetBucketCORS
   s3:GetBucketLocation
   s3:GetBucketPolicy
   s3:GetBucketRequestPayment
   s3:GetBucketVersioning
   s3:GetBucketWebsite
   s3:GetLifecycleConfiguration
   s3:GetObjectAcl
   s3:GetObject
   s3:GetObjectTorrent
   s3:GetObjectVersionAcl
   s3:GetObjectVersion
   s3:GetObjectVersionTorrent
   s3:ListAllMyBuckets
   s3:ListBucketMultiPartUploads
   s3:ListBucket
   s3:ListBucketVersions
   s3:ListMultipartUploadParts
   s3:PutBucketAcl
   s3:PutBucketCORS
   s3:PutBucketPolicy
   s3:PutBucketRequestPayment
   s3:PutBucketVersioning
   s3:PutBucketWebsite
   s3:PutLifecycleConfiguration
   s3:PutObjectAcl
   s3:PutObject
   s3:PutObjectVersionAcl

KEY_SPECIFICATION
^^^^^^^^^^^^^^^^^^^^^^^^^^^

It defines a bucket and its keys/objects. For example:

.. code::

   "arn:aws:s3:::*" - the bucket and all of its objects
   "arn:aws:s3:::MY_SHARED_BUCKET/*" - all objects of mybucket
   "arn:aws:s3:::MY_SHARED_BUCKET/myfolder/*" - all objects which are subkeys to myfolder in mybucket

Conditions
^^^^^^^^^^^^^^^^^^^

Additional conditions to filter access to the bucket. For example you can grant access to the specific IP Address using:

.. code::

   "Condition":  {
         "IpAddress":  {
           "aws:SourceIp":  "USER_IP_ADRESS/32"
         }
   }

or, alternatively, you can permit access to the specific IP using:

.. code::

   "Condition":  {
         "NotIpAddress":  {
           "aws:SourceIp":  "PERMITTED_USER_IP_ADRESS/32"
         }
    }

SETTING A POLICY ON THE BUCKET
--------------------------------------

The policy may be set on a bucket using:

.. code::

   s3cmd setpolicy POLICY_JSON_FILE s3://MY_SHARED_BUCKET command.

To check policy on a bucket, use the following command:

.. code::

   s3cmd info s3://MY_SHARED_BUCKET

The policy may be deleted from the bucket using:

.. code::

   s3cmd delpolicy s3://MY_SHARED_BUCKET


Sample scenarios
--------------------------

1 Grant read/write access to a Bucket User using his **PROJECT_ID**
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

A Bucket Owner wants to grant a bucket a read/write access to a Bucket User, using his **PROJECT_ID**:

.. code::

    {
      "Version": "2012-10-17",
      "Id": "read-write",
      "Statement": [
        {
          "Sid": "project-read-write",
          "Effect": "Allow",
          "Principal": {
            "AWS": [
              "arn:aws:iam::BUCKET_OWNER_PROJECT_ID:root",
              "arn:aws:iam::BUCKET_USER_PROJECT_ID:root"
            ]
          },
          "Action": [
            "s3:ListBucket",
            "s3:PutObject",
            "s3:DeleteObject",
            "s3:GetObject"
          ],
          "Resource": [
            "arn:aws:s3:::*"
          ]
        }
      ]
    }

Let's assume that the file with this policy is named "read-write-policy.json". To apply it, Bucket Owner should issue:

.. code::

   s3cmd setpolicy read-write-policy.json s3://MY_SHARED_BUCKET

Then, to access the bucket, for example list the bucket, Bucket User should issue:

.. code::

   s3cmd ls s3://MY_SHARED_BUCKET


2 -- Limit read/write access to a Bucket to users accessing from specific IP address range
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

A Bucket Owner wants to grant read/write access to Bucket Users which access the bucket from specific IP ranges.

(In this case, we are setting AWS to "*" which will theoretically grant access to every Project in |brand-name|, then however we are going to filter access to only one IP)

.. code::

   {
     "Id":  "Policy1654675551882",
     "Version":  "2012-10-17",
     "Statement":  [
       {
         "Sid":  "Stmt1654675545682",
         "Action":  [
           "s3:GetObject",
           "s3:PutObject"
         ],
         "Effect":  "Allow",
         "Resource":  "arn:aws:s3:::MY_SHARED_BUCKET/*",
         "Condition":  {
           "IpAddress":  {
             "aws:SourceIp":  "IP_ADRESS/32"
           }
         },
         "Principal":  {
           "AWS":  [
             "*"
           ]
         }
       }
     ]
   }

Let's assume that the file with this policy is named "read-write-policy-ip.json". To apply it, Bucket Owner should issue:

.. code::

   s3cmd setpolicy read-write-policy-ip.json s3://MY_SHARED_BUCKET

