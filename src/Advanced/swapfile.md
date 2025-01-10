---
title: Setting Up A Swap File (Not Recommended)
authors:
  - "@antheas"
---
!!! warning

    This tutorial will disable zram which is a default of Bazzite and is an unsupported configuration.

## Why Swapfile?

Some games and hardware setups may benefit from a large swapfile over compressed memory (zram) as it will use parts of your storage as more RAM.

The Bazzite maintainers do **NOT recommend** performing the steps found in this advanced guide in most common gaming scenarios since there are more **negatives than positives** in most outcomes.

## Make Swap Subvolume (e.g., due to Snapper)
```
sudo mkdir -p /var/swap
```

```
sudo btrfs subvolume create /var/swap
```

```
sudo semanage fcontext -a -t var_t /var/swap
```

```
sudo restorecon /var/swap
```

## Create Swapfile

```
SIZE=26G
```

```
sudo btrfs filesystem mkswapfile --size $SIZE /var/swap/swapfile
```

```
sudo semanage fcontext -a -t swapfile_t /var/swap/swapfile
```

```
sudo restorecon /var/swap/swapfile
```

## Sanity Check Validation

```
sudo swapon /var/swap/swapfile
```

## Adding it to fstab

Edit fstab with this **command**:

```
sudo nano /etc/fstab
```

!!! attention

Make sure you edit manually **otherwise boot failures may occur**!

Then add the following **line of code** to fstab:

`/var/swap/swapfile none swap defaults,nofail 0 0`

## Disable zram
```
echo "" | sudo tee /etc/systemd/zram-generator.conf
```

## Reboot
Reboot your device to apply the changes made above.
