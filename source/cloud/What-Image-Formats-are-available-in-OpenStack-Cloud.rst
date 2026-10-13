.. meta::
   :description: What image formats are available in openstack |brand-name| cloud
   :keywords: |brand-name|, formats, available, openstack, operating systems, images, image formats

What Image Formats are Available in OpenStack |brand-name| cloud
================================================================================

In |brand-name| OpenStack ten image format extensions are available:

**QCOW2** - Formatted Virtual Machine Storage is a storage format for virtual machine disk images. QCOW stands for "QEMU copy on write". It is used with the KVM hypervisor. The images are typically smaller than RAW images, so it is often faster to convert a raw image to qcow2 for uploading instead of uploading the raw file directly. Because raw images do not support snapshots, OpenStack Compute will automatically convert raw image files to qcow2 as needed.

**RAW** - The RAW storage is the simplest one, and is natively supported by both KVM and Xen hypervisors. RAW image could be considered as the bit-equivalent of a block device file. It has a performance advantage over QCOW2 in that no formatting is applied to virtual machine disk images stored in the RAW format. No additional work from hosts is required in Virtual machine data operations on disk images stored in this format.

**ISO** - The ISO format is a disk image formatted with the read-only ISO 9660 filesystem which is used for CDs and DVDs. While ISO is not frequently considered as a virtual machine image format, because of ISOs contain bootable filesystems with an installed operating system, it can be treated like other virtual machine image files.

**VDI** - Virtual Disk Image format used by VirtualBox for image files. None of the OpenStack Compute hypervisors supports VDI directly, so it will be needed to convert these files to a different format to use them.

**VHD** -  Virtual Hard Disk format for images, widely used by Microsoft (e.g. Hyper-V, Microsoft Virtual PC).

**VMDK** - Virtual Machine Disk format is used by VMware ESXi hypervisor for images. VMWare’s products use various versions and variations of VMDK disk images, so it’s important to understand where it can be used.

**PLOOP** - A disk format supported and used by Virtuozzo to run OS Containers.

**AKI/AMI/ARI** - was the initial image format supported by Amazon EC2. The image consists of three files:

 * **AKI** - Amazon Kernel Image is a kernel file that the hypervisor will load initially to boot the image. For a Linux machine, this would be a vmlinuz file.
 * **AMI** - Amazon Machine Image is a virtual machine image in raw format, as described above.
 * **ARI** - Amazon Ramdisk Image is an optional ramdisk file mounted at boot time. For a Linux machine, this would be an initrd file.
