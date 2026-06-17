"""
Módulo de interfaces gráficas del juego.

Contiene:
- VentanaMenu: Menú principal
- VentanaSeleccionJugadores: Pantalla de selección de jugadores
- VentanaStats: Ventana de rankings
"""

import tkinter as tk
from tkinter import ttk, messagebox, simpledialog


class VentanaMenu:
    """Ventana del menú principal del juego."""
    
    def __init__(self, root, on_play_callback, on_stats_callback):
        """
        Inicializa la ventana del menú.
        
        Args:
            root: Ventana raíz de Tkinter
            on_play_callback: Función a llamar al presionar "Play"
            on_stats_callback: Función a llamar al presionar "Stats"
        """
        self.root = root
        self.on_play_callback = on_play_callback
        self.on_stats_callback = on_stats_callback
        
        self.setup_window()
        self.create_widgets()
    
    def setup_window(self):
        """Configura la ventana principal."""
        self.root.title("Base Raiders - Menú Principal")
        self.root.geometry("400x300")
        self.root.configure(bg="#2c3e50")
        
        # Centrar ventana
        self.root.update_idletasks()
        width = self.root.winfo_width()
        height = self.root.winfo_height()
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2)
        self.root.geometry(f"{width}x{height}+{x}+{y}")
    
    def create_widgets(self):
        """Crea los widgets de la interfaz."""
        # Frame principal
        main_frame = tk.Frame(self.root, bg="#2c3e50")
        main_frame.pack(expand=True, fill=tk.BOTH)
        
        # Título
        title_label = tk.Label(
            main_frame,
            text="BASE RAIDERS",
            font=("Arial", 28, "bold"),
            bg="#2c3e50",
            fg="#ecf0f1"
        )
        title_label.pack(pady=20)
        
        # Subtítulo
        subtitle_label = tk.Label(
            main_frame,
            text="¡Defiende o Ataca!",
            font=("Arial", 14),
            bg="#2c3e50",
            fg="#95a5a6"
        )
        subtitle_label.pack(pady=10)
        
        # Botón Play
        play_button = tk.Button(
            main_frame,
            text="🎮 PLAY",
            font=("Arial", 14, "bold"),
            bg="#27ae60",
            fg="white",
            padx=40,
            pady=15,
            command=self.on_play_callback,
            cursor="hand2"
        )
        play_button.pack(pady=15)
        
        # Botón Stats
        stats_button = tk.Button(
            main_frame,
            text="📊 STATS",
            font=("Arial", 14, "bold"),
            bg="#2980b9",
            fg="white",
            padx=40,
            pady=15,
            command=self.on_stats_callback,
            cursor="hand2"
        )
        stats_button.pack(pady=15)
        
        # Botón Salir
        exit_button = tk.Button(
            main_frame,
            text="❌ SALIR",
            font=("Arial", 12, "bold"),
            bg="#c0392b",
            fg="white",
            padx=40,
            pady=10,
            command=self.root.quit,
            cursor="hand2"
        )
        exit_button.pack(pady=15)


