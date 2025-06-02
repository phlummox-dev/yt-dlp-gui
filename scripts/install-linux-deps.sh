#!/usr/bin/env sh

# install dependencies needed on debian bullseye for building
# pyinstaller-frozen executable

sudo apt-get update
sudo apt-get install --no-install-recommends -y \
  libatk1.0-0         \
  libdbus-1-3         \
  libgtk-3-0          \
  libxcb-cursor0      \
  libxcb-icccm4       \
  libxcb-keysyms1     \
  libxcb-randr0       \
  libxcb-shape0       \
  libxkbcommon-x11-0  \
  x11-utils

pip3 install uv

