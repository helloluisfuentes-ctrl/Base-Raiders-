"""
Clases:

player

Unit
    Estructure      # estructuras: Torres, muros, base central
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
        self.widht = width
        self.height = height  
        self.x0 = x0
        self.y0 = y0
        self.x1 = x0 + width
        self.y1 = y0 + height
        #self.hitbox = (self.x0, self.y0),(self.x1, self.y1)
        
        self.health = health
        
        
# ---------------------------------------------------------------------------

class Estructure (Unit):
    def __init__(self, pos_x, pos_y, health):
        super().__init__(pos_x, pos_y, health)
        
# ---------------------------------------------------------------------------

class Troop (Unit):
    def __init__(self, x0, y0, width, height, health):
        super().__init__(x0, y0, width, height, health)
        '''
        self.movement_speed
        self.attack
        self.attack_speed
        self.attack_range
        '''
        
# ---------------------------------------------------------------------------

class Tower (Unit):
    def __init__(self, pos_x, pos_y, health):
        super().__init__(pos_x, pos_y, health)\
            
# ---------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------

class Base (Estructure):
    def __init__(self):
        super().__init__()
        
class Wall (Estructure):
    def __init__(self):
        super().__init__()
        
# ----------------------------------------------------------------------------
# ----------------------------------------------------------------------------

class Pekka (Troop):
    def __init__(self,  x0, y0, width, height, health):
        super().__init__( x0, y0, width, height, health)

class Dragon (Troop):
    def __init__(self):
        super().__init__()
        
class Knight (Troop):
    def __init__(self):
        super().__init__()
        
class Archer (Troop):
    def __init__(self):
        super().__init__()
        
class Giant (Troop):
    def __init__(self):
        super().__init__()
        
class Goblin (Troop):
    def __init__(self):
        super().__init__()
        


        

    
        

    