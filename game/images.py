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

img_dragon_fireball = load_image("game/graphics/dragon_fireball.png",  8, 8)
img_archer_arrow = load_image("game/graphics/archer_arrow.png",  4, 4)
img_wizard_spell = load_image("game/graphics/wizard_spell.png",  8, 8)
img_crossbow_bolt = load_image("game/graphics/crossbow_bolt.png",  4, 4)

img_wizard_tower_mdv   = load_image("game/graphics/wizard_tower_mdv.png",   32, 32)
img_crossbow_tower_mdv = load_image("game/graphics/crossbow_tower_mdv.png", 32, 32)
img_spiky_tower_mdv    = load_image("game/graphics/spiky_tower_mdv.png",    32, 32)

img_wall_mdv = load_image("game/graphics/wall_mdv.png", 32, 32)
img_base_mdv = load_image("game/graphics/base_mdv.png", 64, 64)

 # -----------------------------------

img_wizard_tower_ftr   = load_image("game/graphics/wizard_tower_ftr.png",   32, 32)
img_crossbow_tower_ftr = load_image("game/graphics/crossbow_tower_ftr.png", 32, 32)
img_spiky_tower_ftr    = load_image("game/graphics/spiky_tower_ftr.png",    32, 32)

img_wall_ftr = load_image("game/graphics/wall_ftr.png", 32, 32)
img_base_ftr = load_image("game/graphics/base_ftr.png", 64, 64)

# --------------------------------------

img_wizard_tower_ntr   = load_image("game/graphics/wizard_tower_ntr.png",   32, 32)
img_crossbow_tower_ntr = load_image("game/graphics/crossbow_tower_ntr.png", 32, 32)
img_spiky_tower_ntr    = load_image("game/graphics/spiky_tower_ntr.png",    32, 32)

img_wall_ntr = load_image("game/graphics/wall_ntr.png", 32, 32)
img_base_ntr = load_image("game/graphics/base_ntr.png", 64, 64)


FACTIONS = {
    "Medieval": {
        "base": img_base_mdv,
        "wall": img_wall_mdv,
        "wizard_tower": img_wizard_tower_mdv,
        "crossbow_tower": img_crossbow_tower_mdv,
        "spiky_tower": img_spiky_tower_mdv,
        "unit_outline": "gold"
    },
    "Futurista": {
        "base": img_base_ftr,
        "wall": img_wall_ftr,
        "wizard_tower": img_wizard_tower_ftr,
        "crossbow_tower": img_crossbow_tower_ftr,
        "spiky_tower": img_spiky_tower_ftr,
        "unit_outline": "cyan"
    },
    "Naturaleza": {
        "base": img_base_ntr,
        "wall": img_wall_ntr,
        "wizard_tower": img_wizard_tower_ntr,
        "crossbow_tower": img_crossbow_tower_ntr,
        "spiky_tower": img_spiky_tower_ntr,
        "unit_outline": "lime green"
    }
}
