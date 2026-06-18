"""
Sistema de dinero del juego.

Maneja:
- Dinero inicial en cada ronda
- Recompensas por daño (atacante)
- Recompensas por enemigos eliminados (defensor)
- Costo de compras
"""


class MoneySystem:
    """Sistema de gestión de dinero para ambos jugadores."""
    
    # Configuración de dinero
    INITIAL_MONEY = 1000  # Dinero inicial de cada ronda
    ROUND_BONUS = 500     # Dinero adicional por ronda
    MONEY_PER_DAMAGE = 1  # Dinero por daño causado (atacante)
    MONEY_PER_KILL = 100  # Dinero por enemigo eliminado (defensor)
    
    # Costos de construcción
    TOWER_COST = 300
    WALL_COST = 100
    UNIT_COST = 150
    UPGRADE_COST = 200
    
    def __init__(self):
        """Inicializa el sistema de dinero."""
        self.attacker_money = 0
        self.defender_money = 0
    
    def initialize_round(self):
        """
        Inicializa el dinero al comenzar una ronda.
        Ambos jugadores reciben dinero inicial fijo.
        """
        self.attacker_money = self.INITIAL_MONEY
        self.defender_money = self.INITIAL_MONEY
    
    def add_round_bonus(self):
        """
        Agrega dinero adicional por ronda a ambos jugadores.
        Se llama durante la ronda.
        """
        self.attacker_money += self.ROUND_BONUS
        self.defender_money += self.ROUND_BONUS
    
    def reward_attacker_damage(self, damage_dealt):
        """
        Recompensa al atacante basado en el daño causado.
        
        Args:
            damage_dealt (int): Cantidad de daño causado
        """
        reward = int(damage_dealt * self.MONEY_PER_DAMAGE)
        self.attacker_money += reward
        return reward
    
    def reward_defender_kills(self, enemies_killed):
        """
        Recompensa al defensor por enemigos eliminados.
        
        Args:
            enemies_killed (int): Cantidad de enemigos eliminados
        """
        reward = enemies_killed * self.MONEY_PER_KILL
        self.defender_money += reward
        return reward
    
    def buy_tower_attacker(self):
        """
        El atacante compra una torre.
        
        Returns:
            bool: True si la compra fue exitosa
        """
        return self._process_purchase(self.TOWER_COST, 'attacker')
    
    def buy_wall_defender(self):
        """
        El defensor compra un muro.
        
        Returns:
            bool: True si la compra fue exitosa
        """
        return self._process_purchase(self.WALL_COST, 'defender')
    
    def buy_unit_attacker(self):
        """
        El atacante compra una unidad.
        
        Returns:
            bool: True si la compra fue exitosa
        """
        return self._process_purchase(self.UNIT_COST, 'attacker')
    
    def buy_unit_defender(self):
        """
        El defensor compra una unidad defensiva.
        
        Returns:
            bool: True si la compra fue exitosa
        """
        return self._process_purchase(self.UNIT_COST, 'defender')
    
    def buy_upgrade(self, player_type):
        """
        Compra una mejora para el jugador especificado.
        
        Args:
            player_type (str): 'attacker' o 'defender'
            
        Returns:
            bool: True si la compra fue exitosa
        """
        return self._process_purchase(self.UPGRADE_COST, player_type)
    
    def _process_purchase(self, cost, player_type):
        """
        Procesa una compra genérica.
        
        Args:
            cost (int): Costo de la compra
            player_type (str): 'attacker' o 'defender'
            
        Returns:
            bool: True si la compra fue exitosa
        """
        if player_type == 'attacker':
            if self.attacker_money >= cost:
                self.attacker_money -= cost
                return True
            return False
        elif player_type == 'defender':
            if self.defender_money >= cost:
                self.defender_money -= cost
                return True
            return False
        return False
    
    def get_attacker_money(self):
        """Retorna el dinero del atacante."""
        return self.attacker_money
    
    def get_defender_money(self):
        """Retorna el dinero del defensor."""
        return self.defender_money
    
    def can_afford_tower_attacker(self):
        """Verifica si el atacante puede comprar una torre."""
        return self.attacker_money >= self.TOWER_COST
    
    def can_afford_wall_defender(self):
        """Verifica si el defensor puede comprar un muro."""
        return self.defender_money >= self.WALL_COST
    
    def can_afford_unit(self, player_type):
        """
        Verifica si un jugador puede comprar una unidad.
        
        Args:
            player_type (str): 'attacker' o 'defender'
        """
        money = self.attacker_money if player_type == 'attacker' else self.defender_money
        return money >= self.UNIT_COST
    
    def reset(self):
        """Resetea el dinero para una nueva ronda."""
        self.initialize_round()
    
    def get_game_state(self):
        """Retorna el estado actual del dinero."""
        return {
            'attacker_money': self.attacker_money,
            'defender_money': self.defender_money
        }
