Kubernetes & Magnum Release Notes for |brand-name|
==========================================================================

1.9.3   24.03.2023	Magnum Backend
-----------------------------------------

Fix of problem with creating cluster with HMD master nodes. During creation of cluster with HMD master nodes "deployment to server failed" error arouse. Problem was solved by correction of configuration script.

1.9.2   17.03.2023	Magnum Backend
------------------------------------------

 * Race condition in helm charts execution resulting in unusable nginx-ingress deployment was fixed.
 * Magnum will now ensure that helm charts providing core functionality for Kubernetes clusters like CNI, CSI are executed prior to others extras helm charts (e.g. nginx-ingress) requiring cores functionality in cluster.
 * ETCD Heartbeat interval and election timeout have been returned to original values of 100ms and 1000 respectively. Previous change resulted in increased reelections in ETCD cluster when VMs storage resources are overloaded.

1.9.1   08.03.2023	Magnum default templates
---------------------------------------------------------------

Added 3 new default templates:

 * k8s-stable-localstorage-1.21.5
 * k8s-stable-localstorage-1.22.5
 * k8s-stable-localstorage-1.23.5

The templates should be used when creating a cluster with HMD flavors (local storage NVME). Creating the cluster with these templates requires adding a label: **etcd_volume_size=0**

1.9.0   06.03.2023	Magnum Backend
---------------------------------------

CHANGES:

**1.** In magnum-xena-1.9 release there is cluster creation processes logging enabled by default. It is internal logging that helps us detect problems and improve our Magnum service. Following components are gathered by log collector:

    - */var/log/heat-config/heat-config-script/* - output of magnum heat scripts used to deploy and configure k8s system
    - cloud-controller-manager (in-cluster *daemonset*) logs
    - node-problem-detector (in-cluster *daemonset*) logs

   Log collector (fluent-bit) is installed during cluster creation, gathers and sents metioned logs and is removed during cleanup phase after cluster is created.

   If you wish to disable this service, please set label logging_enabled to false

**2.** ETCD loadbalancer is no longer created by default (applied in cases when API loadbalancer was created). This change should not cause any effects, as this loadbalancer was never really used by the cluster.

**3.** ETCD parametrization via labels and timing parameters tuning:

     - etcd_compaction_retention
     - etcd_heartbeat_interval
     - etcd_election_timeout
     - etcd_snapshot_count

Heartbeat interval has been decreased from default 100 ms to 10 ms as a result of tuning for intracloud RTT (~ 1 ms between master nodes avg). Same case for election timeout - decreased from 1 s to 100 ms. ETCD's quota backend bytes now is set automatically with size of the disk.

**4.** Nginx-ingress opt-in helm chart now configures ProxyProtocol by default, which supports getting Real-IPs from clients connecting to ingresses.

**5.** Fedora CoreOS kernel setting /proc/sys/fs/inotify/max_user_instances has been increased to 8192 from default 128.

1.8.0   21.12.2023	Magnum Backend
--------------------------------------

 * Fix - after manual resize of cluster, scheduler does not recognize the added nodes

 * Fix - after autoheal the fixed node is not schedulable

 * Move to Helm deployment of Cinder CSI

 * Fix - autohealer does not work on master nodes

 * Monitoring of LB API on /healthz endpoint

 * Fix of "Fresh clusters come with a wrong /etc/kubernetes/certs/ca.crt

 * Fix - Script make-cert.py generates always same certificate to ca.rt

1.7.0   01.12.2023	Magnum Backend
---------------------------------------

 * Fix of ingress resource floating IP generation

 * Fix of labelling nodes with ingress

 * Fix of makecert.sh and certificate cache

 * LB fix - accepts empty flavor

 * Fix of python_module:oslo.service.loopingcall

 * Fix of 500 errors with Magnum on WAW3-1

 * Fix of nodegroups with Cilium

1.6.0   12.09.2022	Magnum Backend
------------------------------------------

Improvement when user adds nodes manually from Horizon UI. When the number of nodes being added from Horizon exceeds the max_node_count in the default group, the max_node_count will get updated to the requested value.

1.5.0   08.09.2022	Magnum Backend
-------------------------------------------

 * Storage classes are now available by default for HDD and SSD

 * Config for default delete LB timeout changed

 * Systemd restarts a failed service

 * Selinux fixes for Calico

1.4.1   22.08.2022	Magnum backend
--------------------------------------------------

 * Remove unnecessary tracebacks when not finding certificates

1.4.0   11.08.2022	Magnum backend
-----------------------------------------

 * New Kubernetes versions 1.22 and 1.23 added

1.3.0   10.08.2022	Magnum backend
--------------------------------------------

 * Enable LB flavor selection (API and ETCD) in Magnum backend

1.2.0   09.08.2022	Magnum backend
----------------------------------------

 * Move to Helm deployment in Calico

 * Cilium support - changes in Helm

1.1.2   08.08.2022	Magnum backend
------------------------------------------

 * Fix long response times when new instance is created

1.1.1   27.07.2022	Magnum backend
---------------------------------------

 * SQL alchemy issues in Magnum logs

1.0.1 -- 5th of July 2022
-------------------------------------------------------

 * Encourage users to use magnum-auto-healer controller when enabling auto-healing capabilities in Magnum.

1.0.0 -- 1st of July 2022 Magnum UI
------------------------------------------------

 * "NGINX" is available in the "Ingress Controller" dropdown.

 * "Enable Load Balancer for Master Nodes" checkbox. Must be checked when number of masters is greater than 1.

 * "EODATA access enabled" checkbox in the "Addon Software".

 * "Use an Existing Subnet" dropdown is available when "Create New Network" is unchecked.

 * Network driver validation in the cluster templates form. The options available depend on the selected Container Orchestration Engine.

 * Volume driver validation in the cluster templates form. The options available depend on the selected Container Orchestration Engine.

 * Magnum UI version is upgraded to Xena version.

 * Fix eodata network search. Now eodata is searching by tags: "eodata-access", "eodata_access".

 * Support proxy protocol for Load Balancer services with ingress hostname.

 * New boolean label is available: "enable_ingress_hostname". Default value: "false".

 * Autoscaler automaticaly detects all new nodegroups with "worker" role assigned.

 * The "worker" role is assigned by default if not specified. The maximum number of nodes must be specified.

 * Fix routing issue when eodata network is attached by adding an ip autodetection method to calico-node deployment.

 * Fedora CoreOS 35 is now supported in Magnum.

1.0.0   13.06.2022	Magnum UI/Backend
--------------------------------------------------

In production, after staging improvements with:

 * Fix of "Metrics server not available at times, making scaling not possible"

 * Improve validation in Horizon to not allow entries which cannot succeed