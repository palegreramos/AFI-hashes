
import argparse
from ficheros import comprobar_fichero
from hashes import calcular_hash, ALGORITMOS


def main():
    parser = argparse.ArgumentParser(
        description="Calculadora de hashes"
    )

    parser.add_argument(
        "fichero",
        help="Fichero del que calcular el hash"
    )

    parser.add_argument(
        "-a", "--algoritmo",
        default="sha256",
        choices=ALGORITMOS,
        help="Algoritmo de hash (por defecto SHA256)"
    )

    args = parser.parse_args()

    try:
        ruta = comprobar_fichero(args.fichero)
        resultado = calcular_hash(ruta, args.algoritmo)

        print(f"Fichero: {ruta}")
        print(f"{args.algoritmo.upper()}: {resultado}")

    except OSError as error:
        parser.exit(1, f"Error: {error}\n")


if __name__ == "__main__":
    main()
