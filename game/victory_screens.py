import tkinter as tk
from ui_functions import return_to_main_menu


def setup_victory_screens(canvas_win_raiders, canvas_win_defense):
    """
    Configura los textos y botones de victoria en los canvas.
    Retorna al menú principal al presionar los botones.
    """
    
    # ===== PANTALLA DE VICTORIA DEL ATACANTE =====
    # Título
    canvas_win_raiders.create_text(
        512, 150,
        text="¡LOS ATACANTES GANARON!",
        font=("Arial", 60, "bold"),
        fill="yellow"
    )
    
    # Botón para retornar
    return_btn_attackers = tk.Button(
        canvas_win_raiders,
        text="Retornar al Menú",
        font=("Arial", 20, "bold"),
        command=return_to_main_menu,
        bg="green",
        fg="white",
        width=20
    )
    return_btn_attackers.place(x=256, y=600)
    
    # ===== PANTALLA DE VICTORIA DEL DEFENSOR =====
    # Título
    canvas_win_defense.create_text(
        512, 150,
        text="¡LA DEFENSA GANÓ!",
        font=("Arial", 60, "bold"),
        fill="gold"
    )
    
    # Botón para retornar
    return_btn_defense = tk.Button(
        canvas_win_defense,
        text="Retornar al Menú",
        font=("Arial", 20, "bold"),
        command=return_to_main_menu,
        bg="blue",
        fg="white",
        width=20
    )
    return_btn_defense.place(x=256, y=600)
