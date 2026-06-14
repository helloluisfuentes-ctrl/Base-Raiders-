import tkinter as tk
from constants import *

root = tk.Tk()
root.title("Base Raiders")

on_game_frame = tk.Frame(root)
on_game_frame.pack()


canvas_field_on_game = tk.Canvas(
    on_game_frame,
    width= CELL_SIZE *32 ,
    height= CELL_SIZE * 16,
    bg="seagreen4"
)
canvas_field_on_game.pack()

canvas_menu_on_game = tk.Canvas(
    on_game_frame,
    width= CELL_SIZE *32 ,
    height= CELL_SIZE * 8,
    bg="lightcyan3"
)
canvas_menu_on_game.pack()