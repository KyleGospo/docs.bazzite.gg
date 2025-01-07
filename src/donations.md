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

## Universal Blue & Bazzite Maintainers/Contributors

Love Bazzite and want to help sustain it's development?  Consider **sponsoring** the maintainers and contributors of the project.

This list contains members who have contributed heavily to [**Universal Blue**](https://ublue.it) and/or Bazzite since 2021 including alumni members who have contributed in the past and may not be as involved with the project anymore.

<sub>(*If we missed a major contributor, then [**please let use know**](https://github.com/KyleGospo/docs.bazzite.gg/issues) or [**PR a fix**](https://github.com/KyleGospo/docs.bazzite.gg/blob/main/src/donations.md)!*)</sub>

<div style="display: flex; flex-wrap: wrap; gap: 0.3rem;">
{{ contributor("Kyle Gospodnetich", "KyleGospo", "Creator & lead maintainer of Bazzite", "https://github.com/sponsors/KyleGospo") }}
{{ contributor("Jorge Castro", "castrojo", "Creator of Universal Blue", "https://github.com/sponsors/castrojo/") }}
{{ contributor("RJ Trujillo", "EyeCantCU", "Early foundation building, support for alternate desktop environments") }}
{{ contributor("HikariKnight", "HikariKnight", "Virtualization support, scripting", "https://github.com/sponsors/HikariKnight") }}
{{ contributor("Antheas Kapenekakis", "antheas", "Handheld support", "https://github.com/sponsors/antheas") }}
{{ contributor("Pat Connors", "nicknamenamenick", "Documentation", "https://github.com/sponsors/nicknamenamenick") }}
{{ contributor("Noel Miller", "noelmiller", "ISO enhancements, custom image tooling, marketing", "https://github.com/sponsors/noelmiller") }}
{{ contributor("Aarron Lee", "aarron-lee", "SimpleDeckyTDP, scripting, command-line utilities") }}
{{ contributor("Matthew Schwartz", "matte-schwartz", "Steam Gaming Mode consulting and testing") }}
{{ contributor("sentry", "sentry", "Kernel patches, original kernel maintainer") }}
{{ contributor("Zeglius", "Zeglius", "CI/CD pipeline") }}
{{ contributor("wolfyreload", "wolfyreload", "Video tutorials") }}
{{ contributor("CharlieBros", "CharlieBros", "Spanish translations for support literature") }}
{{ contributor("rei.svg", "reisvg", "Branding") }}
{{ contributor("Sean", "SuperRiderTH", "Animations") }}
{{ contributor("Alex Banna", "abanna", "Bazzite Portal prototyping") }}
{{ contributor("Bouhaa", "BoukeHaarsma23", "Steam Gaming Mode support and features") }}
{{ contributor("Marco Rodolfi", "RodoMa92", "Scripting, bug fixes") }}
{{ contributor("Jason Nagin", "JasonN3", "Installer assistance") }}
{{ contributor("fiftydinar", "fiftydinar", "Early bug fixes") }}
{{ contributor("Sterophonick", "Sterophonick", "Driver backports and game fixes") }}
{{ contributor("xAlphaKat", "xAlphaKAT", "Early bug fixes") }}
{{ contributor("dreamyuki", "dreamyukii", "Indonesian translation for support literature") }}
{{ contributor("termdisc", "termdisc", "Technical support") }}
{{ contributor("jerb", "jerbmega", "Early Bazzite tester") }}
{{ contributor("boredsquirrel", "boredsquirrel", "Early Bazzite tester") }}
{{ contributor("Weaver Marquez", "weavermarquez", "Early Bazzite tester") }}
{{ contributor("Benjamin Sherman", "bsherman", "Kernel modules, Universal Blue image maintenance") }}
{{ contributor("Brian Ketelsen", "bketelsen", "Universal Blue image maintenance, experimental tooling") }}
{{ contributor("Robert Sturla", "p5", "Universal Blue image maintenance") }}
{{ contributor("m2", "m2Giles", "Universal Blue image maintenance") }}
{{ contributor("Niklas Haiden", "NiHaiden", "Universal Blue image maintenance") }}
{{ contributor("Tulip Blossom", "tulilirockz", "Universal Blue image maintenance") }}
{{ contributor("Ryan Brue", "ryanabx", "COSMIC desktop environment testing") }}
{{ contributor("Gareth Widlansky", "gerblesh", "Universal Blue image maintenance") }}
{{ contributor("xyny", "xynydev", "Alternate custom image tooling, branding") }}
{{ contributor("Gecked-Deck", "Gecked-Deck", "Social media") }}
{{ contributor("Joseph of Earth", "", "Social media") }}
{{ contributor("Justin Garrison", "rothgar", "Presentation consultant") }}
{{ contributor("RoyalOughtness", "RoyalOughtness", "Security consulting", "https://github.com/sponsors/RoyalOughtness") }}
{{ contributor("bobslept", "bobslept", "Universal Blue alumni") }}
{{ contributor("Primož Ajdišek", "bigpod98", "Universal Blue alumni") }}
{{ contributor("Alex Díaz", "akdev1l", "Universal Blue alumni") }}
{{ contributor("Johnny Arcitec", "Arcitec", "Universal Blue alumni") }}
{{ contributor("Dylan M. Taylor", "dylanmtaylor", "Universal Blue alumni") }}
{{ contributor("Nathaniel Warburton", "storyaddict", "Universal Blue alumni") }}
{{ contributor("Joshua Stone", "joshua-stone", "Universal Blue alumni") }}
{{ contributor("dhoell", "dhoell", "Universal Blue alumni") }}
{{ contributor("Cassidy James Blaede", "cassidyjames", "Universal Blue alumni", "https://github.com/sponsors/cassidyjames") }}
{{ contributor("Marco Ceppi", "marcoceppi", "Co-Creator of Universal Blue, alumni") }}
{{ contributor("Adam Israel", "AdamIsrael", "Co-Creator of Universal Blue, alumni") }}
</div>

### Community Contributors
- [**BlueBuild Project**](https://blue-build.org/) ([**Contribute**](https://blue-build.org/learn/contributing/))
- [**Full list of Bazzite Contributors in the Gitub repository**](https://github.com/ublue-os/bazzite/graphs/contributors) ([**Do your part!**](https://docs.bazzite.gg/CONTRIBUTE/))

## Fedora Project

Bazzite would not exist without [**Fedora Linux**](https://fedoraproject.org/).  The Fedora Project does not take monetary donations, but values hardware donations and contributions to the project.

- [**Donating Hardware**](https://fedoraproject.org/wiki/Donations)
- [**Contributing**](https://fedoraproject.org/wiki/Contribute)

## Projects Included in Bazzite

We also encourage you to donate to the projects that are used in Bazzite which helps us keep open source sustainable!

(*If we missed anything, then [**please let use know**](https://github.com/KyleGospo/docs.bazzite.gg/issues) or [**PR a fix**](https://github.com/KyleGospo/docs.bazzite.gg/blob/main/src/donations.md)!*)

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

Check out the other Universal Blue end-user custom Fedora images especially if you want an experience similar to Bazzite on other hardware that does not require all of the extra gaming packages.  The contributors and maintainers involved with the other Universal Blue projects will usually fix bugs in their images that will eventually be fixed in Bazzite if the same issues occurs in both.

- [**Aurora**](https://getaurora.dev/)
- [**Bluefin**](https://projectbluefin.io/)
- [**uCore**](https://projectucore.io)

<hr>

**See also**: [Special Thanks](https://github.com/ublue-os/bazzite/blob/main/README.md#special-thanks)
