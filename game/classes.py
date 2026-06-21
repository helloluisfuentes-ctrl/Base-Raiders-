from images import *

# ==========================================================================================
# JUGADOR
# ==========================================================================================

class Player:
    """Representa a un jugador registrado con sus victorias acumuladas."""

    def __init__(self, nickname, password):
        self.nickname = nickname
        self.password = password
        self.attack_wins = 0
        self.defense_wins = 0

# ==========================================================================================
# CLASE BASE
# ==========================================================================================

class Unit:
    """
    Clase base para todo elemento del juego con posición, tamaño y vida.
    Todas las tropas, torres y estructuras heredan de aquí.
    """

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
        self.reward = 50

# ---------------------------------------------------------------------------

class Structure(Unit):
    """Elemento estático colocado en la fase de defensa (base, muros)."""

    def __init__(self, x0, y0, width, height, max_health, range=0):
        super().__init__(x0, y0, width, height, max_health, range)

# ---------------------------------------------------------------------------

class Troop(Unit):
    """Unidad controlada por el atacante que se mueve hacia los objetivos."""

    def __init__(self, x0, y0, width, height, max_health, range=0):
        super().__init__(x0, y0, width, height, max_health, range)

# ---------------------------------------------------------------------------

class Tower(Unit):
    """Estructura defensiva que ataca a las tropas en su rango."""

    def __init__(self, x0, y0, width, height, max_health, range=0):
        super().__init__(x0, y0, width, height, max_health, range)

# ==========================================================================================
# ESTRUCTURAS
# ==========================================================================================

class Base(Structure):
    """Base central que el atacante debe destruir para ganar."""

    def __init__(self, x0, y0):
        super().__init__(x0, y0, width=64, height=64, max_health=500, range=0)
        self.name = "Base Central"


# ==========================================================================================
# DEFENSAS (ESTRUCTURAS Y TORRES)
# ==========================================================================================

class Wall(Structure):
    """Bloquea el paso de las tropas, obligándolas a rodear o atacarlo."""

    def __init__(self, x0, y0):
        # BUFFED: Health increased from 200 to 450. At 75 gold, this allows a defender 
        # to buy ~13 walls to create viable chokepoints that can withhold heavy attacks.
        super().__init__(x0, y0, width=32, height=32, max_health=450, range=0)
        self.cost = 75


class Wizard_tower(Tower):
    """Torre de daño en área con buen rango y cooldown moderado."""

    def __init__(self, x0, y0):
        # BALANCED: Great anti-swarm tool. Health adjusted slightly to handle mid-tier threats.
        super().__init__(x0, y0, width=32, height=32, max_health=300, range=180)
        self.name = "wizard_tower"
        self.cooldown = 40  # Slightly slower attack speed to compensate for massive AoE spell damage
        self.cooldown_timer = 0
        self.cost = 200


class Crossbow_tower(Tower):
    """Torre de disparo rápido y largo alcance, daño bajo por impacto."""

    def __init__(self, x0, y0):
        # BALANCED: High single-target DPS (4 damage every 5 frames = 0.8 damage/frame) 
        # designed to melt single targets over a huge distance.
        super().__init__(x0, y0, width=32, height=32, max_health=250, range=250)
        self.name = "crossbow_tower"
        self.cooldown = 5
        self.cooldown_timer = 0
        self.cost = 180


class Spiky_tower(Tower):
    """Torre melee de corto alcance pero daño muy alto por golpe."""

    def __init__(self, x0, y0):
        # BUFFED: High-risk, high-reward defense. Since range is tiny (16), health is 
        # buffed significantly to survive melee skirmishes with Giants or Pekkas.
        super().__init__(x0, y0, width=32, height=32, max_health=400, range=16)
        self.name = "spiky_tower"
        self.attack = 65  # Increased from 50 to punish high-health units
        self.cooldown = 30
        self.cooldown_timer = 0
        self.cost = 150


# ==========================================================================================
# TROPAS
# ==========================================================================================

class Pekka(Troop):
    """Tropa melee de alto daño y costo medio-alto."""

    def __init__(self, x0, y0):
        # REWORKED: Previously had low health (100). Now behaves like a true heavy skirmisher. 
        # High damage per hit (45) but slower attack speed.
        super().__init__(x0, y0, width=24, height=24, max_health=280, range=8)
        self.image = img_pekka
        self.speed = 2
        self.attack = 45
        self.cooldown = 45
        self.cooldown_timer = 0
        self.cost = 150
        self.reward = 90


