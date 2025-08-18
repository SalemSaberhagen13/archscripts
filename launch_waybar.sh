#!/usr/bin/env zsh

pid=$(pidof waybar)

if [ -n "$pid" ]; then
	echo "Killing waybar (PID: $pid)..."
	kill -15 $pid
	sleep 1
	echo "Reboot waybar..."
else
	echo "Lauching waybar..."
fi

waybar &

