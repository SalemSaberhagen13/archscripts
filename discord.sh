#!/bin/bash

exec /usr/bin/discord \
    --enable-features=UseOzonePlatform \
    --ozone-platform=wayland \
    --enable-wayland-ime \
    --disable-gpu-sandbox \
    "$@"
