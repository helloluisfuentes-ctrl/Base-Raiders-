import tkinter as tk
from game_loops import *
from ui_screens import *
from ui_functions import *
from buttons import *
from victory_screens import setup_victory_screens


# Configurar pantallas de victoria
setup_victory_screens(canvas_win_raiders, canvas_win_defense)

# Mostrar menú principal al iniciar
show_main_menu()





root.mainloop()