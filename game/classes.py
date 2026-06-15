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
    def __init__(self, x0, y0, width, height, health):
        self.width = width
        self.height = height  
        self.x0 = x0
        self.y0 = y0
        self.x1 = x0 + width
        self.y1 = y0 + height
        self.health = health
        
# ---------------------------------------------------------------------------

class Structure(Unit):
    def __init__(self, x0, y0, width, height, health):
        super().__init__(x0, y0, width, height, health)
        
# ---------------------------------------------------------------------------

class Troop(Unit):
    def __init__(self, x0, y0, width, height, health):
        super().__init__(x0, y0, width, height, health)
        '''
        self.movement_speed
        self.attack
        self.attack_speed
        self.attack_range
        '''
        
# ---------------------------------------------------------------------------

class Tower(Unit):
    def __init__(self, x0, y0, width, height, health):
        super().__init__(x0, y0, width, height, health)

# ---------------------------------------------------------------------------------------

class Base(Structure):
    def __init__(self, x0, y0, width=96, height=96, health=500):
        super().__init__(x0, y0, width, height, health)
        
        
class Wall(Structure):
    def __init__(self, x0, y0, width=32, height=32, health=200):
        super().__init__(x0, y0, width, height, health)
        
# ----------------------------------------------------------------------------
# ----------------------------------------------------------------------------

class Pekka(Troop):
    def __init__(self, x0, y0, width=32, height=64, health=100):
        super().__init__(x0, y0, width, height, health)
        self.image = "black"

class Dragon(Troop):
    def __init__(self, x0, y0, width=48, height=48, health=80):
        super().__init__(x0, y0, width, height, health)
        self.image = "purple"
        
class Knight(Troop):
    def __init__(self, x0, y0, width=32, height=32, health=100):
        super().__init__(x0, y0, width, height, health)
        self.image = "gray"
        
class Archer(Troop):
    def __init__(self, x0, y0, width=24, height=32, health=60):
        super().__init__(x0, y0, width, height, health)
        self.image = "pink"
        
class Giant(Troop):
    def __init__(self, x0, y0, width=48, height=64, health=300):
        super().__init__(x0, y0, width, height, health)
        self.image = "orange"
        
class Goblin(Troop):
    def __init__(self, x0, y0, width=20, height=24, health=40):
        super().__init__(x0, y0, width, height, health)
        self.image = "green"
        
# ----------------------------------------------------------------------------

class Wizard_tower(Tower):
    def __init__(self, x0, y0, width=48, height=48, health=250):
        super().__init__(x0, y0, width, height, health)
    
class Crossbow_tower(Tower):
    def __init__(self, x0, y0, width=32, height=48, health=200):
        super().__init__(x0, y0, width, height, health)
    
class Spiky_tower(Tower):
    def __init__(self, x0, y0, width=32, height=48, health=150):
        super().__init__(x0, y0, width, height, health)