class VentanaSeleccionJugadores:
    """Ventana para seleccionar o crear jugadores."""
    
    def __init__(self, root, player_manager, on_start_game_callback):
        """
        Inicializa la ventana de selección de jugadores.
        
        Args:
            root: Ventana raíz de Tkinter
            player_manager: Instancia de PlayerManager
            on_start_game_callback: Función a llamar al iniciar juego
        """
        self.root = root
        self.player_manager = player_manager
        self.on_start_game_callback = on_start_game_callback
        
        self.attacker = None
        self.defender = None
        
        self.window = None
        self.create_window()
    
    def create_window(self):
        """Crea la ventana de selección de jugadores."""
        self.window = tk.Toplevel(self.root)
        self.window.title("Seleccionar Jugadores")
        self.window.geometry("600x500")
        self.window.configure(bg="#34495e")
        
        self.setup_widgets()
    
    def setup_widgets(self):
        """Configura los widgets de la ventana."""
        # Título
        title = tk.Label(
            self.window,
            text="Seleccionar Jugadores",
            font=("Arial", 18, "bold"),
            bg="#34495e",
            fg="#ecf0f1"
        )
        title.pack(pady=10)
        
        # Frame de selección de atacante
        attacker_frame = tk.LabelFrame(
            self.window,
            text="⚔️ ATACANTE",
            font=("Arial", 12, "bold"),
            bg="#34495e",
            fg="#ecf0f1",
            padx=10,
            pady=10
        )
        attacker_frame.pack(padx=20, pady=10, fill=tk.BOTH)
        
        tk.Label(attacker_frame, text="Usuario:", bg="#34495e", fg="#ecf0f1").grid(row=0, column=0, sticky="w")
        self.attacker_var = tk.StringVar()
        attacker_combo = ttk.Combobox(
            attacker_frame,
            textvariable=self.attacker_var,
            values=list(self.player_manager.players.keys()),
            state="readonly"
        )
        attacker_combo.grid(row=0, column=1, sticky="ew", padx=5)
        
        tk.Label(attacker_frame, text="Contraseña:", bg="#34495e", fg="#ecf0f1").grid(row=1, column=0, sticky="w", pady=5)
        self.attacker_password = tk.StringVar()
        tk.Entry(attacker_frame, textvariable=self.attacker_password, show="*").grid(row=1, column=1, sticky="ew", padx=5)
        
        attacker_login_btn = tk.Button(
            attacker_frame,
            text="✓ Login",
            bg="#27ae60",
            fg="white",
            command=self.login_attacker
        )
        attacker_login_btn.grid(row=2, column=1, sticky="e", pady=5)
        
        self.attacker_status = tk.Label(attacker_frame, text="No autenticado", bg="#34495e", fg="#e74c3c")
        self.attacker_status.grid(row=3, column=0, columnspan=2, sticky="w", pady=5)
        
        attacker_frame.columnconfigure(1, weight=1)
        
        # Frame de selección de defensor
        defender_frame = tk.LabelFrame(
            self.window,
            text="🛡️ DEFENSOR",
            font=("Arial", 12, "bold"),
            bg="#34495e",
            fg="#ecf0f1",
            padx=10,
            pady=10
        )
        defender_frame.pack(padx=20, pady=10, fill=tk.BOTH)
        
        tk.Label(defender_frame, text="Usuario:", bg="#34495e", fg="#ecf0f1").grid(row=0, column=0, sticky="w")
        self.defender_var = tk.StringVar()
        defender_combo = ttk.Combobox(
            defender_frame,
            textvariable=self.defender_var,
            values=list(self.player_manager.players.keys()),
            state="readonly"
        )
        defender_combo.grid(row=0, column=1, sticky="ew", padx=5)
        
        tk.Label(defender_frame, text="Contraseña:", bg="#34495e", fg="#ecf0f1").grid(row=1, column=0, sticky="w", pady=5)
        self.defender_password = tk.StringVar()
        tk.Entry(defender_frame, textvariable=self.defender_password, show="*").grid(row=1, column=1, sticky="ew", padx=5)
        
        defender_login_btn = tk.Button(
            defender_frame,
            text="✓ Login",
            bg="#2980b9",
            fg="white",
            command=self.login_defender
        )
        defender_login_btn.grid(row=2, column=1, sticky="e", pady=5)
        
        self.defender_status = tk.Label(defender_frame, text="No autenticado", bg="#34495e", fg="#e74c3c")
        self.defender_status.grid(row=3, column=0, columnspan=2, sticky="w", pady=5)
        
        defender_frame.columnconfigure(1, weight=1)
        
        # Frame para crear nuevo jugador
        register_frame = tk.LabelFrame(
            self.window,
            text="📝 CREAR NUEVO JUGADOR",
            font=("Arial", 12, "bold"),
            bg="#34495e",
            fg="#ecf0f1",
            padx=10,
            pady=10
        )
        register_frame.pack(padx=20, pady=10, fill=tk.BOTH)
        
        tk.Label(register_frame, text="Usuario:", bg="#34495e", fg="#ecf0f1").grid(row=0, column=0, sticky="w")
        self.new_username = tk.StringVar()
        tk.Entry(register_frame, textvariable=self.new_username).grid(row=0, column=1, sticky="ew", padx=5)
        
        tk.Label(register_frame, text="Contraseña:", bg="#34495e", fg="#ecf0f1").grid(row=1, column=0, sticky="w", pady=5)
        self.new_password = tk.StringVar()
        tk.Entry(register_frame, textvariable=self.new_password, show="*").grid(row=1, column=1, sticky="ew", padx=5)
        
        register_btn = tk.Button(
            register_frame,
            text="➕ Registrar",
            bg="#9b59b6",
            fg="white",
            command=self.register_new_player
        )
        register_btn.grid(row=2, column=1, sticky="e", pady=5)
        
        register_frame.columnconfigure(1, weight=1)
        
        # Frame de botones finales
        button_frame = tk.Frame(self.window, bg="#34495e")
        button_frame.pack(pady=15)
        
        start_btn = tk.Button(
            button_frame,
            text="▶ INICIAR PARTIDA",
            font=("Arial", 12, "bold"),
            bg="#27ae60",
            fg="white",
            padx=20,
            pady=10,
            command=self.start_game
        )
        start_btn.pack(side=tk.LEFT, padx=10)
        
        back_btn = tk.Button(
            button_frame,
            text="◀ VOLVER",
            font=("Arial", 12, "bold"),
            bg="#95a5a6",
            fg="white",
            padx=20,
            pady=10,
            command=self.window.destroy
        )
        back_btn.pack(side=tk.LEFT, padx=10)
    
    def login_attacker(self):
        """Intenta autenticar al atacante."""
        username = self.attacker_var.get()
        password = self.attacker_password.get()
        
        if not username or not password:
            messagebox.showerror("Error", "Por favor ingresa usuario y contraseña")
            return
        
        player, message = self.player_manager.login_player(username, password)
        
        if player:
            self.attacker = player
            self.attacker_status.config(text=f"✓ {username} autenticado", fg="#27ae60")
            messagebox.showinfo("Éxito", message)
        else:
            messagebox.showerror("Error", message)
    
    def login_defender(self):
        """Intenta autenticar al defensor."""
        username = self.defender_var.get()
        password = self.defender_password.get()
        
        if not username or not password:
            messagebox.showerror("Error", "Por favor ingresa usuario y contraseña")
            return
        
        player, message = self.player_manager.login_player(username, password)
        
        if player:
            self.defender = player
            self.defender_status.config(text=f"✓ {username} autenticado", fg="#2980b9")
            messagebox.showinfo("Éxito", message)
        else:
            messagebox.showerror("Error", message)
    
    def register_new_player(self):
        """Registra un nuevo jugador."""
        username = self.new_username.get()
        password = self.new_password.get()
        
        if not username or not password:
            messagebox.showerror("Error", "Por favor completa todos los campos")
            return
        
        success, message = self.player_manager.register_player(username, password)
        
        if success:
            messagebox.showinfo("Éxito", message)
            self.new_username.delete(0, tk.END)
            self.new_password.delete(0, tk.END)
            # Actualizar comboboxes
            self.attacker_var.set("")
            self.defender_var.set("")
        else:
            messagebox.showerror("Error", message)
    
    def start_game(self):
        """Inicia la partida si ambos jugadores están autenticados."""
        if not self.attacker or not self.defender:
            messagebox.showerror("Error", "Ambos jugadores deben estar autenticados")
            return
        
        if self.attacker.username == self.defender.username:
            messagebox.showerror("Error", "El atacante y defensor deben ser jugadores diferentes")
            return
        
        # Llamar callback con los jugadores
        self.on_start_game_callback(self.attacker, self.defender)
        self.window.destroy()


