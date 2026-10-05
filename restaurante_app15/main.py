import os
from pathlib import Path
from tkinter import ttk, messagebox
import tkinter as tk
from servicios.archivo_servicio import ArchivoServicio
from servicios.restaurante_servicio import RestauranteServicio
from ui.login_view import LoginView
from ui.main_view import MainView

class RestauranteApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Restaurante")
        self.root.geometry("1100x680")
        self.root.minsize(1000, 650)

        estilo = ttk.Style(self.root)
        estilo.theme_use("clam")
        estilo.configure("TFrame", background="#f3f5f7")
        estilo.configure("TLabel", background="#f3f5f7", font=("Arial", 10))
        estilo.configure("TLabelframe", background="#f3f5f7")
        estilo.configure("TLabelframe.Label", background="#f3f5f7", font=("Arial", 10, "bold"))
        estilo.configure("TButton", font=("Arial", 10), padding=(10, 7))
        estilo.configure("TEntry", padding=5)
        estilo.configure("TCombobox", padding=5)
        estilo.configure("TNotebook.Tab", padding=(16, 8), font=("Arial", 10))
        estilo.configure("Treeview", rowheight=30, font=("Arial", 10))
        estilo.configure("Treeview.Heading", font=("Arial", 10, "bold"), padding=6)
        estilo.map("Treeview", background=[("selected", "#235789")])

        ruta_ico = str(Path(__file__).resolve().parent / "assets" / "logo.png")
        if os.path.exists(ruta_ico):
            try:
                img_ico = tk.PhotoImage(file=ruta_ico)
                self.root.iconphoto(False, img_ico)
            except Exception:
                pass

        self.archivo_servicio = ArchivoServicio()
        self.restaurante_servicio = RestauranteServicio(self.archivo_servicio)

        self.container = tk.Frame(self.root)
        self.container.pack(fill="both", expand=True)

        self.login_view = LoginView(self.container, self.restaurante_servicio, self.mostrar_main_view)
        self.main_view = MainView(self.container, self.restaurante_servicio, self.mostrar_login_view)

        # Iniciar mostrando el Login
        self.mostrar_login_view()

    def mostrar_login_view(self):
        self.main_view.pack_forget()
        self.login_view.pack(fill="both", expand=True)

    def mostrar_main_view(self):
        self.login_view.pack_forget()
        self.main_view.cargar_datos()
        self.main_view.pack(fill="both", expand=True)

def main():
    root = tk.Tk()
    try:
        app = RestauranteApp(root)
    except (OSError, ValueError) as error:
        root.withdraw()
        messagebox.showerror("No se pudo iniciar", str(error))
        root.destroy()
        return
    root.mainloop()

if __name__ == "__main__":
    main()
