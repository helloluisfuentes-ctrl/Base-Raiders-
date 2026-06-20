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
    update_on_game_money_display()
    
    
    
    root.after(32, on_game_loop)


def update_on_game_money_display():
    canvas_menu_on_game.delete("money_info")
    canvas_menu_on_game.create_text(
        CELL_SIZE * 6, CELL_SIZE * 2,
        text=f"Ronda {constants.round_number}   Atacante: ${constants.attacker_money}   Defensor: ${constants.defender_money}",
        font=("Arial", 22, "bold"),
        fill="black",
        tags="money_info"
    )
    canvas_menu_on_game.create_text(
        CELL_SIZE * 6, CELL_SIZE * 4,
        text=f"Marcador {constants.attacker_round_wins}-{constants.defender_round_wins}   Dano: {constants.round_damage_dealt}   Bajas: {constants.round_enemies_killed}",
        font=("Arial", 18, "bold"),
        fill="black",
        tags="money_info"
    )
        

        
