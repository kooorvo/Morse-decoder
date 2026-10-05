import customtkinter as ctk

from encoder import encode
from decoder import decode

"""
menu = input(f"Voulez-vous (entrer le numéro): \n"
"1. Encoder \n"
"2. Décoder\n")

if menu == "1":
    print(encode())
elif menu == "2":
    print(decode())
else:
    print("Ce choix n'existe pas")

"""


# <--- UI --->

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Morse decoder")
        self.geometry("625x425")

        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # -- Side bar --

        self.sidebar_frame = ctk.CTkFrame(self, width=150, corner_radius=10)
        self.sidebar_frame.grid(row=0, column=0, padx=(10,0), pady=10, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(3, weight=1)

        self.logo = ctk.CTkLabel(self.sidebar_frame, text="Morse-decoder", font=ctk.CTkFont(size=20, weight="bold"))
        self.logo.grid(row=0, column=0, padx=20, pady=(20, 10))

        self.encodeBtn = ctk.CTkButton(self.sidebar_frame, text="Encoder", command=self.afficherEncode)
        self.encodeBtn.grid(row=1, column=0, pady=20)

        self.decodeBtn = ctk.CTkButton(self.sidebar_frame, text="Décoder", command=self.afficherDecode)
        self.decodeBtn.grid(row=2, column=0)

        # -- Main frame --

        self.main_frame = ctk.CTkFrame(self, corner_radius=10)
        self.main_frame.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

        self.afficherEncode()

    def nettoyer_main_frame(self):
        for widget in self.main_frame.winfo_children():
            widget.destroy()

    def afficherEncode(self):
        self.nettoyer_main_frame()

        titre = ctk.CTkLabel(self.main_frame, text="Encoder", font=ctk.CTkFont(size=18, weight="bold"))
        titre.pack(pady=20)

        self.encodeInput = ctk.CTkEntry(self.main_frame, placeholder_text="Alphanumérique vers Morse", width=300, height=50)
        self.encodeInput.pack(pady=10)

        self.confirmEncode = ctk.CTkButton(self.main_frame, text="Confirmer", command=self.encoder, width=300, height=50)
        self.confirmEncode.pack(pady=10)

        self.resultEncode = ctk.CTkLabel(self.main_frame, text="", font=ctk.CTkFont(size=18))
        self.resultEncode.pack(pady=10)

    def afficherDecode(self):
        self.nettoyer_main_frame()

        titre = ctk.CTkLabel(self.main_frame, text="Décoder", font=ctk.CTkFont(size=18, weight="bold"))
        titre.pack(pady=20)

        self.decodeInput = ctk.CTkEntry(self.main_frame, placeholder_text="Morse vers Alphanumérique", width=300, height=50)
        self.decodeInput.pack(pady=10)

        self.confirmDecode = ctk.CTkButton(self.main_frame, text="Confirmer", command=self.decoder, width=300, height=50)
        self.confirmDecode.pack(pady=10)

        self.resultDecode = ctk.CTkLabel(self.main_frame, text="", font=ctk.CTkFont(size=18))
        self.resultDecode.pack(pady=10)

    def encoder(self):
        inputValue = self.encodeInput.get()
        result = encode(inputValue)

        self.resultEncode.configure(text=result)
    
    def decoder(self):
        inputValue = self.decodeInput.get()
        result = decode(inputValue)

        self.resultDecode.configure(text=result)

app = App()
app.mainloop()

... .- .-.. ..- - / .--- . / -- .- .--. .--. . .-.. .-.. . / -. .- - .... .- -. / . - / .--- . / -.-. --- -.. . / ..- -. / .--. .-. --- --. .-. .- -- -- . / --.- ..- .. / - .-. .- -.. ..- .. - / .-.. . / -- --- .-. ... .