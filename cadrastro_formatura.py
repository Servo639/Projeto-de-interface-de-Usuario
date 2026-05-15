import tkinter as tk
from tkinter import ttk, messagebox

class AppComputacaoGame(tk.Tk):
    def __init__(self):
        super().__init__()

        # Janela
        self.title("GAME REGISTER")
        self.geometry("950x680")
        self.configure(bg="#050816")
        self.resizable(False, False)

        # Cores gamer/neon
        self.bg_color = "#050816"
        self.card_color = "#0B1023"
        self.accent = "#00FFAA"
        self.accent2 = "#8A2BE2"
        self.text = "#FFFFFF"
        self.muted = "#9CA3AF"
        self.input_bg = "#111827"

        # Estilo Combobox
        style = ttk.Style()
        style.theme_use("clam")

        style.configure(
            "TCombobox",
            fieldbackground=self.input_bg,
            background=self.card_color,
            foreground=self.text,
            bordercolor=self.accent,
            arrowcolor=self.accent,
            padding=8
        )

        self.create_widgets()

    def create_widgets(self):

        # TOPO
        top = tk.Frame(self, bg=self.bg_color)
        top.pack(fill="x", pady=(30, 10))

        titulo = tk.Label(
            top,
            text="⚡ GAME SYSTEM ⚡",
            font=("Orbitron", 28, "bold"),
            bg=self.bg_color,
            fg=self.accent
        )
        titulo.pack()

        subtitulo = tk.Label(
            top,
            text="CADASTRO DE JOGADORES",
            font=("Segoe UI", 14, "bold"),
            bg=self.bg_color,
            fg=self.text
        )
        subtitulo.pack(pady=5)

        linha = tk.Frame(top, bg=self.accent, height=3, width=250)
        linha.pack(pady=10)

        # CARD CENTRAL
        card = tk.Frame(
            self,
            bg=self.card_color,
            highlightbackground=self.accent,
            highlightthickness=2
        )

        card.pack(padx=90, pady=20, fill="both", expand=True)

        # Função inputs
        def criar_input(texto, row, col):

            lbl = tk.Label(
                card,
                text=texto,
                font=("Segoe UI", 10, "bold"),
                bg=self.card_color,
                fg=self.muted
            )

            lbl.grid(row=row, column=col, sticky="w", padx=20, pady=(20, 5))

            ent = tk.Entry(
                card,
                font=("Consolas", 13),
                bg=self.input_bg,
                fg=self.accent,
                insertbackground=self.accent,
                relief="flat",
                highlightthickness=2,
                highlightbackground=self.accent2,
                highlightcolor=self.accent,
                width=28
            )

            ent.grid(row=row+1, column=col, padx=20, pady=5, ipady=10)

            return ent

        # Campos
        self.ent_nome = criar_input("PLAYER NAME", 0, 0)
        self.ent_ra = criar_input("ID PLAYER", 0, 1)

        self.ent_email = criar_input("E-MAIL", 2, 0)
        self.ent_telefone = criar_input("DISCORD / TELEFONE", 2, 1)

        # Classe gamer
        lbl_classe = tk.Label(
            card,
            text="CLASSE PRINCIPAL",
            font=("Segoe UI", 10, "bold"),
            bg=self.card_color,
            fg=self.muted
        )

        lbl_classe.grid(row=4, column=0, sticky="w", padx=20, pady=(20, 5))

        self.combo_classe = ttk.Combobox(
            card,
            values=[
                "Programador",
                "Cyber Security",
                "Game Developer",
                "Hacker Elite",
                "IA Developer"
            ],
            font=("Consolas", 12),
            state="readonly"
        )

        self.combo_classe.grid(row=5, column=0, padx=20, pady=5, sticky="we")
        self.combo_classe.set("Programador")

        # Grid
        card.columnconfigure(0, weight=1)
        card.columnconfigure(1, weight=1)

        # BOTÃO
        def entrar(e):
            self.btn.config(bg=self.accent, fg="#000000")

        def sair(e):
            self.btn.config(bg=self.accent2, fg="white")

        self.btn = tk.Button(
            self,
            text="INICIAR CADASTRO",
            font=("Orbitron", 14, "bold"),
            bg=self.accent2,
            fg="white",
            relief="flat",
            cursor="hand2",
            activebackground=self.accent,
            activeforeground="#000000",
            command=self.cadastrar
        )

        self.btn.pack(ipadx=40, ipady=15, pady=20)

        self.btn.bind("<Enter>", entrar)
        self.btn.bind("<Leave>", sair)

        # STATUS
        self.status = tk.Label(
            self,
            text="",
            font=("Consolas", 12),
            bg=self.bg_color,
            fg=self.accent
        )

        self.status.pack(pady=10)

    def cadastrar(self):

        nome = self.ent_nome.get()
        player = self.ent_ra.get()
        classe = self.combo_classe.get()

        if not nome or not player:
            messagebox.showwarning(
                "ERRO",
                "Preencha PLAYER NAME e ID PLAYER!"
            )
            return

        self.status.config(text="Carregando sistema...")
        self.update()
        self.after(700)

        self.status.config(
            text=f"✓ PLAYER {nome.upper()} REGISTRADO COMO {classe}"
        )

        # Limpar
        self.ent_nome.delete(0, tk.END)
        self.ent_ra.delete(0, tk.END)
        self.ent_email.delete(0, tk.END)
        self.ent_telefone.delete(0, tk.END)

        self.combo_classe.set("Programador")

if __name__ == "__main__":
    app = AppComputacaoGame()
    app.mainloop()