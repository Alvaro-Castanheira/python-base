#!/usr/local/env python3
"""Stock de frutas"""
__version__ = "0.1.0"

stock = {
    "banana": 3,
    "maça": 1,
    "pera": 2,
}

print(stock)

for fruta, quantidade in stock.items():
    print(f"Temos {quantidade} de {fruta} em stock.")
