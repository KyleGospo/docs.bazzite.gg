---
title: Handheld Wiki
authors:
  - "@nicknamenamenick"
  - "@aarron-lee"
  - "@antheas"
  - "@wolfyreload"
---

<!-- ANCHOR: METADATA -->
<!--{"url_discourse": "https://universal-blue.discourse.group/docs?topic=1038", "fetched_at": "2024-09-03 16:43:15.186486+00:00"}-->
<!-- ANCHOR_END: METADATA -->

## Handheld Compatibility

!!! attention 

    This list is incomplete and does not indicate that unlisted handhelds do not work with Bazzite currently, but because we lack specific information regarding their post-installation setup, workarounds, and proper hardware support for Linux, they are unlisted here.

**All handhelds except for the Steam Deck make use of [Handheld Daemon](https://github.com/hhd-dev/hhd/blob/master/readme.md) for controls, TDP, etc.**

_Click the name of each hardware to view post-installation setup and known issues/workarounds._

- [**Steam Deck**](./Steam_Deck.md)
- [**Lenovo Legion Go**](./Lenovo_Legion_Go.md)
- [**ASUS ROG Ally**](./ASUS_ROG_Ally.md)
- [**GPD Handhelds**](./GPD_Handhelds.md)
- [**OneXPlayer Handhelds**](./OneXPlayer_Handhelds.md)
- [**Ayn Handhelds**](./Ayn_Handhelds.md)
- [**Ayaneo Handhelds**](./Ayaneo_Handhelds.md)
- [**Other Handhelds**](./Other_Handhelds.md)

Feel free to add new entries or update current wiki pages for your handheld following our [documentation guidelines](https://github.com/KyleGospo/docs.bazzite.gg/blob/main/README.md).

### Support Rating

Bazzite takes a similar approach to [ProtonDB’s medal system](https://www.protondb.com/) by giving a generic label rating for each handheld.

| Status | Definition
| -------- | -------- |
|**Platinum**  | No major issues and/or simple workarounds are needed for small fixes. | 
| **Gold** | Minor issues and/or simple workarounds required, but ultimately works.
| **Silver** | Major issues and/or exhaustive workarounds required, but boots and can game. |
| **Bronze**  | Major issues and/or exhaustive workarounds, but boots and displays a desktop.| 
| **Borked** | Bazzite does not boot on this hardware.
| **Unknown (_Unlisted_)** | The handheld is not listed here and a general guide is under “Other Handhelds.” |

# HHD Setup

!!! attention
    
    HHD is intended and functional for handhelds that are **not** the Steam Deck.

**Read the [HHD README](https://github.com/hhd-dev/hhd/blob/master/readme.md) for more information.**

1. Double press the 'side menu button' to access Handheld Daemon overlay in Steam Gaming Mode

2. Select the controller emulation and RGB color you want

!!! note
    
    Gyro functionality **requires** DualSense emulation

## Decky Setup

To install [Decky Loader](https://decky.xyz), open a host terminal and enter:

```bash
ujust setup-decky
```

You can access Decky Loader by pressing the 'side menu button', also known as the Quick Access Menu (QAM), once from within Steam Gamemode or Steam Big Picture Mode.

## Decky Plugins

!!! attention
    
    Decky may break or uninstall after updates especially if the Steam client or Gamescope is updated.

Install optional [Decky plugins](https://plugins.deckbrew.xyz/) for your handheld. If you experience any major issues then it is recommended to uninstall Decky before reporting Bazzite bugs.

## Bazzite's Steam Gaming Mode Documentation

Check out the [Steam Gaming Mode documentation](../Steam_Gaming_Mode.md) for an in-depth guide on Steam Gaming Mode plus general fixes for common issues.

## eGPU Support

!!! warning
    
    eGPU is **not** a fully supported feature and has many caveats.

### Caveats:

- The same [GPU hardware requirements](/Gaming/Hardware_compatibility_for_gaming.md#steam-gaming-mode-requirements) that apply for Steam Gaming Mode also apply for e-GPUs.
  - Nvidia GPUs are **unsupported**. 
- Proprietary connectors, like the one for the ASUS ROG Ally, will not work.

### Recommended External Guide & Script:

Read this [guide](https://github.com/ewagner12/all-ways-egpu) for eGPU usage on Linux, and use the script at your own risk.

<hr>

← [**View all Bazzite documentation**](/index.md)
