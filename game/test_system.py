"""
Script de prueba para verificar que todos los módulos funcionan correctamente.
"""

import sys
import os
from pathlib import Path

# Agregar la carpeta game al path
sys.path.insert(0, str(Path(__file__).parent))


def test_imports():
    """Verifica que todos los módulos se importan correctamente."""
    print("\n" + "="*60)
    print("TEST 1: Importación de Módulos")
    print("="*60)
    
    try:
        from players_manager import Player, PlayerManager
        print("✓ players_manager importado correctamente")
    except Exception as e:
        print(f"✗ Error en players_manager: {e}")
        return False
    
    try:
        from money_system import MoneySystem
        print("✓ money_system importado correctamente")
    except Exception as e:
        print(f"✗ Error en money_system: {e}")
        return False
    
    try:
        from rankings_manager import RankingManager
        print("✓ rankings_manager importado correctamente")
    except Exception as e:
        print(f"✗ Error en rankings_manager: {e}")
        return False
    
    try:
        from ui_windows import VentanaMenu, VentanaSeleccionJugadores, VentanaStats
        print("✓ ui_windows importado correctamente")
    except Exception as e:
        print(f"✗ Error en ui_windows: {e}")
        return False
    
    return True


def test_player_system():
    """Prueba el sistema de jugadores."""
    print("\n" + "="*60)
    print("TEST 2: Sistema de Jugadores")
    print("="*60)
    
    from players_manager import PlayerManager
    
    manager = PlayerManager(data_folder="test_data")
    
    # Registrar jugador
    print("\n1. Registrando jugador...")
    success, msg = manager.register_player("TestPlayer", "test1234")
    if success:
        print(f"✓ {msg}")
    else:
        print(f"✗ {msg}")
        return False
    
    # Login exitoso
    print("\n2. Iniciando sesión (válido)...")
    player, msg = manager.login_player("TestPlayer", "test1234")
    if player:
        print(f"✓ {msg}")
    else:
        print(f"✗ {msg}")
        return False
    
    # Login fallido
    print("\n3. Iniciando sesión (inválido)...")
    player, msg = manager.login_player("TestPlayer", "wrongpass")
    if not player:
        print(f"✓ Rechazado correctamente: {msg}")
    else:
        print(f"✗ Debería haber rechazado el login")
        return False
    
    # Actualizar victorias
    print("\n4. Actualizando victorias...")
    manager.update_player_wins("TestPlayer", 'attack')
    player = manager.get_player("TestPlayer")
    if player.attack_wins == 1:
        print(f"✓ Victorias actualizadas: attack_wins={player.attack_wins}")
    else:
        print(f"✗ Error al actualizar victorias")
        return False
    
    return True


def test_money_system():
    """Prueba el sistema de dinero."""
    print("\n" + "="*60)
    print("TEST 3: Sistema de Dinero")
    print("="*60)
    
    from money_system import MoneySystem
    
    money = MoneySystem()
    
    # Inicializar dinero
    print("\n1. Inicializando dinero...")
    money.initialize_round()
    initial = money.get_attacker_money()
    if initial == MoneySystem.INITIAL_MONEY:
        print(f"✓ Dinero inicial correcto: ${initial}")
    else:
        print(f"✗ Dinero inicial incorrecto")
        return False
    
    # Recompensa por daño
    print("\n2. Recompensando por daño...")
    damage = 100
    before = money.get_attacker_money()
    reward = money.reward_attacker_damage(damage)
    after = money.get_attacker_money()
    if after > before:
        print(f"✓ Recompensa otorgada: ${reward}, Total: ${after}")
    else:
        print(f"✗ Error en recompensa")
        return False
    
    # Compra
    print("\n3. Comprando unidad...")
    before = money.get_attacker_money()
    if money.buy_unit_attacker():
        after = money.get_attacker_money()
        if after == before - MoneySystem.UNIT_COST:
            print(f"✓ Compra exitosa, dinero restante: ${after}")
        else:
            print(f"✗ Dinero no deducido correctamente")
            return False
    else:
        print(f"✗ Error en la compra")
        return False
    
    return True


