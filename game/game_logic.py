from constants import *
from ui_screens import *




def draw_raiders(): #TODO add images
    for raider in list_raiders:
        x0 = raider.x0
        y0 = raider.y0
        x1 = raider.x1
        y1 = raider.y1
        
        color = raider.image
        
        canvas_field.create_rectangle(x0, y0, x1, y1, fill=color, outline="black", width=2)
        
def draw_walls():
    for wall in list_walls:
        x0 = wall.x0
        y0 = wall.y0
        x1 = wall.x1
        y1 = wall.y1 
        
        canvas_field.create_rectangle(x0, y0, x1, y1, fill="brown", outline="black", width=2)      