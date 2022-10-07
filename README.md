Este repositorio contiene 2 programas. descifra.py y encuentra_hash.py

# descifra.py
## Descripción
Herramienta que ayuda a descifrar mensajes cifrados con un métodod de diccionario (cada letra se corresponde a otra letra)
## Utilizamiento
1. El comando se utiliza así: `python3 descifra.py <nombre de archivo>`
    * Ejemplo: `python3 descifra.py msg.txt`
2. Cambiar `translated_chars` (en la línea 111) `translated_chars = list("...")` para definir los caracteres que se han cifrado.
3. Ejecutar el código e ir cambiando `found_chars` en la línea 41 `found_chars = {...}` (es un diccionario, no un set), a medida que se van descubriendo a que letra se corresponde cada letra.

# encuentra_hash.py
## Descripción
Dada una carpeta llena de archivos y un hash (md5), encuentra el archivo al que le corresponde ese hash.
## Utilizamiento
`python3 <nombre de archivo/carpeta> <hash>`

El hash debe estar en formato hexadecimal.

Ejemplos válidos:
* `python3 encuentra_hash.py archivos 0xe5ed313192776744b9b93b1320b5e268`
* `python3 encuentra_hash.py imagen26.jpg 0xe5ed313192776744b9b93b1320b5e268`

Cambio para tener firmado1