#/usr/bin/env python
# -*- coding: utf-8 -*-
"""Emanuel Galván Fontalba.
Script para ejecutar el juego."""

from g_escenas import Director
from escenas import EscenaInicio

def main():
    "Ejecutar el juego."
    director = Director("Arkanoid (beta) v0.1 Emanuel Galván Fontalba")
    director.ejecutar(EscenaInicio(), 60)

if __name__ == "__main__":
    main()
