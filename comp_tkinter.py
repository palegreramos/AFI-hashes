
import tkinter as tk
from tkinter import ttk, filedialog, messagebox

from ficheros import comprobar_fichero
from hashes import calcular_hash, ALGORITMOS


class ComparadorHashes:

    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Comparador de hashes")
        self.ventana.geometry("800x500")

        self.fichero1 = tk.StringVar()
        self.fichero2 = tk.StringVar()
        self.algoritmo = tk.StringVar(value="sha256")
        self.comparacion = tk.StringVar()

        ttk.Label(ventana, text="Primer fichero:").pack(pady=5)

        ttk.Entry(
            ventana, textvariable=self.fichero1, width=90
        ).pack(pady=5)

        ttk.Button(
            ventana,
            text="Seleccionar primer fichero",
            command=self.seleccionar_fichero1
        ).pack(pady=5)

        ttk.Label(ventana, text="Segundo fichero:").pack(pady=5)

        ttk.Entry(
            ventana, textvariable=self.fichero2, width=90
        ).pack(pady=5)

        ttk.Button(
            ventana,
            text="Seleccionar segundo fichero",
            command=self.seleccionar_fichero2
        ).pack(pady=5)

        ttk.Label(ventana, text="Algoritmo:").pack(pady=5)

        ttk.Combobox(
            ventana,
            textvariable=self.algoritmo,
            values=ALGORITMOS,
            state="readonly"
        ).pack(pady=5)

        ttk.Button(
            ventana,
            text="Comparar hashes",
            command=self.comparar
        ).pack(pady=10)

        ttk.Label(ventana, text="Hashes calculados:").pack(pady=5)

        self.texto_resultado = tk.Text(
            ventana,
            width=90,
            height=7,
            wrap="char"
        )
        self.texto_resultado.pack(pady=5)

        self.etiqueta_comparacion = tk.Label(ventana)
        self.etiqueta_comparacion.pack(pady=10)

    def seleccionar_fichero1(self):
        ruta = filedialog.askopenfilename()
        if ruta:
            self.fichero1.set(ruta)
            self.limpiar_resultados()

    def seleccionar_fichero2(self):
        ruta = filedialog.askopenfilename()
        if ruta:
            self.fichero2.set(ruta)
            self.limpiar_resultados()

    def limpiar_resultados(self):
        self.texto_resultado.delete("1.0", tk.END)
        self.etiqueta_comparacion.config(text="")

    def comparar(self):
        self.limpiar_resultados()

        if not self.fichero1.get().strip() or not self.fichero2.get().strip():
            messagebox.showerror("Error", "Selecciona los dos ficheros.")
            return

        if self.algoritmo.get() not in ALGORITMOS:
            messagebox.showerror("Error", "Algoritmo no válido.")
            return

        try:
            ruta1 = comprobar_fichero(self.fichero1.get())
            ruta2 = comprobar_fichero(self.fichero2.get())

            hash1 = calcular_hash(ruta1, self.algoritmo.get())
            hash2 = calcular_hash(ruta2, self.algoritmo.get())

            self.texto_resultado.insert(
                tk.END,
                f"Fichero 1:\n{hash1}\n\n"
                f"Fichero 2:\n{hash2}"
            )

            if hash1 == hash2:
                self.etiqueta_comparacion.config(
                text="IGUALES", fg="green"
            )
            else:
                self.etiqueta_comparacion.config(
                text="DIFERENTES", fg="red"
                )

        except OSError as error:
            messagebox.showerror("Error", str(error))


def main():
    ventana = tk.Tk()
    app = ComparadorHashes(ventana)
    ventana.mainloop()


if __name__ == "__main__":
    main()
