from genericpath import isdir, isfile
import os
import hashlib
import sys

HASH_LENGTH = 128 # md5 tiene 128 bits
args = sys.argv
if len(args) != 3:
    print(args)
    print("Este comando necesita 1 solo argumento, que es el hash que se desea buscar.")
    print("Se usa así: python3 encuentra_hash.py archivos 0xe5ed313192776744b9b93b1320b5e268")
    exit()
else:
    NOMBRE_CARPETA = args[1]
    HASH = int(args[2], base=16).to_bytes(HASH_LENGTH//8, "big")
if os.path.isfile(NOMBRE_CARPETA):
    print(f"Comparando hash de {NOMBRE_CARPETA}")
    archivos = [NOMBRE_CARPETA]
elif os.path.isdir(NOMBRE_CARPETA):
    print(f"Buscando en la carpeta {NOMBRE_CARPETA}")
    entradas = os.listdir(NOMBRE_CARPETA)
    archivos = []
    for archivo in entradas:
        archivos.append(f"{NOMBRE_CARPETA}/{archivo}")
else:
    print(f"No se encuentra el archivo o carpeta {NOMBRE_CARPETA}")
    archivos = []

for nombre_archivo in archivos:
    with open(nombre_archivo, "rb") as f:
        archivo = f.read()
    hash = hashlib.md5(archivo).digest()
    if hash == HASH:
        print(f"Encontrado: el hash de {nombre_archivo} coincide")
