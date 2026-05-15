import tkinter as tk
from tkinter import messagebox

class RemBeautyApp(tk.Tk):
    def __init__(self):
        super().__init__()

        # Configurações da Janela
        self.title("Campeonato de Jogos - experience")
        self.geometry("800x600")
        self.configure(bg="#000000") # Fundo lilás/gelo bem suave (ethereal)
        self.resizable(False, False)
        
        # Paleta de Cores (Interstellar / Minimalist)
        self.bg_color = "#000000"
        self.fg_color = "#6200FF" # Cinza escuro para texto (mais suave que o preto puro)
        self.accent_color = "#FF00EA" # Lilás (Lavender) característico
        self.btn_active = "#8E7BAE" # Lilás um pouco mais escuro para o hover
        self.input_bg = "#686868"
        self.border_color = "#D5CDDF"
        
        # Fontes (usando Helvetica para simular a tipografia minimalista)
        self.font_normal = ("Helvetica", 11)
        
        self.create_widgets()

    def create_widgets(self):
        # --- CABEÇALHO ---
        header_frame = tk.Frame(self, bg=self.bg_color)
        header_frame.pack(fill="x", pady=(70, 30))
        
        # Título estilo r.e.m. beauty (minúsculo, clean)
        title = tk.Label(header_frame, text="Campeonato de Jogos", 
                         font=("Helvetica", 42, "bold"), bg=self.bg_color, fg=self.fg_color)
        title.pack()
        
        subtitle = tk.Label(header_frame, text="Seja o primeiro a conquistar a copa Pistan", 
                            font=("Helvetica", 14), bg=self.bg_color, fg=self.accent_color)
        subtitle.pack()

        # --- CONTAINER PRINCIPAL (Exemplo de Newsletter/Login) ---
        main_frame = tk.Frame(self, bg=self.bg_color)
        main_frame.pack(expand=True, fill="both", padx=150, pady=10)
        
        # Texto de chamada
        lbl_call = tk.Label(main_frame, text="Junte-se a nossa equipe", 
                            font=("Helvetica", 16), bg=self.bg_color, fg=self.fg_color)
        lbl_call.pack(pady=(0, 25))

        # Função auxiliar para criar inputs padronizados, estilo flat
        def create_input(parent, label_text):
            frame = tk.Frame(parent, bg=self.bg_color)
            frame.pack(fill="x", pady=10, padx=50)
            
            lbl = tk.Label(frame, text=label_text, font=self.font_normal, bg=self.bg_color, fg=self.fg_color)
            lbl.pack(anchor="w", pady=(0, 5))
            
            # Campo de entrada (bordas finas e cores minimalistas)
            entry = tk.Entry(frame, font=("Helvetica", 13), bg=self.input_bg, fg=self.fg_color, 
                             insertbackground=self.accent_color, relief="flat", highlightthickness=1, 
                             highlightbackground=self.border_color, highlightcolor=self.accent_color)
            entry.pack(fill="x", ipady=8)
            
            return entry

        self.ent_nome = create_input(main_frame, "ID:")
        self.ent_email = create_input(main_frame, "Discord:")

        # --- BOTÃO DE AÇÃO ---
        btn_frame = tk.Frame(main_frame, bg=self.bg_color)
        btn_frame.pack(fill="x", pady=(35, 0), padx=50)
        
        # Efeitos de Hover no botão para interatividade (UX)
        def on_enter(e):
            self.btn_submit.config(bg=self.btn_active)
            
        def on_leave(e):
            self.btn_submit.config(bg=self.accent_color)

        self.btn_submit = tk.Button(btn_frame, text="inscrever-se", font=("Helvetica", 12, "bold"), 
                                       bg=self.accent_color, fg="#000000", activebackground=self.btn_active, activeforeground="#FF0000",
                                       relief="flat", cursor="hand2", command=self.submit)
        self.btn_submit.pack(fill="x", ipady=12)
        
        self.btn_submit.bind("<Enter>", on_enter)
        self.btn_submit.bind("<Leave>", on_leave)

        # --- RODAPÉ ---
        footer = tk.Label(self, text="© 2026 r.e.m. beauty inspired. out of this world.", 
                          font=("Helvetica", 9), bg=self.bg_color, fg="#AFAFAF")
        footer.pack(side="bottom", pady=30)

    def submit(self):
        nome = self.ent_nome.get()
        email = self.ent_email.get()
        
        if not nome or not email:
            # Caixa de mensagem também com textos minúsculos para manter a vibe
            messagebox.showwarning("ops", "por favor, preencha todos os campos.", parent=self)
            return
            
        messagebox.showinfo("bem-vindo(a) ao espaço", f"obrigado por se juntar a nós, {nome}!\nem breve você receberá novidades em {email}.", parent=self)
        
        self.ent_nome.delete(0, tk.END)
        self.ent_email.delete(0, tk.END)
        self.ent_nome.focus()

if __name__ == "__main__":
    app = RemBeautyApp()
    app.mainloop()
