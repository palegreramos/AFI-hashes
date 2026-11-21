from ficheros import comprobar_fichero
from hashes import calcular_hash, ALGORITMOS

def main():
    fichero = input("Introduce el nombre o ruta del fichero: ").strip()

    print("Algoritmos disponibles:", ", ".join(ALGORITMOS))
    algoritmo = input("Introduce el algoritmo (por defecto sha256): ").strip().lower()

    if algoritmo == "":
        algoritmo = "sha256"

    if algoritmo not in ALGORITMOS:
        print("Error: algoritmo no válido.")
        return

    try:
        ruta = comprobar_fichero(fichero)
        resultado = calcular_hash(fichero, algoritmo)

        print(f"Fichero: {fichero}")
        print(f"{algoritmo.upper()}: {resultado}")

    except OSError as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    main()
