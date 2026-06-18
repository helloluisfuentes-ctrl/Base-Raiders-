import tkinter as tk
from tkinter import ttk, messagebox
from file_manager import get_all_players, register_player, login_player, player_exists
import constants
from ui_functions import start_plan_defense, hide_main_menu


class PlayerSelectionWindow:
    """Ventana para seleccionar jugadores atacante y defensor."""
    
    def __init__(self, parent_root):
        self.root = parent_root
        self.window = tk.Toplevel(parent_root)
        self.window.title("Seleccionar Jugadores")
        self.window.geometry("700x600")
        self.window.resizable(True, True)
        
        self.attacker_selected = None
        self.defender_selected = None
        
        self.create_widgets()
        self.load_player_list()
    
    def create_widgets(self):
        """Crea todos los elementos de la interfaz."""
        
        # Título
        title_label = tk.Label(
            self.window,
            text="Seleccionar Jugadores",
            font=("Arial", 20, "bold")
        )
        title_label.pack(pady=10)
        
        # ===== ATACANTE =====
        attacker_frame = tk.LabelFrame(
            self.window,
            text="Atacante",
            font=("Arial", 12, "bold"),
            padx=10,
            pady=10
        )
        attacker_frame.pack(padx=20, pady=10, fill=tk.X)
        
        self.attacker_combo = ttk.Combobox(
            attacker_frame,
            width=35,
            state="readonly",
            font=("Arial", 11)
        )
        self.attacker_combo.pack(pady=5)
        
        self.attacker_status = tk.Label(
            attacker_frame,
            text="No seleccionado",
            font=("Arial", 10),
            fg="red"
        )
        self.attacker_status.pack()
        
        attacker_btn_frame = tk.Frame(attacker_frame)
        attacker_btn_frame.pack(pady=5)
        
        confirm_attacker_btn = tk.Button(
            attacker_btn_frame,
            text="Confirmar Atacante",
            font=("Arial", 10),
            command=self.confirm_attacker,
            bg="lightgreen"
        )
        confirm_attacker_btn.pack(side=tk.LEFT, padx=5)
        
        # ===== DEFENSOR =====
        defender_frame = tk.LabelFrame(
            self.window,
            text="Defensor",
            font=("Arial", 12, "bold"),
            padx=10,
            pady=10
        )
        defender_frame.pack(padx=20, pady=10, fill=tk.X)
        
        self.defender_combo = ttk.Combobox(
            defender_frame,
            width=35,
            state="readonly",
            font=("Arial", 11)
        )
        self.defender_combo.pack(pady=5)
        
        self.defender_status = tk.Label(
            defender_frame,
            text="No seleccionado",
            font=("Arial", 10),
            fg="red"
        )
        self.defender_status.pack()
        
        defender_btn_frame = tk.Frame(defender_frame)
        defender_btn_frame.pack(pady=5)
        
        confirm_defender_btn = tk.Button(
            defender_btn_frame,
            text="Confirmar Defensor",
            font=("Arial", 10),
            command=self.confirm_defender,
            bg="lightblue"
        )
        confirm_defender_btn.pack(side=tk.LEFT, padx=5)
        
        # ===== CREAR NUEVO JUGADOR =====
        create_player_frame = tk.LabelFrame(
            self.window,
            text="Crear Nuevo Jugador",
            font=("Arial", 12, "bold"),
            padx=10,
            pady=10
        )
        create_player_frame.pack(padx=20, pady=10, fill=tk.X)
        
        nickname_label = tk.Label(create_player_frame, text="Nombre de usuario:", font=("Arial", 10))
        nickname_label.pack(anchor=tk.W)
        
        self.nickname_entry = tk.Entry(create_player_frame, font=("Arial", 10), width=30)
        self.nickname_entry.pack()
        
        password_label = tk.Label(create_player_frame, text="Contraseña:", font=("Arial", 10))
        password_label.pack(anchor=tk.W)
        
        self.password_entry = tk.Entry(create_player_frame, font=("Arial", 10), width=30, show="*")
        self.password_entry.pack()
        
        create_btn = tk.Button(
            create_player_frame,
            text="Registrar",
            font=("Arial", 10),
            command=self.create_new_player,
            bg="yellow"
        )
        create_btn.pack(pady=5)
        
        # ===== BOTONES INFERIORES =====
        button_frame = tk.Frame(self.window)
        button_frame.pack(pady=10)
        
        play_btn = tk.Button(
            button_frame,
            text="PLAY",
            font=("Arial", 14, "bold"),
            command=self.start_game,
            bg="green",
            fg="white",
            width=15
        )
        play_btn.pack(side=tk.LEFT, padx=5)
        
        cancel_btn = tk.Button(
            button_frame,
            text="Cancelar",
            font=("Arial", 14),
            command=self.window.destroy,
            bg="red",
            fg="white",
            width=15
        )
        cancel_btn.pack(side=tk.LEFT, padx=5)
    
    def load_player_list(self):
        """Carga la lista de jugadores en los combobox."""
        players = get_all_players()
        self.attacker_combo['values'] = players
        self.defender_combo['values'] = players
    
    def confirm_attacker(self):
        """Confirma la selección del atacante."""
        if not self.attacker_combo.get():
            messagebox.showwarning("Error", "Debes seleccionar un atacante")
            return
        
        self.attacker_selected = self.attacker_combo.get()
        self.attacker_status.config(text=f"✓ {self.attacker_selected} confirmado", fg="green")
    
    def confirm_defender(self):
        """Confirma la selección del defensor."""
        if not self.defender_combo.get():
            messagebox.showwarning("Error", "Debes seleccionar un defensor")
            return
        
        self.defender_selected = self.defender_combo.get()
        self.defender_status.config(text=f"✓ {self.defender_selected} confirmado", fg="green")
    
    def create_new_player(self):
        """Crea un nuevo jugador."""
        nickname = self.nickname_entry.get().strip()
        password = self.password_entry.get()
        
        if not nickname or not password:
            messagebox.showerror("Error", "Debes ingresar nombre de usuario y contraseña")
            return
        
        if player_exists(nickname):
            messagebox.showerror("Error", "El jugador ya existe")
            return
        
        if register_player(nickname, password):
            messagebox.showinfo("Éxito", f"Jugador '{nickname}' registrado correctamente")
            self.nickname_entry.delete(0, tk.END)
            self.password_entry.delete(0, tk.END)
            self.load_player_list()
        else:
            messagebox.showerror("Error", "No se pudo registrar el jugador")
    
    def start_game(self):
        """Inicia el juego con los jugadores seleccionados."""
        if not self.attacker_selected:
            messagebox.showerror("Error", "Debes confirmar un atacante")
            return
        
        if not self.defender_selected:
            messagebox.showerror("Error", "Debes confirmar un defensor")
            return
        
        if self.attacker_selected == self.defender_selected:
            messagebox.showerror("Error", "El atacante y defensor deben ser diferentes")
            return
        
        # Guardar jugadores en constantes globales
        constants.current_attacker = self.attacker_selected
        constants.current_defender = self.defender_selected
        constants.attacker_money = constants.INITIAL_MONEY
        constants.defender_money = constants.INITIAL_MONEY
        
        # Cerrar ventana de selección
        self.window.destroy()
        
        # Ocultar menú principal y iniciar juego
        hide_main_menu()
        start_plan_defense()
