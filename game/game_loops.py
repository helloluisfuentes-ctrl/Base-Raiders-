import tkinter as tk
from classes import *
import constants
from ui_screens import *
from game_logic import *


def planning_loop():
    if constants.running != "plan":
        return
    
    canvas_field.delete("all")
    
    draw_raiders()
    draw_walls()
    draw_towers()
    draw_base()
    
    
    root.after(32, planning_loop)
    
    
    


def on_game_loop():
    if constants.running != "game":
        return
    
    canvas_field.delete("all")
    
    draw_raiders()
    draw_walls()
    draw_towers()
    draw_base()
    
    activate_troops()
    activate_towers()
    move_projectiles_raiders()
    move_projectiles_towers()
    
    
    
    root.after(32, on_game_loop)
        

        
