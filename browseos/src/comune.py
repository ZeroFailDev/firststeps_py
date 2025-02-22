"""
Questo programma è da implementare come libreria.

Ivan Granata 3HI.
"""

import icecream
import sys


def visualizza_messaggio(msg):
    """Funzione principale."""
    icecream.ic(msg)


def check_argv(numero_argomenti):
    """
        Controlla se il numero di argomenti passati da linea.

        comando è corretto.
    return:
        True se il numero di argomenti passati da linea.
        comando è uguale a numero_argomenti.
    """
    is_correct = False
    if len(sys.argv) == numero_argomenti:
        is_correct = True
    return is_correct


if __name__ == "__main__":
    visualizza_messaggio("Ciao")
    icecream.ic(check_argv(1))
