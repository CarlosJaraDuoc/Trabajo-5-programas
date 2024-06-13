import os
import time
import csv

try:
    with open ("InfoUsuarios.csv", "x") as info:
        infoW = csv.writer(info)
except FileExistsError:
    pass

with open ("InfoUsuarios.csv", "r") as info:
    infoR = csv.reader(info)
    titulo = next(infoR, 0)
    if titulo != ["Nombre", "Edad", "Ciudad", "Pais", "Sexo"]:
        with open ("InfoUsuarios.csv", "a") as info:
            infoW = csv.writer(info)
            infoW.writerow(["Nombre", "Edad", "Ciudad", "Pais", "Sexo"]) 

def data():
    while True:
        try:
            nombre = input("Ingrese su nombre: ")
            edad = int(input("Ingrese su edad: "))
            ciudad = input("Ingrese su ciudad: ")
            pais = input("Ingrese su pais: ")
            sexo = input("Ingrese su sexo: ")
            with open ("InfoUsuarios.csv", "a") as info:
                infoW = csv.writer(info)
                infoW.writerows([
                [nombre, edad, ciudad, pais, sexo]
                ])
            break
        except ValueError:
            print("Valor incorrecto, vuelva a ingresar los datos")

while True:
    time.sleep(2)
    os.system("cls")
    try:
        print("Eliga su opción: ")
        print("1. Ingresar datos")
        print("2. Revisar usuarios registrados")
        print("3. Salir")
        op = int(input())
        if op == 1:
            data()
        elif op == 2:        
            with open ("InfoUsuarios.csv", "r", newline="") as info:
                infoR = csv.reader(info)
                for i in infoR:
                    if i:
                        print(", ".join(i))
            time.sleep(2)
        elif op == 3:
            print("Gracias por usar el programa.")
            time.sleep(2)
            os.system("cls")
            break
        else:
            print("Ingrese una opción entre (1-3)")
            continue
    except ValueError:
        print("Valor ingresado incorrecto, vuelva a intentarlo.")
        continue