import sys
import datetime
import random
import os
''' Clase09_ej2'''

args = sys.argv[1:]

def generar():
    # timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    temp = round(random.normalvariate(20, 15), 1)
    humidity = round(random.random()*100, 1)
    rain = bool(random.getrandbits(1))

    return (timestamp, temp, humidity, rain)

def generar_n(n):
    for i in range(n):
        print(", ".join([str(i) for i in generar()]))        

def generar_archivo(temp, humidity, rain):
    modo = "w"
    if os.path.isfile("clase09_ej2.csv"):
        modo = "a"
    else:
        with open("clase09_ej2.csv", modo) as f:
            f.write("timestamp, temp, humidity, rain\n")
            f.close()
            modo = "a"
    
    fichero = "clase09_ej2.csv"

    with open(fichero, modo) as f:
            tmstp = round(datetime.datetime.timestamp(datetime.datetime.now()), 0)
            f.write(f"{tmstp}, {temp}, {humidity}, {rain}\n")
    f.close()

if len(args) == 1:
    it = args[0]    
    try:
        it = int(it)
        generar_n(it)        
    except ValueError:
        generar_n(1)
elif len(args) == 3:
    generar_archivo(*args)