class VentanaStats:
    """Ventana para mostrar rankings y estadísticas."""
    
    def __init__(self, root, ranking_manager):
        """
        Inicializa la ventana de estadísticas.
        
        Args:
            root: Ventana raíz de Tkinter
            ranking_manager: Instancia de RankingManager
        """
        self.root = root
        self.ranking_manager = ranking_manager
        
        self.window = None
        self.create_window()
    
    def create_window(self):
        """Crea la ventana de estadísticas."""
        self.window = tk.Toplevel(self.root)
        self.window.title("Estadísticas y Rankings")
        self.window.geometry("700x600")
        self.window.configure(bg="#2c3e50")
        
        self.setup_widgets()
    
    def setup_widgets(self):
        """Configura los widgets de la ventana."""
        # Título
        title = tk.Label(
            self.window,
            text="ESTADÍSTICAS Y RANKINGS",
            font=("Arial", 18, "bold"),
            bg="#2c3e50",
            fg="#ecf0f1"
        )
        title.pack(pady=10)
        
        # Frame principal con pestañas
        notebook = ttk.Notebook(self.window)
        notebook.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Pestaña de ranking de defensores
        defense_frame = tk.Frame(notebook, bg="#34495e")
        notebook.add(defense_frame, text="🛡️ Top Defensores")
        self.create_ranking_tab(defense_frame, self.ranking_manager.get_defense_ranking())
        
        # Pestaña de ranking de atacantes
        attack_frame = tk.Frame(notebook, bg="#34495e")
        notebook.add(attack_frame, text="⚔️ Top Atacantes")
        self.create_ranking_tab(attack_frame, self.ranking_manager.get_attack_ranking())
        
        # Pestaña de ranking general
        general_frame = tk.Frame(notebook, bg="#34495e")
        notebook.add(general_frame, text="🏆 Ranking General")
        self.create_general_ranking_tab(general_frame)
        
        # Botón de cerrar
        close_btn = tk.Button(
            self.window,
            text="Cerrar",
            bg="#95a5a6",
            fg="white",
            command=self.window.destroy,
            padx=20,
            pady=10
        )
        close_btn.pack(pady=10)
    
    def create_ranking_tab(self, parent, ranking_data):
        """
        Crea una pestaña de ranking.
        
        Args:
            parent: Frame padre
            ranking_data: Lista de datos de ranking
        """
        # Tabla de ranking
        tree = ttk.Treeview(
            parent,
            columns=("Posición", "Usuario", "Victorias", "Total"),
            height=15,
            show="headings"
        )
        
        tree.heading("Posición", text="Pos")
        tree.heading("Usuario", text="Usuario")
        tree.heading("Victorias", text="Victorias")
        tree.heading("Total", text="Total")
        
        tree.column("Posición", width=50)
        tree.column("Usuario", width=150)
        tree.column("Victorias", width=100)
        tree.column("Total", width=100)
        
        # Insertar datos
        for position, (username, specific_wins, total_wins) in enumerate(ranking_data, 1):
            tree.insert("", tk.END, values=(position, username, specific_wins, total_wins))
        
        tree.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # Scrollbar
        scrollbar = ttk.Scrollbar(parent, orient=tk.VERTICAL, command=tree.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        tree.configure(yscroll=scrollbar.set)
    
    def create_general_ranking_tab(self, parent):
        """Crea la pestaña de ranking general."""
        ranking_data = self.ranking_manager.get_overall_ranking()
        
        tree = ttk.Treeview(
            parent,
            columns=("Posición", "Usuario", "Total", "Ataque", "Defensa"),
            height=15,
            show="headings"
        )
        
        tree.heading("Posición", text="Pos")
        tree.heading("Usuario", text="Usuario")
        tree.heading("Total", text="Total")
        tree.heading("Ataque", text="Ataque")
        tree.heading("Defensa", text="Defensa")
        
        tree.column("Posición", width=50)
        tree.column("Usuario", width=150)
        tree.column("Total", width=80)
        tree.column("Ataque", width=80)
        tree.column("Defensa", width=80)
        
        # Insertar datos
        for position, (username, total, attack, defense) in enumerate(ranking_data, 1):
            tree.insert("", tk.END, values=(position, username, total, attack, defense))
        
        tree.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # Scrollbar
        scrollbar = ttk.Scrollbar(parent, orient=tk.VERTICAL, command=tree.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        tree.configure(yscroll=scrollbar.set)
