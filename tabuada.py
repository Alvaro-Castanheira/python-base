#!/usr/bin/env python
"""Imprime a tabudada do 1 ao 10.

---Tabudada do 1---

    1 x 1 = 1
    2 x 1 = 2
    3 x 1 = 3
...
##################
---Tabuada do 2---
 
    1 x 1 = 2
    2 x 2 = 4
    3 x 3 = 6
....
##################
 """
__version__ = "0.1.1"
__author__ = "Álvaro Castanheira"

#numeros = [1, 2, 3, 4, 5 , 6, 7, 8,9 ,10]
#Este objeto é Iterable (iteráveis)
numeros = list(range(1, 11))

for n1 in numeros:
    print()
    print("{:-^18}".format(f"Tabuada do {n1}"))
    for n2 in numeros:
        resultado = n1 * n2
        print("{:^18}".format(f"{n1} x {n2} = {resultado}"))
    print()
    print("#" * 18)
