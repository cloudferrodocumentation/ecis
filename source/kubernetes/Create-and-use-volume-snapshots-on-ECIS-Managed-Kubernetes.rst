Create and use volume snapshots on |brand-name| Managed Kubernetes
==================================================================

Kubernetes can create a point-in-time snapshot of a persistent volume and later use that snapshot to restore data into a new PersistentVolumeClaim. Typical examples include:

* preparing a rollback point before application changes,
* testing backup and restore procedures,
* creating a recoverable copy of application data,
* restoring a previous storage state into a new volume.

Unlike cloning, which creates a new volume directly from another PVC, a snapshot creates an intermediate recovery point that can be reused later.

.. raw:: html

   <h2>What We Are Going To Cover</h2>

In this article, you will:

* create a source PersistentVolumeClaim,
* mount it in a pod and write test data,
* create a VolumeSnapshot from the source claim,
* verify that the snapshot is ready,
* create a new PersistentVolumeClaim from the snapshot,
* mount the restored volume in a second pod,
* verify that the restored volume contains the original data.

Prerequisites
-------------

.. jinja:: brand_names

   **1. Hosting account**

   You need:

   * your `{{ brand_name }} account <{{ brand_name_site_auth_link }}>`_
   * access to the |MK8s| dashboard at https://{{ mk8s_url }}

2. **A running Managed Kubernetes cluster**

.. jinja:: brand_names

   You need an existing |brand-name| Managed Kubernetes cluster and a working **kubectl** configuration for that cluster. See :doc:`/kubernetes/How-to-create-a-Managed-Kubernetes-cluster-using-ECIS-launcher-GUI`.

.. jinja:: brand_names

   3. **Supported {{ MK8s }} region**

Volume snapshot availability and storage classes depend on the region and cloud where the cluster is running. Use a cluster in a supported |MK8s| region, and always check the available storage classes and snapshot classes before creating the test resources.

.. jinja:: mk8s_regions

   {% if has_regions %}

   Available |MK8s| regions for {{ brand_name }}:

   {% for region in regions %}

   * **{{ region.display_name }}**

   {% endfor %}

   {% endif %}

4. **At least one schedulable worker node**

At least one worker node should be in the **Ready** state before you continue. To check the available nodes, run:

.. code:: bash

   kubectl get nodes -o wide

Here is what it might look like:

.. jinja:: mk8s_images

   .. figure:: {{ mk8s022 }}

A pod used to verify volume snapshots cannot run if the cluster contains only a control-plane node that is marked to reject normal workload pods.

5. **Basic knowledge of Kubernetes storage**

It is helpful to understand the difference between:

* **PersistentVolume (PV)**, which represents storage available to the cluster,
* **PersistentVolumeClaim (PVC)**, which is a request for storage made by a workload,
* **VolumeSnapshot**, which captures a point-in-time state of a volume.

6. **Available Cinder-backed storage classes**

To see which storage classes are available in your current cluster and region, run:

.. code:: bash

   kubectl get sc

The result may look like this:

.. jinja:: mk8s_images

   .. figure:: {{ mk8s023 }}

Look for storage classes whose provisioner is **cinder.csi.openstack.org**. These are Cinder-backed storage classes and are suitable for the **ReadWriteOnce** PVCs used in this article.

The exact storage class names may differ between clouds and regions. Always use the output of **kubectl get sc** as the source of truth.

In the examples below, replace **<cinder-storage-class-name>** with a valid Cinder-backed storage class from your cluster.

7. **Available VolumeSnapshotClass**

Check which snapshot classes are available in your cluster:

.. code:: bash

   kubectl get volumesnapshotclass

This article uses **cinder-csi-delete**. If your cluster uses a different Cinder-backed snapshot class, replace **cinder-csi-delete** in the examples with a class available in your cluster.

Create the source PersistentVolumeClaim
---------------------------------------

Save the following file as **snapshot-source-pvc.yaml**:

