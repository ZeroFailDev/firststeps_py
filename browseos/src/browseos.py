"""
This program implements an operation.

Similar to the command line 'dir' command.

To list the .extension files present in the path.

Uses os, sys, platform libraries.

comune and icecream.

Ivan Granata 3HI.
"""

import os
import sys
import platform
import time
from icecream import ic

import comune


def set_default_path():
    """Set a default path based on your operating system."""
    sistema = platform.system()
    if sistema in ("Windows", "Linux", "Darwin"):  # Darwin è per macOS
        return "." if sistema == "Windows" else "/etc"
    else:
        comune.visualizza_messaggio("Operating system not supported.")
        return None


def path_esiste(path):
    """Check if the directory exists and is readable."""
    return os.path.exists(path) and os.access(path, os.R_OK)


def set_extension():
    """
    Set the extension to be used.

    Default is .py unless specified otherwise.
    """
    if len(sys.argv) > 2:
        extension = sys.argv[2]
    else:
        extension = ".py"
    return extension


def oswalk(path, extension):
    """
    List the files in the specified directory, along with their path.

    Create two lists: one with .extension files and one with all files.
    """
    files_extension = []
    all_files = []
    for root, _, files in os.walk(path):
        for file in files:
            file_name = os.path.join(root, file)
            if file.endswith(extension):
                files_extension.append(file_name)
            all_files.append(file_name)
    if files_extension:
        definitive_list = files_extension
    else:
        definitive_list = all_files
    return definitive_list


def count_files(path, extension):
    """
    Count all the files it finds.

    If it finds file extension it returns the number of those.
    """
    files_number = 0
    for root, _, files in os.walk(path):
        for file in files:
            if file.endswith(extension):
                files_number += 1
    return files_number


def log(date, msg):
    """Write the data in the tracelog."""
    tracelog_path = "../log/trace.log"
    with open(tracelog_path, mode="a") as tracelog:  # a = append
        tracelog.write(f"{date}; {msg}\n")


if __name__ == "__main__":
    startime = time.time()
    msg = "Start program"
    log(startime, msg)

    print(f"Operative system: {platform.system()}")

    if len(sys.argv) > 1:
        path = sys.argv[1]
    else:
        path = set_default_path()

    if not path_esiste(path):
        print(f"Error: the Dir '{path}' doesn't exist or you can't acces it")
    else:
        extension = set_extension()
        definitive_list = oswalk(path, extension)
        files_number = count_files(path, extension)
        print("Files found:")
        for file in definitive_list:
            ic("_________________________________________________________")
            print(file)
            ic("_________________________________________________________")

        msg = f"In Dir '{path}' there are '{files_number}' file {extension}"
        ic(msg)

    finishtime = time.time()
    msg = "Finish program"
    log(finishtime, msg)
    msg = f"The program execution time is {finishtime - startime}"
    ic(msg)
