"""
Questo programma serve per.

controllare le caratteristiche.

di una serie di file in un file csv.

Ivan Granata 3HI.
"""

import os
import time
import comune
import platform

from icecream import ic


def process_input(input_filename):
    """
    Ricostruisce il percorso.

    di tutti i file nella tabella .csv.
    """
    with open(input_filename, "r") as input:
        righe = input.readlines()

        righe_pulite = []
        for riga in righe:
            riga_pulita = riga.strip()
            if riga_pulita:
                righe_pulite.append(riga_pulita)

    return righe_pulite


def process_dirs(dirs):
    """
    Tira fuori i file nelle cartelle.

    e sottocartelle del file di input.
    """
    dir_valide = []
    lista_file = []

    for dir in dirs:
        if comune.path_esiste(dir):
            dir_valide.append(dir)
        else:
            ic(f"La cartella {dir} non esiste o non è accessibile")

    for dir in dir_valide:
        for root, _, files in os.walk(dir):
            for file in files:
                filename = os.path.join(root, file)
                lista_file.append(filename)

    return lista_file


def preparazione_output(out):
    """
    Riconosce se il file è vuoto (o contiene solo spazi/righe vuote).

    e scrive l'intestazione con i nomi delle colonne.
    """
    with open(out, "r") as f:
        righe = f.readlines()

    if len(righe) == 0:
        with open(out, "w") as f:
            f.write("Datalog; ")
            f.write("Filename; ")
            f.write("Dimensione; ")
            f.write("Ultimo accesso; ")
            f.write("Ultima modifica; ")
            f.write("Creazione; ")
            f.write("Permessi; ")
            f.write("\n")


def elabora_file(file_output, file_path):
    """
    Funzione per scrivere i dati.

    per ogni file.
    """
    stat_info = os.stat(file_path)
    mid_time = time.time()

    with open(file_output, "a") as output:
        output.write(f"{mid_time}; ")
        output.write(f"{file_path}; ")
        output.write(f"{stat_info.st_size}; ")
        output.write(f"{time.ctime(stat_info.st_atime)}; ")
        output.write(f"{time.ctime(stat_info.st_mtime)}; ")
        output.write(f"{time.ctime(stat_info.st_ctime)}; ")
        output.write(f"{stat_info.st_mode}; ")
        if platform.platform() == "Windows":
            output.write(f"{stat_info.st_file_attributes}; ")
        output.write("\n")


if __name__ == "__main__":
    startime = time.time()
    msg = "Start program"
    comune.log(startime, msg)

    comune.visualizza_os()

    input_filename = os.path.join("..", "data", "input.csv")
    output_filename = os.path.join("..", "data", "monitor.csv")

    dirs = process_input(input_filename)
    files = process_dirs(dirs)
    files_validi = []

    preparazione_output(output_filename)

    for file in files:
        if comune.path_esiste(file):
            files_validi.append(file)
            elabora_file(output_filename, file)
        else:
            ic(f"Il file {file} non esiste o non ne hai l'accesso.")

    ic(f"Numero di file da  elaborare: {len(files_validi)}")
    ic(f"Lista dei file da elaborare: {files_validi}")

    finishtime = time.time()
    msg = "Finish program"
    comune.log(finishtime, msg)
    msg = f"The program execution time is {finishtime - startime}"
    ic(msg)
