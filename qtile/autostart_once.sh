#!/bin/sh

/usr/bin/lxpolkit &
xfce4-power-manager &
kdeconnect-indicator &
udiskie --tray &
mpris-proxy &
picom -b -f --experimental-backends &
caffeine &
clipit &
syncthing-gtk -m &
xss-lock -- betterlockscreen -l -t "Non ducor, duco." &
