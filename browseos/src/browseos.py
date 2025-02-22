"""
Questo programma implementa un'operazione.

Simile al comando 'dir' della command line.

Per elencare i file .py presenti nel path.

Utilizza le librerie os, sys, platform.

comune e icecream.

Ivan Granata 3HI.
"""

import os
import sys
import platform
import comune
from icecream import ic


def set_default_path():
    """Imposta un percorso di default in base al sistema operativo."""
    sistema = platform.system()
    if sistema in ("Windows", "Linux", "Darwin"):  # Darwin è per macOS
        return "." if sistema == "Windows" else "/etc"
    else:
        comune.visualizza_messaggio("Sistema operativo non supportato.")
        return None


def path_esiste(path):
    """Verifica se la directory esiste ed è accessibile in lettura."""
    return os.path.exists(path) and os.access(path, os.R_OK)


def oswalk(path):
    """
    Elenca i file nella directory specificata, insieme al loro path.

    Crea due liste: una con i file .py e una con tutti i file.
    """
    files_py = []
    all_files = []
    contatore_filepy = 0
    for root, _, files in os.walk(path):
        # root: la directory corrente che è stata esplorata.
        # _: segnaposto per la lista di sottodirectory
        # files: lista dei file nella root
        for file in files:
            file_name = os.path.join(root, file)
            if file.endswith(".py"):
                files_py.append(file_name)
                contatore_filepy += 1
            all_files.append(file_name)
    if files_py:
        definitive_list = files_py
        definitive_list.append(contatore_filepy)  # numero file py

    else:
        definitive_list = all_files
        definitive_list.append(contatore_filepy)  # aggiungo alla lista il numero di file py
    return definitive_list


if __name__ == "__main__":
    print(f"Operative system: {platform.system()}")

    if comune.check_argv(2):
        path = sys.argv[1]
    else:
        path = set_default_path()

    if not path_esiste(path):
        ic(f"Error: the Dir '{path}' doesn't exist or you have access denied")
    else:
        definitive_list = oswalk(path)
        print("Files found:")
        for file in definitive_list[:-1]:  # tranne l'ultimo elemento
            ic("_________________________________________________________")
            print(file)
            ic("_________________________________________________________")
        print(f"In Dir '{path}' there are '{definitive_list[-1]}' file .py")
