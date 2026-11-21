
import hashlib
from pathlib import Path

# for algoritmo in sorted(hashlib.algorithms_available):
#     print(algoritmo)

ALGORITMOS = ["md5", "sha1", "sha256", "sha512", "sha3_256", "sha3_512"]

def calcular_hash(fichero, algoritmo="sha256"):
    ruta = Path(fichero)

    if not ruta.is_file():
        raise FileNotFoundError("El fichero no existe o no es un archivo.")

    with ruta.open("rb") as f:
        resultado = hashlib.file_digest(f, algoritmo).hexdigest()

    return resultado
