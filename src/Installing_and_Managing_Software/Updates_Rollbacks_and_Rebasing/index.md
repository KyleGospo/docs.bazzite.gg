---
title: Updates, Rollbacks, and Rebasing
authors:
  - "@nicknamenamenick"
---

<!-- ANCHOR: METADATA -->
<!--{"url_discourse": "https://universal-blue.discourse.group/docs?topic=36", "fetched_at": "2024-09-03 16:43:15.473615+00:00"}-->
<!-- ANCHOR_END: METADATA -->

# Updates, Rollbacks, and Rebasing

## Updates

Updates are automatic on Desktop images and manually done on Handheld/HTPC images, and both Bazzite variants upgrade everything at both a system-level and user-installed applications during the updating process.

> **Full Documentation**:
> [Updating guide](./updating_guide.md)

## Rollbacks

Swap back to a previous system update if there are major issues after updating via the GRUB menu or the `rpm-ostree rollback` command.

> **Full Documentation**:
> [Rollbacks guide](./rolling_back_system_updates.md)

## Rebasing

Rebase to Bazzite builds from the last 90 days, change Bazzite update channels, swap between the Desktop and Handheld/HTPC images, or move completely to a different Fedora Atomic Desktop image.

!!! important 
    
    Do **not** rebase to a different desktop environment than the one you are currently using, please backup and reinstall instead.

> **Full Documentation**:
> [Rebase guide](./rebase_guide.md)

## `bazzite-rollback-helper`

Utility to assist with rolling back to older Bazzite images, changing update branches, or swapping to a different Bazzite image.

> **Full Documentation**:
> [Bazzite's Rollback Helper Utility Guide](./bazzite_rollback_helper.md)

<hr>

← [**View all Bazzite documentation**](../../index.md)
