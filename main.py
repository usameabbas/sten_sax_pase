import tkinter as tk
from tkinter import messagebox
from game_logic import StenSaxPase

class StenSaxPaseGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Sten-Sax-Påse")
        self.game = StenSaxPase()

        # GUI Element
        self.label = tk.Label(root, text="Välj sten, sax eller påse!", font=("Arial", 14))
        self.label.pack(pady=20)

        # Knappar
        self.sten_btn = tk.Button(root, text="Sten", command=lambda: self.spela("sten"), width=10)
        self.sax_btn = tk.Button(root, text="Sax", command=lambda: self.spela("sax"), width=10)
        self.påse_btn = tk.Button(root, text="Påse", command=lambda: self.spela("påse"), width=10)
        
        self.sten_btn.pack(pady=5)
        self.sax_btn.pack(pady=5)
        self.påse_btn.pack(pady=5)

        # Poängvisare
        self.poäng_label = tk.Label(root, text="Poäng: Spelare 0 - 0 Datorn", font=("Arial", 12))
        self.poäng_label.pack(pady=20)

    def spela(self, val):
        datorns_val = self.game.datorns_val()
        resultat = self.game.avgör_vinnare(val, datorns_val)
        
        # Visa resultat
        messagebox.showinfo("Resultat", f"Du valde {val}\nDatorn valde {datorns_val}\n\n{resultat}")
        
        # Uppdatera poäng
        self.poäng_label.config(text=f"Poäng: Spelare {self.game.spelarens_poäng} - {self.game.datorns_poäng} Datorn")

if __name__ == "__main__":
    root = tk.Tk()
    app = StenSaxPaseGUI(root)
    root.mainloop()