from ui_functions import *
from tkinter import font

large_font = font.Font(family="Comic Sans MS", size=40)
small_font = font.Font(family="Comic Sans MS", size=18)

# ---------------------------------------------------------------------------------------------
ready_btn = tk.Button(canvas_menu_plan_defense, text= "Ready", width= 10, font=large_font, command=lambda: start_plan_attack())
ready_btn.place(x= CELL_SIZE * 1, y= CELL_SIZE * 1)

delete_btn1 = tk.Button(canvas_menu_plan_defense, text= "Delete", width= 10, font=small_font,
                       command=lambda: select_element("delete_structure"))
delete_btn1.place(x= CELL_SIZE * 12, y= CELL_SIZE * 1)

wall_btn = tk.Button(canvas_menu_plan_defense, text= "Wall", width= 12, font=small_font,
                       command=lambda: select_element("wall"))
wall_btn.place(x= CELL_SIZE * 19, y= CELL_SIZE * 1)

wzrd_tower_btn = tk.Button(canvas_menu_plan_defense, text= "Wizard Tower", width= 12, font=small_font,
                       command=lambda: select_element("wzrd_tower"))
wzrd_tower_btn.place(x= CELL_SIZE * 25, y= CELL_SIZE * 1)

crsbw_tower_btn = tk.Button(canvas_menu_plan_defense, text= "Crossbow Tower", width= 12, font=small_font,
                       command=lambda: select_element("crsbw_tower"))
crsbw_tower_btn.place(x= CELL_SIZE * 25, y= CELL_SIZE * 3)

spk_tower_btn = tk.Button(canvas_menu_plan_defense, text= "Spiky Tower", width= 12, font=small_font,
                       command=lambda: select_element("spk_tower"))
spk_tower_btn.place(x= CELL_SIZE * 25, y= CELL_SIZE * 5)

# ----------------------------------------------------------------------------------------------
start_btn = tk.Button(canvas_menu_plan_attack, text= "Start", width= 10, font=large_font, command=lambda: start_game())
start_btn.place(x= CELL_SIZE * 1, y= CELL_SIZE * 1)

delete_btn2 = tk.Button(canvas_menu_plan_attack, text= "Delete", width= 10, font=small_font,
                       command=lambda: select_element("delete_troop"))
delete_btn2.place(x= CELL_SIZE * 12, y= CELL_SIZE * 1)

knight_btn = tk.Button(canvas_menu_plan_attack, text= "knight", width= 12, font=small_font,
                       command=lambda: select_element("knight"))
knight_btn.place(x= CELL_SIZE * 19, y= CELL_SIZE * 1)

goblin_btn = tk.Button(canvas_menu_plan_attack, text= "Goblin", width= 12, font=small_font,
                       command=lambda: select_element("goblin"))
goblin_btn.place(x= CELL_SIZE * 19, y= CELL_SIZE * 3)

archer_btn = tk.Button(canvas_menu_plan_attack, text= "Archer", width= 12, font=small_font,
                       command=lambda: select_element("archer"))
archer_btn.place(x= CELL_SIZE * 19, y= CELL_SIZE * 5)

giant_btn = tk.Button(canvas_menu_plan_attack, text= "Giant", width= 12, font=small_font,
                       command=lambda: select_element("giant"))
giant_btn.place(x= CELL_SIZE * 25, y= CELL_SIZE * 1)

dragon_btn = tk.Button(canvas_menu_plan_attack, text= "Dragon", width= 12, font=small_font,
                       command=lambda: select_element("dragon"))
dragon_btn.place(x= CELL_SIZE * 25, y= CELL_SIZE * 3)

pekka_btn = tk.Button(canvas_menu_plan_attack, text= "Pekka", width= 12, font=small_font,
                       command=lambda: select_element("pekka"))
pekka_btn.place(x= CELL_SIZE * 25, y= CELL_SIZE * 5)