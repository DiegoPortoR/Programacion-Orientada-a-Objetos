import tkinter as tk
from tkinter import ttk, messagebox
from abc import ABC, abstractmethod
import math

# =====================================================================
# 1. CAPA DE LÓGICA MATEMÁTICA (Jerarquía de Clases - POO)
# =====================================================================

class FiguraSolida(ABC):
    """Clase abstracta pura que sirve de molde para los sólidos."""
    def __init__(self, nombre: str):
        self.nombre = nombre

    @abstractmethod
    def calcular_volumen(self) -> float:
        pass

    @abstractmethod
    def calcular_superficie(self) -> float:
        pass


class Cilindro(FiguraSolida):
    def __init__(self, radio: float, altura: float):
        super().__init__("Cilindro")
        self.radio = radio
        self.altura = altura

    def calcular_volumen(self) -> float:
        return math.pi * (self.radio ** 2) * self.altura

    def calcular_superficie(self) -> float:
        area_lateral = 2 * math.pi * self.radio * self.altura
        area_bases = 2 * math.pi * (self.radio ** 2)
        return area_lateral + area_bases


class Esfera(FiguraSolida):
    def __init__(self, radio: float):
        super().__init__("Esfera")
        self.radio = radio

    def calcular_volumen(self) -> float:
        return (4 / 3) * math.pi * (self.radio ** 3)

    def calcular_superficie(self) -> float:
        return 4 * math.pi * (self.radio ** 2)


class PiramideCuadrada(FiguraSolida):
    def __init__(self, lado_base: float, altura: float, apotema: float):
        super().__init__("Pirámide Cuadrada")
        self.lado_base = lado_base
        self.altura = altura
        self.apotema = apotema

    def calcular_volumen(self) -> float:
        area_base = self.lado_base ** 2
        return (1 / 3) * area_base * self.altura

    def calcular_superficie(self) -> float:
        area_base = self.lado_base ** 2
        perimetro_base = 4 * self.lado_base
        area_lateral = (perimetro_base * self.apotema) / 2
        return area_base + area_lateral


# =====================================================================
# 2. CAPA DE INTERFAZ GRÁFICA DE USUARIO
# =====================================================================

class CalculadoraGeometricaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculador Geométrico Pro")
        self.root.geometry("450x420")
        self.root.resizable(False, False)
        
        # Configuración de estilos Tkinter (Temas y Colores)
        style = ttk.Style()
        style.theme_use('clam')
        
        # Personalización de las pestañas
        style.configure("TNotebook", background="#f0f2f5")
        style.configure("TNotebook.Tab", font=("Arial", 10, "bold"), padding=[12, 4])
        style.configure("TFrame", background="#ffffff")
        style.configure("TLabelframe", background="#ffffff")
        style.configure("TLabelframe.Label", font=("Arial", 10, "bold"), background="#ffffff", foreground="#333333")
        style.configure("TLabel", background="#ffffff", font=("Arial", 10))
        
        # Botón personalizado estilizado
        style.configure("Accent.TButton", font=("Arial", 10, "bold"), foreground="white", background="#007bff")
        style.map("Accent.TButton", background=[('active', '#0056b3')])

        # Contenedor principal de pestañas
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(expand=True, fill="both", padx=15, pady=15)
        
        # Inicialización de pestañas
        self.crear_pestana_cilindro()
        self.crear_pestana_esfera()
        self.crear_pestana_piramide()

    def obtener_valor_valido(self, entrada_widget, nombre_campo) -> float:
        """Valida que la entrada sea un número float positivo."""
        try:
            texto = entrada_widget.get().replace(",", ".").strip()
            valor = float(texto)
            if valor <= 0:
                raise ValueError
            return valor
        except ValueError:
            raise ValueError(f"El campo '{nombre_campo}' debe ser un número válido mayor a cero.")

    # -----------------------------------------------------------------
    # PESTAÑA: CILINDRO
    # -----------------------------------------------------------------
    def crear_pestana_cilindro(self):
        pestana = ttk.Frame(self.notebook, padding=15)
        self.notebook.add(pestana, text="Cilindro")
        
        # Texto informativo / Guía
        lbl_info = ttk.Label(pestana, text="Cálculo basado en el Radio de las bases y su Altura.", 
                             font=("Arial", 9, "italic"), foreground="#666666")
        lbl_info.grid(row=0, column=0, columnspan=2, sticky="w", pady=(0, 10))
        
        # Entradas
        ttk.Label(pestana, text="Radio (r) en cm:").grid(row=1, column=0, sticky="w", pady=6)
        entry_radio = ttk.Entry(pestana, width=18, font=("Arial", 10))
        entry_radio.grid(row=1, column=1, pady=6, padx=10, sticky="w")
        entry_radio.insert(0, "5.0")
        
        ttk.Label(pestana, text="Altura (h) en cm:").grid(row=2, column=0, sticky="w", pady=6)
        entry_altura = ttk.Entry(pestana, width=18, font=("Arial", 10))
        entry_altura.grid(row=2, column=1, pady=6, padx=10, sticky="w")
        entry_altura.insert(0, "10.0")
        
        # Cuadro de Resultados Destacados
        frame_res = ttk.LabelFrame(pestana, text=" Resultados Calculados ", padding=12)
        frame_res.grid(row=4, column=0, columnspan=2, sticky="ew", pady=(15, 0))
        
        lbl_res_vol = ttk.Label(frame_res, text="Volumen (V): --", font=("Arial", 11, "bold"), foreground="#0056b3")
        lbl_res_vol.pack(anchor="w", pady=4)
        lbl_res_sup = ttk.Label(frame_res, text="Superficie Total (A): --", font=("Arial", 11, "bold"), foreground="#28a745")
        lbl_res_sup.pack(anchor="w", pady=4)
        
        def calcular():
            try:
                r = self.obtener_valor_valido(entry_radio, "Radio")
                h = self.obtener_valor_valido(entry_altura, "Altura")
                
                cilindro = Cilindro(r, h)
                lbl_res_vol.config(text=f"Volumen (V): {cilindro.calcular_volumen():.2f} cm³")
                lbl_res_sup.config(text=f"Superficie Total (A): {cilindro.calcular_superficie():.2f} cm²")
            except ValueError as e:
                messagebox.showerror("Error de datos", str(e))

        ttk.Button(pestana, text="Calcular Cilindro", style="Accent.TButton", command=calcular).grid(row=3, column=0, columnspan=2, pady=(15, 5))

    # -----------------------------------------------------------------
    # PESTAÑA: ESFERA
    # -----------------------------------------------------------------
    def crear_pestana_esfera(self):
        pestana = ttk.Frame(self.notebook, padding=15)
        self.notebook.add(pestana, text="Esfera")
        
        lbl_info = ttk.Label(pestana, text="Cálculo simétrico basado únicamente en el Radio del cuerpo.", 
                             font=("Arial", 9, "italic"), foreground="#666666")
        lbl_info.grid(row=0, column=0, columnspan=2, sticky="w", pady=(0, 10))
        
        ttk.Label(pestana, text="Radio (r) en cm:").grid(row=1, column=0, sticky="w", pady=6)
        entry_radio = ttk.Entry(pestana, width=18, font=("Arial", 10))
        entry_radio.grid(row=1, column=1, pady=6, padx=10, sticky="w")
        entry_radio.insert(0, "5.0")
        
        frame_res = ttk.LabelFrame(pestana, text=" Resultados Calculados ", padding=12)
        frame_res.grid(row=3, column=0, columnspan=2, sticky="ew", pady=(15, 0))
        
        lbl_res_vol = ttk.Label(frame_res, text="Volumen (V): --", font=("Arial", 11, "bold"), foreground="#0056b3")
        lbl_res_vol.pack(anchor="w", pady=4)
        lbl_res_sup = ttk.Label(frame_res, text="Superficie Total (A): --", font=("Arial", 11, "bold"), foreground="#28a745")
        lbl_res_sup.pack(anchor="w", pady=4)
        
        def calcular():
            try:
                r = self.obtener_valor_valido(entry_radio, "Radio")
                
                esfera = Esfera(r)
                lbl_res_vol.config(text=f"Volumen (V): {esfera.calcular_volumen():.2f} cm³")
                lbl_res_sup.config(text=f"Superficie Total (A): {esfera.calcular_superficie():.2f} cm²")
            except ValueError as e:
                messagebox.showerror("Error de datos", str(e))

        ttk.Button(pestana, text="Calcular Esfera", style="Accent.TButton", command=calcular).grid(row=2, column=0, columnspan=2, pady=(15, 5))

    # -----------------------------------------------------------------
    # PESTAÑA: PIRÁMIDE CUADRADA
    # -----------------------------------------------------------------
    def crear_pestana_piramide(self):
        pestana = ttk.Frame(self.notebook, padding=15)
        self.notebook.add(pestana, text="Pirámide")
        
        lbl_info = ttk.Label(pestana, text="Cálculo diseñado para una Pirámide Regular de Base Cuadrada.", 
                             font=("Arial", 9, "italic"), foreground="#666666")
        lbl_info.grid(row=0, column=0, columnspan=2, sticky="w", pady=(0, 10))
        
        ttk.Label(pestana, text="Lado de la Base (cm):").grid(row=1, column=0, sticky="w", pady=6)
        entry_lado = ttk.Entry(pestana, width=18, font=("Arial", 10))
        entry_lado.grid(row=1, column=1, pady=6, padx=10, sticky="w")
        entry_lado.insert(0, "5.0")
        
        ttk.Label(pestana, text="Altura (h) en cm:").grid(row=2, column=0, sticky="w", pady=6)
        entry_altura = ttk.Entry(pestana, width=18, font=("Arial", 10))
        entry_altura.grid(row=2, column=1, pady=6, padx=10, sticky="w")
        entry_altura.insert(0, "10.0")
        
        ttk.Label(pestana, text="Apotema (a) en cm:").grid(row=3, column=0, sticky="w", pady=6)
        entry_apotema = ttk.Entry(pestana, width=18, font=("Arial", 10))
        entry_apotema.grid(row=3, column=1, pady=6, padx=10, sticky="w")
        entry_apotema.insert(0, "12.0")
        
        frame_res = ttk.LabelFrame(pestana, text=" Resultados Calculados ", padding=12)
        frame_res.grid(row=5, column=0, columnspan=2, sticky="ew", pady=(15, 0))
        
        lbl_res_vol = ttk.Label(frame_res, text="Volumen (V): --", font=("Arial", 11, "bold"), foreground="#0056b3")
        lbl_res_vol.pack(anchor="w", pady=4)
        lbl_res_sup = ttk.Label(frame_res, text="Superficie Total (A): --", font=("Arial", 11, "bold"), foreground="#28a745")
        lbl_res_sup.pack(anchor="w", pady=4)
        
        def calcular():
            try:
                l = self.obtener_valor_valido(entry_lado, "Lado de la Base")
                h = self.obtener_valor_valido(entry_altura, "Altura")
                a = self.obtener_valor_valido(entry_apotema, "Apotema")
                
                piramide = PiramideCuadrada(l, h, a)
                lbl_res_vol.config(text=f"Volumen (V): {piramide.calcular_volumen():.2f} cm³")
                lbl_res_sup.config(text=f"Superficie Total (A): {piramide.calcular_superficie():.2f} cm²")
            except ValueError as e:
                messagebox.showerror("Error de datos", str(e))

        ttk.Button(pestana, text="Calcular Pirámide", style="Accent.TButton", command=calcular).grid(row=4, column=0, columnspan=2, pady=(15, 5))


# =====================================================================
# 3. HILO DE EJECUCIÓN PRINCIPAL
# =====================================================================
if __name__ == "__main__":
    root = tk.Tk()
    app = CalculadoraGeometricaApp(root)
    root.mainloop()