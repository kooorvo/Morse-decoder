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

        self.title("Pymodoro")
        self.geometry("525x425")

        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # -- Side bare --

        self.sidebar_frame = ctk.CTkFrame(self, width=150, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(2, weight=1)

        self.logo = ctk.CTkLabel(self.sidebar_frame, text="Morse-decoder", font=ctk.CTkFont(size=20, weight="bold"))
        self.logo.grid(row=0, column=0, padx=20, pady=(20, 10))

app = App()
app.mainloop()