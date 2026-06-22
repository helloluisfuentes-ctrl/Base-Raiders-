# Base Raiders

Base Raiders es un juego de estrategia para dos jugadores desarrollado en Python utilizando Tkinter. El proyecto fue realizado como parte del curso de Introduccion a la Programacion.

En el juego, un jugador toma el rol de defensor y debe proteger una base central. El otro jugador toma el rol de atacante y debe destruir la base utilizando diferentes unidades.

## Caracteristicas principales

- Juego para dos jugadores.
- Roles de atacante y defensor.
- Registro de jugadores con usuario y contrasena.
- Inicio de sesion para seleccionar jugadores.
- Seleccion de facciones.
- Sistema de rondas hasta que un jugador gane 3 rondas.
- Sistema economico para comprar torres, muros y unidades.
- Reembolso al eliminar elementos durante la fase de colocacion.
- Combate automatico entre unidades y torres.
- Ranking de mejores atacantes y defensores.
- Almacenamiento de datos mediante archivos JSON.
- Interfaz grafica desarrollada con Tkinter.

## Requisitos

Para ejecutar el proyecto se necesita:

- Python 3.
- Pillow, para cargar las imagenes del juego.

Instalacion de Pillow:

```bash
pip install pillow
```

## Instalacion

1. Descargar o clonar el repositorio.
2. Entrar a la carpeta principal del proyecto.
3. Instalar las dependencias necesarias.

Ejemplo:

```bash
pip install pillow
```

## Como ejecutar el programa

Desde la carpeta principal del proyecto, ejecutar:

```bash
python game/main.py
```

El archivo principal del programa es:

```text
game/main.py
```

## Estructura de archivos

```text
Base-Raiders--main/
  README.md
  docs/
    MANUAL_USUARIO.md
    DOCUMENTACION_TECNICA.md
  game/
    main.py
    classes.py
    constants.py
    buttons.py
    ui_screens.py
    ui_functions.py
    game_logic.py
    game_loops.py
    player_selection.py
    stats_window.py
    file_manager.py
    players_manager.py
    money_management.py
    money_system.py
    rankings_manager.py
    config.py
    victory_screens.py
    images.py
    graphics/
    game_data/
      players.json
```

## Ejemplos de uso

### Registrar un jugador

1. Abrir el programa.
2. Presionar el boton **REGISTRAR**.
3. Escribir usuario y contrasena.
4. Confirmar el registro.

### Iniciar una partida

1. Presionar **JUGAR**.
2. Seleccionar el jugador atacante.
3. Escribir la contrasena del atacante.
4. Seleccionar la faccion del atacante.
5. Seleccionar el jugador defensor.
6. Escribir la contrasena del defensor.
7. Seleccionar una faccion diferente para el defensor.
8. Confirmar ambos jugadores.
9. Presionar **PLAY**.

### Jugar una ronda

1. El defensor coloca muros y torres.
2. El defensor presiona **Ready**.
3. El atacante coloca unidades.
4. El atacante presiona **Start**.
5. El combate se ejecuta automaticamente.

La partida termina cuando un jugador gana 3 rondas.

## Tecnologias utilizadas

- Python.
- Tkinter.
- Pillow.
- JSON.
- Programacion orientada a objetos.

## Documentacion

El proyecto incluye documentacion adicional:

- [Manual de Usuario](docs/MANUAL_USUARIO.md)
- [Documentacion Tecnica](docs/DOCUMENTACION_TECNICA.md)

## Autores

Agregar nombres de los integrantes del grupo.

## Posibles mejoras futuras

- Agregar sonidos usando pygame.
- Mejorar el diseno visual del tablero.
- Agregar imagenes para torres, muros y base.
- Crear pruebas automatizadas.
- Mejorar el balance de tropas y torres.
- Agregar mas facciones.
- Agregar una pantalla de ayuda dentro del juego.
- Unificar algunos modulos que actualmente tienen funciones parecidas.
