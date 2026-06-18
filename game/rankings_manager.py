"""
Sistema de rankings y estadísticas.

Maneja:
- Rankings de defensores
- Rankings de atacantes
- Ordenamiento automático
- Obtención de datos desde JSON
"""


class RankingManager:
    """Gestiona los rankings de jugadores."""
    
    def __init__(self, player_manager):
        """
        Inicializa el gestor de rankings.
        
        Args:
            player_manager: Instancia de PlayerManager
        """
        self.player_manager = player_manager
    
    def get_defense_ranking(self, top_n=5):
        """
        Obtiene el ranking de defensores (ordenado por victorias defensivas).
        
        Args:
            top_n (int): Número de mejores defensores a retornar
            
        Returns:
            list: Lista de tuplas (username, defense_wins, total_wins)
        """
        players = self.player_manager.get_all_players()
        
        # Ordenar por victorias defensivas en orden descendente
        sorted_players = sorted(
            players,
            key=lambda p: p.defense_wins,
            reverse=True
        )
        
        # Construir ranking
        ranking = [
            (player.username, player.defense_wins, player.total_wins())
            for player in sorted_players[:top_n]
        ]
        
        return ranking
    
    def get_attack_ranking(self, top_n=5):
        """
        Obtiene el ranking de atacantes (ordenado por victorias de ataque).
        
        Args:
            top_n (int): Número de mejores atacantes a retornar
            
        Returns:
            list: Lista de tuplas (username, attack_wins, total_wins)
        """
        players = self.player_manager.get_all_players()
        
        # Ordenar por victorias de ataque en orden descendente
        sorted_players = sorted(
            players,
            key=lambda p: p.attack_wins,
            reverse=True
        )
        
        # Construir ranking
        ranking = [
            (player.username, player.attack_wins, player.total_wins())
            for player in sorted_players[:top_n]
        ]
        
        return ranking
    
    def get_overall_ranking(self, top_n=5):
        """
        Obtiene el ranking general (ordenado por total de victorias).
        
        Args:
            top_n (int): Número de mejores jugadores a retornar
            
        Returns:
            list: Lista de tuplas (username, total_wins, attack_wins, defense_wins)
        """
        players = self.player_manager.get_all_players()
        
        # Ordenar por total de victorias en orden descendente
        sorted_players = sorted(
            players,
            key=lambda p: p.total_wins(),
            reverse=True
        )
        
        # Construir ranking
        ranking = [
            (player.username, player.total_wins(), player.attack_wins, player.defense_wins)
            for player in sorted_players[:top_n]
        ]
        
        return ranking
    
    def get_player_stats(self, username):
        """
        Obtiene estadísticas específicas de un jugador.
        
        Args:
            username (str): Nombre del jugador
            
        Returns:
            dict o None: Diccionario con estadísticas del jugador
        """
        player = self.player_manager.get_player(username)
        
        if not player:
            return None
        
        return {
            'username': player.username,
            'attack_wins': player.attack_wins,
            'defense_wins': player.defense_wins,
            'total_wins': player.total_wins()
        }
    
    def get_defense_rank_for_player(self, username):
        """
        Obtiene la posición en el ranking defensivo de un jugador.
        
        Args:
            username (str): Nombre del jugador
            
        Returns:
            int o None: Posición en el ranking (1-based) o None si no existe
        """
        ranking = self.get_defense_ranking(top_n=1000)  # Obtener ranking completo
        
        for position, (name, _, _) in enumerate(ranking, 1):
            if name == username:
                return position
        
        return None
    
    def get_attack_rank_for_player(self, username):
        """
        Obtiene la posición en el ranking ofensivo de un jugador.
        
        Args:
            username (str): Nombre del jugador
            
        Returns:
            int o None: Posición en el ranking (1-based) o None si no existe
        """
        ranking = self.get_attack_ranking(top_n=1000)  # Obtener ranking completo
        
        for position, (name, _, _) in enumerate(ranking, 1):
            if name == username:
                return position
        
        return None
    
    def format_defense_ranking_display(self, top_n=5):
        """
        Formatea el ranking defensivo para mostrar en la interfaz.
        
        Args:
            top_n (int): Número de mejores defensores
            
        Returns:
            str: Texto formateado del ranking
        """
        ranking = self.get_defense_ranking(top_n)
        
        if not ranking:
            return "No hay datos disponibles"
        
        lines = ["=== TOP DEFENSORES ===\n"]
        for position, (username, defense_wins, total_wins) in enumerate(ranking, 1):
            lines.append(f"{position}. {username}: {defense_wins} victorias (Total: {total_wins})")
        
        return "\n".join(lines)
    
    def format_attack_ranking_display(self, top_n=5):
        """
        Formatea el ranking ofensivo para mostrar en la interfaz.
        
        Args:
            top_n (int): Número de mejores atacantes
            
        Returns:
            str: Texto formateado del ranking
        """
        ranking = self.get_attack_ranking(top_n)
        
        if not ranking:
            return "No hay datos disponibles"
        
        lines = ["=== TOP ATACANTES ===\n"]
        for position, (username, attack_wins, total_wins) in enumerate(ranking, 1):
            lines.append(f"{position}. {username}: {attack_wins} victorias (Total: {total_wins})")
        
        return "\n".join(lines)
