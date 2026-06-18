"""
Ejemplos de uso del sistema Base Raiders.

Este archivo demuestra cómo utilizar los módulos principales del juego.
"""

from players_manager import PlayerManager
from money_system import MoneySystem
from rankings_manager import RankingManager


def ejemplo_1_gestion_jugadores():
    """Ejemplo 1: Crear, registrar y autenticar jugadores."""
    print("\n" + "="*60)
    print("EJEMPLO 1: Gestión de Jugadores")
    print("="*60)
    
    # Crear gestor de jugadores
    manager = PlayerManager(data_folder="game_data")
    
    # Registrar nuevos jugadores
    print("\n1. Registrando nuevos jugadores...")
    success, msg = manager.register_player("Hero1", "pass1234")
    print(f"   {msg}")
    
    success, msg = manager.register_player("Defender1", "pass5678")
    print(f"   {msg}")
    
    # Intentar registrar jugador duplicado (debe fallar)
    print("\n2. Intentando registrar jugador duplicado...")
    success, msg = manager.register_player("Hero1", "otra_pass")
    print(f"   {msg}")
    
    # Autenticar jugadores
    print("\n3. Autenticando jugadores...")
    player, msg = manager.login_player("Hero1", "pass1234")
    if player:
        print(f"   ✓ {msg}")
    
    # Intento de login con contraseña incorrecta
    print("\n4. Intento con contraseña incorrecta...")
    player, msg = manager.login_player("Hero1", "wrong_pass")
    if not player:
        print(f"   ✗ {msg}")
    
    # Ver estadísticas
    print("\n5. Estadísticas de jugadores...")
    for username, player in manager.players.items():
        print(f"   {username}: {player.attack_wins} victorias ofensivas, "
              f"{player.defense_wins} defensivas (Total: {player.total_wins()})")


def ejemplo_2_sistema_dinero():
    """Ejemplo 2: Sistema de dinero y compras."""
    print("\n" + "="*60)
    print("EJEMPLO 2: Sistema de Dinero")
    print("="*60)
    
    # Crear sistema de dinero
    money = MoneySystem()
    
    # Inicializar dinero de ronda
    print("\n1. Inicializando dinero de ronda...")
    money.initialize_round()
    print(f"   Atacante: ${money.get_attacker_money()}")
    print(f"   Defensor: ${money.get_defender_money()}")
    
    # Recompensar por daño
    print("\n2. Atacante causa 75 de daño...")
    reward = money.reward_attacker_damage(75)
    print(f"   Ganancia: ${reward}")
    print(f"   Dinero atacante: ${money.get_attacker_money()}")
    
    # Recompensar por eliminaciones
    print("\n3. Defensor elimina 3 unidades...")
    reward = money.reward_defender_kills(3)
    print(f"   Ganancia: ${reward}")
    print(f"   Dinero defensor: ${money.get_defender_money()}")
    
    # Comprar elementos
    print("\n4. Comprando elementos...")
    if money.can_afford_unit('attacker'):
        if money.buy_unit_attacker():
            print(f"   ✓ Atacante compró unidad")
            print(f"   Dinero atacante: ${money.get_attacker_money()}")
    
    # Intento de compra sin dinero suficiente
    print("\n5. Intentando comprar 5 torres (sin dinero)...")
    for i in range(5):
        if not money.can_afford_tower_attacker():
            print(f"   ✗ Dinero insuficiente en intento {i+1}")
            break


