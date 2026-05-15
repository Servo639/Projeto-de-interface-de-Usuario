import tkinter as tk
from tkinter import ttk

class SearchApp(tk.Tk):
    def __init__(self):
        super().__init__()

        # Configurações da janela
        self.title("Google Gamer")
        self.geometry("900x600")
        self.configure(bg="#0d0d0d")
        self.minsize(500, 400)

        # Container principal
        main_frame = tk.Frame(self, bg="#0d0d0d")
        main_frame.place(relx=0.5, rely=0.5, anchor="center")

        # ===== TÍTULO ESTILO GAME =====
        title_frame = tk.Frame(main_frame, bg="#0d0d0d")
        title_frame.pack(pady=(0, 40))

        colors = [
            "#00ffff", "#ff00ff", "#00ff00", "#ff00ff", "#00ff00", "#ffea00", "#00ffff", "#ff00ff", "#ffea00"]

        text = "Gameouver"

        for i, char in enumerate(text):
            tk.Label(
                title_frame,
                text=char,
                font=("Orbitron", 60, "bold"),
                fg=colors[i],
                bg="#0d0d0d"
            ).pack(side="left")

        # ===== BARRA DE PESQUISA =====
        search_frame = tk.Frame(
            main_frame,
            bg="#1a1a1a",
            bd=2,
            relief="solid",
            highlightbackground="#00ffff",
            highlightthickness=2
        )
        search_frame.pack(ipadx=10, ipady=8)

        # Ícone lupa
        search_icon = tk.Label(
            search_frame,
            text="🔍",
            bg="#1a1a1a",
            fg="#00ffff",
            font=("Arial", 16)
        )
        search_icon.pack(side="left", padx=(10, 5))

        # Placeholder
        self.placeholder_text = "Digite sua dúvida gamer..."
        self.search_var = tk.StringVar()

        self.search_entry = tk.Entry(
            search_frame,
            textvariable=self.search_var,
            font=("Consolas", 16),
            width=40,
            bd=0,
            bg="#1a1a1a",
            fg="gray",
            insertbackground="#00ffff",
            highlightthickness=0
        )

        self.search_entry.pack(side="left", padx=5, pady=5)
        self.search_entry.insert(0, self.placeholder_text)

        # Ícone microfone
        mic_icon = tk.Label(
            search_frame,
            text="🎮",
            bg="#1a1a1a",
            fg="#ff00ff",
            font=("Arial", 16)
        )
        mic_icon.pack(side="right", padx=(5, 10))

        # Eventos
        self.search_entry.bind("<FocusIn>", self.on_entry_click)
        self.search_entry.bind("<FocusOut>", self.on_focus_out)
        self.search_entry.bind("<Return>", self.perform_search)

        # ===== BOTÕES =====
        buttons_frame = tk.Frame(main_frame, bg="#0d0d0d")
        buttons_frame.pack(pady=35)

        style_button = {
            "font": ("Orbitron", 11, "bold"),
            "bg": "#111111",
            "fg": "#00ffff",
            "activebackground": "#222222",
            "activeforeground": "#ff00ff",
            "relief": "flat",
            "padx": 20,
            "pady": 10,
            "cursor": "hand2",
            "bd": 2
        }

        search_button = tk.Button(
            buttons_frame,
            text="Pesquisar",
            command=self.perform_search,
            **style_button
        )
        search_button.pack(side="left", padx=15)

        lucky_button = tk.Button(
            buttons_frame,
            text="Modo Pro",
            **style_button
        )
        lucky_button.pack(side="left", padx=15)

        # ===== TEXTO INFERIOR =====
        footer = tk.Label(
            main_frame,
            text="⚡ Powered by Gamer Search Engine ⚡",
            font=("Consolas", 12),
            fg="#666666",
            bg="#0d0d0d"
        )
        footer.pack(pady=(20, 0))

    def on_entry_click(self, event):
        if self.search_entry.get() == self.placeholder_text:
            self.search_entry.delete(0, tk.END)
            self.search_entry.config(fg="#00ffff")

    def on_focus_out(self, event):
        if self.search_entry.get() == "":
            self.search_entry.insert(0, self.placeholder_text)
            self.search_entry.config(fg="gray")

    def perform_search(self, event=None):
        query = self.search_entry.get()

        if query and query != self.placeholder_text:
            print(f"🎮 Buscando por: {query}")

if __name__ == "__main__":
    app = SearchApp()
    app.mainloop()