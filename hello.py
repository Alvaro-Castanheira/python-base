#!/usr/bin/env python3
""" Hello World Multi Linguas

Dependendo da lingua configurada no ambiente o programa exibe a mensagem
correspondente.

Utilização:
Ter a variável LANG devidamente configurada:

    export LANG=pt_PT

Ou informe através o CLI argument "--lang="

Ou o utilizar terá de inserir.

Execução:

    python3 hello.py
    ou
    ./hello.py
"""
__version__ = "0.1.4"
__author__ = "Álvaro Castanheira"
__licence__ = "Unlicense"

import os
import sys

arguments = {
    "lang": None,
    "count": 1,
}

for arg in sys.argv[1:]:
    # TODO: Tratar ValueError
    key, value = arg.split("=")
    key = key.lstrip("-").strip()
    value = value.strip()
    if key not in arguments:
        print(f"Invalid Option ´{key}´")
        sys.exit()
    arguments[key] = value


current_language = arguments["lang"]
if current_language is None:
    # TODO: Usar repetição 
    if "LANG" in os.environ:
        current_language = os.getenv("LANG")
    else:
        current_language = input("Choose a language:")


        
current_language = current_language[:5]
    
# sets(Hash table) - O(1) - constante
# dicts(hash table) - O(1)

#msg  = "Hello, World!"

msg = {
    "en_US": "Hello World!",
    "pt_PT": "Olá, Mundo!",
    "it_IT": "Ciao, Mondo!",
    "es_SP": "Hola, Mundo!",
    "fr_FR": "Bonjor Monde",
}

# Ordem de complexiade deste algoritmo O(n) sendo o n o número de testes feito
# if current_language == "pt_PT":
#     msg = "Olá, Mundo!"
# elif current_language == "it_IT":
#     msg = "Ciao, Mondo!"
# elif current_language == "es_SP":
#     msg = "Hola, Mundo!"
# elif current_language == "fr_FR":
#     msg = "Bonjor Monde!"    


print(
    msg[current_language] * int(arguments["count"])
    ) 
