---
authors:
  - "@nicknamenamenick"
---

<!-- ANCHOR: METADATA -->
<!--{"url_discourse": "https://universal-blue.discourse.group/docs?topic=1849", "fetched_at": "2024-09-03 16:43:16.550432+00:00"}-->
<!-- ANCHOR_END: METADATA -->

## Steam Deck (LCD & OLED)

![Steam Deck LCD|690x348, 100%](../../img/Steam_Deck_LCD.jpeg)

**Status**: Platinum

## Installing Bazzite

Read the [**Installing Bazzite on Steam Deck**](/General/Installation_Guide/Installing_Bazzite_for_Steam_Deck.md).

### Post-Installation Setup

- No additional setup required, but make sure to read the [Installation Guide](/General/Installation_Guide/Installing_Bazzite_for_Steam_Deck.md).
- It should function nearly identical to SteamOS with the benefits of [Fedora Atomic Desktop](https://fedoraproject.org/atomic-desktops/):
  - Layer Fedora packages to the image without losing them between updates/reboots.
  - Newer package upgrades including the Linux kernel and drivers.
- Regressions may occur since this Bazzite upgrades base packages faster than SteamOS.
- View our [FAQ](https://faq.bazzite.gg) for more information.

## SteamOS and Bazzite Comparison

Both run Steam Gaming Mode and share packages, but what about under the hood?  Bazzite should have most of the functionality from SteamOS with Steam Gaming Mode working as intended.  

Bazzite Steam Deck images include the latest Gamescope and packages, which means we are always ahead of SteamOS in terms of Steam Gaming Mode and Desktop Mode features.  The Quick Access Menu (accessed with the <kbd>...</kbd> button on Steam Deck) is functional for TDP, framerate limiting, scaling, etc.  Third-party software like [Decky Loader](https://decky.xyz/), [Emudeck](https://www.emudeck.com/), [RetroDeck](https://retrodeck.net/), etc. should install and function properly.

>If you want to see a more in-depth comparison, see [here](/General/SteamOS_Comparison.md)

### Does the Steam Deck image receive BIOS updates like SteamOS?

**Yes**.  If a BIOS update is available then it will install when you update Bazzite normally. It also supports controller firmware updates too.

If desired, there is a **command to disable BIOS updates** at your own risk:

```
ujust disable-bios-updates
```

<hr>

**See also**: [Steam Gaming Mode Overview](../Steam_Gaming_Mode.md)

**<-- Back to [Handheld Wiki](./index.md)**
