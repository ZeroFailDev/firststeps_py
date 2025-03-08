"""
This program is to be implemented as a library.

Ivan Granata 3HI.
"""

import icecream
import sys


def visualizza_messaggio(msg):
    """Funzione principale."""
    icecream.ic(msg)


def check_argv(numero_argomenti):
    """
        Checks whether the number of arguments passed by line.

        are correct.
    return:
        True if the number of arguments passed by line.
        command is equal to number_of arguments.
    """
    is_correct = False
    if len(sys.argv) == numero_argomenti:
        is_correct = True
    return is_correct


if __name__ == "__main__":
    visualizza_messaggio("Ciao")
    icecream.ic(check_argv(1))
