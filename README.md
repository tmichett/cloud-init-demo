# cloud-init-demo
Cloud-Init Repo for Configuring KVM/QCOW2 images

Generate the CIData ISO image with a volume ID of **cidata**. The `user-data` contains the users, settings, and files that you want cloud-init to change. The `meta-data` contains the VM hostname and other settings, and the `vendor-data` is currently empty and could be left out.

```
genisoimage -output cidata.iso -V cidata -r -J user-data meta-data vendor-data
```

## Cloud-Init CD-ROM VM Definition Attachment

When attached, the VM will automatically identify the cloud-init settings because of the **cidata** label on the volume. The settings contained in the CD will be applied as part of the boot and cloud-init process.

/etc/libvirt/qemu/rhel9.4-cloud.xml
```
<domain type='kvm'>
  <name>rhel9.4-cloud</name>

... OUTPUT OMITTED ...

    <disk type='file' device='cdrom'>
      <driver name='qemu' type='raw'/>
      <source file='/home/kiosk/cloud/cidata.iso'/>
      <target dev='sdb' bus='sata'/>
      <readonly/>
      <address type='drive' controller='0' bus='0' target='0' unit='1'/>
    </disk>

    <controller type='usb' index='0' model='qemu-xhci' ports='15'>
      <address type='pci' domain='0x0000' bus='0x02' slot='0x00' function='0x0'/>
    </controller>
... OUTPUT OMITTED ...

  </devices>
</domain>
```
