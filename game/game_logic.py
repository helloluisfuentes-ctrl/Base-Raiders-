import constants
from ui_screens import *
from classes import *
from file_manager import update_player_wins
from money_management import money_manager
from tkinter import messagebox
import images


# ==========================================================================================
# Check_win
# ==========================================================================================
def check_win():
    if constants.running != "game":
        return
    if len(list_raiders) < 1:
        show_defense_win()
    elif constants.central_base.actual_health <= 0:
        show_raiders_win()
        
def show_raiders_win():
    """Detiene el juego y muestra pantalla de victoria para los raiders."""
    money_manager.save_previous_round_stats()
    constants.attacker_round_wins += 1
    if constants.attacker_round_wins >= constants.MATCH_WIN_ROUNDS:
        if constants.current_attacker:
            update_player_wins(constants.current_attacker, "attack")
        constants.running = "win"
        game_frame.pack_forget()
        canvas_win_raiders.delete("match_info")
        canvas_win_raiders.create_text(
            CELL_SIZE * 16, CELL_SIZE * 11,
            text=f"Marcador final: {constants.attacker_round_wins} - {constants.defender_round_wins}",
            font=("Arial", 24, "bold"),
            fill="white",
            tags="match_info"
        )
        win_raiders_frame.pack()
        return
    finish_round("Atacante")

def finish_round(winner_name):
    """Cierra una ronda y prepara la siguiente si la partida no ha terminado."""
    constants.running = "win"
    messagebox.showinfo(
        "Ronda terminada",
        f"Gano la ronda: {winner_name}\nMarcador: Atacante {constants.attacker_round_wins} - Defensor {constants.defender_round_wins}"
    )
    constants.round_number += 1
    from ui_functions import reset_game_state, start_plan_defense
    reset_game_state(reset_match=False)
    start_plan_defense()

def show_defense_win():
    """Detiene el juego y muestra pantalla de victoria para la defensa."""
    money_manager.save_previous_round_stats()
    constants.defender_round_wins += 1
    if constants.defender_round_wins >= constants.MATCH_WIN_ROUNDS:
        if constants.current_defender:
            update_player_wins(constants.current_defender, "defense")
        constants.running = "win"
        game_frame.pack_forget()
        canvas_win_defense.delete("match_info")
        canvas_win_defense.create_text(
            CELL_SIZE * 16, CELL_SIZE * 11,
            text=f"Marcador final: {constants.attacker_round_wins} - {constants.defender_round_wins}",
            font=("Arial", 24, "bold"),
            fill="white",
            tags="match_info"
        )
        win_defense_frame.pack()
        return
    finish_round("Defensor")

# ==========================================================================================
# DIBUJO
# ==========================================================================================
def draw_limit_line():
    canvas_field.create_line(18 * CELL_SIZE, 0, 18 * CELL_SIZE, 16 * CELL_SIZE, fill= "white", width= 4)

def draw_hp(unit):
    """Dibuja la barra de vida encima de la unidad. No se muestra si está al máximo."""
    if unit.actual_health == unit.max_health:
        return
        
    x0 = unit.x0
    y0 = unit.y0
    x1 = unit.x1

    # Fondo negro de la barra
    canvas_field.create_rectangle(x0 - 1, y0 - 14, x1 + 1, y0 - 9, fill="black")
    # Barra verde proporcional a la vida actual
    hp_width = (unit.width / unit.max_health) * unit.actual_health
    canvas_field.create_rectangle(x0, y0 - 13, x0 + hp_width, y0 - 10, fill="lightgreen")


def draw_raiders():
    """Dibuja todos los raiders. Elimina los que tienen vida <= 0."""
    for raider in list_raiders[:]:
        if raider.actual_health <= 0:
            list_raiders.remove(raider)
            if not getattr(raider, "reward_paid", False):
                money_manager.give_defender_unit_bonus(raider)
                raider.reward_paid = True
            continue
        
        outline = images.FACTIONS[constants.attacker_faction]["unit_outline"]
        canvas_field.create_line(raider.x0 + 2, raider.y1 + 2, raider.x1 - 2, raider.y1 + 2,
                                      fill=outline, width=2)
        canvas_field.create_image(raider.x0, raider.y0, image=raider.image, anchor="nw")
        draw_hp(raider)


