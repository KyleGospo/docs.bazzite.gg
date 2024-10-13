---
title: Installing and Managing Applications
authors:
  - "@nicknamenamenick"
  - "@HikariKnight"
---

<!-- ANCHOR: METADATA -->
<!--{"url_discourse": "https://universal-blue.discourse.group/docs?topic=35", "fetched_at": "2024-09-03 16:43:05.697052+00:00"}-->
<!-- ANCHOR_END: METADATA -->

# Installing Software

## Linux Package Formats

> **Package formats ranked from most recommended for daily usage**:
>
> 1. [Flatpak](./Flatpak.md) - Universal package format using a permissions-based model; use for most graphical applications.
> 2. [`ujust`](./ujust.md) - Custom scripts maintained by Bazzite & Universal Blue contributors that can install applications.
> 3. [Homebrew](./Homebrew.md) - Install applications intended to run inside of the terminal (CLI/TUI).
> 4. [Distrobox](./Distrobox.md) - Intended for legacy applications that do not support Flatpak and Homebrew, or for use as development boxes.
> 5. [AppImage](./AppImage.md) - Portable universal package format that relies on specific host libraries at a system-level, usually obtained from a project's website.
> 6. [`rpm-ostree`](./rpm-ostree.md) - Layer Fedora packages at a system-level (**not recommended, use as a last resort**)

## How do I run Windows applications?

> **Use a [WINE](https://www.winehq.org/) front-end**:
>
> - [Steam](https://store.steampowered.com/) (_pre-installed_) has a Windows compatibility layer built-in.
> - [Lutris](https://lutris.net/about) (_pre-installed_) for non-Steam video games.
> - [Heroic](https://heroicgameslauncher.com/) for Epic Games, GOG, and Amazon Games integration.
> - [Bottles](https://usebottles.com/) for general-purpose applications or as an alternative to Lutris.
> - [Zoom Platform](https://www.zoom-platform.com/) has a built-in [Windows compatibility layer](https://zoom-platform.sh/) making use of [`umu-launcher`](https://github.com/Open-Wine-Components/umu-launcher).
> - [itch](https://flathub.org/apps/io.itch.itch) for games on itch.io.
> - [WineZGUI](https://github.com/fastrizwaan/WineZGUI) (_pre-installed_) for Windows applications that don’t require special considerations for their prefix.

Read the [Bazzite Gaming Guide](https://docs.bazzite.gg/Gaming/) for more information on running Windows games on Linux.

## How do I install Android applications?

Follow the [Waydroid Setup Guide](./Waydroid_Setup_Guide.md) to install Android applications on Bazzite.

> **Note**: Waydroid is **not supported** on other Universal Blue images like [Aurora](https://getaurora.dev/) and [Bluefin](https://projectbluefin.io/).

## Tutorials for Installing Other Software

- [Plex Media Server](https://universal-blue.discourse.group/t/video-tutorial-how-to-install-plex-media-server-using-distrobox-on-bazzite/1999)
  - **DISCLAIMER**: Podman, Docker, or [linuxserver.io](https://www.linuxserver.io/) is recommended over Distrobox for most software that you host.
- [Flash Games](https://universal-blue.discourse.group/t/how-to-run-old-browser-games-with-web-apps/486)

### Video Showcase of Installing Software

> **Note**: This video is missing Homebrew.

https://www.youtube.com/watch?v=ITuT23YrgPs

<hr>

**See also**: [Updates, Rollbacks, & Rebasing](../Installing_and_Managing_Software/Updates_Rollbacks_and_Rebasing/index.md)

<-- [**View all Bazzite documentation**](../index.md)
