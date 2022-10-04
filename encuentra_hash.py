import os
import hashlib

NOMBRE_CARPETA = "archivos"
HASH_LENGTH = 128 # md5 tiene 128 bits
HASH = 0xe5ed313192776744b9b93b1320b5e268.to_bytes(HASH_LENGTH//8, "big")
archivos = os.listdir(NOMBRE_CARPETA)
for nombre_archivo in archivos:
    with open(f"{NOMBRE_CARPETA}/{nombre_archivo}", "rb") as f:
        archivo = f.read()
    hash = hashlib.md5(archivo).digest()
    if hash == HASH:
        print(f"Encontrado: {nombre_archivo}")
