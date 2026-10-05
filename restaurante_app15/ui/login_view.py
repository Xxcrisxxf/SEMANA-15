import os
import math
from pathlib import Path
import tkinter as tk
from tkinter import ttk

class LoginView(ttk.Frame):
    def __init__(self, parent, restaurante_servicio, on_login_success):
        super().__init__(parent)
        self.restaurante_servicio = restaurante_servicio
        self.on_login_success = on_login_success
        self.logo_image = None
        self._crear_componentes()

    def _crear_componentes(self):
        card = ttk.LabelFrame(self, text=" Acceso al Sistema de Restaurante ", padding=20)
        card.place(relx=0.5, rely=0.5, anchor="center")

        ruta_logo = str(Path(__file__).resolve().parents[1] / "assets" / "logo.png")
        if os.path.exists(ruta_logo):
            try:
                imagen = tk.PhotoImage(file=ruta_logo)
                escala = max(1, math.ceil(max(imagen.width(), imagen.height()) / 110))
                self.logo_image = imagen.subsample(escala, escala)
                lbl_logo = ttk.Label(card, image=self.logo_image)
                lbl_logo.grid(row=0, column=0, columnspan=2, pady=(0, 18))
            except Exception:
                pass

        ttk.Label(card, text="ID de Usuario:").grid(row=1, column=0, sticky="w", pady=5)
        self.ent_usuario = ttk.Entry(card, width=25)
        self.ent_usuario.grid(row=1, column=1, pady=5)

        ttk.Label(card, text="Contraseña:").grid(row=2, column=0, sticky="w", pady=5)
        self.ent_clave = ttk.Entry(card, show="*", width=25)
        self.ent_clave.grid(row=2, column=1, pady=5)

        self.lbl_mensaje = ttk.Label(card, text="", foreground="red")
        self.lbl_mensaje.grid(row=3, column=0, columnspan=2, pady=5)

        btn_ingresar = ttk.Button(card, text="Ingresar", command=self._ejecutar_login)
        btn_ingresar.grid(row=4, column=0, columnspan=2, pady=10)

    def _ejecutar_login(self):
        usr = self.ent_usuario.get()
        clave = self.ent_clave.get()

        if not usr or not clave:
            self.lbl_mensaje.config(text="Por favor complete todos los campos.")
            return

        if self.restaurante_servicio.validar_acceso(usr, clave):
            self.lbl_mensaje.config(text="")
            self.ent_usuario.delete(0, tk.END)
            self.ent_clave.delete(0, tk.END)
            self.on_login_success()
        else:
            self.lbl_mensaje.config(text="Credenciales incorrectas.")
