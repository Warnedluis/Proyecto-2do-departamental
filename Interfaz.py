import customtkinter as ctk

# --- Configuración Visual Global ---
ctk.set_appearance_mode("Dark")        # Modo oscuro (más profesional para programación)
ctk.set_default_color_theme("blue")    # Color de acento

class InterfazRK(ctk.CTk):
    def __init__(self):
        super().__init__()

        # 1. Configuración de la Ventana Principal
        self.title("Solver Ecuaciones Diferenciales - RK4")
        self.geometry("900x600") # Hacemos la ventana más ancha

        # Configuración de la rejilla principal (Grid Layout)
        # Columna 0 (Panel Izquierdo): Ancho fijo
        # Columna 1 (Panel Derecho): Se estira (weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # =================================================
        # PANEL LATERAL (IZQUIERDA) - Entradas y Botones
        # =================================================
        self.sidebar_frame = ctk.CTkFrame(self, width=250, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, sticky="nsew")

        # Título del Panel
        self.logo_label = ctk.CTkLabel(self.sidebar_frame, text="Parámetros", font=ctk.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))

        # --- Inputs (Función auxiliar para no repetir código) ---
        self.crear_input_lateral("Ecuación y' = f(x,y)", "Ej: x + y", 1)
        self.crear_input_lateral("Valor inicial X0", "0", 2)
        self.crear_input_lateral("Valor inicial Y0", "1", 3)
        self.crear_input_lateral("Paso (h)", "0.1", 4)
        self.crear_input_lateral("Valor X final", "2", 5)

        # Botón Calcular (Color principal)

        self.btn_calcular = ctk.CTkButton(self.sidebar_frame, text="CALCULAR SOLUCIÓN")
        self.btn_calcular.grid(row=7, column=0, padx=20, pady=(90, 10))
                
        self.btn_calcular = ctk.CTkButton(self.sidebar_frame, text="Limpiar", fg_color="transparent",border_width = 2, text_color = ("gray10","#DCE4EE"))
        self.btn_calcular.grid(row=10, column=0, padx=20, pady=(90, 10))


        # =================================================
        # ÁREA PRINCIPAL (DERECHA) - Resultados
        # =================================================
        self.main_frame = ctk.CTkFrame(self, corner_radius=10)
        self.main_frame.grid(row=0, column=1, padx=20, pady=20, sticky="nsew")

        # Título de Resultados
        self.label_resultados = ctk.CTkLabel(self.main_frame, text="Tabla de Iteraciones", font=ctk.CTkFont(size=18))
        self.label_resultados.pack(pady=15)

        # Caja de texto para mostrar la "tabla" (Solo lectura)
        self.textbox_resultados = ctk.CTkTextbox(self.main_frame, font=("Consolas", 14))
        self.textbox_resultados.pack(fill="both", expand=True, padx=15, pady=(0, 15))
        
        # Texto de ejemplo para ver cómo queda
        texto_ejemplo = "Iteración\t\tX\t\tY\n" + "-"*50 + "\n"
        self.textbox_resultados.insert("0.0", texto_ejemplo)


    def crear_input_lateral(self, texto, placeholder, fila):
        """Ayuda a crear etiquetas y cajas de texto en el panel lateral ordenadamente"""
        label = ctk.CTkLabel(self.sidebar_frame, text=texto, anchor="w")
        label.grid(row=fila*2-1, column=0, padx=20, pady=(10, 0), sticky="w") # fila impar
        
        entry = ctk.CTkEntry(self.sidebar_frame, placeholder_text=placeholder)
        entry.grid(row=fila*2, column=0, padx=20, pady=(0, 0), sticky="ew")   # fila par

if __name__ == "__main__":
    app = InterfazRK()
    app.mainloop()