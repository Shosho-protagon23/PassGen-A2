import tkinter as tk
from tkinter import messagebox
import re
import random
import string

class SecurityTool:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Strength & Gen")
        self.root.geometry("500x550")
        self.root.configure(bg="#1a1a1a")

        # --- SECTION 1: STRENGTH CHECKER ---
        self.check_frame = tk.LabelFrame(root, text=" 1. Cek Kekuatan Password ", 
                                         font=("Arial", 12, "bold"), bg="#1a1a1a", fg="#00ffcc", bd=2)
        self.check_frame.pack(pady=15, padx=20, fill="x")

        tk.Label(self.check_frame, text="Masukkan Password:", bg="#1a1a1a", fg="white").pack(pady=5)
        
        # Binding event 'KeyRelease' agar pengecekan terjadi real-time saat mengetik
        self.pass_input = tk.Entry(self.check_frame, font=("Arial", 12), show="*")
        self.pass_input.pack(pady=5, ipadx=10, ipady=3)
        self.pass_input.bind('<KeyRelease>', self.check_strength)

        # Indikator Visual (Bar & Text)
        self.lbl_result = tk.Label(self.check_frame, text="Menunggu Input...", 
                                   font=("Arial", 11, "bold"), bg="#1a1a1a", fg="gray")
        self.lbl_result.pack(pady=10)

        # --- SECTION 2: PASSWORD GENERATOR ---
        self.gen_frame = tk.LabelFrame(root, text=" 2. Buat Password Baru ", 
                                       font=("Arial", 12, "bold"), bg="#1a1a1a", fg="#ffcc00", bd=2)
        self.gen_frame.pack(pady=15, padx=20, fill="x")

        tk.Label(self.gen_frame, text="Panjang Password:", bg="#1a1a1a", fg="white").pack(pady=5)
        self.scale_len = tk.Scale(self.gen_frame, from_=8, to=32, orient="horizontal", 
                                  bg="#1a1a1a", fg="white", highlightthickness=0)
        self.scale_len.set(16) # Default 16
        self.scale_len.pack(fill="x", padx=40)

        btn_gen = tk.Button(self.gen_frame, text="GENERATE RANDOM", bg="#ffcc00", fg="black", 
                            font=("Arial", 10, "bold"), command=self.generate_password)
        btn_gen.pack(pady=10)

        self.entry_generated = tk.Entry(self.gen_frame, font=("Consolas", 14), justify="center", bg="#333", fg="#ffcc00")
        self.entry_generated.pack(pady=10, fill="x", padx=20)

        btn_copy = tk.Button(self.gen_frame, text="Copy Result", bg="#444", fg="white", command=self.copy_pass)
        btn_copy.pack(pady=5)

    def check_strength(self, event=None):
        password = self.pass_input.get()
        score = 0
        feedback = []

        if not password:
            self.lbl_result.config(text="Menunggu Input...", fg="gray")
            return

        # --- LOGIKA REGEX (Regular Expression) ---
        
        # 1. Cek Panjang
        if len(password) >= 8: score += 1
        if len(password) >= 12: score += 1 # Bonus panjang

        # 2. Cek Komplesitas menggunakan ReGex
        if re.search(r"[a-z]", password): score += 1       # Ada huruf kecil
        if re.search(r"[A-Z]", password): score += 1       # Ada huruf besar
        if re.search(r"[0-9]", password): score += 1       # Ada angka
        if re.search(r"[\W_]", password): score += 1       # Ada simbol (non-alphanumeric)

        # Total Skor Maksimal: 6
        
        # --- PENENTUAN STATUS ---
        if score < 3:
            status = "LEMAH (Weak)"
            color = "#ff4d4d" # Merah
        elif score < 5:
            status = "SEDANG (Medium)"
            color = "#ffbb33" # Oranye
        else:
            status = "KUAT (Strong)"
            color = "#00C851" # Hijau

        self.lbl_result.config(text=f"{status}", fg=color)

    def generate_password(self):
        length = self.scale_len.get()
        # Menggunakan kombinasi lengkap untuk generator
        chars = string.ascii_letters + string.digits + string.punctuation
        
        # Acak password
        password = "".join(random.choice(chars) for _ in range(length))
        
        self.entry_generated.delete(0, tk.END)
        self.entry_generated.insert(0, password)

        # Opsional: Langsung cek kekuatan password yang baru digenerate
        # self.pass_input.delete(0, tk.END)
        # self.pass_input.insert(0, password)
        # self.check_strength()

    def copy_pass(self):
        pw = self.entry_generated.get()
        if pw:
            self.root.clipboard_clear()
            self.root.clipboard_append(pw)
            messagebox.showinfo("Copied", "Password tersalin ke clipboard!")

if __name__ == "__main__":
    root = tk.Tk()
    app = SecurityTool(root)
    root.mainloop()