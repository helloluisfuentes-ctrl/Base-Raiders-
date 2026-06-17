from PIL import Image, ImageTk
from ui_screens import *

def load_image(path, width, height):
    img = Image.open(path).resize((width, height))
    return ImageTk.PhotoImage(img)

# Troops
img_knight  = load_image("game/graphics/knight.png",  16, 16)
img_goblin  = load_image("game/graphics/goblin.png",   10,  10)
img_archer  = load_image("game/graphics/archer.png",   10,  12)
img_giant   = load_image("game/graphics/giant.png",    56, 58)
img_dragon  = load_image("game/graphics/dragon.png",   28, 16)
img_pekka   = load_image("game/graphics/pekka.png",    24, 24)


"""
# Towers
img_wizard_tower   = load_image("assets/wizard_tower.png",   32, 32)
img_crossbow_tower = load_image("assets/crossbow_tower.png", 32, 32)
img_spiky_tower    = load_image("assets/spiky_tower.png",    32, 32)

# Structures
img_wall = load_image("assets/wall.png", 32, 32)
img_base = load_image("assets/base.png", 96, 96)
"""