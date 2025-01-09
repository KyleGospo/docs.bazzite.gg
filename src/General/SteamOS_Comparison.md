---
authors:
  - "@aarron-lee"
  - "@nicknamenamenick"
---

## Comparison of Bazzite vs SteamOS

### Why should I consider Bazzite over SteamOS?

Bazzite is great for users who feel that the device is too limited by SteamOS in comparison to other Linux operating systems, but do not want to sacrifice Steam Gaming Mode, stability, and the user friendliness of SteamOS.

#### Enhancements

- Bazzite generally ships newer software vs SteamOS.
  - Examples include newer graphics drivers, newer Linux kernels, KDE Plasma, etc.
- Bazzite allows you to install software on top of the base OS which means you can install software that you cannot install on SteamOS.
  - Installing such software on SteamOS requires you to unlock the root filesystem on SteamOS, and those changes will get reset from SteamOS updates.
- Android applications can be installed with [Waydroid](/Installing_and_Managing_Software/Waydroid_Setup_Guide.md) which is pre-installed.
- Works on different hardware configurations.
- Updating in Steam Gaming Mode will also update installed applications.
- Access to multiple desktop environments
  - GNOME (Not Available on SteamOS)
  - Budgie (Planned for the future)
- [`ujust`](/Installing_and_Managing_Software/ujust.md) convenience scripts for to setup software and tweaks such as supporting specific input peripherals, secure boot, and additional software.
- Useful gaming-related software preinstalled, such as Lutris, Umu-Launcher, ProtonUp-QT, Protontricks, and more
- "Fearless Updates"
  - Due to the atomic nature of Bazzite, users have access to trivially easy OS rollbacks.
  - If an OS update introduces a bug, you can simply [rollback the bad update with one simple command](/Installing_and_Managing_Software/Updates_Rollbacks_and_Rebasing/bazzite_rollback_helper.md), and wait until the bug gets fixed in a future build
  - Once bugs are fixed, then you can again just resume regular OS updates with a simple command

#### Handheld Improvements

Handheld Daemon (aka HHD) ships with Bazzite for PC handhelds, and adds the following functionality:

- Game controller support for a large selection of PC handhelds
  - See the [supported Bazzite handhelds in our Handheld Wiki](/Handheld_and_HTPC_edition/Handheld_Wiki.md)).
- Hardware controls for TDP, GPU, Power Governor, CPU Boost, etc.
- RGB controls for select devices only.
- Swipe gestures while in Steam Gaming Mode.

#### Daily Driving

- System packages that get updated on a regular basis.
  - Follows Fedora's [update cycle](https://docs.fedoraproject.org/en-US/releases/lifecycle/) and receive updates directly from upstream
    - This includes graphics drivers, the Linux kernel, and desktop environment upgrades
- Wayland is the default session for Desktop Mode.

#### For Developers

- Access to multiple package managers and repositories in [containers](/Installing_and_Managing_Software/Distrobox.md).
- [Homebrew](https://brew.sh/) is pre-installed for command-line packages.
- [Layer](/Installing_and_Managing_Software/rpm-ostree.md) Fedora packages to the system which survive between system updates.
- Host software as services using [Quadlet](/Installing_and_Managing_Software/Quadlet.md.).

#### Security Improvements

Bazzite supports LUKS Disk Encryption, Secure Boot, and TPM unlock of the encrypted disk. Bazzite also has the [Security Enhanced Linux](https://www.redhat.com/en/topics/linux/what-is-selinux) kernel module enabled and pre-configured by default. None of these are currently offered on SteamOS.  Note that, in Bazzite, disk encryption must be enabled manually during the OS installation process, and will require you to create an encryption password that you will remember to decrypt the disk.  For to not have to enter the disk decryption password on every reboot, you can configure TPM unlock via `ujust setup-luks-tpm-unlock`.  Secure Boot enables is useful for if you want to dual-boot with Windows, and requires Secure Boot for certain anti-cheat software. Read more in our [guide](/General/Installation_Guide/secure_boot.md).

>Please note: SELinux can affect certain games that run on the Source Engine, but there is a [fix](/Gaming/Common_gaming_issues.md) if you run into issues.

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
