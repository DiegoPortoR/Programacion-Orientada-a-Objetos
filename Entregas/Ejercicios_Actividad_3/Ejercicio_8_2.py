import tkinter as tk
from tkinter import ttk, messagebox

# ==========================================
# LÓGICA DE NEGOCIO / PROCESAMIENTO DE DATOS
# ==========================================
class EstadisticaNotas:
    def __init__(self):
        # Inicializamos con una lista vacía para almacenar los floats
        self.calificaciones = []

    def registrar_calificaciones(self, *notas_texto):
        """Procesa, limpia y valida las notas ingresadas desde la GUI."""
        try:
            # Convertimos todas las entradas a float quitando espacios en un solo paso
            self.calificaciones = [float(nota.strip()) for nota in notas_texto]
        except ValueError:
            raise ValueError("Por favor, asegúrate de ingresar únicamente valores numéricos.")

    def obtener_promedio(self):
        if not self.calificaciones:
            return 0.0
        return sum(self.calificaciones) / len(self.calificaciones)

    def obtener_maximo(self):
        return max(self.calificaciones) if self.calificaciones else 0.0

    def obtener_minimo(self):
        return min(self.calificaciones) if self.calificaciones else 0.0

    def calcular_desviacion(self):
        if not self.calificaciones:
            return 0.0
        
        media = self.obtener_promedio()
        # Calculamos la varianza de forma más directa y pythonica
        varianza = sum((nota - media) ** 2 for nota in self.calificaciones) / len(self.calificaciones)
        # Retornamos la raíz cuadrada de la varianza (Desviación estándar poblacional)
        return varianza ** 0.5


# ==========================================
# INTERFAZ GRÁFICA DE USUARIO (GUI)
# ==========================================
class VentanaNotasApp:
    def __init__(self, ventana_principal):
        self.root = ventana_principal
        self.root.title("Gestor Estadístico de Calificaciones")
        self.root.resizable(False, False)
        
        # Instancia del motor de cálculo
        self.procesador = EstadisticaNotas()
        self.campos_entrada = []

        # --- SECCIÓN DE ENTRADA DE DATOS ---
        seccion_entrada = ttk.LabelFrame(ventana_principal, text=" Registro de Notas ", padding=15)
        seccion_entrada.pack(padx=15, pady=10, fill="x")

        for idx in range(5):
            lbl = ttk.Label(seccion_entrada, text=f"Calificación {idx + 1}:")
            lbl.grid(row=idx, column=0, padx=8, pady=6, sticky="e")
            
            txt_entry = ttk.Entry(seccion_entrada, width=12)
            txt_entry.grid(row=idx, column=1, padx=8, pady=6)
            txt_entry.insert(0, "0.0")
            
            self.campos_entrada.append(txt_entry)

        # --- BOTÓN DE ACCIÓN ---
        self.btn_procesar = ttk.Button(
            ventana_principal, 
            text="Calcular Métricas", 
            command=self.ejecutar_calculos
        )
        self.btn_procesar.pack(pady=10)

        # --- SECCIÓN DE RESULTADOS ---
        seccion_resultados = ttk.LabelFrame(ventana_principal, text=" Métricas Calculadas ", padding=15)
        seccion_resultados.pack(padx=15, pady=10, fill="x")

        # Usamos un diccionario para gestionar las etiquetas de salida de forma limpia
        self.indicadores = {}
        metricas = [
            ("promedio", "Promedio General:"),
            ("maximo", "Nota Más Alta:"),
            ("minimo", "Nota Más Baja:"),
            ("desviacion", "Desviación Estándar:")
        ]

        for posicion, (clave, texto) in enumerate(metricas):
            lbl_titulo = ttk.Label(seccion_resultados, text=texto, font=("Helvetica", 9, "bold"))
            lbl_titulo.grid(row=posicion, column=0, sticky="w", pady=4, padx=5)
            
            lbl_valor = ttk.Label(seccion_resultados, text="-")
            lbl_valor.grid(row=posicion, column=1, sticky="w", pady=4, padx=5)
            
            self.indicadores[clave] = lbl_valor

    def ejecutar_calculos(self):
        """Pone en comunicación la interfaz con la lógica de negocio."""
        try:
            # Extraemos los textos de las cajas usando list comprehension
            valores_ingresados = [campo.get() for campo in self.campos_entrada]
            
            # Enviamos los datos a la clase lógica
            self.procesador.registrar_calificaciones(*valores_ingresados)
            
            # Realizamos los cálculos correspondientes
            media = self.procesador.obtener_promedio()
            nota_max = self.procesador.obtener_maximo()
            nota_min = self.procesador.obtener_minimo()
            desv_est = self.procesador.calcular_desviacion()

            # Actualizamos los elementos visuales con los nuevos formatos
            self.indicadores["promedio"].config(text=f"{media:.2f}")
            self.indicadores["maximo"].config(text=f"{nota_max:.1f}")
            self.indicadores["minimo"].config(text=f"{nota_min:.1f}")
            self.indicadores["desviacion"].config(text=f"{desv_est:.3f}")

        except ValueError as error_mensaje:
            # Alerta flotante en caso de errores de escritura
            messagebox.showerror("Error en los Datos", str(error_mensaje))


# ==========================================
# ARRANQUE DE LA APLICACIÓN
# ==========================================
if __name__ == "__main__":
    ventana_raiz = tk.Tk()
    app = VentanaNotasApp(ventana_raiz)
    ventana_raiz.mainloop()