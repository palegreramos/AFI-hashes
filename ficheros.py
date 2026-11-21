from pathlib import Path


def comprobar_fichero(fichero):
    ruta = Path(fichero)

    if not ruta.is_file():
        raise FileNotFoundError("El fichero no existe o no es un archivo.")

    return ruta