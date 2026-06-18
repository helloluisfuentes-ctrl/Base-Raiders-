"""
Módulo de utilidades y configuración del juego.
"""

# Rutas de carpetas
DATA_FOLDER = "game_data"
GRAPHICS_FOLDER = "graphics"

# Configuración de la ventana principal
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
WINDOW_TITLE = "Base Raiders - Juego de Estrategia"

# Colores (tema oscuro)
COLORS = {
    'bg_primary': '#2c3e50',      # Fondo principal oscuro
    'bg_secondary': '#34495e',    # Fondo secundario
    'text_light': '#ecf0f1',      # Texto claro
    'text_muted': '#95a5a6',      # Texto atenuado
    'button_success': '#27ae60',  # Verde
    'button_info': '#2980b9',     # Azul
    'button_warning': '#f39c12',  # Naranja
    'button_danger': '#c0392b',   # Rojo
    'button_purple': '#9b59b6',   # Púrpura
    'text_error': '#e74c3c',      # Rojo claro
}

# Configuración del dinero
MONEY_CONFIG = {
    'initial_money': 1000,        # Dinero inicial por ronda
    'round_bonus': 500,           # Bonificación por ronda
    'money_per_damage': 1,        # Dinero por daño (atacante)
    'money_per_kill': 100,        # Dinero por eliminación (defensor)
}

# Costos de elementos
COSTS = {
    'tower': 300,
    'wall': 100,
    'unit': 150,
    'upgrade': 200,
}

# Configuración de rankings
TOP_PLAYERS = 5  # Número de jugadores en los rankings

# Validación de jugadores
MIN_USERNAME_LENGTH = 3
MIN_PASSWORD_LENGTH = 4
MAX_USERNAME_LENGTH = 20
MAX_PASSWORD_LENGTH = 50
