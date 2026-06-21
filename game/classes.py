from images import *
"""
Clases:

player

Unit
    Estructure      # estructuras:  muros, base central
        Base
        Wall
    Troop           # tropas:
        Knight
        Dragon
        Pekka
        Archer
        Giant
        Goblin
    Tower
        Wizard_tower
        Crossbow_tower
        spiky_tower
        
        
        
        
        
"""

# ===========================================================================

class Player:
    def __init__(self, nickname, password):
        self.nickname = nickname
        self.password = password
        self.attack_wins = 0
        self.defense_wins = 0
        
# ===========================================================================
      
class Unit:
    def __init__(self, x0, y0, width, height, max_health, range=0):
        self.width = width
        self.height = height  
        self.x0 = x0
        self.y0 = y0
        self.x1 = x0 + width
        self.y1 = y0 + height
        self.max_health = max_health
        self.actual_health = max_health
        self.range = range
        self.name = self.__class__.__name__
        self.cost = 0
        self.attack_count = 0
        self.ability_name = "Sin habilidad"
        self.ability_turns = 0
        self.reward = 50

# ---------------------------------------------------------------------------

class Structure(Unit):
    def __init__(self, x0, y0, width, height, max_health, range=0):
        super().__init__(x0, y0, width, height, max_health, range)
        
# ---------------------------------------------------------------------------

class Troop(Unit):
    def __init__(self, x0, y0, width, height, max_health, range=0):
        super().__init__(x0, y0, width, height, max_health, range)
        
# ---------------------------------------------------------------------------

class Tower(Unit):
    def __init__(self, x0, y0, width, height, max_health, range=0):
        super().__init__(x0, y0, width, height, max_health, range)

# ---------------------------------------------------------------------------------------

class Base(Structure):
    def __init__(self, x0, y0):
        super().__init__(x0, y0, width=64, height=64, max_health=500, range=0)
        self.name = "Base Central"
        
class Wall(Structure):
    def __init__(self, x0, y0):
        super().__init__(x0, y0, width=32, height=32, max_health=200, range=0)
        self.name = "Muro"
        self.cost = 75
        
# ----------------------------------------------------------------------------

class Pekka(Troop):
    def __init__(self, x0, y0):
        super().__init__(x0, y0, width=24, height=24, max_health=100, range=8)
        self.image = img_pekka
        self.speed = 2
        self.attack = 35
        self.cooldown = 40
        self.cooldown_timer = 0
        self.cost = 150
        self.reward = 90
        self.ability_name = "Rompe torres"
        self.ability_turns = 1

class Dragon(Troop):
    def __init__(self, x0, y0):
        super().__init__(x0, y0, width=32, height=16, max_health=80, range=64)
        self.image = img_dragon
        self.speed = 4
        self.projectiles = []
        self.cooldown = 25
        self.cooldown_timer = 0
        self.cost = 180
        self.reward = 100
        self.ability_name = "Fuego potenciado"
        self.ability_turns = 3
        
class Knight(Troop):
    def __init__(self, x0, y0):
        super().__init__(x0, y0, width=16, height=16, max_health=100, range=8)
        self.image = img_knight
        self.speed = 3
        self.attack = 20
        self.cooldown = 30
        self.cooldown_timer = 0
        self.cost = 100
        self.reward = 60
        self.ability_name = "Ataque doble"
        self.ability_turns = 3

class Archer(Troop):
    def __init__(self, x0, y0):
        super().__init__(x0, y0, width=10, height=12, max_health=60, range=96)
        self.image = img_archer
        self.speed = 3
        self.projectiles = []
        self.cooldown = 20
        self.cooldown_timer = 0
        self.cost = 120
        self.reward = 70
        self.ability_name = "Doble flecha"
        self.ability_turns = 4

class Giant(Troop):
    def __init__(self, x0, y0):
        super().__init__(x0, y0, width=56, height=58, max_health=300, range=8)
        self.image = img_giant
        self.speed = 1
        self.attack = 60
        self.cooldown = 60
        self.cooldown_timer = 0
        self.cost = 200
        self.reward = 120
        self.ability_name = "Escudo pesado"
        self.ability_turns = 1

class Goblin(Troop):
    def __init__(self, x0, y0):
        super().__init__(x0, y0, width=10, height=10, max_health=40, range=8)
        self.image = img_goblin
        self.speed = 5
        self.attack = 8
        self.cooldown = 15
        self.cooldown_timer = 0
        self.cost = 50
        self.reward = 40
        self.ability_name = "Aumento de velocidad"
        self.ability_turns = 1

# ----------------------------------------------------------------------------

class Wizard_tower(Tower):
    def __init__(self, x0, y0):
        super().__init__(x0, y0, width=32, height=32, max_health=250, range=180)
        self.name = "wizard_tower"
        self.image = "blue"
        self.projectiles = []
        self.cooldown = 35
        self.cooldown_timer = 0
        self.cost = 200
        self.attack = 30
        self.ability_name = "Dano en area"
        self.ability_turns = 3

class Crossbow_tower(Tower):
    def __init__(self, x0, y0):
        super().__init__(x0, y0, width=32, height=32, max_health=200, range=250)
        self.name = "crossbow_tower"
        self.image = "lightblue"
        self.projectiles = []
        self.cooldown = 5
        self.cooldown_timer = 0
        self.cost = 180
        self.attack = 2
        self.ability_name = "Disparo doble"
        self.ability_turns = 3

class Spiky_tower(Tower):
    def __init__(self, x0, y0):
        super().__init__(x0, y0, width=32, height=32, max_health=150, range=16)
        self.name = "spiky_tower"
        self.image = "yellow"
        self.attack = 50
        self.cooldown = 25
        self.cooldown_timer = 0
        self.cost = 150
        self.ability_name = "Congelar unidad"
        self.ability_turns = 4
        
# ------------------------------------------------------------------------------

class DragonFireball(Unit):
    def __init__(self, x0, y0):
        super().__init__(x0, y0, width=8, height=8, max_health=1, range=1)
        self.attack = 15
        self.speed = 6
        self.image = img_dragon_fireball

class ArcherArrow(Unit):
    def __init__(self, x0, y0):
        super().__init__(x0, y0, width=4, height=4, max_health=1, range=1)
        self.attack = 10
        self.speed = 8
        self.image = img_archer_arrow

class WizardSpell(Unit):
    def __init__(self, x0, y0):
        super().__init__(x0, y0, width=8, height=8, max_health=1, range=1)
        self.attack = 30
        self.speed = 5
        self.image = img_wizard_spell

class CrossbowBolt(Unit):
    def __init__(self, x0, y0):
        super().__init__(x0, y0, width=4, height=4, max_health=1, range=1)
        self.attack = 4
        self.speed = 10
        self.image = img_crossbow_bolt
