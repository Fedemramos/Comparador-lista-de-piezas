import pandas as pd
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk

class ComparadorDePiezasApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Comparador de Piezas")
        self.configure(bg="#1e1e1e")  # Fondo principal oscuro
        self.geometry("900x500")
        self.original_file = None
        self.compare_file = None
        
        self.create_widgets()

    def create_widgets(self):
        # Frame principal
        main_frame = tk.Frame(self, bg="#1e1e1e")  # Fondo oscuro
        main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

        # Frame izquierdo para logo y botones
        left_frame = tk.Frame(main_frame, bg="#1e1e1e")
        left_frame.pack(side=tk.LEFT, padx=20, pady=20, fill=tk.Y)

        # Redimensionar el logo
        original_logo = Image.open("logo.png")
        resized_logo = original_logo.resize((100, 100), Image.Resampling.LANCZOS)
        logo = ImageTk.PhotoImage(resized_logo)
        
        # Mostrar el logo redimensionado
        logo_label = tk.Label(left_frame, image=logo, bg="#1e1e1e")
        logo_label.image = logo
        logo_label.pack(pady=10)

        
        # Botones en el lado izquierdo
        button_frame = tk.Frame(left_frame, bg="#1e1e1e")
        button_frame.pack(pady=20)

        button_style = {
            "font": ("Montserrat", 12), 
            "bg": "#2c3e50",  # Fondo de botón oscuro
            "fg": "white",  # Texto blanco
            "activebackground": "#34495e",  # Fondo de botón activo ligeramente más claro
            "activeforeground": "white", 
            "width": 25, 
            "height": 2, 
            "bd": 0, 
            "relief": "flat",
            "cursor": "hand2"
        }
        
        self.original_button = tk.Button(button_frame, text="Cargar Archivo Original", 
                                         command=self.load_original_file,
                                         **button_style)
        self.original_button.pack(pady=10)
        
        self.compare_button = tk.Button(button_frame, text="Cargar Archivo a Comparar", 
                                        command=self.load_compare_file, 
                                        **button_style, state="disabled")
        self.compare_button.pack(pady=10)

        # Texto "by Fede Ramos"
        author_label = tk.Label(left_frame, text="by Fede Ramos", font=("Nunito", 10), 
                                fg="#bdc3c7", bg="#1e1e1e")
        author_label.pack(pady=50)

        # Frame derecho para resultados
        result_frame = tk.Frame(main_frame, bg="#1e1e1e")
        result_frame.pack(side=tk.RIGHT, padx=20, pady=20, fill=tk.BOTH, expand=True)

        # Mostrar las piezas faltantes en la parte superior
        self.missing_pieces_text = tk.Text(result_frame, height=5, bg="#2c3e50", fg="#ecf0f1", 
                                           font=("Montserrat", 14), state="disabled", relief="flat", padx=10, pady=10)
        self.missing_pieces_text.pack(pady=(0, 20), fill=tk.BOTH, expand=False)

        # Widget de texto para ambas listas en columnas
        self.pieces_text = tk.Text(result_frame, height=20, bg="#2c3e50", fg="#ecf0f1", 
                                   font=("Montserrat", 12), state="disabled", relief="flat", padx=10, pady=10)
        self.pieces_text.pack(fill=tk.BOTH, expand=True)

        # Texto inferior
        self.footer_label = tk.Label(main_frame, text="by Fede Ramos", font=("Montserrat", 10), 
                                     fg="#bdc3c7", bg="#1e1e1e")
        self.footer_label.pack(side=tk.BOTTOM, pady=10)

    def load_original_file(self):
        self.original_file = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx;*.xls")])
        if self.original_file:
            messagebox.showinfo("Archivo Cargado", "Archivo cargado exitosamente.")
            self.compare_button.config(state="normal")

    def load_compare_file(self):
        self.compare_file = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx;*.xls")])
        if self.compare_file:
            messagebox.showinfo("Archivo Cargado", "Archivo cargado exitosamente.")
            if self.original_file:
                self.ejecutar_comparacion()

    def mostrar_piezas_faltantes(self, piezas_faltantes):
        self.missing_pieces_text.config(state="normal")
        self.missing_pieces_text.delete('1.0', tk.END)
        
        if piezas_faltantes:
            self.missing_pieces_text.insert(tk.END, f"Piezas faltantes: {len(piezas_faltantes)}\n")
            print("\n")
            for pieza in piezas_faltantes:
                self.missing_pieces_text.insert(tk.END, f"Nombre: {pieza[0]} de {pieza[1]}, máquina: {pieza[2]}\n")
        else:
            self.missing_pieces_text.insert(tk.END, "La lista está completa, no falto ninguna pieza.")
        
        self.missing_pieces_text.config(state="disabled")

    def mostrar_lista_piezas_en_columnas(self, piezas_1, piezas_2):
        self.pieces_text.config(state="normal")
        self.pieces_text.delete('1.0', tk.END)

        # Titulos para las columnas
        titulo_1 = "Lista Original"
        titulo_2 = "Lista a Comparar"

        # Insertar títulos con un espaciado adecuado
        line = f"{titulo_1:<70}{titulo_2}\n"
        self.pieces_text.insert(tk.END, line)
        
        # Línea separadora entre título y contenido
        self.pieces_text.insert(tk.END, "-" * 100 + "\n\n")

        # Determinar la longitud máxima de las listas
        max_length = max(len(piezas_1), len(piezas_2))

        # Iterar sobre ambas listas hasta la longitud máxima
        for i in range(max_length):
            # Procesar la primera lista
            if i < len(piezas_1):
                p1 = piezas_1[i]
                line = f"{p1[0]} {p1[1]},de {p1[2]:<40}"
            else:
                line = f"{'':<30}"  # Espaciado en blanco si la lista 1 es más corta

            # Procesar la segunda lista
            if i < len(piezas_2):
                p2 = piezas_2[i]
                line += f"{p2[0]} {p2[1]} - {p2[2]}\n"
            else:
                line += f"\n"  # Línea en blanco si la lista 2 es más corta

            # Insertar la línea formateada en el widget de texto
            self.pieces_text.insert(tk.END, line)
        
        # Añadir separación entre las listas y los totales
        self.pieces_text.insert(tk.END, "\n")
        self.pieces_text.insert(tk.END, "-" * 100 + "\n\n")

        # Mostrar la cantidad de piezas en cada lista
        total_piezas_1 = len(piezas_1)
        total_piezas_2 = len(piezas_2)
        line = f"Piezas de Lista Original: {total_piezas_1:<25}Piezas de Lista CUT: {total_piezas_2}\n"
        self.pieces_text.insert(tk.END, line)

        self.pieces_text.config(state="disabled")

    def ejecutar_comparacion(self):
        if not self.original_file or not self.compare_file:
            messagebox.showerror("Error", "Debe seleccionar ambos archivos para comparar.")
            return

        df1 = pd.read_excel(self.original_file)
        df2 = pd.read_excel(self.compare_file)

        piezas_1 = list(zip(df1['Pieza'], df1['Espesor'], df1['Maquina']))
        piezas_2 = list(zip(df2['Pieza'], df2['Espesor'], df2['Maquina']))

        piezas_faltantes = list(set(piezas_1) - set(piezas_2))

        self.mostrar_piezas_faltantes(piezas_faltantes)
        self.mostrar_lista_piezas_en_columnas(piezas_1, piezas_2)

if __name__ == "__main__":
    app = ComparadorDePiezasApp()
    app.mainloop()
