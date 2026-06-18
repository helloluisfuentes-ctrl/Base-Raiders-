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

# ====================================================================================
# Variables globales - DINERO
# ====================================================================================

INITIAL_MONEY = 1000
ROUND_INCOME = 100

attacker_money = INITIAL_MONEY
defender_money = INITIAL_MONEY