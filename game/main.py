"""
Base Raiders - Juego de Estrategia en Tkinter

Juego de estrategia para dos jugadores:
- Un atacante que debe conquistar la base
- Un defensor que debe proteger su base

Autor: Equipo Base Raiders
Versión: 1.0
"""

import tkinter as tk
from pathlib import Path

# Importar módulos del proyecto
from players_manager import PlayerManager
from money_system import MoneySystem
from rankings_manager import RankingManager
from ui_windows import VentanaMenu, VentanaSeleccionJugadores, VentanaStats


class GameController:
    """Controlador principal del juego. Orquesta toda la lógica."""
    
    def __init__(self, root):
        """
        Inicializa el controlador del juego.
        
        Args:
            root: Ventana raíz de Tkinter
        """
        self.root = root
        
        # Inicializar gestores
        self.player_manager = PlayerManager(data_folder="game_data")
        self.ranking_manager = RankingManager(self.player_manager)
        self.money_system = MoneySystem()
        
        # Variables de estado del juego
        self.current_attacker = None
        self.current_defender = None
        self.game_in_progress = False
        
        # Crear interfaz
        self.menu = VentanaMenu(
            root,
            on_play_callback=self.show_player_selection,
            on_stats_callback=self.show_stats
        )
    
    def show_player_selection(self):
        """Muestra la ventana de selección de jugadores."""
        player_selection = VentanaSeleccionJugadores(
            self.root,
            self.player_manager,
            on_start_game_callback=self.start_game
        )
    
    def show_stats(self):
        """Muestra la ventana de estadísticas."""
        VentanaStats(self.root, self.ranking_manager)
    
    def start_game(self, attacker, defender):
        """
        Inicia una partida con los jugadores especificados.
        
        Args:
            attacker: Objeto Player del atacante
            defender: Objeto Player del defensor
        """
        self.current_attacker = attacker
        self.current_defender = defender
        self.game_in_progress = True
        
        # Inicializar sistema de dinero
        self.money_system.initialize_round()
        
        print(f"\n{'='*50}")
        print(f"¡Partida iniciada!")
        print(f"{'='*50}")
        print(f"Atacante: {attacker.username}")
        print(f"Defensor: {defender.username}")
        print(f"{'='*50}\n")
        
        # Aquí iría la lógica de juego real
        # Por ahora, es un placeholder para demostración
        self.demo_game_session()
    
    def demo_game_session(self):
        """
        Demostración de una sesión de juego.
        En una implementación real, esto sería reemplazado por el loop de juego.
        """
        # Simular una ronda de juego
        print(f"Dinero inicial del atacante: {self.money_system.get_attacker_money()}")
        print(f"Dinero inicial del defensor: {self.money_system.get_defender_money()}\n")
        
        # Simular daño y recompensas
        print("--- Simulación de Ronda ---")
        
        # El atacante causa daño
        damage = 50
        reward = self.money_system.reward_attacker_damage(damage)
        print(f"Atacante causa {damage} de daño → Gana ${reward}")
        
        # El defensor elimina unidades
        kills = 2
        reward = self.money_system.reward_defender_kills(kills)
        print(f"Defensor elimina {kills} unidades → Gana ${reward}")
        
        print(f"\nDinero del atacante después: {self.money_system.get_attacker_money()}")
        print(f"Dinero del defensor después: {self.money_system.get_defender_money()}\n")
        
        # Simular compras
        if self.money_system.can_afford_unit('attacker'):
            if self.money_system.buy_unit_attacker():
                print("Atacante compró una unidad")
        
        print(f"Dinero del atacante tras compra: {self.money_system.get_attacker_money()}\n")
        
        # Simular fin de partida
        print("--- Fin de Ronda ---")
        self.end_game_session(winner='attacker')
    
    def end_game_session(self, winner):
        """
        Finaliza la sesión de juego y actualiza estadísticas.
        
        Args:
            winner (str): 'attacker' o 'defender'
        """
        if winner == 'attacker':
            self.player_manager.update_player_wins(self.current_attacker.username, 'attack')
            self.player_manager.update_player_wins(self.current_defender.username, 'defense')
            print(f"\n¡{self.current_attacker.username} ganó como Atacante!")
        else:
            self.player_manager.update_player_wins(self.current_defender.username, 'defense')
            self.player_manager.update_player_wins(self.current_attacker.username, 'attack')
            print(f"\n¡{self.current_defender.username} ganó como Defensor!")
        
        self.game_in_progress = False
        self.current_attacker = None
        self.current_defender = None
        
        print("Estadísticas actualizadas. Volviendo al menú...\n")


def main():
    """Función principal que inicia la aplicación."""
    # Crear ventana raíz
    root = tk.Tk()
    
    # Crear controlador del juego
    app = GameController(root)
    
    # Iniciar bucle de eventos
    root.mainloop()


if __name__ == "__main__":
    main()