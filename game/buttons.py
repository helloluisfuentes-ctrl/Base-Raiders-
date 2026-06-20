from ui_functions import *
from tkinter import font
from tkinter import messagebox
from player_selection import PlayerSelectionWindow
from stats_window import StatsWindow
from file_manager import register_player, player_exists

# ==========================================================================================
# FUENTES
# ==========================================================================================

large_font = font.Font(family="Comic Sans MS", size=40)
small_font = font.Font(family="Comic Sans MS", size=18)
huge_font = font.Font(family="Comic Sans MS", size=60)
title_font = font.Font(family="Comic Sans MS", size=54, weight="bold")

# ==========================================================================================
# MENÚ DE DEFENSA
# ==========================================================================================

# --- Acciones ---
ready_btn = tk.Button(canvas_menu_plan_defense, text="Ready", width=10,
                      font=large_font, command=lambda: start_plan_attack())
ready_btn.place(x=CELL_SIZE * 1, y=CELL_SIZE * 1)

delete_btn1 = tk.Button(canvas_menu_plan_defense, text="Delete", width=10,
                         font=small_font, command=lambda: select_element("delete_structure"))
delete_btn1.place(x=CELL_SIZE * 12, y=CELL_SIZE * 1)

# --- Estructuras ---
wall_btn = tk.Button(canvas_menu_plan_defense, text="Wall $75", width=12,
                     font=small_font, command=lambda: select_element("wall"))
wall_btn.place(x=CELL_SIZE * 19, y=CELL_SIZE * 1)

wzrd_tower_btn = tk.Button(canvas_menu_plan_defense, text="Wizard $200", width=12,
                            font=small_font, command=lambda: select_element("wzrd_tower"))
wzrd_tower_btn.place(x=CELL_SIZE * 25, y=CELL_SIZE * 1)

crsbw_tower_btn = tk.Button(canvas_menu_plan_defense, text="Crossbow $180", width=12,
                             font=small_font, command=lambda: select_element("crsbw_tower"))
crsbw_tower_btn.place(x=CELL_SIZE * 25, y=CELL_SIZE * 3)

spk_tower_btn = tk.Button(canvas_menu_plan_defense, text="Spiky $150", width=12,
                           font=small_font, command=lambda: select_element("spk_tower"))
spk_tower_btn.place(x=CELL_SIZE * 25, y=CELL_SIZE * 5)

# ==========================================================================================
# MENÚ DE ATAQUE
# ==========================================================================================

# --- Acciones ---
start_btn = tk.Button(canvas_menu_plan_attack, text="Start", width=10,
                      font=large_font, command=lambda: start_game())
start_btn.place(x=CELL_SIZE * 1, y=CELL_SIZE * 1)

delete_btn2 = tk.Button(canvas_menu_plan_attack, text="Delete", width=10,
                         font=small_font, command=lambda: select_element("delete_troop"))
delete_btn2.place(x=CELL_SIZE * 12, y=CELL_SIZE * 1)

# --- Tropas ---
knight_btn = tk.Button(canvas_menu_plan_attack, text="Knight $100", width=12,
                       font=small_font, command=lambda: select_element("knight"))
knight_btn.place(x=CELL_SIZE * 19, y=CELL_SIZE * 1)

goblin_btn = tk.Button(canvas_menu_plan_attack, text="Goblin $50", width=12,
                       font=small_font, command=lambda: select_element("goblin"))
goblin_btn.place(x=CELL_SIZE * 19, y=CELL_SIZE * 3)

archer_btn = tk.Button(canvas_menu_plan_attack, text="Archer $120", width=12,
                       font=small_font, command=lambda: select_element("archer"))
archer_btn.place(x=CELL_SIZE * 19, y=CELL_SIZE * 5)

giant_btn = tk.Button(canvas_menu_plan_attack, text="Giant $200", width=12,
                      font=small_font, command=lambda: select_element("giant"))
giant_btn.place(x=CELL_SIZE * 25, y=CELL_SIZE * 1)

dragon_btn = tk.Button(canvas_menu_plan_attack, text="Dragon $180", width=12,
                       font=small_font, command=lambda: select_element("dragon"))
dragon_btn.place(x=CELL_SIZE * 25, y=CELL_SIZE * 3)

pekka_btn = tk.Button(canvas_menu_plan_attack, text="Pekka $150", width=12,
                      font=small_font, command=lambda: select_element("pekka"))
pekka_btn.place(x=CELL_SIZE * 25, y=CELL_SIZE * 5)

# ==========================================================================================
# MENÚ PRINCIPAL
# ==========================================================================================

def open_player_selection():
    """Abre la ventana de selección de jugadores."""
    PlayerSelectionWindow(root)

def open_stats_window():
    """Abre la ventana de estadísticas."""
    StatsWindow(root)


def open_register_window():
    """Abre una ventana separada para registrar jugadores."""
    window = tk.Toplevel(root)
    window.title("Registrar jugador")
    window.geometry("360x260")
    window.resizable(False, False)

    tk.Label(window, text="Registrar jugador", font=("Arial", 18, "bold")).pack(pady=12)
    tk.Label(window, text="Usuario:", font=("Arial", 11)).pack(anchor=tk.W, padx=32)
    username_entry = tk.Entry(window, font=("Arial", 11), width=28)
    username_entry.pack(pady=4)

    tk.Label(window, text="Contrasena:", font=("Arial", 11)).pack(anchor=tk.W, padx=32)
    password_entry = tk.Entry(window, font=("Arial", 11), width=28, show="*")
    password_entry.pack(pady=4)

    def register():
        username = username_entry.get().strip()
        password = password_entry.get()
        if not username or not password:
            messagebox.showerror("Error", "Debes ingresar usuario y contrasena")
            return
        if player_exists(username):
            messagebox.showerror("Error", "Ese jugador ya existe")
            return
        if register_player(username, password):
            messagebox.showinfo("Listo", f"Jugador '{username}' registrado")
            window.destroy()
        else:
            messagebox.showerror("Error", "No se pudo registrar el jugador")

    tk.Button(window, text="Registrar", font=("Arial", 12, "bold"),
              command=register, bg="gold", width=16).pack(pady=16)

# Botones del menú principal
canvas_main_menu.create_text(CELL_SIZE * 16, CELL_SIZE * 4, text="BASE RAIDERS",
                             font=title_font, fill="white")
canvas_main_menu.create_text(CELL_SIZE * 16, CELL_SIZE * 6, text="Defensa y Asalto de Base",
                             font=("Arial", 22, "bold"), fill="lightgreen")

play_btn = tk.Button(canvas_main_menu, text="JUGAR", width=18,
                     font=large_font, command=open_player_selection,
                     bg="green", fg="white")
play_btn.place(x=CELL_SIZE * 7, y=CELL_SIZE * 8)

register_btn = tk.Button(canvas_main_menu, text="REGISTRAR", width=18,
                         font=large_font, command=open_register_window,
                         bg="gold", fg="black")
register_btn.place(x=CELL_SIZE * 7, y=CELL_SIZE * 12)

stats_btn = tk.Button(canvas_main_menu, text="RANKINGS", width=18,
                      font=large_font, command=open_stats_window,
                      bg="skyblue", fg="black")
stats_btn.place(x=CELL_SIZE * 7, y=CELL_SIZE * 16)
