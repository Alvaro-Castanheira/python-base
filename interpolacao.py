#!/usr/local/python env
"""Imprime a mensagem de um email

Atrevés de um template
"""
__version__="0.1.1"

import os
import sys

arguments = sys.argv[1:]
if not arguments:
    print("Indique o ficheiro com os emails")
    sys.exit(1)
    
filename = arguments[0]
templatename = arguments[1]

path = os.curdir
filepath = os.path.join(path, filename) # emails.txt
templatepath = os.path.join(path, templatename) # email_tmpl.txt


clientes = []
for line in open(filepath):
    name, email = line.split(",")


    # TODO: Substituir por envio de email
    print(f"Enviando email para: {email}")
    print()
    print(
      open(templatepath).read()
      % {
      "nome": name,
      "produto": "rato",
      "texto": "sessões de trabalho sem se preocupar com a ergonomia.",
      "link": "https://link-exmplo.com",
      "quantidade": 3,
      "preco": 30.99,
      }
    )
    print("-" * 50)
  
