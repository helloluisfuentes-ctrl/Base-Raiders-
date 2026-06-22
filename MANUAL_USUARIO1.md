# Manual de Usuario

# Base Raiders

## Introduccion

Este manual explica como utilizar el juego **Base Raiders**. El documento esta dirigido a usuarios que desean ejecutar el programa, registrar jugadores, iniciar una partida y entender las opciones principales del juego.

Base Raiders fue desarrollado en Python utilizando la biblioteca Tkinter para la interfaz grafica. El juego esta pensado para dos jugadores: uno toma el rol de atacante y el otro toma el rol de defensor.

## Descripcion general del juego

Base Raiders es un juego de estrategia por rondas. En cada partida participan dos jugadores:

- **Defensor:** debe colocar muros y torres para proteger la base central.
- **Atacante:** debe comprar y colocar unidades para destruir la base del defensor.

La partida se divide en rondas. El defensor prepara primero sus defensas y despues el atacante coloca sus tropas. Cuando inicia el combate, las unidades atacantes avanzan y atacan estructuras, mientras que las torres defensivas intentan eliminar a las unidades enemigas.

El primer jugador que gane 3 rondas gana la partida completa.

## Requisitos para ejecutar el programa

Para ejecutar Base Raiders se necesita:

- Tener Python instalado.
- Tener instalada la biblioteca Pillow, porque el proyecto usa imagenes.
- Tener todos los archivos del proyecto en la misma estructura de carpetas.

La biblioteca Pillow se puede instalar con:

```bash
pip install pillow
```

## Como iniciar la aplicacion

Para iniciar el juego se debe abrir una terminal en la carpeta principal del proyecto y ejecutar:

```bash
python game/main.py
```

El archivo principal del programa es `game/main.py`.

## Explicacion del menu principal

Al abrir el juego aparece el menu principal. Este menu contiene tres opciones principales:

- **JUGAR:** abre la ventana para elegir el atacante y el defensor.
- **REGISTRAR:** permite registrar un nuevo jugador.
- **RANKINGS:** abre la ventana de estadisticas con los mejores jugadores.

El menu principal sirve como punto de inicio para todas las acciones importantes del programa.

## Como registrar nuevos jugadores

Para registrar un jugador se debe presionar el boton **REGISTRAR** en el menu principal.

Luego aparece una ventana donde se deben ingresar:

- Nombre de usuario.
- Contrasena.

Si el usuario no existe, el programa lo guarda en el archivo de datos. Si el usuario ya existe, se muestra un mensaje de error.

La informacion de jugadores se guarda en el archivo:

```text
game/game_data/players.json
```

## Como iniciar sesion

El inicio de sesion se realiza cuando se elige un jugador para una partida.

En la ventana de seleccion de jugadores, cada rol debe ingresar:

- Jugador registrado.
- Contrasena.
- Faccion.

El programa verifica que la contrasena coincida con la informacion guardada. Si la contrasena es incorrecta, no se permite confirmar ese jugador.

## Como seleccionar al atacante y al defensor

Al presionar **JUGAR**, se abre una ventana con dos secciones:

- Atacante.
- Defensor.

En cada seccion se selecciona un jugador registrado desde una lista. Despues se escribe la contrasena y se escoge una faccion.

El atacante y el defensor deben ser jugadores diferentes. Tambien deben usar facciones distintas.

Las facciones disponibles son:

- Medieval.
- Futurista.
- Naturaleza.

Las facciones cambian la apariencia visual de algunas partes del juego, como la base, muros, torres y unidades.

## Como iniciar una partida

Despues de confirmar atacante y defensor, se presiona el boton **PLAY**.

La partida inicia con la fase del defensor. En esta fase el defensor puede colocar:

- Muros.
- Wizard Tower.
- Crossbow Tower.
- Spiky Tower.

Cuando el defensor termina, presiona **Ready**. Luego inicia la fase del atacante, donde puede colocar unidades:

- Knight.
- Goblin.
- Archer.
- Giant.
- Dragon.
- Pekka.

Cuando el atacante termina, presiona **Start** para iniciar el combate.

Durante el combate, las tropas atacantes avanzan y atacan estructuras. Las torres defensivas atacan a las tropas. La ronda termina cuando:

- El atacante destruye la base central.
- El defensor elimina todas las unidades atacantes.

La partida termina cuando alguno de los dos jugadores gana 3 rondas.

## Explicacion de la ventana de estadisticas y rankings

La ventana de rankings se abre desde el boton **RANKINGS** del menu principal.

Esta ventana muestra dos tablas:

- **Top 5 Atacantes:** jugadores con mas victorias como atacante.
- **Top 5 Defensores:** jugadores con mas victorias como defensor.

Los datos se leen desde el archivo JSON de jugadores.

## Descripcion del sistema economico

El juego utiliza un sistema de dinero para controlar las compras.

Cada jugador recibe dinero al iniciar una ronda. El dinero se usa para comprar tropas, muros y torres.

Costos principales:

- Wall: 75.
- Wizard Tower: 200.
- Crossbow Tower: 180.
- Spiky Tower: 150.
- Knight: 100.
- Goblin: 50.
- Archer: 120.
- Giant: 200.
- Dragon: 180.
- Pekka: 150.

El atacante gana dinero por causar dano a estructuras y por destruir torres. El defensor gana dinero por eliminar unidades enemigas. Ademas, si se elimina una unidad o estructura durante la fase de colocacion usando **Delete**, se devuelve el costo correspondiente al jugador.

## Posibles errores y soluciones

### El programa no abre

Posible causa: Python no esta instalado o no se esta ejecutando desde la carpeta correcta.

Solucion: verificar que Python este instalado y ejecutar:

```bash
python game/main.py
```

### Error relacionado con imagenes

Posible causa: falta la biblioteca Pillow o no estan las imagenes en la carpeta `game/graphics`.

Solucion:

```bash
pip install pillow
```

Tambien se debe revisar que existan las imagenes de las unidades.

### No se puede iniciar sesion

Posible causa: la contrasena escrita no coincide con la guardada.

Solucion: revisar el usuario seleccionado y escribir la contrasena correcta.

### No aparece un jugador en la lista

Posible causa: el jugador no fue registrado o el archivo JSON no se guardo correctamente.

Solucion: registrar el jugador desde el boton **REGISTRAR**.

### No se puede colocar una unidad o estructura

Posibles causas:

- No hay suficiente dinero.
- Se esta intentando colocar fuera de la zona permitida.
- Ya existe una estructura en esa posicion.

Solucion: revisar el dinero disponible y colocar el elemento en la zona correspondiente.

## Conclusiones

Base Raiders es un juego sencillo de estrategia que permite practicar el uso de interfaces graficas, clases, listas, archivos JSON y logica de juego por rondas. El usuario puede registrar jugadores, seleccionar roles, comprar elementos y competir hasta que uno gane la partida. Aunque el juego tiene reglas simples, permite entender de forma practica como se puede organizar un proyecto de programacion en varios archivos.
