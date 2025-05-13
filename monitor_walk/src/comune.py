#!/usr/bin/env python3
"""
This program is to be implemented as a library.

Ivan Granata 3HI.
"""

import sys
import platform
import os
from icecream import ic


def visualizza_messaggio(msg):
    """Display a message using icecream."""
    ic(msg)


def path_esiste(path):
    """Check if the directory exists and is readable."""
    return os.path.exists(path) and os.access(path, os.R_OK)


def log(date, msg):
    """Write the data in the tracelog."""
    tracelog_path = "../log/trace.log"
    with open(tracelog_path, mode="a") as tracelog:
        tracelog.write(f"Operating System: {platform.system()}; ")
        tracelog.write(f"{date}; {msg}\n")


def visualizza_os():
    """Display the operating system in use."""
    msg = f"Operative System: {platform.system()}"
    ic(msg)


def check_argv(numero_argomenti):
    """
    Check whether the number of command-line arguments is correct.

    Returns:
        bool: True if len(sys.argv) equals numero_argomenti.
    """
    return len(sys.argv) == numero_argomenti


if __name__ == "__main__":
    visualizza_messaggio("Ciao")
    ic(check_argv(1))
