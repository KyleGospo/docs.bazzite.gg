---
authors:
  - "@nicknamenamenick"
  - "@HikariKnight"
  - "@lethedata"
  - "@Zeglius"
tags:
  - Guide
---

<!-- ANCHOR: METADATA -->
<!--{"url_discourse": "https://universal-blue.discourse.group/docs?topic=3781", "fetched_at": "2024-09-03 16:43:10.816923+00:00"}-->
<!-- ANCHOR_END: METADATA -->

# GNOME Disks Auto-Mount Guide

![GNOME|120x120, 50%](../img/GNOME_Disks_icon.png)

**This comes pre-installed on GNOME images.**

{% include 'automounting_guide_depr.md' %}

## Instructions

![GNOME_Disks|690x463, 75%](../img/GNOME_Disks.png)

1. Open GNOME Disks (`gnome-disk-utility`)
2. Locate the disk and partition you want to mount
3. Click the cog icon on the partition
4. Select "Edit Mount Options"
5. Turn off "User Session Default"
6. Check: "**Mount at system startup**" and "**Show in user interface**"
7. In the space where this is no label: `nosuid,nodev,nofail,x-gvfs-show,` (refer to the correct filesystem below for more options)
8. `/var/mnt/games` (or whatever directory you made)
9. `auto`
10. Select "Take Ownership"
11. Open the terminal to test the mounts by running the **command**:

    `sudo systemctl daemon-reload && sudo mount -a`

12. **If no errors appeared then it should be safe to reboot.**

If an error occurs, then research the error and undo what you did and try again.

Also a Display Name should be added too. Name it whatever you want it to be identified as.

### Filesystem Arguments

!!! warning 

    If a drive is formatted, then do not remove it from `/etc/fstab`, so the "nofail" option is a must to avoid issues with booting.

![GNOME_Edit_Mount_Options|690x465, 75%](../img/GNOME_Edit_Mount_Options.png)

![GNOME_Mount_Options|549x500, 75%](../img/GNOME_Mount_Options.png)

#### **BTRFS**:

```command
defaults,compress-force=zstd:3,noatime,lazytime,commit=120,space_cache=v2,nofail
```

#### **Ext4**:

```command
defaults,noatime,errors=remount-ro,nofail,rw,users,exec
```

#### **NTFS**:

```command
defaults,noatime,nofail,rw,users,exec
```

!!! note
    
    Bazzite does **not** support NTFS. Using the NTFS filesystem will lead to a lot of issues and should be avoided.

### Permissions for the drive

```command
sudo chown $USER:$USER /var/mnt/games
```

#### Advanced Options (Not required for most setups)

!!! warning

    Change at your own risk!

#### Information about compression:

**3** is a good balance, older CPUs should use **1**.

### Information about subvolumes:

use `subvol=name` as an option, KDE and GNOME Disks let you only mount 1 subvolume through the GUI, you can mount the root with `subvol=/` if a default subvolume is configured in the filesystem

## Installing GNOME Disks on non-GNOME images

If you would like to install this, then it can be layered to your system by entering in a terminal:

```
rpm-ostree install gnome-disk-utility
```

Reboot your system after it has finished installing the terminal.
