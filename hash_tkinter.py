
import tkinter as tk
from tkinter import ttk, filedialog, messagebox

from ficheros import comprobar_fichero
from hashes import calcular_hash, ALGORITMOS


class CalculadoraHash:

    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Calculadora de hashes")
        self.ventana.geometry("700x400")

        # Variables
        self.fichero = tk.StringVar()
        self.algoritmo = tk.StringVar(value="sha256")

        # Selección del fichero
        ttk.Label(
            self.ventana,
            text="Fichero:"
        ).pack(pady=5)

        ttk.Entry(
            self.ventana,
            textvariable=self.fichero,
            width=85
        ).pack(pady=5)

        ttk.Button(
            self.ventana,
            text="Seleccionar fichero",
            command=self.seleccionar_fichero
        ).pack(pady=5)

        # Selección del algoritmo
        ttk.Label(
            self.ventana,
            text="Algoritmo:"
        ).pack(pady=5)

        ttk.Combobox(
            self.ventana,
            textvariable=self.algoritmo,
            values=ALGORITMOS,
            state="readonly"
        ).pack(pady=5)

        # Botón para calcular
        ttk.Button(
            self.ventana,
            text="Calcular hash",
            command=self.calcular
        ).pack(pady=10)

        # Resultado
        ttk.Label(
            self.ventana,
            text="Hash calculado:"
        ).pack(pady=5)

        self.texto_resultado = tk.Text(
            self.ventana,
            width=80,
            height=4,
            wrap="char"
        )
        self.texto_resultado.pack(pady=5)

        # Botón para copiar
        ttk.Button(
            self.ventana,
            text="Copiar hash",
            command=self.copiar_hash
        ).pack(pady=5)

    def seleccionar_fichero(self):
        ruta = filedialog.askopenfilename()

        if ruta:
            self.fichero.set(ruta)
            self.texto_resultado.delete("1.0", tk.END)

    def calcular(self):
        self.texto_resultado.delete("1.0", tk.END)

        if not self.fichero.get().strip():
            messagebox.showerror("Error", "Selecciona un fichero.")
            return

        if self.algoritmo.get() not in ALGORITMOS:
            messagebox.showerror("Error", "Algoritmo no válido.")
            return

        try:
            ruta = comprobar_fichero(self.fichero.get())
            hash_valor = calcular_hash(ruta, self.algoritmo.get())

            self.texto_resultado.insert("1.0", hash_valor)

        except OSError as error:
            messagebox.showerror("Error", str(error))

    def copiar_hash(self):
        hash_valor = self.texto_resultado.get("1.0", "end-1c").strip()

        if not hash_valor:
            messagebox.showwarning(
                "Aviso",
                "No hay ningún hash para copiar."
            )
            return

        self.ventana.clipboard_clear()
        self.ventana.clipboard_append(hash_valor)
        self.ventana.update()

        messagebox.showinfo(
            "Información",
            "Hash copiado al portapapeles."
        )


def main():
    ventana = tk.Tk()
    app = CalculadoraHash(ventana)
    ventana.mainloop()


if __name__ == "__main__":
    main()
