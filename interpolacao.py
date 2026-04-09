#!/usr/local/python env

clientes = ["Alvaro", "Miguel", "Castanheira"]

email_tmpl = """
Olá, %(nome)s

Tem interesse em adquirir uma %(produto)s?

Este produto é ideal para garantir %(texto)s

Clique agora em %(link)s

Apenas %(quantidade)d disponiveis!
 
Preco promocial %(preco).2f
 """

for cliente in clientes:
    print(email_tmpl
      % {
      "nome": cliente,
      "produto": "rato",
      "texto": "sessões de trabalho sem se preocupar com a ergonomia.",
      "link": "https://link-exmplo.com",
      "quantidade": 3,
      "preco": 30.99,
      }
 )
  
