#! /usr/bin/env python3
"""Script para aprender o tratamento de erros
"""
__version__ = "0.1.0"

import sys
import os
# LBYL - Look Before you Leap
if os.path.exists("names.txt"):
    print("The file exists")
    input("...") # Race Condition
    names = open("names.txt").readlines()
else:
    print("[Error] File names.txt not found.")
    sys.exit(1)

# LBYL - Look Before you Leap
if len(names) >= 3:
    print(names[2])
else:
    print("[Error] Missing name in the list")
    sys.exit(1)
