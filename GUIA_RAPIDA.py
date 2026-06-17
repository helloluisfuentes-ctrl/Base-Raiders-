"""
Guía Rápida de Inicio - BASE RAIDERS

Este archivo contiene instrucciones para ejecutar la aplicación.
"""

# ============================================================================
# REQUISITOS
# ============================================================================
# - Python 3.6 o superior
# - Tkinter (generalmente incluido con Python)
# - Acceso a escribir en la carpeta del proyecto (para guardar datos)

# ============================================================================
# INSTRUCCIONES DE INICIO RÁPIDO
# ============================================================================

# OPCIÓN 1: Ejecutar la aplicación con interfaz gráfica
# ============================================================================
# En la terminal, ejecuta:
# 
#     python main.py
# 
# O si Python no está en PATH:
# 
#     C:\Python\python.exe main.py
# 
# Se abrirá la ventana del menú principal.

# OPCIÓN 2: Ejecutar los ejemplos de demostración
# ============================================================================
# En la terminal, ejecuta:
# 
#     python examples.py
# 
# Esto ejecutará ejemplos de:
# - Gestión de jugadores
# - Sistema de dinero
# - Rankings
# - Flujo completo de partida

# OPCIÓN 3: Ejecutar las pruebas del sistema
# ============================================================================
# En la terminal, ejecuta:
# 
#     python test_system.py
# 
# Esto verificará que todos los módulos funcionan correctamente.

# ============================================================================
# ESTRUCTURA DE CARPETAS GENERADAS
# ============================================================================
# 
# Después de ejecutar por primera vez, se creará:
#
# game_data/
#   └── players.json    # Base de datos de jugadores
#
# Este archivo guarda automáticamente:
# - Nombres de usuario
# - Contraseñas (sin cifrar - solo para demostración)
# - Victorias como atacante y defensor

# ============================================================================
# PRIMEROS PASOS EN LA APLICACIÓN
# ============================================================================

# 1. MENÚ PRINCIPAL
#    - Botón "PLAY": Ir a seleccionar jugadores
#    - Botón "STATS": Ver rankings
#    - Botón "SALIR": Cerrar aplicación

# 2. PANTALLA DE SELECCIÓN DE JUGADORES
#    a) CREAR NUEVO JUGADOR:
#       - Ingresa un usuario (mínimo 3 caracteres)
#       - Ingresa una contraseña (mínimo 4 caracteres)
#       - Presiona "Registrar"
#
#    b) INICIAR SESIÓN:
#       - Selecciona usuario del dropdown
#       - Ingresa contraseña
#       - Presiona "Login"
#       - Repite para el otro jugador (atacante y defensor deben ser diferentes)
#
#    c) INICIAR PARTIDA:
#       - Ambos jugadores deben estar autenticados
#       - Presiona "INICIAR PARTIDA"

# 3. VENTANA DE ESTADÍSTICAS
#    - Pestaña "🛡️ Top Defensores": Mejores defensores por victorias defensivas
#    - Pestaña "⚔️ Top Atacantes": Mejores atacantes por victorias ofensivas
#    - Pestaña "🏆 Ranking General": Ranking por total de victorias

# ============================================================================
# ARCHIVOS DEL PROYECTO
# ============================================================================

# players_manager.py
#   - Gestión de jugadores
#   - Registro e inicio de sesión
#   - Guardado en JSON
#   - Actualización de victorias

# money_system.py
#   - Sistema económico del juego
#   - Dinero inicial y bonificaciones
#   - Recompensas por daño y muertes
#   - Sistema de costos

# rankings_manager.py
#   - Sistema de rankings
#   - Ordenamiento automático
#   - Estadísticas de jugadores

# ui_windows.py
#   - Interfaces gráficas con Tkinter
#   - Menú principal
#   - Selección de jugadores
#   - Ventana de estadísticas

# main.py
#   - Archivo principal
#   - Controlador del juego
#   - Orquestación de módulos

# ============================================================================
# EJEMPLO DE USO PROGRAMÁTICO
# ============================================================================

"""
from players_manager import PlayerManager
from rankings_manager import RankingManager
from money_system import MoneySystem

# Crear gestor de jugadores
pm = PlayerManager()

# Registrar jugadores
pm.register_player("Hero", "pass123")
pm.register_player("Defender", "pass456")

# Autenticar
attacker, _ = pm.login_player("Hero", "pass123")
defender, _ = pm.login_player("Defender", "pass456")

# Ver rankings
ranking = RankingManager(pm)
print(ranking.get_defense_ranking())
print(ranking.get_attack_ranking())

# Sistema de dinero
money = MoneySystem()
money.initialize_round()
money.reward_attacker_damage(100)
money.buy_unit_attacker()

# Actualizar victorias
pm.update_player_wins("Hero", 'attack')
pm.update_player_wins("Defender", 'defense')
"""

# ============================================================================
# TROUBLESHOOTING
# ============================================================================

# Problema: "ModuleNotFoundError: No module named 'tkinter'"
# Solución: Reinstalar Python con Tkinter incluido
# 
# Problema: "FileNotFoundError: players.json"
# Solución: La carpeta game_data se crea automáticamente al registrar un jugador
#
# Problema: La contraseña no funciona
# Solución: Las contraseñas son sensibles a mayúsculas/minúsculas
#
# Problema: No aparecen jugadores en los dropdowns
# Solución: Primero registra un nuevo jugador usando "CREAR NUEVO JUGADOR"

# ============================================================================
# CONFIGURACIÓN PERSONALIZADA
# ============================================================================

# Edita config.py para personalizar:

# Dinero inicial
# INITIAL_MONEY = 1000

# Costos de elementos
# COSTS = {'tower': 300, 'wall': 100, 'unit': 150, 'upgrade': 200}

# Número de jugadores en rankings
# TOP_PLAYERS = 5

# ============================================================================
# PRÓXIMOS PASOS
# ============================================================================

# 1. Integrar lógica de juego completa en game_loops.py
# 2. Implementar renderizado gráfico del mapa
# 3. Agregar sistema de combate
# 4. Implementar IA para modo single-player
# 5. Agregar sistema de chat
# 6. Crear editor de mapas

# ============================================================================
