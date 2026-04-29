#! /usr/bin/env python3
"""Script para aprender o tratamento de erros
"""
__version__ = "0.1.0"

import sys
import os

# EAFP - Easy to Ask Forgiveness than permission
try:
    names = open("names.txt").readlines() # FileNotFoundError
    # 1 / 1 # ZeroDivisionError
    # print(names.append) # AttributeError
except FileNotFoundError as e:
    print(f"{str(e)}.")
    sys.exit(1)
    # TODO: Usar retry
else:
    print("Success")
finally:
    print("Always executes")


try:
    print(names[0])
except:
    print("[Error] Missing name in the list")
    sys.exit(1)
