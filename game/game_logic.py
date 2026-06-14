from constants import *
from ui_screens import *




def draw_raiders(): #TODO add images
    for raider in list_raiders:
        x0 = raider.x0
        y0 = raider.y0
        x1 = raider.x1
        y1 = raider.y1
        
        canvas_field_on_game.create_rectangle(x0, y0, x1, y1, fill="blue", outline="black", width=2)
        
        