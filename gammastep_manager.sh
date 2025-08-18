#!/usr/bin/env zsh

pid=$(pidof gammastep)

if [ -n "$pid" ]; then
	echo "Killing gammastep (PID: $pid)..."
	kill -15 $pid
	sleep 5
	echo "Reboot gammastep..."
else
	echo "Lauching gammastep..."
fi


if [ $# -eq 0 ]; then
	gammastep &
else
	gammastep -c "$XDG_CONFIG_HOME"/gammastep/"$1".ini &
fi

