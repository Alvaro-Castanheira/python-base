#!/usr/local/env python3
"""Caluladora prefix

Instruções:

[operaçao] [n1] [n2]

Operações:
sum -> +
sub -> -
mul -> *
div -> /

Utilização:
$ prefixcalc.py sum 5 2
7

$ prefixcalc.py mul 10 5 
50

$ prefixcalc.py
operação: sum
n1: 5
n2: 4
20
"""
__version__: "0.1.0"

import sys

debug = False

args = { 
    "operation": sys.argv[1],
    "n1": int(sys.argv[2]),
    "n2": int(sys.argv[3]),
}

operacoes = {
    "sum": "+",
    "sub": "-",
    "mul": "*",
    "div": "/",
}

if debug:
    print("DEBUG")
    print(sys.argv[1],sys.argv[2],sys.argv[3])
    print(args)


if args["operation"] not in operacoes:
    print("Não passou uma operação válida")

if args["operation"] == "sum":
    conta = args["n1"] + args["n2"]
    print(conta)
elif args["operation"] == "sub":
    conta = args["n1"] - args["n2"]
    print(conta)
elif args["operation"] == "mul":
    conta = args["n1"] * args["n2"]
    print(conta)
elif args["operation"] == "div":
    conta = args["n1"] / args["n2"]
    print(conta)


