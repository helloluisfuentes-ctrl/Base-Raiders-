"""
Módulo de gestión de jugadores.

Este módulo maneja:
- Registro de nuevos jugadores
- Inicio de sesión
- Guardado y carga desde JSON
- Actualización de victorias
"""

import json
import os
from pathlib import Path


class Player:
    """Clase que representa un jugador del juego."""
    
    def __init__(self, username, password):
        """
        Inicializa un nuevo jugador.
        
        Args:
            username (str): Nombre de usuario único
            password (str): Contraseña del jugador
        """
        self.username = username
        self.password = password
        self.attack_wins = 0
        self.defense_wins = 0
    
    def to_dict(self):
        """Convierte el jugador a diccionario para JSON."""
        return {
            'username': self.username,
            'password': self.password,
            'attack_wins': self.attack_wins,
            'defense_wins': self.defense_wins
        }
    
    @staticmethod
    def from_dict(data):
        """Crea un jugador desde diccionario JSON."""
        player = Player(data['username'], data['password'])
        player.attack_wins = data.get('attack_wins', 0)
        player.defense_wins = data.get('defense_wins', 0)
        return player
    
    def add_attack_win(self):
        """Incrementa las victorias como atacante."""
        self.attack_wins += 1
    
    def add_defense_win(self):
        """Incrementa las victorias como defensor."""
        self.defense_wins += 1
    
    def total_wins(self):
        """Retorna el total de victorias."""
        return self.attack_wins + self.defense_wins


class PlayerManager:
    """Gestiona el almacenamiento y carga de jugadores desde JSON."""
    
    def __init__(self, data_folder="game_data"):
        """
        Inicializa el gestor de jugadores.
        
        Args:
            data_folder (str): Carpeta donde se guardan los datos
        """
        self.data_folder = Path(data_folder)
        self.players_file = self.data_folder / "players.json"
        self.players = {}
        
        # Crear carpeta si no existe
        self.data_folder.mkdir(exist_ok=True)
        
        # Cargar jugadores existentes
        self.load_players()
    
    def load_players(self):
        """Carga todos los jugadores desde el archivo JSON."""
        try:
            if self.players_file.exists():
                with open(self.players_file, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    self.players = {
                        username: Player.from_dict(player_data)
                        for username, player_data in data.items()
                    }
            else:
                self.players = {}
        except (json.JSONDecodeError, IOError) as e:
            print(f"Error al cargar jugadores: {e}")
            self.players = {}
    
    def save_players(self):
        """Guarda todos los jugadores en el archivo JSON."""
        try:
            with open(self.players_file, 'w', encoding='utf-8') as f:
                data = {
                    username: player.to_dict()
                    for username, player in self.players.items()
                }
                json.dump(data, f, ensure_ascii=False, indent=4)
        except IOError as e:
            print(f"Error al guardar jugadores: {e}")
    
    def register_player(self, username, password):
        """
        Registra un nuevo jugador.
        
        Args:
            username (str): Nombre de usuario
            password (str): Contraseña
            
        Returns:
            tuple: (bool éxito, str mensaje)
        """
        if not username or not password:
            return False, "El usuario y contraseña no pueden estar vacíos"
        
        if username in self.players:
            return False, f"El usuario '{username}' ya existe"
        
        # Validar longitud
        if len(username) < 3:
            return False, "El usuario debe tener al menos 3 caracteres"
        
        if len(password) < 4:
            return False, "La contraseña debe tener al menos 4 caracteres"
        
        # Crear nuevo jugador
        new_player = Player(username, password)
        self.players[username] = new_player
        self.save_players()
        
        return True, f"Jugador '{username}' registrado exitosamente"
    
    def login_player(self, username, password):
        """
        Intenta iniciar sesión con un jugador.
        
        Args:
            username (str): Nombre de usuario
            password (str): Contraseña
            
        Returns:
            tuple: (Player o None, str mensaje)
        """
        if username not in self.players:
            return None, f"El usuario '{username}' no existe"
        
        player = self.players[username]
        if player.password != password:
            return None, "Contraseña incorrecta"
        
        return player, f"Bienvenido {username}"
    
    def get_player(self, username):
        """
        Obtiene un jugador por nombre de usuario.
        
        Args:
            username (str): Nombre de usuario
            
        Returns:
            Player o None
        """
        return self.players.get(username)
    
    def get_all_players(self):
        """Retorna lista de todos los jugadores."""
        return list(self.players.values())
    
    def player_exists(self, username):
        """Verifica si un jugador existe."""
        return username in self.players
    
    def update_player_wins(self, username, role):
        """
        Actualiza las victorias de un jugador.
        
        Args:
            username (str): Nombre de usuario
            role (str): 'attack' o 'defense'
        """
        if username in self.players:
            if role == 'attack':
                self.players[username].add_attack_win()
            elif role == 'defense':
                self.players[username].add_defense_win()
            self.save_players()
