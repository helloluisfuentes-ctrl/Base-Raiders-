import constants


class MoneyManager:
    """Gestiona el dinero de atacantes y defensores durante el juego."""
    
    # Costos de compra
    KNIGHT_COST = 100
    GOBLIN_COST = 50
    ARCHER_COST = 120
    GIANT_COST = 200
    DRAGON_COST = 180
    PEKKA_COST = 150
    
    WALL_COST = 75
    WIZARD_TOWER_COST = 200
    CROSSBOW_TOWER_COST = 180
    SPIKY_TOWER_COST = 150
    
    def __init__(self):
        """Inicializa el gestor de dinero."""
        pass
    
    # ===== OBTENER DINERO =====
    
    def get_attacker_money(self):
        """Retorna el dinero actual del atacante."""
        return constants.attacker_money
    
    def get_defender_money(self):
        """Retorna el dinero actual del defensor."""
        return constants.defender_money
    
    # ===== GASTAR DINERO =====
    
    def spend_attacker_money(self, amount):
        """Gasta dinero del atacante."""
        if constants.attacker_money >= amount:
            constants.attacker_money -= amount
            return True
        return False
    
    def spend_defender_money(self, amount):
        """Gasta dinero del defensor."""
        if constants.defender_money >= amount:
            constants.defender_money -= amount
            return True
        return False
    
    # ===== AGREGAR DINERO =====
    
    def add_attacker_money(self, amount):
        """Agrega dinero al atacante."""
        constants.attacker_money += amount
    
    def add_defender_money(self, amount):
        """Agrega dinero al defensor."""
        constants.defender_money += amount
    
    # ===== RONDA =====
    
    def give_round_income(self):
        """Da ingreso al inicio de la ronda a ambos jugadores."""
        self.add_attacker_money(constants.ROUND_INCOME)
        self.add_defender_money(constants.ROUND_INCOME)

    def give_previous_round_bonuses(self):
        """Aplica los bonos ganados en la ronda anterior."""
        attacker_bonus = int(constants.previous_round_damage_dealt * constants.ATTACKER_DAMAGE_REWARD_RATE)
        defender_bonus = constants.previous_round_enemies_killed * constants.DEFENDER_KILL_REWARD
        self.add_attacker_money(attacker_bonus)
        self.add_defender_money(defender_bonus)
        constants.previous_round_damage_dealt = 0
        constants.previous_round_enemies_killed = 0
        return attacker_bonus, defender_bonus

    def save_previous_round_stats(self):
        """Guarda el resultado de la ronda actual para calcular bonos futuros."""
        constants.previous_round_damage_dealt = constants.round_damage_dealt
        constants.previous_round_enemies_killed = constants.round_enemies_killed
    
    def give_attacker_damage_bonus(self, damage_amount):
        """Da bonificación al atacante por daño realizado."""
        constants.round_damage_dealt += damage_amount
        bonus = int(damage_amount * constants.ATTACKER_DAMAGE_REWARD_RATE)
        self.add_attacker_money(bonus)
        return bonus
    
    def give_defender_kill_bonus(self, kill_count):
        """Da bonificación al defensor por unidades enemigas eliminadas."""
        constants.round_enemies_killed += kill_count
        bonus = kill_count * constants.DEFENDER_KILL_REWARD
        self.add_defender_money(bonus)
        return bonus

    def give_defender_unit_bonus(self, troop):
        """Da dinero al defensor segun el tipo de unidad eliminada."""
        constants.round_enemies_killed += 1
        bonus = getattr(troop, "reward", constants.DEFENDER_KILL_REWARD)
        self.add_defender_money(bonus)
        return bonus

    def give_tower_destroy_bonus(self):
        """Da dinero extra al atacante por destruir una torre."""
        self.add_attacker_money(constants.TOWER_DESTROY_REWARD)
        return constants.TOWER_DESTROY_REWARD
    
    # ===== VALIDAR COMPRA =====
    
    def can_attacker_buy(self, amount):
        """Verifica si el atacante puede comprar."""
        return constants.attacker_money >= amount
    
    def can_defender_buy(self, amount):
        """Verifica si el defensor puede comprar."""
        return constants.defender_money >= amount
    
    # ===== COSTOS DE COMPRA =====
    
    def get_knight_cost(self):
        return self.KNIGHT_COST
    
    def get_goblin_cost(self):
        return self.GOBLIN_COST
    
    def get_archer_cost(self):
        return self.ARCHER_COST
    
    def get_giant_cost(self):
        return self.GIANT_COST
    
    def get_dragon_cost(self):
        return self.DRAGON_COST
    
    def get_pekka_cost(self):
        return self.PEKKA_COST
    
    def get_wall_cost(self):
        return self.WALL_COST
    
    def get_wizard_tower_cost(self):
        return self.WIZARD_TOWER_COST
    
    def get_crossbow_tower_cost(self):
        return self.CROSSBOW_TOWER_COST
    
    def get_spiky_tower_cost(self):
        return self.SPIKY_TOWER_COST
    
    # ===== RESETEAR RONDA =====
    
    def reset_round_money(self):
        """Resetea el dinero al valor inicial para una nueva ronda."""
        constants.attacker_money = constants.INITIAL_MONEY
        constants.defender_money = constants.INITIAL_MONEY
        constants.round_damage_dealt = 0
        constants.round_enemies_killed = 0


# Instancia global
money_manager = MoneyManager()
