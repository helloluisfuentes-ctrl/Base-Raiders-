import tkinter as tk
from classes import *
import constants
from ui_screens import *
from game_logic import *


def planning_loop():
    if constants.running != "plan":
        return
    
    canvas_field.delete("all")
    
    draw_limit_line()
    draw_base()
    draw_walls()
    draw_towers()
    draw_raiders()
    
    root.after(32, planning_loop)
    
    
    


def on_game_loop():
    
    check_win()
    
    if constants.running != "game":
        return
    
    canvas_field.delete("all")
    
    
    
    draw_base()
    draw_walls()
    draw_towers()
    draw_raiders()
    draw_projectiles_raiders()
    draw_projectiles_towers()
    
    activate_troops()
    activate_towers()
    move_projectiles_raiders()
    move_projectiles_towers()
    
    
    
    root.after(32, on_game_loop)
        

        
