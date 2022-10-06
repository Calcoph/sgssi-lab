# Aviso: el código es bastante ineficiente, pero cumple su función
from typing import Tuple

def get_freq_vec() -> list[str]:
    """
    Por defecto, devuelve una lista con las letras en orden según su frecuencia en el castellano.
    A medida que se encuentran letras, se van añadiendo a found_chars.
    
    # Ejemplo:
    Si sabemos que el mensaje es "un coche",
    pero el programa devuelve "pn coche", tendremos que añadir `p: u` a found_chars
    """
    # Solución del labo:
    # found_chars = {
    #     "a": "a",
    #     "q": "f",
    #     "u": "c",
    #     "r": "d",
    #     "e": "e",
    #     "y": "b",
    #     "v": "g",
    #     "j": "h",
    #     "s": "i",
    #     "h": "j",
    #     "k": "k",
    #     "d": "l",
    #     "p": "m",
    #     "n": "n",
    #     "l": "o",
    #     "m": "p",
    #     "b": "q",
    #     "o": "r",
    #     "t": "t",
    #     "c": "s",
    #     "i": "u",
    #     "g": "y",
    #     "z": "z",
    #     "f": "v",
    #     "ñ": "x"
    # }
    found_chars = {
    }
    freq_vec = [
        'e',
        'a',
        'o',
        'l',
        's',
        'n',
        'd',
        'r',
        'u',
        'i',
        't',
        'c',
        'p',
        'm',
        'y',
        'q',
        'b',
        'h',
        'g',
        'f',
        'v',
        'j',
        'ñ',
        'z',
        'x',
        'k',
        'w',
    ]
    final_vec = []
    for i in freq_vec:
        if i in found_chars.keys():
            final_vec.append(found_chars[i])
        else:
            final_vec.append(i)

    return final_vec

def is_registered(char: str, chars: list[str]) -> bool:
    registered = False
    for c, _ in chars:
        if c == char:
            registered = True
            break
    return registered

def get_msg_charcount(msg: str) -> list[Tuple[str, int]]:
    chars = []
    for char in msg:
        if is_registered(char, chars):
            for index, (c, count) in enumerate(chars):
                if c == char:
                    chars[index] = (c, count+1)
                    break
        else:
            chars.append((char, 1))
    
    return chars

def find_index(l: list[Tuple[str, int]], char: str) -> int:
    for index, (i, _) in enumerate(l):
        if i == char:
            return index

freq_table = get_freq_vec()
with open("msg.txt", "r") as f:
    msg = f.read()
char_count = get_msg_charcount(msg)
translated_chars = list("abcdefghijklmnopqrstuvwxyz")

char_count = filter(lambda x: x[0].lower() in translated_chars, char_count)
ordered_chars = sorted(char_count, key=lambda x: x[1], reverse=True)

translated_msg = ""
for i in msg:
    if i.lower() in translated_chars:
        index = find_index(ordered_chars, i)
        translated_msg += freq_table[index]
    else:
        translated_msg += i

print(translated_msg)
print()
found_q = False
some_q = False
some_fails = False
for i in translated_msg:
    if found_q:
        if i != "u":
            some_fails = True
            print("No todas las Q van seguidas de 1 U")
        found_q = False
    elif i == "q":
        found_q = True
        some_q = True

if not some_q:
    print("No se ha encontrado ninguna Q")
elif not some_fails:
    print("Todas las Q van seguidas de 1 U")
