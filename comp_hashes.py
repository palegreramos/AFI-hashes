from ficheros import comprobar_fichero
from hashes import calcular_hash, ALGORITMOS


def main():
    
    fichero1 = input("Introduce el primer fichero: ").strip()
    fichero2 = input("Introduce el segundo fichero: ").strip()

    print("Algoritmos disponibles:", ", ".join(ALGORITMOS))
    algoritmo = input("Introduce el algoritmo (por defecto sha256): ").strip().lower()

    if algoritmo == "":
        algoritmo = "sha256"

    if algoritmo not in ALGORITMOS:
        print("Error: algoritmo no válido.")
        return

    try:
        ruta1 = comprobar_fichero(fichero1)
        ruta2 = comprobar_fichero(fichero2)

        hash1 = calcular_hash(ruta1, algoritmo)
        hash2 = calcular_hash(ruta2, algoritmo)

        print(f"{ruta1}: {hash1}")
        print(f"{ruta2}: {hash2}")

        if hash1 == hash2:
            print("Los hashes son IGUALES.")
        else:
            print("Los hashes son DIFERENTES.")

    except OSError as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    main()
