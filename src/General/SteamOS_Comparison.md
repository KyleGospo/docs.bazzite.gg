---
authors:
  - "@nicknamenamenick"
  - "@aarron-lee"
---

## Comparison of Bazzite vs SteamOS

### Why should I consider Bazzite over SteamOS?

Bazzite is great for users who feel that the device is too limited by SteamOS in comparison to other Linux operating systems, but do not want to sacrifice Steam Gaming Mode, stability, and the user friendliness of SteamOS.

#### Security Improvements

Bazzite supports Luks Disk Encryption, Secure Boot, and TPM unlock of the encrypted disk. Bazzite also has the [Security Enhanced Linux](https://www.redhat.com/en/topics/linux/what-is-selinux) kernel module enabled by default. None of these are offered on SteamOS.

Disk encryption is important on mobile devices, such as PC handhelds, for security. Without an encrypted disk, a thief or malicious actor can just pull out your unencrypted disk, and read your data directly off it.

Note that, in Bazzite, disk encryption must be enabled manually during the OS installation process, and will require you to make a password for to decrypt the disk.

For to not have to enter the disk decryption password on every reboot, you can configure TPM unlock via `ujust setup-luks-tpm-unlock`.

And finally, Secure Boot enables is useful for if you want to Dual boot with Windows, and requires Secure Boot for certain anti-cheat software. See guide [here](/General/Installation_Guide/secure_boot.md)

#### Enhancements

- Bazzite generally ships newer software vs SteamOS
  - Examples include newer AMD Graphics drivers, newer kernels, newer versions of the KDE Desktop, etc.
- Bazzite allows you to install software overlaid on top of the immutable root base OS, which means you can install software that you cannot install on SteamOS
  - installing such software on SteamOS requires you to unlock the root filesystem on SteamOS, and those changes will get reset from SteamOS updates
- Android applications can be installed with [Waydroid](/Installing_and_Managing_Software/Waydroid_Setup_Guide.md)
  - while you can install Waydroid on SteamOS too, it requires unlocking the root filesystem, so those changes will get reset from SteamOS updates too.
- Works on different hardware configurations (nvidia, desktops, handhelds, etc.)
- Updating in Steam Gaming Mode will also update installed applications
- Access to multiple desktop environments
  - KDE
  - GNOME (Not Available on SteamOS)
- [`ujust`](/Installing_and_Managing_Software/ujust.md) convenience scripts for to setup software and tweaks such as supporting specific input peripherals, secure boot, OpenRGB, Sunshine, etc
- Useful gaming-related software preinstalled, such as Lutris, Umu-Launcher, ProtonUp-QT, Protontricks, and more
- "Fearless Updates" - Due to the atomic nature of Bazzite, users have access to trivially easy OS rollbacks
  - if an OS update introduces a bug, you can simply [rollback the bad update with one simple command](/Installing_and_Managing_Software/Updates_Rollbacks_and_Rebasing/bazzite_rollback_helper.md), and wait until the bug gets fixed in a future build
  - once bugs are fixed, you can again just resume regular OS updates with a simple command

#### HHD-related improvements

Handheld Daemon (aka HHD) ships with Bazzite for PC handhelds, and adds the following functionality:

- Game Controller support for a large selection of PC handhelds (see [supported devices](https://github.com/hhd-dev/hhd?tab=readme-ov-file#supported-devices))
- Hardware controls for TDP, GPU, Power Governor, CPU Boost, and more
- RGB controls (select devices only)
- Swipe gestures for Steam/QAM menus while in gamescope-session (aka Steam Game Mode)
- and more

#### Daily Driving

- System packages that get updated on a regular basis
  - Follows Fedora's [update cycle](https://docs.fedoraproject.org/en-US/releases/lifecycle/) and receive updates directly from upstream
    - This includes graphics drivers, the Linux kernel, and desktop environment upgrades
- Printer and Printing support out of the box
- Wayland is the default session for Desktop Mode

#### For Developers

- Access to multiple package managers and repositories in [containers](/Installing_and_Managing_Software/Distrobox.md)
- [Homebrew](https://brew.sh/) is preinstalled
- [Layer](/Installing_and_Managing_Software/rpm-ostree.md) Fedora packages to the system which survive between updates
- (Work in Progress) Docker support

### Will there be any performance improvements with Bazzite?

Performance should be on par with SteamOS, and every game capable of running on SteamOS should run on Bazzite. Bazzite and SteamOS share the same packages, so the difference is usually negligible.

However there are some **advantages** that Bazzite may have in some edge cases:

- Performance Governor
  - Bazzite uses powersave w/ [`amd-pstate`](https://www.kernel.org/doc/html/latest/admin-guide/pm/amd-pstate.html) which is more efficient on the hardware
- MGLRU is already enabled by default by Fedora
- Watchdog is disabled by default
- Memory lock is tweaked for [RPCS3](https://rpcs3.net/)
- Kyber I/O scheduler is used
- File access times is disabled
- Transparent Huge Pages is not used
  - Bazzite does not use a swapfile and rely on zram with zstd by default (compressed memory)
- Kernel is using 1000hz tick

> Performance tweaks are sourced from this [Medium article](https://medium.com/@a.b.t./here-are-some-possibly-useful-tweaks-for-steamos-on-the-steam-deck-fcb6b571b577).
