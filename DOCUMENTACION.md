# BASE RAIDERS - Juego de Estrategia en Tkinter

## Descripción

Base Raiders es un juego de estrategia en tiempo real para dos jugadores desarrollado en Python con Tkinter y programación orientada a objetos.

**Objetivo del Juego:**
- **Atacante**: Conquistar la base del defensor
- **Defensor**: Proteger su base del atacante

## Características Principales

### 1. Sistema de Jugadores
- ✅ Registro de nuevos jugadores
- ✅ Autenticación con contraseña
- ✅ Guardado automático en JSON
- ✅ Tracking de victorias como atacante y defensor

### 2. Menú Principal
- ✅ Botón "Play" para iniciar partida
- ✅ Botón "Stats" para ver rankings
- ✅ Interfaz moderna y amigable

### 3. Pantalla de Selección de Jugadores
- ✅ Selección de jugador atacante
- ✅ Selección de jugador defensor
- ✅ Creación de nuevos jugadores
- ✅ Validación de autenticación

### 4. Sistema de Dinero
- ✅ Dinero inicial por ronda ($1000)
- ✅ Bonificación por ronda ($500)
- ✅ Recompensas por daño (atacante)
- ✅ Recompensas por eliminaciones (defensor)
- ✅ Sistema de costos para compras

### 5. Sistema de Rankings
- ✅ Ranking de defensores
- ✅ Ranking de atacantes
- ✅ Ranking general
- ✅ Ordenamiento automático

## Estructura del Proyecto

```
game/
├── main.py                    # Archivo principal - inicia la aplicación
├── players_manager.py         # Gestión de jugadores y autenticación
├── money_system.py            # Sistema de dinero y compras
├── rankings_manager.py        # Sistema de rankings y estadísticas
├── ui_windows.py              # Interfaces gráficas (Tkinter)
├── config.py                  # Configuración global
├── examples.py                # Ejemplos de uso
├── classes.py                 # Clases de unidades, estructuras, etc.
├── game_data/                 # Carpeta con datos guardados
│   └── players.json           # Base de datos de jugadores
└── graphics/                  # Recursos gráficos
```

## Módulos Principales

### `players_manager.py`
Gestiona la autenticación y datos de jugadores.

**Clases:**
- `Player`: Representa un jugador individual
- `PlayerManager`: Gestiona todos los jugadores

**Funciones principales:**
```python
manager = PlayerManager()
success, msg = manager.register_player("usuario", "contraseña")
player, msg = manager.login_player("usuario", "contraseña")
manager.update_player_wins(username, 'attack')
```

### `money_system.py`
Sistema de dinero y económico del juego.

**Clase:**
- `MoneySystem`: Gestiona dinero y compras

**Funciones principales:**
```python
money = MoneySystem()
money.initialize_round()  # Inicia dinero de ronda
money.reward_attacker_damage(50)  # Recompensa por daño
money.reward_defender_kills(2)    # Recompensa por muertes
money.buy_unit_attacker()  # Comprar unidad
```

### `rankings_manager.py`
Sistema de rankings y estadísticas.

**Clase:**
- `RankingManager`: Gestiona rankings de jugadores

**Funciones principales:**
```python
ranking = RankingManager(player_manager)
defense_ranking = ranking.get_defense_ranking(5)
attack_ranking = ranking.get_attack_ranking(5)
overall_ranking = ranking.get_overall_ranking(5)
```

### `ui_windows.py`
Interfaces gráficas con Tkinter.

**Clases:**
- `VentanaMenu`: Menú principal
- `VentanaSeleccionJugadores`: Selección de jugadores
- `VentanaStats`: Ventana de rankings

## Instalación y Ejecución

### Requisitos
- Python 3.6+
- Tkinter (incluido con Python)

### Instalación
1. Clonar el repositorio
2. Navegar a la carpeta `game/`

### Ejecución
```bash
python main.py
```

## Datos Guardados

Los jugadores se guardan automáticamente en `game_data/players.json`:

```json
{
    "username": {
        "username": "username",
        "password": "contraseña",
        "attack_wins": 5,
        "defense_wins": 3
    }
}
```

## Flujo de Uso

1. **Inicio**: Se muestra el menú principal
2. **Play**: Abre la ventana de selección de jugadores
3. **Registración**: Los jugadores pueden crear nuevas cuentas
4. **Autenticación**: Los jugadores deben iniciar sesión
5. **Partida**: Se inicia el juego con los jugadores autenticados
6. **Actualización**: Al finalizar, se actualizan las victorias
7. **Stats**: Ver rankings y estadísticas

## Configuración

El archivo `config.py` contiene constantes configurables:

```python
# Dinero
INITIAL_MONEY = 1000
ROUND_BONUS = 500

# Costos
COSTS = {
    'tower': 300,
    'wall': 100,
    'unit': 150,
    'upgrade': 200,
}

# Validación
MIN_USERNAME_LENGTH = 3
MIN_PASSWORD_LENGTH = 4
```

## Ejemplos de Uso

Ver `examples.py` para ejemplos completos:

```bash
python examples.py
```

### Ejemplo Básico
```python
from players_manager import PlayerManager
from rankings_manager import RankingManager

# Crear gestor de jugadores
manager = PlayerManager()

# Registrar jugador
manager.register_player("Hero1", "pass1234")

# Autenticar
player, msg = manager.login_player("Hero1", "pass1234")

# Ver rankings
ranking = RankingManager(manager)
top_defenders = ranking.get_defense_ranking(5)
```

## Puntos de Extensión

El código está diseñado para ser fácil de extender:

### Agregar Nuevas Clases de Unidades
Editar `classes.py` y agregar nuevas clases que hereden de `Unit`.

### Agregar Nuevas Compras
En `money_system.py`, agregar nuevos métodos de compra.

### Agregar Nuevas Ventanas
En `ui_windows.py`, crear nuevas clases que hereden de `tk.Toplevel`.

### Agregar Lógica de Juego
En `main.py`, reemplazar `demo_game_session()` con la lógica real del juego.

## Características Futuras

- [ ] Lógica de juego completa (movimiento de unidades, combate, etc.)
- [ ] Sistema de chat entre jugadores
- [ ] Replay de partidas
- [ ] Logros y badges
- [ ] Modo multijugador en red
- [ ] Sistema de clanes
- [ ] Tienda de cosméticos
- [ ] Diarios y misiones

## Manejo de Errores

El sistema incluye manejo robusto de errores:

- Validación de entrada de usuarios
- Manejo de archivos JSON corruptos
- Validación de contraseñas
- Verificación de dinero suficiente

## Convenciones de Código

- Nombres en español para interfaces y lógica de negocio
- Nombres en inglés para clases técnicas
- Docstrings en español para todas las clases y funciones
- Type hints donde es aplicable
- Manejo de excepciones explícito

## Licencia

Este proyecto es de código abierto.

## Autor

Equipo Base Raiders

## Versión

1.0 (Inicial)

---

**Última actualización:** 2024
