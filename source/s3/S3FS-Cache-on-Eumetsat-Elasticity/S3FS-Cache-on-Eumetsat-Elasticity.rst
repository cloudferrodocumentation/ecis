S3FS cache on |brand-name|
==========================

By default, S3FS cache may be enabled in preconfigured Linux images on
|brand-name|. If the **/eodata** repository is mounted through **s3fs**, you
can check the cache configuration in **/etc/fstab**.

The entry may look similar to this:

.. jinja:: regional_clouds

   .. tabs::

      {% for region in regions %}
      .. tab:: {{ region.display_name }}

         .. code-block:: text

            #s3fs#eodata /eodata fuse passwd_file=/root/.passwd-s3fs,_netdev,allow_other,use_path_request_style,uid=0,umask=0222,mp_umask=0222,gid=0,stat_cache_expire=20,url={{ region.eodata_endpoint }},use_cache=1,max_stat_cache_size=60000,list_object_max_keys=10000 0 0

      {% endfor %}

In this example, the **use_cache** parameter points to the cache directory
**/1**. The value **1** is interpreted as a directory name at the beginning of
the filesystem hierarchy.

The **s3fs** documentation describes this option as follows:

.. code-block:: text

   -o use_cache (default="" which means disabled)
   local folder to use for local file cache.

Directory **/1** is therefore used as a local cache destination for products
from the **EODATA** repository during processing or downloading.

Clearing the cache
------------------

If you encounter problems with displaying folders or files inside **/eodata**,
for example errors such as **No such file or directory**, empty the **/1**
folder.

Before doing this, make sure that no process is currently using files from
**/eodata** or from the cache directory.

Preventing disk space problems
------------------------------

If the cache directory occupies too much disk space, you may have problems
remounting the **/eodata** repository.

A common error message is:

.. code-block:: text

   clnt_create: RPC: Timed out
   s3fs: There is no enough disk space for used as cache(or temporary) directory by s3fs.

To reduce the risk of this situation, consider setting the **ensure_diskfree**
parameter in the **s3fs** mount configuration.

The **s3fs** documentation describes this option as follows:

.. code-block:: text

   -o ensure_diskfree(default 0)

This option defines the minimum amount of free disk space that should remain
available on the disk used for the **s3fs** cache. **s3fs** creates files for
downloading, uploading, and caching. If the available free space is smaller
than the configured value, **s3fs** avoids using additional disk space where
possible, at the cost of lower performance.

Example with ensure_diskfree
----------------------------

The following example keeps the same structure as the previous **/etc/fstab**
entry, but adds **ensure_diskfree**.

.. jinja:: regional_clouds

   .. tabs::

      {% for region in regions %}
      .. tab:: {{ region.display_name }}

         .. code-block:: text

            #s3fs#eodata /eodata fuse passwd_file=/root/.passwd-s3fs,_netdev,allow_other,use_path_request_style,uid=0,umask=0222,mp_umask=0222,gid=0,stat_cache_expire=20,url={{ region.eodata_endpoint }},use_cache=1,ensure_diskfree=1024,max_stat_cache_size=60000,list_object_max_keys=10000 0 0

      {% endfor %}

In this example, **ensure_diskfree=1024** tells **s3fs** to avoid using the
cache disk when less than 1024 MB of free space remains.

Adjust this value to match the size of your disk and the expected workload.
After editing **/etc/fstab**, reload systemd and remount the resource if
needed:

.. code-block:: bash

   sudo systemctl daemon-reload
   sudo mount /eodata