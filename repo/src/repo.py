"""
Questo programma implementa una funzione.

per copiare tutti i file .py da una dir di origine.

ad una di destinazione.

Usa le librerie os, sys, platform.

comune and icecream.

Ivan Granata 3HI.
"""

import os
import sys
import time
import shutil
import platform
from icecream import ic

import comune


def path_esiste(path):
    """Check if the directory exists and is readable."""
    return os.path.exists(path) and os.access(path, os.R_OK)


def copy(path_origine, path_destinazione, extension):
    """
    Copia ed enumera i file Python dalla directory di origine.

    a quella di destinazione.
    """
    counter = 1
    copied_files = []
    for root, _, files in os.walk(path_origine):
        for file in files:
            if file.endswith(extension):
                nome_file, estensione = os.path.splitext(file)
                file_destinazione = os.path.join(
                    path_destinazione, f"{nome_file}_{counter}{estensione}"
                )
                file_origine = os.path.join(root, file)
                while os.path.exists(file_destinazione):
                    counter += 1
                    file_destinazione = os.path.join(
                        path_destinazione,
                        f"{nome_file}_{counter}{estensione}"
                    )
                shutil.copy(file_origine, file_destinazione)
                copied_files.append((file_origine, file_destinazione))
                counter += 1
    return copied_files


def print_copy(copied_files):
    """
    Stampa a schermo i file che vengono copiati.

    nella directory di destinazione.
    """
    for file_origine, file_destinazione in copied_files:
        ic(f"COPY {file_origine} TO {file_destinazione}")


def log(date, msg):
    """Write the data in the tracelog."""
    tracelog_path = "../log/trace.log"
    with open(tracelog_path, mode="a") as tracelog:  # a = append
        tracelog.write(f"Operating System: {platform.system()}; ")
        tracelog.write(f"{date}; {msg}\n")


if __name__ == "__main__":
    startime = time.time()
    msg = "Start program"
    log(startime, msg)

    if comune.check_argv(3):
        path_origine = sys.argv[1]
        path_destinazione = sys.argv[2]

        if path_esiste(path_origine):
            if path_esiste(path_destinazione):
                print(
                    f"Esecuzione COPY *.py da {path_origine} "
                    f"to {path_destinazione}"
                )
                extension = ".py"
                copied_files = copy(path_origine, path_destinazione, extension)
                print_copy(copied_files)
            else:
                msg = "Il path di destinazione non esiste"
                ic(msg)
        else:
            msg = "Il path di origine non esiste"
            ic(msg)
    else:
        msg = (
            "Parametri da linea comando errati: "
            "eseguire il programma nel seguente modo:"
        )
        ic(msg)
        msg = "python.exe <pathorigine> <pathdestinazione>"
        ic(msg)

    finishtime = time.time()
    msg = "Finish program"
    log(finishtime, msg)
