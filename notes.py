#!/usr/bin/env python3
"""Bloco de notas
$ notes.py new "Minha Nota"
tag: tech
text: 
Anotações sobre carreira de DevOps

$ notes.py read tech
...
...

"""
__version__= "0.1.0"

import os
import sys

path = os.curdir
filepath = os.path.join(path, "notes.txt")
cmds = ("read", "new")

arguments = sys.argv[1:]
if not arguments:
    print("Invalid usage")
    print(f"Usage:notes.py {cmds} [ARGS]")
    sys.exit(1)


if arguments[0] not in cmds:
    print(f"Invalid command {arguments[0]}")
    print(f"Avaliable commands: {cmds}")

if arguments[0] == "read":
    # leitura das notas

    for line in open(filepath):
        title, tag, text = line.split("\t")
        if tag.lower() == arguments[1].lower():
            print(f"title: {title}")
            print(f"text: {text}")
            print("-" * 30)
            print()
            
if arguments[0] == "new":
    title = arguments[1] # TODO: Tratar exception
    text = [
        f"{title}",
        input("tag:").strip(),
        input("text:\n").strip(),
    ]
    # \t - tsv
    with open(filepath, "a") as file_:
        file_.write("\t".join(text) + "\n")
