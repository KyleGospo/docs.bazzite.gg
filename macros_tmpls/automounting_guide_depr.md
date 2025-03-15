!!! warning "Deprecation notice"

    {# TODO: Remove :testing mention whenever gets merged into main #}
    {# TODO: Write section explaining partition labeling requirements and procedure #}
    15/03/2025 ~ If you are using the `:testing` branch, this procedure is no longer needed as by [commit `0982eda`](https://github.com/ublue-os/bazzite/commit/0982eda834e2dee52497b9758f6b99711eb298de). [`ublue-os-media-automount-udev`](https://github.com/ublue-os/packages/tree/main/packages/ublue-os-media-automount-udev) will handle automounting in non-removable devices (BTRFS and ext4 supported only).

    Only labeled partitions will be automounted.
    
    Partitions will be mounted under `/run/media/system/PARTITION_LABEL`.
    You can place a custom named shortcut to the partition with:

    ```sh
    sudo ln -s /run/media/system/PARTITION_LABEL /mnt/CUSTOM_NAME
    ```
