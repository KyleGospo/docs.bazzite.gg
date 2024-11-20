---
authors:
  - "@castrojo"
  - "@nicknamenamenick"
---

<!-- ANCHOR: METADATA -->
<!--{"url_discourse": "https://universal-blue.discourse.group/docs?topic=43", "fetched_at": "2024-09-03 16:43:11.309087+00:00"}-->
<!-- ANCHOR_END: METADATA -->

## Using the Image template

Use the [**official template image**](https://github.com/ublue-os/image-template) to build off of to make your own custom Bazzite preferred over forking the project.
 
## Forking Bazzite

Sometimes you don't want to make a whole new image from scratch, you just want to change some things without too much extra work by forking Bazzite.  It is highly recommended to use the [Pull application for Github](https://github.com/apps/pull) to keep your fork in sync.

## Using BlueBuild

[BlueBuild](https://blue-build.org/learn/universal-blue/) is a project that orginally started as a starting point base for Universal Blue images and eventually became its own separate entity.  All support for Blue-Build images should be directed to the appropriate [communication channels](https://blue-build.org/community/) outside of Universal Blue.
 
## Use Cases
 
- You want to help development by being able to test your contributions prior to submiting to the community.
    - Hardware enablement, experimental features, confirming fixes ahead of merge
- You want to change out applications and other default choices but want to stick close to Bazzite/Bluefin to get improvements automatically
    - For example, Bluefin DX has Visual Studio baked into the image. If you want the rest of it but don't use vscode you could replace it or remove it. 
    - You need to layer something like VPN software that has to be on an image but you don't want to maintain your own standalone image. (Deriving off of others is always easier, that's why we made this project)
    - You want a personal-use image with config and software changes, but also want to benefit from work being completed upstream.
 
[`ublue-os/main`](https://github.com/ublue-os/main) are used to generate base images of everything, so are usually not good candidates for this unless you are familiar with git, containers, and GitHub Actions.

<hr>

**See also**: [Community Created Custom Images](https://universal-blue.discourse.group/t/list-of-community-created-custom-images/340)
