import tkinter as tk
from classes import *
from constants import *
from ui_screens import *
from game_logic import *

def on_game_loop():
    running = True
    canvas_field_on_game.delete("all")
    
    draw_raiders()
    #testing delete
    p1.x0 += 3
    p1.x1 += 3
    
    p2.x0 += 10
    p2.x1 += 10
    
    
    
    
    
    
    
    if running:
        root.after(32, on_game_loop)
        
        
        
# eliminar testing   
p1 = Pekka(50,50, 32, 64, 100)
list_raiders.append(p1)

p2 = Pekka(100,50, 32, 64, 100)
list_raiders.append(p2)