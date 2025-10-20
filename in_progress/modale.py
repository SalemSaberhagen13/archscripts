#!/usr/bin/env python
import subprocess
import sys

try:
    result = subprocess.run(
        [
            "zenity",
            "--question",
            "--title=Obscure second screen?",
            "--text=Wanna obscure secondo screen?",
            "--width=300",
        ],
        capture_output=True,
    )

    if result.returncode == 0:
        print("Esecuzione dello script...")
        _ = subprocess.run(["../gammastep/gammastep_manager.sh movie"])
    else:
        print("Aborted")

except FileNotFoundError:
    print("Errore: Zenity not installed")
    sys.exit(1)