def draw_towers():
    """Dibuja todas las torres. Elimina las que tienen vida <= 0."""
    for tower in list_towers[:]:
        if tower.actual_health <= 0:
            list_towers.remove(tower)
            continue
        
        image_var = images.FACTIONS[constants.defender_faction][tower.name]
        
        canvas_field.create_image(tower.x0, tower.y0, image=image_var, anchor="nw")
        draw_hp(tower)


def draw_walls():
    """Dibuja todas las paredes. Elimina las que tienen vida <= 0."""
    for wall in list_walls[:]:
        if wall.actual_health <= 0:
            list_walls.remove(wall)
            continue
        image_var = images.FACTIONS[constants.defender_faction]["wall"]
        canvas_field.create_image(wall.x0, wall.y0, image=image_var, anchor ="nw")
        draw_hp(wall)


def draw_base():
    """Dibuja la base central. La elimina si tiene vida <= 0."""
    if constants.central_base.actual_health <= 0:
        check_win()
        return
    
    image_var = images.FACTIONS[constants.defender_faction]["base"]
    canvas_field.create_image(constants.central_base.x0, constants.central_base.y0, image= image_var, anchor = "nw")
    draw_hp(constants.central_base)


def draw_projectiles_raiders():
    """Dibuja los proyectiles de los raiders (flechas, bolas de fuego)."""
    for projectile in constants.list_projectiles_raiders:
        canvas_field.create_image(projectile.x0, projectile.y0, image = projectile.image, anchor = "nw")


def draw_projectiles_towers():
    """Dibuja los proyectiles de las torres (hechizos, ballestas)."""
    for projectile in constants.list_projectiles_towers:
        canvas_field.create_image(projectile.x0, projectile.y0, image= projectile.image)


# ==========================================================================================
# DETECCIÓN DE RANGO
# ==========================================================================================

def what_structure_is_in_range(element):
    """
    Verifica si hay alguna estructura dentro del rango del elemento.
    Prioridad: paredes → torres → base central.
    Retorna la primera estructura encontrada, o None.
    """
    x0 = element.x0 - element.range
    y0 = element.y0 - element.range
    x1 = element.x1 + element.range
    y1 = element.y1 + element.range

    for wall in list_walls[:]:
        if x0 <= wall.x1 and x1 >= wall.x0 and y0 <= wall.y1 and y1 >= wall.y0:
            return wall

    for tower in list_towers[:]:
        if x0 <= tower.x1 and x1 >= tower.x0 and y0 <= tower.y1 and y1 >= tower.y0:
            return tower

    if constants.central_base:
        base = constants.central_base
        if x0 <= base.x1 and x1 >= base.x0 and y0 <= base.y1 and y1 >= base.y0:
            return base

    return None


def what_troop_is_in_range(element):
    """
    Verifica si hay algún raider dentro del rango del elemento.
    Retorna el primero encontrado, o None.
    """
    x0 = element.x0 - element.range
    y0 = element.y0 - element.range
    x1 = element.x1 + element.range
    y1 = element.y1 + element.range

    for troop in list_raiders[:]:
        if x0 <= troop.x1 and x1 >= troop.x0 and y0 <= troop.y1 and y1 >= troop.y0:
            return troop

    return None


# ==========================================================================================
# MOVIMIENTO
# ==========================================================================================

def nearest_structure_target(troop):
    """
    Retorna la estructura más cercana al troop.
    Si no hay torres, apunta a la base central.
    """
    targets = list_towers if list_towers else ([constants.central_base] if constants.central_base else [])

    if not targets:
        return None

    def distance(unit):
        cx_troop  = troop.x0 + troop.width  / 2
        cy_troop  = troop.y0 + troop.height / 2
        cx_target = unit.x0  + unit.width   / 2
        cy_target = unit.y0  + unit.height  / 2
        return ((cx_troop - cx_target)**2 + (cy_troop - cy_target)**2) ** 0.5

    return min(targets, key=distance)


