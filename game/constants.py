# ==========================================================================================
# CONSTANTES GLOBALES
# ==========================================================================================

CELL_SIZE = 32

# ==========================================================================================
# VARIABLES GLOBALES - JUEGO
# ==========================================================================================

running = None  # estado actual: "plan", "game", "win", etc.

list_raiders = []
list_walls = []
list_towers = []
list_projectiles_raiders = []
list_projectiles_towers = []
central_base = None

selected_element = None  # elemento actualmente seleccionado para colocar/borrar

# ==========================================================================================
# VARIABLES GLOBALES - JUGADORES
# ==========================================================================================

current_attacker = None
current_defender = None
attacker_round_wins = 0
defender_round_wins = 0
round_number = 1
MATCH_WIN_ROUNDS = 3

# ==========================================================================================
# VARIABLES GLOBALES - DINERO
# ==========================================================================================

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

# ==========================================================================================
# VARIABLES GLOBALES - FACCIONES
# ==========================================================================================

FACTIONS = {
    "Medieval": {

    },
    "Futurista": {

    },
    "Naturaleza": {

    }
}

attacker_faction = "Medieval"
defender_faction = "Futurista"