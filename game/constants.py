# ====================================================================================
# Constantes globales
# ====================================================================================

CELL_SIZE = 32

# ====================================================================================
# Variables globales - JUEGO
# ====================================================================================

running = None

list_raiders = []
list_walls = []
list_towers = []
list_projectiles_raiders = []
list_projectiles_towers = []
central_base = None

selected_element = None

# ====================================================================================
# Variables globales - JUGADORES
# ====================================================================================

current_attacker = None
current_defender = None
attacker_round_wins = 0
defender_round_wins = 0
round_number = 1
MATCH_WIN_ROUNDS = 3

# ====================================================================================
# Variables globales - FACCIONES
# ====================================================================================

FACTIONS = {
    "Medieval": {
        "base": "white",
        "wall": "saddle brown",
        "tower": "royal blue",
        "unit_outline": "gold"
    },
    "Futurista": {
        "base": "cyan",
        "wall": "gray35",
        "tower": "deep sky blue",
        "unit_outline": "cyan"
    },
    "Naturaleza": {
        "base": "pale green",
        "wall": "forest green",
        "tower": "dark olive green",
        "unit_outline": "lime green"
    }
}
attacker_faction = "Medieval"
defender_faction = "Futurista"

# ====================================================================================
# Variables globales - DINERO
# ====================================================================================

INITIAL_MONEY = 1000
ROUND_INCOME = 100
ATTACKER_DAMAGE_REWARD_RATE = 0.1
DEFENDER_KILL_REWARD = 50
TOWER_DESTROY_REWARD = 100

attacker_money = INITIAL_MONEY
defender_money = INITIAL_MONEY
round_damage_dealt = 0
round_enemies_killed = 0
previous_round_damage_dealt = 0
previous_round_enemies_killed = 0
