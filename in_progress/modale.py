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
        _ = subprocess.run(["../gammastep/gammastep_manager.sh movie"])

except FileNotFoundError:
    print("Error: Zenity not installed")
    sys.exit(1)
