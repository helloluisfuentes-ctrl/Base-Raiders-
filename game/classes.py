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
    def __init__(self, pos_x, pos_y, health):  
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.health = health
        
        
# ---------------------------------------------------------------------------

class Estructure (Unit):
    def __init__(self, pos_x, pos_y, health):
        super().__init__(pos_x, pos_y, health)
        
# ---------------------------------------------------------------------------

class Troop (Unit):
    def __init__(self, pos_x, pos_y, health):
        super().__init__(pos_x, pos_y, health)
        self.movement_speed
        self.attack
        self.attack_speed
        self.attack_range
        
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
    def __init__(self):
        super().__init__()

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
        


        

    
        

    