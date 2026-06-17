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
        
class Wall(Structure):
    def __init__(self, x0, y0):
        super().__init__(x0, y0, width=32, height=32, max_health=200, range=0)
        
# ----------------------------------------------------------------------------

class Pekka(Troop):
    def __init__(self, x0, y0):
        super().__init__(x0, y0, width=24, height=24, max_health=100, range=16)
        self.image = img_pekka
        self.speed = 2
        self.attack = 25
        self.cooldown = 40
        self.cooldown_timer = 0

class Dragon(Troop):
    def __init__(self, x0, y0):
        super().__init__(x0, y0, width=32, height=16, max_health=80, range=64)
        self.image = img_dragon
        self.speed = 4
        self.projectiles = []
        self.cooldown = 25
        self.cooldown_timer = 0
        
class Knight(Troop):
    def __init__(self, x0, y0):
        super().__init__(x0, y0, width=16, height=16, max_health=100, range=16)
        self.image = img_knight
        self.speed = 3
        self.attack = 20
        self.cooldown = 30
        self.cooldown_timer = 0

class Archer(Troop):
    def __init__(self, x0, y0):
        super().__init__(x0, y0, width=10, height=12, max_health=60, range=96)
        self.image = img_archer
        self.speed = 3
        self.projectiles = []
        self.cooldown = 20
        self.cooldown_timer = 0

class Giant(Troop):
    def __init__(self, x0, y0):
        super().__init__(x0, y0, width=56, height=58, max_health=300, range=16)
        self.image = img_giant
        self.speed = 1
        self.attack = 35
        self.cooldown = 60
        self.cooldown_timer = 0

class Goblin(Troop):
    def __init__(self, x0, y0):
        super().__init__(x0, y0, width=10, height=10, max_health=40, range=16)
        self.image = img_goblin
        self.speed = 5
        self.attack = 8
        self.cooldown = 15
        self.cooldown_timer = 0

# ----------------------------------------------------------------------------

class Wizard_tower(Tower):
    def __init__(self, x0, y0):
        super().__init__(x0, y0, width=32, height=32, max_health=250, range=180)
        self.image = "blue"
        self.projectiles = []
        self.cooldown = 35
        self.cooldown_timer = 0

class Crossbow_tower(Tower):
    def __init__(self, x0, y0):
        super().__init__(x0, y0, width=32, height=32, max_health=200, range=250)
        self.image = "lightblue"
        self.projectiles = []
        self.cooldown = 20
        self.cooldown_timer = 0

class Spiky_tower(Tower):
    def __init__(self, x0, y0):
        super().__init__(x0, y0, width=32, height=32, max_health=150, range=100)
        self.image = "yellow"
        self.attack = 20
        self.cooldown = 25
        self.cooldown_timer = 0
        
# ------------------------------------------------------------------------------

class DragonFireball(Unit):
    def __init__(self, x0, y0):
        super().__init__(x0, y0, width=8, height=8, max_health=1, range=1)
        self.attack = 15
        self.speed = 6
        self.image = "orange red"

class ArcherArrow(Unit):
    def __init__(self, x0, y0):
        super().__init__(x0, y0, width=4, height=4, max_health=1, range=1)
        self.attack = 10
        self.speed = 8
        self.image = "brown"

class WizardSpell(Unit):
    def __init__(self, x0, y0):
        super().__init__(x0, y0, width=8, height=8, max_health=1, range=1)
        self.attack = 30
        self.speed = 5
        self.image = "deep sky blue"

class CrossbowBolt(Unit):
    def __init__(self, x0, y0):
        super().__init__(x0, y0, width=4, height=4, max_health=1, range=1)
        self.attack = 15
        self.speed = 10
        self.image = "dark gray"