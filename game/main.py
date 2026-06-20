"""
Base Raiders - Juego de Estrategia en Tkinter

Juego de estrategia para dos jugadores:
- Un atacante que debe conquistar la base
- Un defensor que debe proteger su base

Autor: Equipo Base Raiders
Versión: 1.0
"""

from py_compile import main
import tkinter as tk
from pathlib import Path

# Importar módulos del proyecto
from players_manager import PlayerManager
from money_system import MoneySystem
from rankings_manager import RankingManager
from ui_windows import VentanaMenu, VentanaSeleccionJugadores, VentanaStats



if __name__ == "__main__":
    main()