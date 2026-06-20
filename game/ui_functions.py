from ui_screens import *
from classes import *
import constants
from game_loops import *

# ==========================================================================================
# MANEJO DE ESTADOS DEL JUEGO
# ==========================================================================================

def start_plan_defense():
    """Inicia la fase de planeación de defensa. Coloca la base central y arranca el loop."""
    game_frame.pack()
    canvas_field.pack()
    canvas_menu_plan_defense.pack()
    constants.central_base = Base(x0=CELL_SIZE * 2, y0=CELL_SIZE * 7)
    constants.running = "plan"
    root.after(32, planning_loop)


def start_plan_attack():
    """Transiciona a la fase de planeación de ataque."""
    canvas_menu_plan_defense.pack_forget()
    constants.selected_element = None
    canvas_menu_plan_attack.pack()


def start_game():
    """Inicia la fase de juego y arranca el loop principal."""
    canvas_menu_plan_attack.pack_forget()
    canvas_menu_on_game.pack()
    constants.selected_element = None
    constants.running = "game"
    root.after(32, on_game_loop)

# ==========================================================================================
# SELECCIÓN DE ELEMENTOS
# ==========================================================================================

def select_element(element):
    """Guarda el elemento seleccionado para ser colocado al hacer clic en el campo."""
    constants.selected_element = element


# ==========================================================================================
# VALIDACIONES DE PLACEMENT
# ==========================================================================================

def is_there_a_structure(x, y):
    """
    Verifica si ya existe una estructura en la posición (x, y).
    Se usa para evitar colocar elementos encima de otros.
    """
    for wall in list_walls[:]:
        if wall.x0 <= x <= wall.x1 and wall.y0 <= y <= wall.y1:
            return True

    for tower in list_towers[:]:
        if tower.x0 <= x <= tower.x1 and tower.y0 <= y <= tower.y1:
            return True

    if constants.central_base:
        base = constants.central_base
        if base.x0 <= x <= base.x1 and base.y0 <= y <= base.y1:
            return True

    return False


def in_attack_zone(x, y):
    """Verifica que la posición esté en la zona de ataque (mitad derecha del campo)."""
    return CELL_SIZE * 18 <= x <= CELL_SIZE * 32 and 0 <= y <= CELL_SIZE * 16


def in_defense_zone(x, y):
    """Verifica que la posición esté en la zona de defensa (mitad izquierda del campo)."""
    return 0 <= x < CELL_SIZE * 18 and 0 <= y <= CELL_SIZE * 16


# ==========================================================================================
# COLOCACIÓN DE ELEMENTOS EN EL MAPA
# ==========================================================================================

def place_troop(event):
    """
    Coloca un troop en la zona de ataque según el elemento seleccionado.
    Los troops no se alinean a la grilla.
    """
    if not in_attack_zone(event.x, event.y):
        return

    sel = constants.selected_element

    if sel == "knight":
        list_raiders.append(Knight(event.x, event.y))
    elif sel == "goblin":
        list_raiders.append(Goblin(event.x, event.y))
    elif sel == "archer":
        list_raiders.append(Archer(event.x, event.y))
    elif sel == "giant":
        list_raiders.append(Giant(event.x, event.y))
    elif sel == "dragon":
        list_raiders.append(Dragon(event.x, event.y))
    elif sel == "pekka":
        list_raiders.append(Pekka(event.x, event.y))


def place_tower(event):
    """
    Coloca una torre en la zona de defensa según el elemento seleccionado.
    Se alinea al grid. No se coloca si ya hay una estructura en ese punto.
    """
    if not in_defense_zone(event.x, event.y):
        return
    if is_there_a_structure(event.x, event.y):
        return

    # Alinear al grid
    gx = event.x - event.x % CELL_SIZE
    gy = event.y - event.y % CELL_SIZE

    sel = constants.selected_element

    if sel == "wzrd_tower":
        list_towers.append(Wizard_tower(gx, gy))
    elif sel == "crsbw_tower":
        list_towers.append(Crossbow_tower(gx, gy))
    elif sel == "spk_tower":
        list_towers.append(Spiky_tower(gx, gy))


def place_wall(event):
    """
    Coloca una pared en la zona de defensa.
    Se alinea al grid. No se coloca si ya hay una estructura en ese punto.
    """
    if not in_defense_zone(event.x, event.y):
        return
    if is_there_a_structure(event.x, event.y):
        return

    gx = event.x - event.x % CELL_SIZE
    gy = event.y - event.y % CELL_SIZE
    list_walls.append(Wall(gx, gy))


def delete_structure(event):
    """Elimina la pared o torre en la posición clickeada."""
    for wall in list_walls[:]:
        if wall.x0 <= event.x <= wall.x1 and wall.y0 <= event.y <= wall.y1:
            list_walls.remove(wall)
            return

    for tower in list_towers[:]:
        if tower.x0 <= event.x <= tower.x1 and tower.y0 <= event.y <= tower.y1:
            list_towers.remove(tower)
            return


def delete_troop(event):
    """Elimina el troop en la posición clickeada."""
    for troop in list_raiders[:]:
        if troop.x0 <= event.x <= troop.x1 and troop.y0 <= event.y <= troop.y1:
            list_raiders.remove(troop)


# ==========================================================================================
# DISPATCHER PRINCIPAL DE CLICKS
# ==========================================================================================

def place_element(event):
    """
    Recibe el click en el campo y delega la acción según el elemento seleccionado.
    """
    sel = constants.selected_element

    if sel in ("knight", "goblin", "archer", "giant", "dragon", "pekka"):
        place_troop(event)

    elif sel in ("wzrd_tower", "crsbw_tower", "spk_tower"):
        place_tower(event)

    elif sel == "wall":
        place_wall(event)

    elif sel == "delete_structure":
        delete_structure(event)

    elif sel == "delete_troop":
        delete_troop(event)


canvas_field.bind("<Button-1>", place_element)

# ==========================================================================================
# MENÚ PRINCIPAL
# ==========================================================================================

def show_main_menu():
    """Muestra el menú principal."""
    main_menu_frame.pack()
    canvas_main_menu.pack()


def hide_main_menu():
    """Oculta el menú principal."""
    main_menu_frame.pack_forget()


def reset_game_state():
    """Resetea el estado del juego para una nueva partida."""
    # Limpiar listas de elementos
    list_raiders.clear()
    list_walls.clear()
    list_towers.clear()
    list_projectiles_raiders.clear()
    list_projectiles_towers.clear()
    
    # Resetear variables
    constants.central_base = None
    constants.selected_element = None
    constants.running = None
    
    # Resetear dinero
    from money_management import money_manager
    money_manager.reset_round_money()


def return_to_main_menu():
    """Retorna al menú principal desde la pantalla de victoria."""
    # Ocultar pantallas de victoria
    win_raiders_frame.pack_forget()
    win_defense_frame.pack_forget()
    
    # Resetear estado del juego
    reset_game_state()
    
    # Mostrar menú principal
    show_main_menu()