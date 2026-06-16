from ui_screens import *
from classes import *
import constants
from game_loops import *
# =========================================================================================
#   FUNCIONES PARA MANEJAR LA UI
# =========================================================================================

def start_plan_defense():
    #choose_player_frame.pack_forget()
    game_frame.pack()
    canvas_field.pack()
    canvas_menu_plan_defense.pack()
    constants.central_base = Base(x0=CELL_SIZE*2, y0=CELL_SIZE*7)
    constants.running = "plan"
    root.after(32, planning_loop)
    
    
def start_plan_attack():
    canvas_menu_plan_defense.pack_forget()
    constants.selected_element = None
    canvas_menu_plan_attack.pack()
    
def start_game():
    canvas_menu_plan_attack.pack_forget()
    canvas_menu_on_game.pack()
    constants.selected_element = None
    constants.running = "game"
    root.after(32, on_game_loop)
    

# =========================================================================================
#   FUNCIONES PARA PONER ELEMENTOS EN EL MAPA
# =========================================================================================
def select_element(element):
    global selected_element
    selected_element = element

def place_element(event):
    global central_base
    
    if selected_element in ("knight", "goblin", "archer", "giant", "dragon", "pekka"):
        if selected_element == "knight":
            element = Knight(event.x, event.y)
        elif selected_element == "goblin":
            element = Goblin(event.x, event.y)
        elif selected_element == "archer":
            element = Archer(event.x, event.y)
        elif selected_element == "giant":
            element = Giant(event.x, event.y)
        elif selected_element == "dragon":
            element = Dragon(event.x, event.y)
        elif selected_element == "pekka":
            element = Pekka(event.x, event.y)
       
        list_raiders.append(element)
    
    elif selected_element in ("wzrd_tower", "crsbw_tower", "spk_tower"):
        if selected_element == "wzrd_tower":
            element = Wizard_tower(event.x - event.x%CELL_SIZE, event.y - event.y%CELL_SIZE)
        elif selected_element == "crsbw_tower":
            element = Crossbow_tower(event.x - event.x%CELL_SIZE, event.y - event.y%CELL_SIZE)
        elif selected_element == "spk_tower":
            element = Spiky_tower(event.x - event.x%CELL_SIZE, event.y - event.y%CELL_SIZE)
            
        list_towers.append(element)
        
    elif selected_element == "wall":
        element = Wall(event.x - event.x%CELL_SIZE, event.y - event.y%CELL_SIZE)
        list_walls.append(element)
        
    elif selected_element == "base":
        element = Base(event.x - event.x%CELL_SIZE, event.y - event.y%CELL_SIZE)
        central_base = element
        
    elif selected_element == "delete_structure":
        
        for wall in list_walls[:]:
            if wall.x0 <= event.x <= wall.x1 and wall.y0 <= event.y <= wall.y1:
                list_walls.remove(wall)
                return
    
        for tower in list_towers[:]:
            if tower.x0 <= event.x <= tower.x1 and tower.y0 <= event.y <= tower.y1:
                list_towers.remove(tower)
                return
            
        if central_base.x0 <= event.x <= central_base.x1 and central_base.y0 <= event.y <= central_base.y1:
            central_base = None
    
    elif selected_element == "delete_troop":
        
        for troop in list_raiders[:]:
            if troop.x0 <= event.x <= troop.x1 and troop.y0 <= event.y <= troop.y1:
                list_raiders.remove(troop)
        
canvas_field.bind("<Button-1>", place_element)


