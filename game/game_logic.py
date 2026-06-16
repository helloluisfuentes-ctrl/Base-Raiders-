import constants
from ui_screens import *
from classes import *

# ==========================================================================================
# Funciones para dibujar personajes
# ==========================================================================================
def draw_hp(unit):
    if unit.actual_health == unit.max_health:
        return
        
    x0 = unit.x0
    y0 = unit.y0
    x1 = unit.x1

    canvas_field.create_rectangle(x0 -1 , y0 - 14, x1 + 1, y0 - 9, fill= "black")
    hp_width = (unit.width/unit.max_health)*unit.actual_health
    canvas_field.create_rectangle(x0, y0 - 13, x0 + hp_width, y0 - 10, fill= "lightgreen")

def draw_raiders(): #TODO add images
    for raider in list_raiders:
        
        if raider.actual_health <= 0:
            list_raiders.remove(raider)
            continue
        
        x0 = raider.x0
        y0 = raider.y0
        x1 = raider.x1
        y1 = raider.y1
        
        color = raider.image
        
        canvas_field.create_rectangle(x0, y0, x1, y1, fill=color, outline="black", width=2)
        
        
        draw_hp(raider)
        
        

def draw_towers(): #TODO add images
    for tower in list_towers:
        
        if tower.actual_health <= 0:
            list_towers.remove(tower)
            continue
        
        x0 = tower.x0
        y0 = tower.y0
        x1 = tower.x1
        y1 = tower.y1
        
        color = tower.image
        
        canvas_field.create_rectangle(x0, y0, x1, y1, fill=color, outline="black", width=2)
        
        
        draw_hp(tower)
                
def draw_walls():
    for wall in list_walls:
        
        if wall.actual_health <= 0:
            list_walls.remove(wall)
            continue
        
        x0 = wall.x0
        y0 = wall.y0
        x1 = wall.x1
        y1 = wall.y1 
        
        canvas_field.create_rectangle(x0, y0, x1, y1, fill="brown", outline="black", width=2)
        draw_hp(wall)

def draw_base():
    if constants.central_base.actual_health <= 0:
        constants.central_base = None
    
    x0 = constants.central_base.x0
    y0 = constants.central_base.y0
    x1 = constants.central_base.x1
    y1 = constants.central_base.y1 
        
    canvas_field.create_rectangle(x0, y0, x1, y1, fill="white", outline="black", width=2)
    draw_hp(constants.central_base)    
    
# ==========================================================================================
# Funciones con hitbox
# ==========================================================================================
      
def what_structure_is_in_range(element):
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
        if x0 <= constants.central_base.x1 and x1 >= constants.central_base.x0 and y0 <= constants.central_base.y1 and y1 >= constants.central_base.y0:
            return constants.central_base
        
    return None

def what_troop_is_in_range(element):
    x0 = element.x0 - element.range
    y0 = element.y0 - element.range
    x1 = element.x1 + element.range
    y1 = element.y1 + element.range
    
    for troop in list_raiders[:]:
        if x0 <= troop.x1 and x1 >= troop.x0 and y0 <= troop.y1 and y1 >= troop.y0:
            return troop

    return None

# ==========================================================================================
# Funciones con movimiento
# ==========================================================================================

def nearest_structure_target(troop):
    targets = list_towers if list_towers else ([constants.central_base] if constants.central_base else [])
    
    if not targets:
        return None
    
    def distance(unit):
        center_troop_x = troop.x0 + troop.width / 2
        center_troop_y = troop.y0 + troop.height / 2
        center_target_x = unit.x0 + unit.width / 2
        center_target_y = unit.y0 + unit.height / 2
        return ((center_troop_x - center_target_x)**2 + (center_troop_y - center_target_y)**2) ** 0.5
    
    return min(targets, key=distance)

def nearest_troop_target(tower):
    if not list_raiders:
        return None
    
    def distance(troop):
        center_tower_x = tower.x0 + tower.width / 2
        center_tower_y = tower.y0 + tower.height / 2
        center_troop_x = troop.x0 + troop.width / 2
        center_troop_y = troop.y0 + troop.height / 2
        return ((center_tower_x - center_troop_x)**2 + (center_tower_y - center_troop_y)**2) ** 0.5
    
    return min(list_raiders, key=distance)

def move_troop(troop, target):
    center_troop_x = troop.x0 + troop.width / 2
    center_troop_y = troop.y0 + troop.height / 2
    center_target_x = target.x0 + target.width / 2
    center_target_y = target.y0 + target.height / 2

    dx = center_target_x - center_troop_x
    dy = center_target_y - center_troop_y
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
    for projectile in constants.list_projectiles_raiders[:]:
        target = nearest_structure_target(projectile)
        if target is None:
            constants.list_projectiles_raiders.remove(projectile)
            continue
        move_troop(projectile, target)

def move_projectiles_towers():
    for projectile in constants.list_projectiles_towers[:]:
        target = nearest_troop_target(projectile)
        if target is None:
            constants.list_projectiles_towers.remove(projectile)
            continue
        move_troop(projectile, target)

# ==========================================================================================
# Funciones con ataque
# ==========================================================================================

def attack_structure(troop, structure):
    
    if isinstance(troop, ArcherArrow) or isinstance(troop, DragonFireball):
        structure.actual_health -= troop.attack
        constants.list_projectiles_raiders.remove(troop)
        return
    
    if troop.cooldown_timer > 0:
        troop.cooldown_timer -= 1
        return
    
    if isinstance(troop, Archer) or isinstance(troop, Dragon):
        shoot_structure(troop)
    else:
        structure.actual_health -= troop.attack
        
    troop.cooldown_timer = troop.cooldown
               
def shoot_structure(troop):
    if isinstance(troop, Archer):
        arrow = ArcherArrow(troop.x0, troop.y0)
        constants.list_projectiles_raiders.append(arrow) 
    elif isinstance(troop, Dragon):
        fireball = DragonFireball(troop.x0, troop.y0)
        constants.list_projectiles_raiders.append(fireball)

# ----------------------------------------------------------------------------------------

def attack_troop(structure, troop):

    if isinstance(structure, WizardSpell) or isinstance(structure, CrossbowBolt):
        troop.actual_health -= structure.attack
        constants.list_projectiles_towers.remove(structure)
        return

    if structure.cooldown_timer > 0:
        structure.cooldown_timer -= 1
        return

    if isinstance(structure, Wizard_tower) or isinstance(structure, Crossbow_tower):
        shoot_troop(structure)
    else:
        troop.actual_health -= structure.attack  # spiky tower

    structure.cooldown_timer = structure.cooldown

def shoot_troop(structure):
    if isinstance(structure, Wizard_tower):
        spell = WizardSpell(structure.x0, structure.y0)
        constants.list_projectiles_towers.append(spell)
    elif isinstance(structure, Crossbow_tower):
        bolt = CrossbowBolt(structure.x0, structure.y0)
        constants.list_projectiles_towers.append(bolt)

# ==========================================================================================
# Funciones con manejo de acciones
# ==========================================================================================

def activate_troops():
    for troop in list_raiders:
        move_or_attack(troop)

def activate_towers():
    for structure in list_towers:
        troop_in_range = what_troop_is_in_range(structure)
        if troop_in_range:
            attack_troop(structure, troop_in_range)

def move_or_attack(troop):
    structure_in_range = what_structure_is_in_range(troop)
    
    if structure_in_range:
        attack_structure(troop, structure_in_range)
        return
    
    target = nearest_structure_target(troop)
    if target:
        move_troop(troop, target)