def test_rankings():
    """Prueba el sistema de rankings."""
    print("\n" + "="*60)
    print("TEST 4: Sistema de Rankings")
    print("="*60)
    
    from players_manager import PlayerManager
    from rankings_manager import RankingManager
    
    manager = PlayerManager(data_folder="test_data")
    ranking = RankingManager(manager)
    
    # Obtener rankings
    print("\n1. Obteniendo rankings...")
    defense_ranking = ranking.get_defense_ranking(5)
    print(f"✓ Ranking de defensa obtenido: {len(defense_ranking)} jugadores")
    
    attack_ranking = ranking.get_attack_ranking(5)
    print(f"✓ Ranking de ataque obtenido: {len(attack_ranking)} jugadores")
    
    overall_ranking = ranking.get_overall_ranking(5)
    print(f"✓ Ranking general obtenido: {len(overall_ranking)} jugadores")
    
    # Mostrar datos
    if defense_ranking:
        print(f"\n2. Top 3 Defensores:")
        for pos, (username, wins, total) in enumerate(defense_ranking[:3], 1):
            print(f"   {pos}. {username}: {wins} victorias ({total} total)")
    
    return True


def test_data_persistence():
    """Prueba la persistencia de datos en JSON."""
    print("\n" + "="*60)
    print("TEST 5: Persistencia de Datos")
    print("="*60)
    
    from players_manager import PlayerManager
    from pathlib import Path
    
    test_folder = "test_data"
    players_file = Path(test_folder) / "players.json"
    
    print("\n1. Verificando archivo JSON...")
    if players_file.exists():
        print(f"✓ Archivo encontrado: {players_file}")
        
        # Verificar contenido
        import json
        with open(players_file, 'r') as f:
            data = json.load(f)
            if isinstance(data, dict):
                print(f"✓ JSON válido con {len(data)} jugador(es)")
                for username in data:
                    print(f"   - {username}")
            else:
                print(f"✗ JSON mal formado")
                return False
    else:
        print(f"✗ Archivo no encontrado: {players_file}")
        return False
    
    return True


def test_ui_windows():
    """Verifica que las ventanas se puedan importar (sin iniciarlas)."""
    print("\n" + "="*60)
    print("TEST 6: Ventanas de Interfaz")
    print("="*60)
    
    try:
        import tkinter as tk
        from ui_windows import VentanaMenu, VentanaSeleccionJugadores, VentanaStats
        
        print("\n1. Verificando clases de ventanas...")
        print("✓ VentanaMenu disponible")
        print("✓ VentanaSeleccionJugadores disponible")
        print("✓ VentanaStats disponible")
        
        # Verificar que tienen los métodos requeridos
        print("\n2. Verificando métodos...")
        if hasattr(VentanaMenu, 'create_widgets'):
            print("✓ VentanaMenu.create_widgets existe")
        
        if hasattr(VentanaSeleccionJugadores, 'start_game'):
            print("✓ VentanaSeleccionJugadores.start_game existe")
        
        if hasattr(VentanaStats, 'create_ranking_tab'):
            print("✓ VentanaStats.create_ranking_tab existe")
        
        return True
    except Exception as e:
        print(f"✗ Error: {e}")
        return False


def run_all_tests():
    """Ejecuta todas las pruebas."""
    print("\n" + "="*70)
    print(" "*15 + "PRUEBAS DEL SISTEMA BASE RAIDERS")
    print("="*70)
    
    tests = [
        ("Importación de módulos", test_imports),
        ("Sistema de jugadores", test_player_system),
        ("Sistema de dinero", test_money_system),
        ("Sistema de rankings", test_rankings),
        ("Persistencia de datos", test_data_persistence),
        ("Ventanas de interfaz", test_ui_windows),
    ]
    
    results = []
    for name, test_func in tests:
        try:
            result = test_func()
            results.append((name, result))
        except Exception as e:
            print(f"\n✗ EXCEPCIÓN en {name}: {e}")
            import traceback
            traceback.print_exc()
            results.append((name, False))
    
    # Resumen
    print("\n" + "="*70)
    print("RESUMEN DE PRUEBAS")
    print("="*70)
    
    passed = sum(1 for _, result in results if result)
    total = len(results)
    
    for name, result in results:
        status = "✓ PASÓ" if result else "✗ FALLÓ"
        print(f"{status:10} - {name}")
    
    print("\n" + "="*70)
    print(f"Resultado: {passed}/{total} pruebas pasadas")
    print("="*70 + "\n")
    
    return passed == total


if __name__ == "__main__":
    success = run_all_tests()
    sys.exit(0 if success else 1)
