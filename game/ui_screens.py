import tkinter as tk
from constants import *

root = tk.Tk()
root.title("Base Raiders")

# =========================================================================================
#   FRAMES
# =========================================================================================
game_frame = tk.Frame(root)
game_frame.pack()

win_raiders_frame = tk.Frame(root)

win_defense_frame = tk.Frame(root)

# =========================================================================================
#   CANVAS
# =========================================================================================
canvas_field = tk.Canvas(
    game_frame,
    width= CELL_SIZE *32 ,
    height= CELL_SIZE * 16,
    bg="seagreen4"
)
# -----------------------------------------------------------------------------------------------
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
# ---------------------------------------------------------------------------------------------------

canvas_win_raiders = tk.Canvas(
    win_raiders_frame,
    width= CELL_SIZE *32 ,
    height= CELL_SIZE * 24,
    bg="red"
)
canvas_win_raiders.pack()

canvas_win_defense = tk.Canvas(
    win_defense_frame,
    width= CELL_SIZE *32 ,
    height= CELL_SIZE * 24,
    bg="blue"
)
canvas_win_defense.pack()


