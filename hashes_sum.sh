#!/bin/bash

if [ $# -lt 2 ] || [ $# -gt 3 ]; then
    echo "Uso: $0 fichero1 fichero2 [algoritmo]"
    exit 1
fi

fichero1="$1"
fichero2="$2"

if [ ! -f "$fichero1" ] || [ ! -f "$fichero2" ]; then
    echo "Error: uno o ambos ficheros no existen."
    exit 1
fi

#algoritmo por defecto es sha256 si no se proporciona
algoritmo=${3:-sha256}

case "$algoritmo" in
    md5|sha1|sha256|sha512) ;;
    *)
        echo "Error: algoritmo no válido."
        exit 1
        ;;
esac

echo "Calculando hashes usando el algoritmo $algoritmo..."

hash1=$("${algoritmo}sum" "$fichero1" | cut -d ' ' -f1)
hash2=$("${algoritmo}sum" "$fichero2" | cut -d ' ' -f1)

if [ -z "$hash1" ] || [ -z "$hash2" ]; then
    echo "Error: no se ha podido calcular alguno de los hashes."
    exit 1
fi

echo "$fichero1: $hash1"
echo "$fichero2: $hash2"

if [ "$hash1" = "$hash2" ]; then
    echo "Los hashes son IGUALES."
else
    echo "Los hashes son DIFERENTES."
fi
