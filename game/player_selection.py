import tkinter as tk
from tkinter import ttk, messagebox
from file_manager import get_all_players, login_player
import constants
from ui_functions import start_plan_defense, hide_main_menu


class PlayerSelectionWindow:
    """Ventana para elegir jugadores registrados, rol y faccion."""

    def __init__(self, parent_root):
        self.root = parent_root
        self.window = tk.Toplevel(parent_root)
        self.window.title("Elegir jugadores")
        self.window.geometry("760x430")
        self.window.resizable(False, False)

        self.attacker_selected = None
        self.defender_selected = None

        self.create_widgets()
        self.load_player_list()

    def create_widgets(self):
        tk.Label(
            self.window,
            text="Elegir atacante y defensor",
            font=("Arial", 22, "bold")
        ).pack(pady=14)

        content = tk.Frame(self.window)
        content.pack(padx=18, pady=8, fill=tk.BOTH, expand=True)

        attacker_frame = self.create_role_frame(content, "Atacante")
        attacker_frame.grid(row=0, column=0, padx=10, sticky="nsew")

        defender_frame = self.create_role_frame(content, "Defensor")
        defender_frame.grid(row=0, column=1, padx=10, sticky="nsew")

        content.columnconfigure(0, weight=1)
        content.columnconfigure(1, weight=1)

        self.attacker_combo, self.attacker_password_entry, self.attacker_faction_combo, self.attacker_status = self.create_role_inputs(
            attacker_frame, 0
        )
        self.defender_combo, self.defender_password_entry, self.defender_faction_combo, self.defender_status = self.create_role_inputs(
            defender_frame, 1
        )

        tk.Button(
            attacker_frame,
            text="Confirmar atacante",
            font=("Arial", 11, "bold"),
            command=self.confirm_attacker,
            bg="lightgreen",
            width=20
        ).pack(pady=10)

        tk.Button(
            defender_frame,
            text="Confirmar defensor",
            font=("Arial", 11, "bold"),
            command=self.confirm_defender,
            bg="lightblue",
            width=20
        ).pack(pady=10)

        bottom = tk.Frame(self.window)
        bottom.pack(pady=14)

        tk.Button(
            bottom,
            text="PLAY",
            font=("Arial", 15, "bold"),
            command=self.start_game,
            bg="green",
            fg="white",
            width=16
        ).pack(side=tk.LEFT, padx=8)

        tk.Button(
            bottom,
            text="Cancelar",
            font=("Arial", 15),
            command=self.window.destroy,
            bg="red",
            fg="white",
            width=16
        ).pack(side=tk.LEFT, padx=8)

    def create_role_frame(self, parent, title):
        return tk.LabelFrame(
            parent,
            text=title,
            font=("Arial", 13, "bold"),
            padx=18,
            pady=14
        )

    def create_role_inputs(self, parent, faction_index):
        tk.Label(parent, text="Jugador registrado:", font=("Arial", 10)).pack(anchor=tk.W)
        player_combo = ttk.Combobox(parent, width=30, state="readonly", font=("Arial", 11))
        player_combo.pack(pady=5)

        tk.Label(parent, text="Contrasena:", font=("Arial", 10)).pack(anchor=tk.W)
        password_entry = tk.Entry(parent, font=("Arial", 11), width=30, show="*")
        password_entry.pack(pady=5)

        tk.Label(parent, text="Faccion:", font=("Arial", 10)).pack(anchor=tk.W)
        faction_combo = ttk.Combobox(
            parent,
            width=30,
            state="readonly",
            font=("Arial", 11),
            values=list(constants.FACTIONS.keys())
        )
        faction_combo.current(faction_index)
        faction_combo.pack(pady=5)

        status = tk.Label(parent, text="No confirmado", font=("Arial", 10), fg="red")
        status.pack(pady=5)

        return player_combo, password_entry, faction_combo, status

    def load_player_list(self):
        players = get_all_players()
        self.attacker_combo["values"] = players
        self.defender_combo["values"] = players

    def confirm_attacker(self):
        if not self.attacker_combo.get():
            messagebox.showwarning("Error", "Debes seleccionar un atacante")
            return
        if not login_player(self.attacker_combo.get(), self.attacker_password_entry.get()):
            messagebox.showerror("Error", "Contrasena incorrecta para el atacante")
            return

        self.attacker_selected = self.attacker_combo.get()
        self.attacker_status.config(text=f"{self.attacker_selected} confirmado", fg="green")

    def confirm_defender(self):
        if not self.defender_combo.get():
            messagebox.showwarning("Error", "Debes seleccionar un defensor")
            return
        if not login_player(self.defender_combo.get(), self.defender_password_entry.get()):
            messagebox.showerror("Error", "Contrasena incorrecta para el defensor")
            return

        self.defender_selected = self.defender_combo.get()
        self.defender_status.config(text=f"{self.defender_selected} confirmado", fg="green")

    def start_game(self):
        if not self.attacker_selected:
            messagebox.showerror("Error", "Debes confirmar un atacante")
            return
        if not self.defender_selected:
            messagebox.showerror("Error", "Debes confirmar un defensor")
            return
        if self.attacker_selected == self.defender_selected:
            messagebox.showerror("Error", "El atacante y defensor deben ser diferentes")
            return
        if self.attacker_faction_combo.get() == self.defender_faction_combo.get():
            messagebox.showerror("Error", "El atacante y defensor no pueden usar la misma faccion")
            return

        constants.current_attacker = self.attacker_selected
        constants.current_defender = self.defender_selected
        constants.attacker_faction = self.attacker_faction_combo.get()
        constants.defender_faction = self.defender_faction_combo.get()
        constants.attacker_round_wins = 0
        constants.defender_round_wins = 0
        constants.round_number = 1
        constants.attacker_money = constants.INITIAL_MONEY
        constants.defender_money = constants.INITIAL_MONEY

        self.window.destroy()
        hide_main_menu()
        start_plan_defense()
