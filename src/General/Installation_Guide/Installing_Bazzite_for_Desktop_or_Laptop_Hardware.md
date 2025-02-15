---
authors:
  - "@nicknamenamenick"
  - "@KyleGospo"
  - "@storyaddict"
  - "@castrojo"
  - "@noelmiller"
  - "@rothgar"
---

<!-- ANCHOR: METADATA -->
<!--{"url_discourse": "https://universal-blue.discourse.group/docs?topic=1146", "fetched_at": "2024-09-03 16:43:27.199924+00:00"}-->
<!-- ANCHOR_END: METADATA -->

![Desktop|690x448](../../img/Desktop.jpeg)

## Pre-Installation

> Pre-requisites and steps before installing Bazzite.

### Minimum System Requirements

- **Architecture**: x86_64
- **Firmware**: UEFI (CSM Support should be **disabled** if available)
- **Processor (CPU)** : 2GHz quad core processor or better
- **System Memory (RAM)**: 4GB
- **Graphics**: A graphics card that can utilize Vulkan 1.3+
- **Storage**: 64GB free on an internal solid-state drive
- **Network**: Stable internet connection with no bandwidth caps
- **Additional Notes**: Certain drivers are **not** compatible with Bazzite
  - For example: [a list of compatible USB Wi-Fi adapters](https://github.com/morrownr/USB-WiFi/blob/main/home/USB_WiFi_Adapters_that_are_supported_with_Linux_in-kernel_drivers.md) 

#### Installer Requirements

- A USB flash drive with 10GB free space
  - **Note**: All data on this drive will be wiped when flashed
- Software to flash the image:
  - [Fedora Media Writer](https://www.fedoraproject.org/en/workstation/download/), [Ventoy](https://www.ventoy.net/en/index.html), or [Rufus](https://rufus.ie/en/)
    - Make sure to properly eject the drive after flashing the ISO to it
- Physical keyboard

{% include 'desktop_envs.md' %}

### Dual Boot Preliminary Setup + Post-Setup Guide

Read the [Dual Boot Guide](./dual_boot_setup_guide.md) **after** reading this guide before proceeding.

## Installation Guide

> The part of the guide that requires the most effort.

### 1. Download and Flash Bazzite

- Download [Bazzite](https://download.bazzite.gg) after choosing the correct ISO for your hardware with our Image Picker tool.
- Flash Bazzite to your bootable medium.
- Eject drive.

#### Current Fedora Atomic Desktop Users

Current [Fedora Atomic Desktop](https://fedoraproject.org/atomic-desktops/) users can rebase with the terminal command listed on the website under the "**Existing Fedora Atomic Desktop Users**" section and can skip the next step.

### 2. Boot Bazzite

- Connect your bootable medium to your device and boot into it.
- After connecting the device, boot into the Bazzite installer.
- This depends on your motherboard hardware, but most of the time it could be a function keys like <kbd>F9</kbd> or similar.
  - Sometimes you need to consult the manual, look up your device online, or read any hotkeys that appear when you boot your PC.
    - Alternatively change the BIOS settings to boot with your bootable device first before your current storage, but this is **not recommended** to keep enabled after installing Bazzite.
- Verify the media correctly and proceed to the installer.

### 3. Installer

![Installer](../../img/anaconda_installer.png)

![Automatic drive configuration|690x497, 75%](../../img/anaconda_drive_configuration.png)

![User setup example|690x359, 75%](../../img/anaconda_user_setup.png)

- Select your language, region, keyboard layout, and time zone.
- Select the drive that Bazzite is going to be installed on.
  - Delete any partitions that you have remaining on the drive **unless dual booting on the same drive**.
  - Recommended to use the automatic storage configuration **unless dual booting on the same drive**.
- Optionally encrypt the drive with a password if desired.
  - **If you lose this password, then it cannot be decrypted**.
- Setup a user account.
  - Give administrative privileges and **set a user password**.
- Begin the installation.
- Reboot device after it has finished installing.

#### Important information for users with Secure Boot **enabled**:

Read the [Secure Boot Guide](https://universal-blue.discourse.group/docs?topic=2742) for more information.

<hr>

## Post-Installation

> The fine tuning before gaming.

### GRUB Menu

![Rollbacks|690x402, 50%](../../img/GRUB_Menu.png)

The first boot will show a screen showing your current and last deployment. It is important to note that the GRUB menu can be used to rollback Bazzite deployments if you encounter issues.

Read more about this in the [Updates, Rollback, and Rebasing documentation](../../Installing_and_Managing_Software/Updates_Rollbacks_and_Rebasing/index.md).

### Configuring System Settings for KDE Plasma and GNOME

![Display Settings (KDE Plasma)|690x370, 75%](../../img/KDE_Display_Settings.png)
**_KDE Plasma's System Settings application_**

![Display Settings (GNOME)|690x344, 75%](../../img/GNOME_Display_Settings.png)
**_GNOME's Settings application_**

It is important to configure the system settings on a first boot to personalize your desktop especially if you notice the scaling is incorrect on first-boot.

### First Boot Setup Utility: Bazzite Portal

![Welcome to Bazzite|618x500, 75%](../../img/yafti_welcome.jpeg)

!!! attention 

    Make sure you are connected to the internet.

An application will pop up welcoming you to Bazzite when you boot into the desktop for the first time. This is a utility that allows you to tailor Bazzite to your liking by installing additional software.

- Click "Next" to begin configuring Bazzite.
- Press the toggle switch button next to the item to have the option enabled or disabled for your installation, some are already toggled on by default.
- If you would like to customize any of the options, then press the arrow next to the toggle switch button if available.
- Installing items from the portal **may take a long time**.

!!! attention
    
    There is a rare chance you will be asked to setup KDE Wallet or GNOME Keyring and set a password to continue installing items from the Bazzite Portal.

### Installing additional software

The [Installing and Managing Applications documentation](../../Installing_and_Managing_Software/index.md) is useful to learn how to install additional software on Bazzite outside of the Bazzite Portal.

### Calculating ISO SHA256 Checksum Hash

https://www.youtube.com/watch?v=wUDbMJtR1sM

## Ready to Game

**You have now installed Bazzite!**

View our [Gaming Guide](../../Gaming/index.md) for a quick rundown of Linux gaming, useful resources, and setting up Proton on Steam.

Check out the additional [documentation](/index.md) surrounding the project.

<hr>

## **Video Tutorial - Dual Boot Setup w/ Secure Boot Enabled**:

https://www.youtube.com/watch?v=pbxM_1ZJCCc

<hr>

## Issues Installing Bazzite?

View the [Installation Troubleshoot Guide](./troubleshoot_guide.md).

<hr>

**See also:** [Upstream Manual Partitioning Guide](https://docs.fedoraproject.org/en-US/fedora-silverblue/installation/#manual-partition) & [Auto-Mounting Secondary Drives](../../Advanced/Auto-Mounting_Secondary_Drives.md)

<-- [**View all Bazzite documentation**](../../index.md)