.. code:: yaml

   apiVersion: v1
   kind: PersistentVolumeClaim
   metadata:
     name: snapshot-source-pvc
   spec:
     storageClassName: <cinder-storage-class-name>
     accessModes:
       - ReadWriteOnce
     resources:
       requests:
         storage: 5Gi

Replace **<cinder-storage-class-name>** with a Cinder-backed storage class available in your cluster.

For example, if **kubectl get sc** shows a Cinder-backed storage class named **general-performance**, use:

.. code:: yaml

   storageClassName: general-performance

Apply the manifest:

.. code:: bash

   kubectl apply -f snapshot-source-pvc.yaml

Wait until the source PVC is **Bound**:

.. code:: bash

   kubectl wait --for=jsonpath='{.status.phase}'=Bound pvc/snapshot-source-pvc --timeout=180s
   kubectl get pvc snapshot-source-pvc

Do not continue until the PVC is **Bound**. If you create the snapshot before the PVC is bound to a PersistentVolume, the snapshot controller will not be able to create the snapshot.

Write data to the source volume
-------------------------------

Save the following file as **snapshot-writer-pod.yaml**:

.. code:: yaml

   apiVersion: v1
   kind: Pod
   metadata:
     name: snapshot-writer
   spec:
     containers:
     - name: app
       image: busybox
       command: ["sh", "-c", "echo hello-from-snapshot-source > /data/file.txt; sleep 3600"]
       volumeMounts:
       - mountPath: /data
         name: data
     volumes:
     - name: data
       persistentVolumeClaim:
         claimName: snapshot-source-pvc

Apply the manifest and wait for the pod to become ready:

.. code:: bash

   kubectl apply -f snapshot-writer-pod.yaml
   kubectl wait --for=condition=Ready pod/snapshot-writer --timeout=120s

To verify that the file was written successfully, run:

.. code:: bash

   kubectl exec snapshot-writer -- cat /data/file.txt

You should see:

.. code-block:: console

   hello-from-snapshot-source

Delete the writer pod
---------------------

Before creating the snapshot, delete the writer pod so that the source volume is no longer mounted by the pod.

Run:

.. code:: bash

   kubectl delete pod snapshot-writer

The result is:

.. code-block:: console

   pod "snapshot-writer" deleted

This step is necessary because the cloud storage backend, OpenStack Cinder, requires the source volume to be in the correct state before a snapshot can be created.

Before continuing, verify again that the source PVC is still **Bound**:

.. code:: bash

   kubectl get pvc snapshot-source-pvc

Create a VolumeSnapshot
-----------------------

Save the following file as **volume-snapshot.yaml**:

.. code:: yaml

   apiVersion: snapshot.storage.k8s.io/v1
   kind: VolumeSnapshot
   metadata:
     name: snapshot-copy
   spec:
     volumeSnapshotClassName: cinder-csi-delete
     source:
       persistentVolumeClaimName: snapshot-source-pvc

The value **cinder-csi-delete** means that when this **VolumeSnapshot** object is deleted, the corresponding backend snapshot is also removed.

If your cluster uses another Cinder-backed snapshot class, replace **cinder-csi-delete** with the correct value from **kubectl get volumesnapshotclass**.

Apply the manifest:

.. code:: bash

   kubectl apply -f volume-snapshot.yaml

Verify that the snapshot is ready
---------------------------------

To verify that the snapshot was created successfully, run:

.. code:: bash

   kubectl get volumesnapshot
   kubectl describe volumesnapshot snapshot-copy

The snapshot should eventually show **READYTOUSE** as **true** in the output.

You can watch the status with:

.. code:: bash

   watch -n 3 kubectl get volumesnapshot snapshot-copy

When **READYTOUSE** becomes **true**, press **Ctrl+C** to stop watching.

.. jinja:: mk8s_images

   .. figure:: {{ mk8s024 }}

Create a new PVC from the snapshot
----------------------------------

Save the following file as **snapshot-restored-pvc.yaml**:

.. code:: yaml

   apiVersion: v1
   kind: PersistentVolumeClaim
   metadata:
     name: snapshot-restored-pvc
   spec:
     storageClassName: <cinder-storage-class-name>
     accessModes:
       - ReadWriteOnce
     dataSource:
       name: snapshot-copy
       kind: VolumeSnapshot
       apiGroup: snapshot.storage.k8s.io
     resources:
       requests:
         storage: 5Gi

