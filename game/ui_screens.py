import tkinter as tk
from constants import *

root = tk.Tk()
root.title("Base Raiders")

# =========================================================================================
#   FRAMES
# =========================================================================================
game_frame = tk.Frame(root)
game_frame.pack()

# =========================================================================================
#   CANVAS
# =========================================================================================
canvas_field = tk.Canvas(
    game_frame,
    width= CELL_SIZE *32 ,
    height= CELL_SIZE * 16,
    bg="seagreen4"
)

canvas_menu_plan_defense = tk.Canvas(
    game_frame,
    width= CELL_SIZE *32 ,
    height= CELL_SIZE * 8,
    bg="honeydew2"
)

canvas_menu_plan_attack = tk.Canvas(
    game_frame,
    width= CELL_SIZE *32 ,
    height= CELL_SIZE * 8,
    bg="honeydew2"
)

canvas_menu_on_game = tk.Canvas(
    game_frame,
    width= CELL_SIZE *32 ,
    height= CELL_SIZE * 8,
    bg="honeydew2"
)





