import tkinter as tk
from tkinter import ttk
from file_manager import get_top_attackers, get_top_defenders


class StatsWindow:
    """Ventana para mostrar estadísticas y rankings de jugadores."""
    
    def __init__(self, parent_root):
        self.root = parent_root
        self.window = tk.Toplevel(parent_root)
        self.window.title("Estadísticas y Rankings")
        self.window.geometry("700x500")
        self.window.resizable(False, False)
        
        self.create_widgets()
    
    def create_widgets(self):
        """Crea todos los elementos de la interfaz."""
        
        # Título
        title_label = tk.Label(
            self.window,
            text="Rankings Globales",
            font=("Arial", 20, "bold")
        )
        title_label.pack(pady=10)
        
        # Main frame para dos columnas
        main_frame = tk.Frame(self.window)
        main_frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
        
        # ===== COLUMNA IZQUIERDA: TOP ATACANTES =====
        left_frame = tk.LabelFrame(
            main_frame,
            text="Top 5 Atacantes",
            font=("Arial", 12, "bold"),
            padx=10,
            pady=10
        )
        left_frame.pack(side=tk.LEFT, padx=5, fill=tk.BOTH, expand=True)
        
        self.create_ranking_table(left_frame, "attack")
        
        # ===== COLUMNA DERECHA: TOP DEFENSORES =====
        right_frame = tk.LabelFrame(
            main_frame,
            text="Top 5 Defensores",
            font=("Arial", 12, "bold"),
            padx=10,
            pady=10
        )
        right_frame.pack(side=tk.RIGHT, padx=5, fill=tk.BOTH, expand=True)
        
        self.create_ranking_table(right_frame, "defense")
        
        # Botón cerrar
        close_btn = tk.Button(
            self.window,
            text="Cerrar",
            font=("Arial", 12),
            command=self.window.destroy,
            bg="lightcoral",
            width=20
        )
        close_btn.pack(pady=10)
    
    def create_ranking_table(self, parent, role_type):
        """Crea una tabla de rankings."""
        
        if role_type == "attack":
            data = get_top_attackers(5)
        else:
            data = get_top_defenders(5)
        
        # Crear tabla con Treeview
        columns = ("Rango", "Jugador", "Victorias")
        table = ttk.Treeview(parent, columns=columns, height=6, show="headings")
        
        # Definir encabezados
        table.column("Rango", width=50, anchor="center")
        table.column("Jugador", width=100, anchor="center")
        table.column("Victorias", width=50, anchor="center")
        
        table.heading("Rango", text="Rango")
        table.heading("Jugador", text="Jugador")
        table.heading("Victorias", text="Victorias")
        
        # Insertar datos
        for idx, player in enumerate(data, 1):
            table.insert("", "end", values=(
                f"#{idx}",
                player["nickname"],
                player["wins"]
            ))
        
        # Scrollbar
        scrollbar = ttk.Scrollbar(parent, orient=tk.VERTICAL, command=table.yview)
        table.configure(yscroll=scrollbar.set)
        
        table.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
