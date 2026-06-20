import json
import os
from pathlib import Path

# Ruta del archivo de jugadores
PLAYERS_FILE = "players.json"

# ==========================================================================================
# CARGAR Y GUARDAR JUGADORES
# ==========================================================================================

def load_players():
    """Carga todos los jugadores desde players.json. Retorna dict vacío si no existe."""
    try:
        if os.path.exists(PLAYERS_FILE):
            with open(PLAYERS_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
    except Exception as e:
        print(f"Error al cargar jugadores: {e}")
    return {}


def save_players(players_dict):
    """Guarda el diccionario de jugadores en players.json."""
    try:
        with open(PLAYERS_FILE, "w", encoding="utf-8") as f:
            json.dump(players_dict, f, indent=4, ensure_ascii=False)
    except Exception as e:
        print(f"Error al guardar jugadores: {e}")


# ==========================================================================================
# REGISTRO E INICIO DE SESIÓN
# ==========================================================================================

def register_player(nickname, password):
    """
    Registra un nuevo jugador. Retorna True si se registró correctamente.
    Retorna False si el jugador ya existe.
    """
    players = load_players()
    
    if nickname in players:
        return False  # Jugador ya existe
    
    players[nickname] = {
        "password": password,
        "attack_wins": 0,
        "defense_wins": 0
    }
    save_players(players)
    return True


def login_player(nickname, password):
    """
    Valida credenciales del jugador. Retorna True si son correctas.
    """
    players = load_players()
    
    if nickname not in players:
        return False  # Jugador no existe
    
    if players[nickname]["password"] != password:
        return False  # Contraseña incorrecta
    
    return True


# ==========================================================================================
# OBTENER INFORMACIÓN DE JUGADORES
# ==========================================================================================

def get_all_players():
    """Retorna lista de todos los nombres de jugadores."""
    players = load_players()
    return list(players.keys())


def player_exists(nickname):
    """Verifica si un jugador existe."""
    players = load_players()
    return nickname in players


# ==========================================================================================
# ACTUALIZAR VICTORIAS
# ==========================================================================================

def update_player_wins(nickname, role):
    """
    Actualiza las victorias de un jugador.
    role puede ser "attack" o "defense".
    """
    players = load_players()
    
    if nickname not in players:
        return False
    
    if role == "attack":
        players[nickname]["attack_wins"] += 1
    elif role == "defense":
        players[nickname]["defense_wins"] += 1
    else:
        return False
    
    save_players(players)
    return True


def get_player_stats(nickname):
    """Retorna diccionario con estadísticas del jugador."""
    players = load_players()
    
    if nickname not in players:
        return None
    
    return {
        "nickname": nickname,
        "attack_wins": players[nickname]["attack_wins"],
        "defense_wins": players[nickname]["defense_wins"]
    }


# ==========================================================================================
# RANKINGS
# ==========================================================================================

def get_top_attackers(limit=5):
    """Retorna lista de Top N atacantes ordenados por victorias."""
    players = load_players()
    
    sorted_players = sorted(
        players.items(),
        key=lambda x: x[1]["attack_wins"],
        reverse=True
    )
    
    result = []
    for nickname, data in sorted_players[:limit]:
        result.append({
            "nickname": nickname,
            "wins": data["attack_wins"]
        })
    
    return result


def get_top_defenders(limit=5):
    """Retorna lista de Top N defensores ordenados por victorias."""
    players = load_players()
    
    sorted_players = sorted(
        players.items(),
        key=lambda x: x[1]["defense_wins"],
        reverse=True
    )
    
    result = []
    for nickname, data in sorted_players[:limit]:
        result.append({
            "nickname": nickname,
            "wins": data["defense_wins"]
        })
    
    return result