def ejemplo_3_rankings():
    """Ejemplo 3: Sistema de rankings."""
    print("\n" + "="*60)
    print("EJEMPLO 3: Sistema de Rankings")
    print("="*60)
    
    # Crear gestor de jugadores y rankings
    player_manager = PlayerManager(data_folder="game_data")
    ranking = RankingManager(player_manager)
    
    # Registrar jugadores con diferentes estadísticas
    print("\n1. Registrando jugadores de prueba...")
    test_players = [
        ("Champion", "pass123"),
        ("Defender", "pass123"),
        ("Attacker", "pass123"),
        ("Legend", "pass123"),
    ]
    
    for username, password in test_players:
        player_manager.register_player(username, password)
        player = player_manager.get_player(username)
        
        # Asignar victorias aleatorias para demostración
        if username == "Champion":
            player.defense_wins = 15
            player.attack_wins = 10
        elif username == "Defender":
            player.defense_wins = 20
            player.attack_wins = 5
        elif username == "Attacker":
            player.defense_wins = 3
            player.attack_wins = 18
        elif username == "Legend":
            player.defense_wins = 12
            player.attack_wins = 14
    
    player_manager.save_players()
    
    # Mostrar rankings
    print("\n2. Ranking de Defensores (Top 5):")
    defense_ranking = ranking.get_defense_ranking(5)
    for pos, (username, wins, total) in enumerate(defense_ranking, 1):
        print(f"   {pos}. {username}: {wins} victorias defensivas (Total: {total})")
    
    print("\n3. Ranking de Atacantes (Top 5):")
    attack_ranking = ranking.get_attack_ranking(5)
    for pos, (username, wins, total) in enumerate(attack_ranking, 1):
        print(f"   {pos}. {username}: {wins} victorias ofensivas (Total: {total})")
    
    print("\n4. Ranking General (Top 5):")
    general_ranking = ranking.get_overall_ranking(5)
    for pos, (username, total, ataque, defensa) in enumerate(general_ranking, 1):
        print(f"   {pos}. {username}: {total} total ({ataque} ataque, {defensa} defensa)")


def ejemplo_4_flujo_completo():
    """Ejemplo 4: Flujo completo de una partida."""
    print("\n" + "="*60)
    print("EJEMPLO 4: Flujo Completo de una Partida")
    print("="*60)
    
    # Crear gestores
    player_manager = PlayerManager(data_folder="game_data")
    ranking = RankingManager(player_manager)
    money = MoneySystem()
    
    # Registrar jugadores si no existen
    print("\n1. Preparando jugadores...")
    if not player_manager.player_exists("Player1"):
        player_manager.register_player("Player1", "pass1")
    if not player_manager.player_exists("Player2"):
        player_manager.register_player("Player2", "pass2")
    
    attacker, _ = player_manager.login_player("Player1", "pass1")
    defender, _ = player_manager.login_player("Player2", "pass2")
    print(f"   Atacante: {attacker.username}")
    print(f"   Defensor: {defender.username}")
    
    # Iniciar partida
    print("\n2. Iniciando partida...")
    money.initialize_round()
    print(f"   Dinero inicial - Atacante: ${money.get_attacker_money()}, Defensor: ${money.get_defender_money()}")
    
    # Simular acciones durante la partida
    print("\n3. Simulando acciones de la partida...")
    
    # Ronda 1
    print("   RONDA 1:")
    damage = 100
    money.reward_attacker_damage(damage)
    print(f"      Atacante causa {damage} daño")
    
    money.buy_wall_defender()
    print(f"      Defensor compra muro: ${money.get_defender_money()}")
    
    money.buy_unit_attacker()
    print(f"      Atacante compra unidad: ${money.get_attacker_money()}")
    
    # Determinar ganador
    print("\n4. Determinando ganador...")
    winner = attacker if attacker.attack_wins > defender.attack_wins else defender
    print(f"   ¡{winner.username} gana esta partida!")
    
    # Actualizar estadísticas
    print("\n5. Actualizando estadísticas...")
    player_manager.update_player_wins(attacker.username, 'attack')
    player_manager.update_player_wins(defender.username, 'defense')
    
    print(f"   {attacker.username}: {attacker.attack_wins} victorias ofensivas")
    print(f"   {defender.username}: {defender.defense_wins} victorias defensivas")


if __name__ == "__main__":
    # Ejecutar ejemplos
    ejemplo_1_gestion_jugadores()
    ejemplo_2_sistema_dinero()
    ejemplo_3_rankings()
    ejemplo_4_flujo_completo()
    
    print("\n" + "="*60)
    print("Ejemplos completados")
    print("="*60 + "\n")
