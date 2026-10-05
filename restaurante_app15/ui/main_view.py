import os
import math
from pathlib import Path
import tkinter as tk
from tkinter import ttk, messagebox

class MainView(ttk.Frame):
    def __init__(self, parent, restaurante_servicio, on_logout):
        super().__init__(parent)
        self.restaurante_servicio = restaurante_servicio
        self.on_logout = on_logout
        self.logo_image = None
        self.iconos = {}
        self._cargar_iconos()
        self._crear_componentes()

    def _cargar_iconos(self):
        archivos = {
            "registrar": "add.png",
            "consultar": "search.png",
            "actualizar": "edit.png",
            "eliminar": "delete.png"
        }
        for clave, nombre_archivo in archivos.items():
            ruta = str(Path(__file__).resolve().parents[1] / "assets" / nombre_archivo)
            if os.path.exists(ruta):
                try:
                    imagen = tk.PhotoImage(file=ruta)
                    escala = max(1, math.ceil(max(imagen.width(), imagen.height()) / 20))
                    self.iconos[clave] = imagen.subsample(escala, escala)
                except Exception:
                    self.iconos[clave] = None
            else:
                self.iconos[clave] = None

    def _cargar_logo(self, contenedor):
        ruta_logo = str(Path(__file__).resolve().parents[1] / "assets" / "logo.png")
        if os.path.exists(ruta_logo):
            try:
                img_temp = tk.PhotoImage(file=ruta_logo)
                self.logo_image = img_temp.subsample(8, 8) 
                lbl_logo = ttk.Label(contenedor, image=self.logo_image)
                lbl_logo.pack(side="left", padx=(0, 10))
            except Exception:
                pass

    def _crear_componentes(self):
        header = ttk.Frame(self, padding=10)
        header.pack(fill="x")

        self._cargar_logo(header)

        lbl_titulo = ttk.Label(header, text="Sistema de Restaurante — Panel de Control", font=("Arial", 16, "bold"))
        lbl_titulo.pack(side="left")

        btn_logout = ttk.Button(header, text="Cerrar Sesión", command=self.on_logout)
        btn_logout.pack(side="right")

        self.notebook = ttk.Notebook(self)
        self.notebook.pack(fill="both", expand=True, padx=10, pady=5)

        self.tab_productos = ttk.Frame(self.notebook, padding=10)
        self.notebook.add(self.tab_productos, text="Gestión de Productos")
        self._construir_tab_productos()

        self.tab_usuarios = ttk.Frame(self.notebook, padding=10)
        self.notebook.add(self.tab_usuarios, text="Consulta de Usuarios")
        self._construir_tab_usuarios()

        self.tab_ventas = ttk.Frame(self.notebook, padding=10)
        self.notebook.add(self.tab_ventas, text="Gestión de Ventas")
        self._construir_tab_ventas()

    def _construir_tab_productos(self):
        frame_izq = ttk.Frame(self.tab_productos, padding=5)
        frame_izq.pack(side="left", fill="y", padx=(0, 10))

        frm_datos = ttk.LabelFrame(frame_izq, text=" Formulario de Producto ", padding=10)
        frm_datos.pack(fill="x", pady=(0, 10))

        ttk.Label(frm_datos, text="Código:").grid(row=0, column=0, sticky="w", pady=3)
        self.ent_codigo = ttk.Entry(frm_datos, width=20)
        self.ent_codigo.grid(row=0, column=1, pady=3, padx=5)

        ttk.Label(frm_datos, text="Nombre:").grid(row=1, column=0, sticky="w", pady=3)
        self.ent_nombre = ttk.Entry(frm_datos, width=20)
        self.ent_nombre.grid(row=1, column=1, pady=3, padx=5)

        ttk.Label(frm_datos, text="Categoría:").grid(row=2, column=0, sticky="w", pady=3)
        self.ent_categoria = ttk.Entry(frm_datos, width=20)
        self.ent_categoria.grid(row=2, column=1, pady=3, padx=5)

        ttk.Label(frm_datos, text="Precio ($):").grid(row=3, column=0, sticky="w", pady=3)
        self.ent_precio = ttk.Entry(frm_datos, width=20)
        self.ent_precio.grid(row=3, column=1, pady=3, padx=5)

        ttk.Label(frm_datos, text="Stock:").grid(row=4, column=0, sticky="w", pady=3)
        self.ent_stock = ttk.Entry(frm_datos, width=20)
        self.ent_stock.grid(row=4, column=1, pady=3, padx=5)

        frm_botones = ttk.LabelFrame(frame_izq, text=" Acciones ", padding=10)
        frm_botones.pack(fill="x")

        ttk.Button(
            frm_botones, 
            text=" Registrar", 
            image=self.iconos.get("registrar"), 
            compound="left", 
            command=self._btn_registrar
        ).grid(row=0, column=0, padx=3, pady=3, sticky="ew")

        ttk.Button(
            frm_botones, 
            text=" Consultar", 
            image=self.iconos.get("consultar"), 
            compound="left", 
            command=self._btn_consultar
        ).grid(row=0, column=1, padx=3, pady=3, sticky="ew")

        ttk.Button(
            frm_botones, 
            text=" Actualizar", 
            image=self.iconos.get("actualizar"), 
            compound="left", 
            command=self._btn_actualizar
        ).grid(row=1, column=0, padx=3, pady=3, sticky="ew")

        ttk.Button(
            frm_botones, 
            text=" Eliminar", 
            image=self.iconos.get("eliminar"), 
            compound="left", 
            command=self._btn_eliminar
        ).grid(row=1, column=1, padx=3, pady=3, sticky="ew")

        ttk.Button(
            frm_botones, 
            text="Limpiar Campos", 
            command=self._limpiar_formulario
        ).grid(row=2, column=0, columnspan=2, padx=3, pady=5, sticky="ew")

        frame_der = ttk.LabelFrame(self.tab_productos, text=" Productos Registrados ", padding=5)
        frame_der.pack(side="right", fill="both", expand=True)

        columnas = ("codigo", "nombre", "categoria", "precio", "stock")
        self.tabla_prod = ttk.Treeview(frame_der, columns=columnas, show="headings")
        self.tabla_prod.heading("codigo", text="Código")
        self.tabla_prod.heading("nombre", text="Nombre")
        self.tabla_prod.heading("categoria", text="Categoría")
        self.tabla_prod.heading("precio", text="Precio ($)")
        self.tabla_prod.heading("stock", text="Stock")

        self.tabla_prod.column("codigo", width=75, minwidth=65, anchor="center")
        self.tabla_prod.column("nombre", width=200, minwidth=150, anchor="w")
        self.tabla_prod.column("categoria", width=120, minwidth=95, anchor="w")
        self.tabla_prod.column("precio", width=70, anchor="e")
        self.tabla_prod.column("stock", width=60, anchor="center")

        scrollbar = ttk.Scrollbar(frame_der, orient="vertical", command=self.tabla_prod.yview)
        self.tabla_prod.configure(yscrollcommand=scrollbar.set)

        self.tabla_prod.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

    def _construir_tab_usuarios(self):
        frame_tab = ttk.LabelFrame(self.tab_usuarios, text=" Usuarios Registrados ", padding=10)
        frame_tab.pack(fill="both", expand=True)

        columnas = ("id", "nombre", "correo")
        self.tabla_user = ttk.Treeview(frame_tab, columns=columnas, show="headings")
        self.tabla_user.heading("id", text="ID Usuario")
        self.tabla_user.heading("nombre", text="Nombre Completo")
        self.tabla_user.heading("correo", text="Correo Electrónico")

        self.tabla_user.column("id", width=100, anchor="center")
        self.tabla_user.column("nombre", width=200, anchor="w")
        self.tabla_user.column("correo", width=250, anchor="w")

        scroll_usuarios = ttk.Scrollbar(frame_tab, orient="vertical", command=self.tabla_user.yview)
        self.tabla_user.configure(yscrollcommand=scroll_usuarios.set)
        self.tabla_user.pack(side="left", fill="both", expand=True)
        scroll_usuarios.pack(side="right", fill="y")

    def _construir_tab_ventas(self):
        frame_izq = ttk.Frame(self.tab_ventas, padding=5)
        frame_izq.pack(side="left", fill="y", padx=(0, 10))

        frm_venta = ttk.LabelFrame(frame_izq, text=" Nueva Venta ", padding=10)
        frm_venta.pack(fill="x", pady=(0, 10))

        ttk.Label(frm_venta, text="Seleccionar Usuario:").grid(row=0, column=0, sticky="w", pady=5)
        self.cb_usuarios = ttk.Combobox(frm_venta, state="readonly", width=25)
        self.cb_usuarios.grid(row=1, column=0, pady=5)

        ttk.Label(frm_venta, text="Seleccionar Producto:").grid(row=2, column=0, sticky="w", pady=5)
        self.cb_productos = ttk.Combobox(frm_venta, state="readonly", width=25)
        self.cb_productos.grid(row=3, column=0, pady=5)

        ttk.Label(frm_venta, text="Cantidad a Vender:").grid(row=4, column=0, sticky="w", pady=5)
        self.ent_cantidad_venta = ttk.Entry(frm_venta, width=27)
        self.ent_cantidad_venta.grid(row=5, column=0, pady=5)
        self.ent_cantidad_venta.insert(0, "1")

        btn_registrar_venta = ttk.Button(
            frm_venta, 
            text="Registrar Venta", 
            # command recibe el método sin paréntesis: el clic lo ejecutará.
            command=self._callback_registrar_venta
        )
        btn_registrar_venta.grid(row=6, column=0, pady=15, sticky="ew")

        frame_der = ttk.LabelFrame(self.tab_ventas, text=" Registro de Ventas Realizadas ", padding=5)
        frame_der.pack(side="right", fill="both", expand=True)

        columnas = ("fecha", "usuario", "producto", "cantidad")
        self.tabla_ventas = ttk.Treeview(frame_der, columns=columnas, show="headings")
        self.tabla_ventas.heading("fecha", text="Fecha / Hora")
        self.tabla_ventas.heading("usuario", text="ID Usuario")
        self.tabla_ventas.heading("producto", text="Código Producto")
        self.tabla_ventas.heading("cantidad", text="Cantidad")

        self.tabla_ventas.column("fecha", width=140, anchor="center")
        self.tabla_ventas.column("usuario", width=90, anchor="center")
        self.tabla_ventas.column("producto", width=110, anchor="center")
        self.tabla_ventas.column("cantidad", width=70, anchor="center")

        scroll_v = ttk.Scrollbar(frame_der, orient="vertical", command=self.tabla_ventas.yview)
        self.tabla_ventas.configure(yscrollcommand=scroll_v.set)

        self.tabla_ventas.pack(side="left", fill="both", expand=True)
        scroll_v.pack(side="right", fill="y")

    def _callback_registrar_venta(self):
        """Obtiene selecciones, delega al servicio y muestra la respuesta."""
        indice_usuario = self.cb_usuarios.current()
        indice_producto = self.cb_productos.current()
        # El callback solo recoge datos; el servicio valida la operación.
        usuario_id = self.usuarios_venta[indice_usuario].identificacion if indice_usuario >= 0 else None
        codigo = self.productos_venta[indice_producto].codigo if indice_producto >= 0 else ""
        cantidad = self.ent_cantidad_venta.get().strip()

        exito, mensaje = self.restaurante_servicio.registrar_venta(usuario_id, codigo, cantidad)
        if exito:
            self.cargar_datos()
            self.ent_cantidad_venta.delete(0, tk.END)
            self.ent_cantidad_venta.insert(0, "1")
            messagebox.showinfo("Venta registrada", mensaje)
        else:
            messagebox.showwarning("No se registró la venta", mensaje)

    def _limpiar_formulario(self):
        self.ent_codigo.delete(0, tk.END)
        self.ent_nombre.delete(0, tk.END)
        self.ent_categoria.delete(0, tk.END)
        self.ent_precio.delete(0, tk.END)
        self.ent_stock.delete(0, tk.END)

    def _extraer_datos_formulario(self):
        codigo = self.ent_codigo.get().strip()
        nombre = self.ent_nombre.get().strip()
        categoria = self.ent_categoria.get().strip()
        precio_str = self.ent_precio.get().strip()
        stock_str = self.ent_stock.get().strip()

        if not codigo or not nombre or not categoria or not precio_str or not stock_str:
            raise ValueError("Por favor complete todos los campos del formulario.")

        try:
            precio = float(precio_str.replace(",", "."))
            stock = int(stock_str)
        except ValueError:
            raise ValueError("Precio debe ser numérico y Stock entero.")

        return codigo, nombre, categoria, precio, stock

    def _btn_registrar(self):
        try:
            codigo, nombre, categoria, precio, stock = self._extraer_datos_formulario()
            exito, msj = self.restaurante_servicio.registrar_producto(codigo, nombre, categoria, precio, stock)
            if exito:
                messagebox.showinfo("Éxito", msj)
                self.cargar_datos()
                self._limpiar_formulario()
            else:
                messagebox.showerror("Error", msj)
        except ValueError as e:
            messagebox.showwarning("Atención", str(e))

    def _btn_consultar(self):
        codigo = self.ent_codigo.get().strip()
        if not codigo:
            messagebox.showwarning("Atención", "Ingrese el código del producto a consultar.")
            return

        prod = self.restaurante_servicio.buscar_producto(codigo)
        if prod:
            self._limpiar_formulario()
            self.ent_codigo.insert(0, prod.codigo)
            self.ent_nombre.insert(0, prod.nombre)
            self.ent_categoria.insert(0, prod.categoria)
            self.ent_precio.insert(0, str(prod.precio))
            self.ent_stock.insert(0, str(prod.stock))
            messagebox.showinfo("Consulta Exitosa", f"Producto '{prod.nombre}' cargado.")
        else:
            messagebox.showerror("No Encontrado", f"No se encontró el producto '{codigo}'.")

    def _btn_actualizar(self):
        try:
            codigo, nombre, categoria, precio, stock = self._extraer_datos_formulario()
            exito, msj = self.restaurante_servicio.actualizar_producto(codigo, nombre, categoria, precio, stock)
            if exito:
                messagebox.showinfo("Éxito", msj)
                self.cargar_datos()
                self._limpiar_formulario()
            else:
                messagebox.showerror("Error", msj)
        except ValueError as e:
            messagebox.showwarning("Atención", str(e))

    def _btn_eliminar(self):
        codigo = self.ent_codigo.get().strip()
        if not codigo:
            messagebox.showwarning("Atención", "Ingrese el código del producto a eliminar.")
            return

        if messagebox.askyesno("Confirmar", f"¿Está seguro de eliminar el producto '{codigo}'?"):
            exito, msj = self.restaurante_servicio.eliminar_producto(codigo)
            if exito:
                messagebox.showinfo("Éxito", msj)
                self.cargar_datos()
                self._limpiar_formulario()
            else:
                messagebox.showerror("Error", msj)

    def cargar_datos(self):
        # Poblar Productos
        for item in self.tabla_prod.get_children():
            self.tabla_prod.delete(item)
        lista_prods = self.restaurante_servicio.listar_productos()
        for p in lista_prods:
            self.tabla_prod.insert("", "end", values=(p.codigo, p.nombre, p.categoria, f"{p.precio:.2f}", p.stock))

        # Poblar Usuarios
        for item in self.tabla_user.get_children():
            self.tabla_user.delete(item)
        lista_users = self.restaurante_servicio.listar_usuarios()
        for u in lista_users:
            self.tabla_user.insert("", "end", values=(u.identificacion, u.nombre, u.correo))

        # Poblar Ventas
        for item in self.tabla_ventas.get_children():
            self.tabla_ventas.delete(item)
        for v in self.restaurante_servicio.listar_ventas():
            self.tabla_ventas.insert("", "end", values=(v.fecha, v.usuario_id, v.producto_codigo, v.cantidad))

        # Se conserva la relación por índice; no se separan nombres con split.
        self.usuarios_venta = lista_users
        self.productos_venta = [p for p in lista_prods if p.stock > 0]
        self.cb_usuarios.set("")
        self.cb_productos.set("")
        # Cargar opciones en los Comboboxes de Ventas
        self.cb_usuarios["values"] = [f"{u.identificacion} - {u.nombre}" for u in lista_users]
        self.cb_productos["values"] = [f"{p.codigo} - {p.nombre} (Stock: {p.stock})" for p in self.productos_venta]
