#!/usr/bin/env python3
""" Hello World Multi Linguas

Dependendo da lingua configurada no ambiente o programa exibe a mensagem
correspondente.

Utilização:
Ter a variável LANG devidamente configurada:

    export LANG=pt_PT

Execução:

    python3 hello.py
    ou
    ./hello.py
"""
__version__ = "0.0.1"
__author__ = "Álvaro Castanheira"
__licence__ = "Unlicense"

import os

current_language = os.getenv("LANG", "en_US")[:5] 

msg  = "Hello, World!"

if current_language == "pt_PT":
    msg = "Olá, Mundo!"
elif current_language == "it_IT":
    msg = "Ciao, Mondo!"
elif current_language == "es_SP":
    msg = "Hola, Mundo!"
elif current_language == "fr_FR":
    msg = "Bonjor Monde!"    


print(msg) 
