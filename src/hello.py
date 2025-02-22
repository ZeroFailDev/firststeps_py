"""
Questo programma chiede in input il nome e l'anno di nascita.

da linea di comando o standard input.

Calcola l'età e saluta l'utente indicando il suo nome e la sua età.
"""

import sys


def main():
    """
    Funzione principale che calcola l'età di un utente.

    Se vengono forniti argomenti da riga di comando, utilizzali per il nome.
    e l'anno di nascita. Altrimenti, chiede i dati tramite input standard.

    Stampa un messaggio di saluto con il nome e l'età calcolata.
    """
    anno = 2024

    if len(sys.argv) < 3:
        nome = input("Inserisci il tuo nome: ")
        anno_nascita = int(input("Inserisci il tuo anno di nascita: "))
    else:
        nome = sys.argv[1]
        anno_nascita = int(sys.argv[2])

    eta = anno - anno_nascita
    print(f"Hello {nome}, hai {eta} anni.")


if __name__ == "__main__":
    main()
