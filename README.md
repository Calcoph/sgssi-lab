Este repositorio contiene 2 programas. descifra.py y encuentra_hash.py

# descifra.py
## Descripción
Herramienta que ayuda a descifrar mensajes cifrados con un métodod de diccionario (cada letra se corresponde a otra letra)
## Utilizamiento
1. poner el mensaje en msg.txt al mismo nivel que descifra.py. De esta manera:
```
carpeta
├─msg.txt
└─descifra.py
```
2. Cambiar `translated_chars` (en la línea 111) `translated_chars = list("...")` para definir los caracteres que se han cifrado.
3. Ejecutar el código e ir cambiando `found_chars` en la línea 41 `found_chars = {...}` (es un diccionario, no un set), a medida que se van descubriendo a que letra se corresponde cada letra.

# encuentra_hash.py
## Descripción
Dada una carpeta llena de archivos y un hash (md5), encuentra el archivo al que le corresponde ese hash.
## Utilizamiento
1. Poner la carpeta con archivos al mismo nivel que descifra.py. Se tiene que llamar "archivos". De esta manera:
```
carpeta
├─archivos
│ ├─archivo1
│ ├─archivo2
│ ├─archivo3
│ │ ...
│ └─archivon
└─encuentra_hash.py
```
2. Cambiar el HASH en la línea 6 `HASH = ...`
3. Si se quiere usar otro algoritmo, hay que cambiar `HASH_LENGTH` (línea 5) y `hash = hashlib.<ALGORITMO>(archivo).digest()` (línea 11)