class Dragon(Troop):
    """Tropa a distancia con proyectiles, rápida y de alcance largo."""

    def __init__(self, x0, y0):
        # NERFED DPS/BUFFED HP: Flight and range (64) make it slippery. 
        # Health increased slightly, but attack speed slowed down to keep its damage output reasonable.
        super().__init__(x0, y0, width=32, height=16, max_health=160, range=64)
        self.image = img_dragon
        self.speed = 3  # Reduced speed from 4 to 3 so it doesn't leave its frontline tank behind
        self.cooldown = 40  # Increased cooldown from 25 to match fireball damage balance
        self.cooldown_timer = 0
        self.cost = 180
        self.reward = 100


class Knight(Troop):
    """Tropa melee equilibrada, opción estándar de costo medio."""

    def __init__(self, x0, y0):
        # BALANCED: The baseline standard unit. Good effective health pool for 100 gold.
        super().__init__(x0, y0, width=16, height=16, max_health=190, range=8)
        self.image = img_knight
        self.speed = 3
        self.attack = 22
        self.cooldown = 25  # Faster swinging speed makes him efficient at cleaning up small targets
        self.cooldown_timer = 0
        self.cost = 100
        self.reward = 60


class Archer(Troop):
    """Tropa a distancia frágil pero con buen alcance."""

    def __init__(self, x0, y0):
        # BALANCED: High backline value, highly vulnerable to any tower that reaches her.
        super().__init__(x0, y0, width=10, height=12, max_health=70, range=96)
        self.image = img_archer
        self.speed = 3
        self.cooldown = 28  # Moderate attack speed allows them to group up and rain damage
        self.cooldown_timer = 0
        self.cost = 120
        self.reward = 70


class Giant(Troop):
    """Tropa tanque: mucha vida y daño alto, pero lenta."""

    def __init__(self, x0, y0):
        # BUFFED: True ultimate sponge. Massive health pool to soak up Crossbow bolts and Wizard spells.
        super().__init__(x0, y0, width=56, height=58, max_health=550, range=8)
        self.image = img_giant
        self.speed = 1
        self.attack = 55
        self.cooldown = 50
        self.cooldown_timer = 0
        self.cost = 200
        self.reward = 120


class Goblin(Troop):
    """Tropa barata y veloz, ideal para distraer o saturar la defensa."""

    def __init__(self, x0, y0):
        # BALANCED: Excellent value if bought in bulk (20 goblins for 1000 gold). 
        # Melts quickly to Wizard Towers but overwhelms Crossbows.
        super().__init__(x0, y0, width=10, height=10, max_health=45, range=8)
        self.image = img_goblin
        self.speed = 5
        self.attack = 10
        self.cooldown = 15
        self.cooldown_timer = 0
        self.cost = 50
        self.reward = 40


# ==========================================================================================
# PROYECTILES
# ==========================================================================================

class DragonFireball(Unit):
    """Proyectil disparado por el Dragon."""

    def __init__(self, x0, y0):
        super().__init__(x0, y0, width=8, height=8, max_health=1, range=1)
        self.attack = 20  # Adjusted slightly up because cooldown was slowed down
        self.speed = 6
        self.image = img_dragon_fireball


class ArcherArrow(Unit):
    """Proyectil disparado por el Archer."""

    def __init__(self, x0, y0):
        super().__init__(x0, y0, width=4, height=4, max_health=1, range=1)
        self.attack = 12  # Brings archer DPS to a competitive level for 120 gold
        self.speed = 8
        self.image = img_archer_arrow


class WizardSpell(Unit):
    """Proyectil disparado por la Wizard_tower."""

    def __init__(self, x0, y0):
        super().__init__(x0, y0, width=8, height=8, max_health=1, range=1)
        self.attack = 35  # High impact threat to wipe out low-health swarms (Goblins/Archers)
        self.speed = 5
        self.image = img_wizard_spell


class CrossbowBolt(Unit):
    """Proyectil disparado por la Crossbow_tower."""

    def __init__(self, x0, y0):
        super().__init__(x0, y0, width=4, height=4, max_health=1, range=1)
        self.attack = 4  # Relies on high frequency (cooldown 5) to deal massive damage
        self.speed = 10
        self.image = img_crossbow_bolt