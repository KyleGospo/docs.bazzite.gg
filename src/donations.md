---
title: Credits and Donating
---

{% macro contributor(real_name, github, description, sponsor) -%}
    <div style="
    display: inline-flex;
    flex-direction: row;
    gap: 0.5rem;
    align-items: center;
    background-color: #00000066;
    border-radius: 24px;
    padding: 0.3rem;
    padding-right: 0.4rem;
    min-width: 200px;"
    >
        {% if github %}
            <img
            src="https://github.com/{{ github }}.png?size=60" class="no-lightbox"
            loading="lazy"
            style="max-height:60px;
                border-radius: 24px;"
            >
        {% endif %}
        <div>
            {% if github %}
                <a href="https://github.com/{{ github }}">{{ real_name }}</a>
            {% else %}
                <span>{{ real_name }}</span>
            {% endif %}
            {% if sponsor %}
                <small><a href="{{ sponsor }}">(Sponsor)</a></small>
            {% endif %}
            <div><small>{{ description or "" }}</small></div>
        </div>
    </div>
{%- endmacro %}

## Bazzite Maintainers/Contributors & Universal Blue Alumni

Love Bazzite and want to help sustain it's development?  Consider **sponsoring** the maintainers and contributors of the project.

This list contains members who have contributed heavily to Bazzite and/or the [**Universal Blue project**](https://ublue.it) since 2021 which includes past contributors who may not be active with the project currently.

<sub>(*If we missed a major contributor, then [**please let us know**](https://github.com/KyleGospo/docs.bazzite.gg/issues) or [**PR a fix**](https://github.com/KyleGospo/docs.bazzite.gg/blob/main/src/donations.md)!*)</sub>

<div style="display: flex; flex-wrap: wrap; gap: 0.3rem;">
{{ contributor("Kyle Gospodnetich", "KyleGospo", "Founder / Lead Maintainer", "https://github.com/sponsors/KyleGospo") }}
{{ contributor("Antheas Kapenekakis", "antheas", "Handheld Daemon Lead Maintainer / Handheld Support", "https://github.com/sponsors/antheas") }}
{{ contributor("HikariKnight", "HikariKnight", "Virtualization Support / Scripting", "https://github.com/sponsors/HikariKnight") }}
{{ contributor("Noel Miller", "noelmiller", "Installer Enhancements / Custom Image Tooling / Marketing", "https://github.com/sponsors/noelmiller") }}
{{ contributor("RJ Trujillo", "EyeCantCU", "Tooling for CI/CD Pipelines / Initial Support for Alternate Desktop Environments") }}
{{ contributor("Zeglius", "Zeglius", "Documentation Maintenance / Scripting") }}
{{ contributor("Aarron Lee", "aarron-lee", "SimpleDeckyTDP / Scripting / Command-Line Utilities") }}
{{ contributor("Matthew Schwartz", "matte-schwartz", "Steam Gaming Mode Testing and Consulting") }}
{{ contributor("Bouhaa", "BoukeHaarsma23", "Steam Gaming Mode Testing and Consulting") }}
{{ contributor("Jan", "Jan200101", "Kernel Patches") }}
{{ contributor("Jason Nagin", "JasonN3", "Creator of Build Container Installer") }}
{{ contributor("Sterophonick", "Sterophonick", "Driver Backports / Game Fixes") }}
{{ contributor("dreamyuki", "dreamyukii", "Scripting") }}
{{ contributor ("Adelia", "adeliasvg", "Branding Manager") }}
{{ contributor("Sean Srock", "SuperRiderTH", "Animator / Bug Fixing") }}
{{ contributor("wolfyreload", "wolfyreload", "Video Tutorials / Documentation") }}
{{ contributor("Kurt Himebauch", "xXJSONDeruloXx", "Decky Plugins / ujust Extraordinaire") }}
{{ contributor("Benjamin Sherman", "bsherman", "Image Maintenance") }}
{{ contributor("Brian Ketelsen", "bketelsen", "Image Maintenance") }}
{{ contributor("Robert Sturla", "p5", "Image Maintenance") }}
{{ contributor("m2", "m2Giles", "Image Maintenance") }}
{{ contributor("Niklas Haiden", "NiHaiden", "Image Maintenance") }}
{{ contributor("Tulip Blossom", "tulilirockz", "Image Maintenance", "https://github.com/sponsors/tulilirockz") }}
{{ contributor("Gareth Widlansky", "gerblesh", "Image Maintenance") }}
{{ contributor("Ryan Brue", "ryanabx", "Image Maintenance") }}
{{ contributor("Ian Off", "atimeofday", "Documentation / Testing") }}
{{ contributor("XYNY", "xynydev", "Alternate Custom Image Tooling / Infographics") }}
{{ contributor("FiftyDinar", "fiftydinar", "Alternate Custom Image Tooling / Bug Fixes") }}
{{ contributor("RoyalOughtness", "RoyalOughtness", "Security Consulting", "https://github.com/sponsors/RoyalOughtness") }}
{{ contributor("Gecked-Deck", "Gecked-Deck", "Technical Support / Social Media") }}
{{ contributor("termdisc", "termdisc", "Technical Support") }}
{{ contributor("Crono", "EPOCHvoyager", "Translations / Performance Scheduler Enthusiast") }}
{{ contributor("Justin Garrison", "rothgar", "Developer Relations") }}
{{ contributor("Tony", "cyrv6737", "Pilot") }}
{{ contributor("jerb", "jerbmega", "Early Tester") }}
{{ contributor("boredsquirrel", "boredsquirrel", "Early Tester") }}
{{ contributor("Weaver Marquez", "weavermarquez", "Early Tester") }}
{{ contributor("Marco Ceppi", "marcoceppi", "Contributor Emeritus") }}
{{ contributor("Adam Israel", "AdamIsrael", "Contributor Emeritus") }}
{{ contributor("Joseph of Earth", "", "Contributor Emeritus") }}
{{ contributor("Pat Connors", "nicknamenamenick", "Contributor Emeritus") }}
{{ contributor("Marco Rodolfi", "RodoMa92", "Contributor Emeritus") }}
{{ contributor("CharlieBros", "CharlieBros", "Contributor Emeritus") }}
{{ contributor("xAlphaKat", "xAlphaKAT", "Contributor Emeritus") }}
{{ contributor("Alex Banna", "abanna", "Contributor Emeritus") }}
{{ contributor("bobslept", "bobslept", "Contributor Emeritus") }}
{{ contributor("Primož Ajdišek", "bigpod98", "Contributor Emeritus") }}
{{ contributor("Alex Díaz", "akdev1l", "Contributor Emeritus") }}
{{ contributor("Johnny Arcitec", "Arcitec", "Contributor Emeritus") }}
{{ contributor("Dylan M. Taylor", "dylanmtaylor", "Contributor Emeritus") }}
{{ contributor("Nathaniel Warburton", "storyaddict", "Contributor Emeritus") }}
{{ contributor("Joshua Stone", "joshua-stone", "Contributor Emeritus") }}
{{ contributor("dhoell", "dhoell", "Contributor Emeritus") }}
{{ contributor("Cassidy James Blaede", "cassidyjames", "Contributor Emeritus", "https://github.com/sponsors/cassidyjames") }}
{{ contributor("Jorge Castro", "castrojo", "Dinosaur Guy", "https://github.com/sponsors/castrojo/") }}
</div>

### Community Contributors
- [**BlueBuild Project**](https://blue-build.org/) ([**Contribute**](https://blue-build.org/learn/contributing/))
- [**Full list of Bazzite Contributors in the Gitub repository**](https://github.com/ublue-os/bazzite/graphs/contributors) ([**Do your part!**](/CONTRIBUTE.md))

## Fedora Project

Bazzite would not exist without [**Fedora Linux**](https://fedoraproject.org/).  The Fedora Project does not take monetary donations, but values hardware donations and contributions to the project.

- [**Donating Hardware**](https://fedoraproject.org/wiki/Donations)
- [**Contributing**](https://fedoraproject.org/wiki/Contribute)

## Projects Included in Bazzite

We also encourage you to donate to the projects that are used in Bazzite which helps us keep open source sustainable!

<sub>(*If we missed software that is part of Bazzite and can be donated to, then [**please let us know**](https://github.com/KyleGospo/docs.bazzite.gg/issues) or [**PR a fix**](https://github.com/KyleGospo/docs.bazzite.gg/blob/main/src/donations.md)!*)</sub>

- [**Atuin**](https://github.com/sponsors/atuinsh)
- [**BORE Scheduler**](https://ko-fi.com/firelzrd)
- [**Blur My Shell**](https://github.com/sponsors/aunetx)
- [**Clapper**](https://liberapay.com/Clapper)
- [**Davincibox**](https://ko-fi.com/akzel94)
- [**Deja Dup**](https://liberapay.com/DejaDup)
- [**Extensions Manager**](https://github.com/sponsors/mjakeman)
- [**eza**](https://github.com/sponsors/cafkafk)
- [**fastfetch**](https://github.com/sponsors/LinusDierheimer)
- **fd: [David Peter](https://github.com/sponsors/sharkdp) and [Tavian Barnes](https://github.com/sponsors/tavianator)**
- **Flatpak**: *Currently migrating fiscal hosts*
- [**fzf**](https://github.com/sponsors/junegunn)
- [**freedesktop.org**](https://www.freedesktop.org/wiki/#donations)
- [**Gear Lever**](https://ko-fi.com/mijorus)
- [**GNOME**](https://www.gnome.org/donate/)
- [**GNOME themes for Firefox and Thunderbird**](https://www.patreon.com/rafaelmardojai)
- [**Hanabi**](https://ko-fi.com/jeffshee)
- [**Handheld Daemon**](https://github.com/sponsors/antheas)
- [**Homebrew**](https://github.com/Homebrew/brew#donations)
- [**KDE**](https://kde.org/donate/)
- [**Logo Menu**](https://github.com/sponsors/Aryan20)
- [**Mozilla**](https://foundation.mozilla.org/en/?form=donate&gad_source=1)
- [**Pika Backup**](https://opencollective.com/pika-backup)
- [**Terra**](https://github.com/sponsors/FyraLabs)
- [**Thunderbird**](https://www.thunderbird.net/en-US/donate/)
- [**Warehouse**](https://ko-fi.com/heliguy)
- [**Waydroid**](https://opencollective.com/waydroid/donate)
- [**xone**](https://www.paypal.com/donate?hosted_button_id=BWUECKFDNY446)
- [**yq**](https://github.com/sponsors/mikefarah)

## Collaborated Projects

Similar desktop Linux projects that share resources with us.

- [**ChimeraOS**](https://chimeraos.org/) ([**Support**](https://opencollective.com/chimeraos/donate))
- [**Ultramarine Linux**](https://ultramarine-linux.org/) ([**Support**](https://github.com/sponsors/FyraLabs))
- [**Nobara Project**](https://nobaraproject.org/download-nobara/) ([**Support**](https://www.patreon.com/gloriouseggroll))
- [**Jovian NixOS**](https://jovian-experiments.github.io/Jovian-NixOS/) ([**Contribute**](https://github.com/Jovian-Experiments/Jovian-NixOS/blob/development/CONTRIBUTING.md))
- [**CachyOS**](https://cachyos.org/) ([**Support**](https://www.patreon.com/CachyOS))
- [**SteamFork**](https://wiki.steamfork.org/) ([**Contribute**](https://github.com/SteamFork#support))

## Other Universal Blue Images: Aurora, Bluefin, and uCore

Check out the other Universal Blue end-user custom Fedora images especially if you want an experience similar to Bazzite on other hardware that does not require all of the extra gaming packages. Aurora and Bluefin are recommended operating systems to install for your family who may not be into PC gaming or for work colleagues who like to develop software in containers.  uCore is strictly for server usage only.

The contributors and maintainers involved with the other Universal Blue projects will usually fix bugs in their images that will eventually be fixed in Bazzite around the same time if the same issues occur in both.

- [**Aurora**](https://getaurora.dev/)
- [**Bluefin**](https://projectbluefin.io/)
- [**uCore**](https://projectucore.io)

<hr>

**See also**: [Special Thanks](https://github.com/ublue-os/bazzite/blob/main/README.md#special-thanks)
