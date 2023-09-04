import sys

""" clase09_ej1.py"""

args = sys.argv[1:]

if len(args) != 3:
    raise Exception("Error en la cantidad de parametros ( != 3)")

for i in args:
    print("param", i, ": ", i)
