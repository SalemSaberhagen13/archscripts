#!/usr/bin/env zsh

AUTOMATIC=false
CONFIG_ARG=""

while [[ $# -gt 0 ]]; do
    case $1 in
        -a|--automatic)
            AUTOMATIC=true
            shift
            ;;
        *)
            CONFIG_ARG="$1"
            shift
            ;;
    esac
done

pid=$(pidof gammastep)
if [ -n "$pid" ]; then
	echo "Killing gammastep (PID: $pid)..."
	kill -15 $pid
	echo "Rebooting gammastep..."
	sleep 5
fi

if [ "AUTOMATIC" = true ]; then
    python "$HOME/.local/bin/gammastep/gammastep_week.py"
else
   	echo "Launching gammastep..."
    if [ -z "$CONFIG_ARG" ]; then
    	gammastep &
    else
    	gammastep -c "$XDG_CONFIG_HOME"/gammastep/"$CONFIG_ARG".ini &
    fi
    sleep 2
fi
