import tkinter as tk
from classes import *
from constants import *
from ui_screens import *
from game_logic import *

def planning_loop():
    running = True
    canvas_field.delete("all")
    
    draw_raiders()
    draw_walls()
    

    
    if running:
        root.after(32, planning_loop)
    
    
    


def on_game_loop():
    running = True
    canvas_field.delete("all")
    
    draw_raiders()
    draw_walls()
    
    
    
    
    
    
    
    if running:
        root.after(32, on_game_loop)
        
        
        