def nearest_troop_target(tower):
    """Retorna el raider más cercano a la torre. Retorna None si no hay raiders."""
    if not list_raiders:
        return None

    def distance(troop):
        cx_tower = tower.x0 + tower.width  / 2
        cy_tower = tower.y0 + tower.height / 2
        cx_troop = troop.x0 + troop.width  / 2
        cy_troop = troop.y0 + troop.height / 2
        return ((cx_tower - cx_troop)**2 + (cy_tower - cy_troop)**2) ** 0.5

    return min(list_raiders, key=distance)


def move_troop(troop, target):
    """
    Mueve el troop un paso hacia el target.
    El tamaño del paso depende de troop.speed.
    """
    cx_troop  = troop.x0  + troop.width   / 2
    cy_troop  = troop.y0  + troop.height  / 2
    cx_target = target.x0 + target.width  / 2
    cy_target = target.y0 + target.height / 2

    dx = cx_target - cx_troop
    dy = cy_target - cy_troop
    distance = (dx**2 + dy**2) ** 0.5

    if distance == 0:
        return

    step_x = (dx / distance) * troop.speed
    step_y = (dy / distance) * troop.speed

    troop.x0 += step_x
    troop.y0 += step_y
    troop.x1 += step_x
    troop.y1 += step_y


def move_projectiles_raiders():
    """Mueve cada proyectil de raider y verifica si golpeó una estructura."""
    for projectile in constants.list_projectiles_raiders[:]:
        target = nearest_structure_target(projectile)
        if target is None:
            constants.list_projectiles_raiders.remove(projectile)
            continue
        move_troop(projectile, target)
        # verificar si el proyectil llegó al objetivo
        structure_hit = what_structure_is_in_range(projectile)
        if structure_hit:
            damage_structure(structure_hit, projectile.attack)
            constants.list_projectiles_raiders.remove(projectile)


def move_projectiles_towers():
    """Mueve cada proyectil de torre y verifica si golpeó un raider."""
    for projectile in constants.list_projectiles_towers[:]:
        target = nearest_troop_target(projectile)
        if target is None:
            constants.list_projectiles_towers.remove(projectile)
            continue
        move_troop(projectile, target)
        # verificar si el proyectil llegó al objetivo
        troop_hit = what_troop_is_in_range(projectile)
        if troop_hit:
            damage_troop(troop_hit, projectile.attack)
            if isinstance(projectile, WizardSpell):
                apply_area_damage(projectile, troop_hit, 10)
            constants.list_projectiles_towers.remove(projectile)

# ==========================================================================================
# ATAQUE
# ==========================================================================================

def attack_structure(troop, structure):
    """
    El troop ataca la estructura.
    - Si está en cooldown: espera.
    - Si es Archer o Dragon: dispara un proyectil.
    - Si es melee: daña directamente.
    """

    # Cooldown activo: decrementar y esperar
    if troop.cooldown_timer > 0:
        troop.cooldown_timer -= 1
        return

    # Ataque ranged: dispara proyectil
    if isinstance(troop, (Archer, Dragon)):
        shoot_structure(troop)
    # Ataque melee: daño directo
    else:
        attack_amount = troop.attack
        troop.attack_count += 1
        if isinstance(troop, Knight) and troop.attack_count % troop.ability_turns == 0:
            attack_amount *= 2
        if isinstance(troop, Pekka) and isinstance(structure, Tower):
            attack_amount += 15
        damage_structure(structure, attack_amount)

    troop.cooldown_timer = troop.cooldown


