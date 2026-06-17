import constants
from ui_screens import *
from classes import *


# ==========================================================================================
# Check_win
# ==========================================================================================
def check_win():
    if len(list_raiders) < 1:
        show_defense_win()
    elif constants.central_base.actual_health <= 0:
        show_raiders_win()
        
def show_raiders_win():
    """Detiene el juego y muestra pantalla de victoria para los raiders."""
    constants.running = "win"
    game_frame.pack_forget()
    win_raiders_frame.pack()

def show_defense_win():
    """Detiene el juego y muestra pantalla de victoria para la defensa."""
    constants.running = "win"
    game_frame.pack_forget()
    win_defense_frame.pack()

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
    for raider in list_raiders:
        if raider.actual_health <= 0:
            list_raiders.remove(raider)
            continue
        
        canvas_field.create_image(raider.x0, raider.y0, image=raider.image, anchor="nw")
        draw_hp(raider)


def draw_towers():
    """Dibuja todas las torres. Elimina las que tienen vida <= 0."""
    for tower in list_towers:
        if tower.actual_health <= 0:
            list_towers.remove(tower)
            continue
        canvas_field.create_rectangle(tower.x0, tower.y0, tower.x1, tower.y1,
                                      fill=tower.image, outline="black", width=2)
        draw_hp(tower)


def draw_walls():
    """Dibuja todas las paredes. Elimina las que tienen vida <= 0."""
    for wall in list_walls:
        if wall.actual_health <= 0:
            list_walls.remove(wall)
            continue
        canvas_field.create_rectangle(wall.x0, wall.y0, wall.x1, wall.y1,
                                      fill="brown", outline="black", width=2)
        draw_hp(wall)


def draw_base():
    """Dibuja la base central. La elimina si tiene vida <= 0."""
    if constants.central_base.actual_health <= 0:
        check_win()
        return
    canvas_field.create_rectangle(constants.central_base.x0, constants.central_base.y0,
                                  constants.central_base.x1, constants.central_base.y1,
                                  fill="white", outline="black", width=2)
    draw_hp(constants.central_base)


def draw_projectiles_raiders():
    """Dibuja los proyectiles de los raiders (flechas, bolas de fuego)."""
    for projectile in constants.list_projectiles_raiders:
        canvas_field.create_rectangle(projectile.x0, projectile.y0, projectile.x1, projectile.y1,
                                      fill=projectile.image, outline="")


def draw_projectiles_towers():
    """Dibuja los proyectiles de las torres (hechizos, ballestas)."""
    for projectile in constants.list_projectiles_towers:
        canvas_field.create_rectangle(projectile.x0, projectile.y0, projectile.x1, projectile.y1,
                                      fill=projectile.image, outline="")


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
            structure_hit.actual_health -= projectile.attack
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
            troop_hit.actual_health -= projectile.attack
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
        structure.actual_health -= troop.attack

    troop.cooldown_timer = troop.cooldown


def shoot_structure(troop):
    """Crea el proyectil correspondiente al troop y lo agrega a list_projectiles_raiders."""
    if isinstance(troop, Archer):
        constants.list_projectiles_raiders.append(ArcherArrow(troop.x0, troop.y0))
    elif isinstance(troop, Dragon):
        constants.list_projectiles_raiders.append(DragonFireball(troop.x0, troop.y0))


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

    # Ataque ranged: dispara proyectil
    if isinstance(structure, (Wizard_tower, Crossbow_tower)):
        shoot_troop(structure)
    # Ataque melee: daño directo (Spiky_tower)
    else:
        troop.actual_health -= structure.attack

    structure.cooldown_timer = structure.cooldown


def shoot_troop(structure):
    """Crea el proyectil correspondiente a la torre y lo agrega a list_projectiles_towers."""
    if isinstance(structure, Wizard_tower):
        constants.list_projectiles_towers.append(WizardSpell(structure.x0, structure.y0))
    elif isinstance(structure, Crossbow_tower):
        constants.list_projectiles_towers.append(CrossbowBolt(structure.x0, structure.y0))


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