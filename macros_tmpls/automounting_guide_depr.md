!!! warning "Deprecation notice"

    {# TODO: Remove :testing mention whenever gets merged into main #}
    19/02/2024 ~ If you are using the `:testing` branch, this procedure is no longer needed as by [commit `e25e48b`](https://github.com/ublue-os/bazzite/commit/e25e48b383e36c431311f2cc9303e590e8cf3f99). [`media-automount-generator`](https://github.com/Zeglius/media-automount-generator) will handle automounting in non-removable devices (BTRFS and ext4 supported only).

    Partitions will be mounted under `/run/media/media-automount/PARTITION_UUID`.
    You can place a custom named shortcut to the partition with:

    ```sh
    sudo ln -s /run/media/media-automount/PARTITION_UUID /mnt/CUSTOM_NAME
    ```