def damage_structure(structure, attack_amount):
    """Aplica dano a estructuras y recompensa al atacante por el dano real."""
    damage_done = min(attack_amount, max(0, structure.actual_health))
    structure.actual_health -= attack_amount
    if damage_done > 0:
        money_manager.give_attacker_damage_bonus(damage_done)
    if isinstance(structure, Tower) and structure.actual_health <= 0 and not getattr(structure, "destroy_bonus_paid", False):
        money_manager.give_tower_destroy_bonus()
        structure.destroy_bonus_paid = True


def shoot_structure(troop):
    """Crea el proyectil correspondiente al troop y lo agrega a list_projectiles_raiders."""
    if isinstance(troop, Archer):
        constants.list_projectiles_raiders.append(ArcherArrow(troop.x0, troop.y0))
        troop.attack_count += 1
        if troop.attack_count % troop.ability_turns == 0:
            constants.list_projectiles_raiders.append(ArcherArrow(troop.x0 + 6, troop.y0))
    elif isinstance(troop, Dragon):
        fireball = DragonFireball(troop.x0, troop.y0)
        troop.attack_count += 1
        if troop.attack_count % troop.ability_turns == 0:
            fireball.attack += 10
        constants.list_projectiles_raiders.append(fireball)


def attack_troop(structure, troop):
    """
    La estructura ataca al troop.
    - Si está en cooldown: espera.
    - Si es Wizard_tower o Crossbow_tower: dispara un proyectil.
    - Si es Spiky_tower: daño melee directo.
    """
    # Cooldown activo: decrementar y esperar
    if structure.cooldown_timer > 0:
        structure.cooldown_timer -= 1
        return

    structure.attack_count += 1
    # Ataque ranged: dispara proyectil
    if isinstance(structure, (Wizard_tower, Crossbow_tower)):
        shoot_troop(structure)
        if isinstance(structure, Crossbow_tower) and structure.attack_count % structure.ability_turns == 0:
            shoot_troop(structure)
    # Ataque melee: daño directo (Spiky_tower)
    else:
        damage_troop(troop, structure.attack)
        if structure.attack_count % structure.ability_turns == 0:
            troop.speed = max(1, troop.speed - 1)

    structure.cooldown_timer = structure.cooldown


def shoot_troop(structure):
    """Crea el proyectil correspondiente a la torre y lo agrega a list_projectiles_towers."""
    if isinstance(structure, Wizard_tower):
        constants.list_projectiles_towers.append(WizardSpell(structure.x0, structure.y0))
    elif isinstance(structure, Crossbow_tower):
        constants.list_projectiles_towers.append(CrossbowBolt(structure.x0, structure.y0))


def damage_troop(troop, attack_amount):
    """Aplica dano a una unidad, tomando en cuenta habilidades defensivas."""
    if isinstance(troop, Giant):
        attack_amount = max(1, attack_amount - 5)
    troop.actual_health -= attack_amount


def apply_area_damage(projectile, main_target, attack_amount):
    """Habilidad de torre magica: dana unidades cercanas al objetivo principal."""
    for troop in list_raiders[:]:
        if troop is main_target:
            continue
        if abs(troop.x0 - main_target.x0) <= CELL_SIZE and abs(troop.y0 - main_target.y0) <= CELL_SIZE:
            damage_troop(troop, attack_amount)


# ==========================================================================================
# LOOP DE ACCIONES
# ==========================================================================================

def activate_troops():
    """Itera sobre todos los raiders y ejecuta su acción (atacar o moverse)."""
    for troop in list_raiders:
        move_or_attack(troop)


def activate_towers():
    """Itera sobre todas las torres y ataca al raider más cercano si está en rango."""
    for structure in list_towers:
        troop_in_range = what_troop_is_in_range(structure)
        if troop_in_range:
            attack_troop(structure, troop_in_range)


def move_or_attack(troop):
    """
    Decide si el troop ataca o se mueve.
    Si hay una estructura en rango: ataca.
    Si no: se mueve hacia la estructura más cercana.
    """
    structure_in_range = what_structure_is_in_range(troop)

    if structure_in_range:
        attack_structure(troop, structure_in_range)
        return

    target = nearest_structure_target(troop)
    if target:
        move_troop(troop, target)