Use the same valid Cinder-backed storage class as in **snapshot-source-pvc.yaml**.

For example, if **kubectl get sc** shows a Cinder-backed storage class named **general-performance**, use:

.. code:: yaml

   storageClassName: general-performance

Apply the manifest:

.. code:: bash

   kubectl apply -f snapshot-restored-pvc.yaml

Wait until the restored PVC is **Bound**:

.. code:: bash

   kubectl wait --for=jsonpath='{.status.phase}'=Bound pvc/snapshot-restored-pvc --timeout=180s
   kubectl get pvc

The restored claim should show status **Bound**, which means the new volume has been created successfully from the snapshot.

.. jinja:: mk8s_images

   .. figure:: {{ mk8s025 }}

Mount the restored volume in a second pod
-----------------------------------------

Save the following file as **snapshot-reader-pod.yaml**:

.. code:: yaml

   apiVersion: v1
   kind: Pod
   metadata:
     name: snapshot-reader
   spec:
     containers:
     - name: app
       image: busybox
       command: ["sh", "-c", "cat /data/file.txt; sleep 3600"]
       volumeMounts:
       - mountPath: /data
         name: data
     volumes:
     - name: data
       persistentVolumeClaim:
         claimName: snapshot-restored-pvc

Apply the manifest:

.. code:: bash

   kubectl apply -f snapshot-reader-pod.yaml
   kubectl wait --for=condition=Ready pod/snapshot-reader --timeout=120s

Verify the restored data
------------------------

Check the pod log:

.. code:: bash

   kubectl logs snapshot-reader

If the pod starts successfully, you should see:

.. code:: text

   hello-from-snapshot-source

.. jinja:: mk8s_images

   .. figure:: {{ mk8s026 }}

This confirms that the snapshot captured the original data and that the restored PVC contains that data.

A volume snapshot captures a point-in-time state
------------------------------------------------

Volume snapshots preserve storage state at a specific point in time, but they are not the same as shared access or live synchronization.

This means:

* a snapshot captures the volume state only at the moment it is created,
* later changes to the source volume do not automatically update the snapshot,
* restoring from a snapshot creates a separate volume.

What to do next
---------------

You have now created a volume snapshot and restored a new PersistentVolumeClaim from it.

As a next step, you can compare this approach with:

.. jinja:: brand_names

   * :doc:`/kubernetes/Volume-cloning-Managed-Kubernetes`
   * Cinder-backed **ReadWriteOnce** storage for standard persistence.

Clean up the resources created in this article
----------------------------------------------

If you no longer need the test resources created in this article, delete the restored pod, the snapshot, and both PersistentVolumeClaims.

Run:

.. code:: bash

   kubectl delete pod snapshot-reader snapshot-writer --ignore-not-found
   kubectl delete volumesnapshot snapshot-copy --ignore-not-found
   kubectl delete pvc snapshot-restored-pvc snapshot-source-pvc --ignore-not-found

In the normal workflow, the writer pod was already deleted earlier in the procedure before the snapshot was created. The command above includes it as well so that the cleanup works even if you recreated it manually during testing.

The **PersistentVolumes** used in this workflow were created dynamically from the **PersistentVolumeClaims**. Because the associated storage class uses the **Delete** reclaim policy, deleting the PVCs also triggers removal of the dynamically provisioned volumes created for this test.

To verify the cleanup status, run:

.. code:: bash

   kubectl get pod
   kubectl get volumesnapshot
   kubectl get pvc
   kubectl get pv

The pods **snapshot-reader** and **snapshot-writer**, the snapshot **snapshot-copy**, and the claims **snapshot-source-pvc** and **snapshot-restored-pvc** should disappear immediately.

The corresponding dynamically created **PersistentVolumes** may remain temporarily in the **Released** state while backend cleanup is still in progress. After the cleanup finishes, they should also disappear from the output.