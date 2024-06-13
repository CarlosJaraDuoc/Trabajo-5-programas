import os
import time
import csv
pedido = 1
camion = 450
kilosT = 0
total = 0
try:
    with open ("listaCilindros.csv", "x") as cilindros:
        cilindrosW = csv.writer(cilindros)
        print("lista creada... Cargando.")
except FileExistsError:
    print("Lista ya existente... Cargando.")

with open ("listaCilindros.csv", "r") as cilindros:
    cilindrosR = csv.reader(cilindros)
    nomC = next(cilindrosR, 0)
    if nomC != (["Tipo de cilindro", "Capacidad (kilos)"]):
        with open ("listaCilindros.csv", "w", newline="") as cilindros:
            cilindrosW = csv.writer(cilindros)
            cilindrosW.writerow(["Tipo de cilindro", "Capacidad (kilos)"])
            cilindrosW.writerows([["Cilindros de 5", 5], ["Cilindros de 15", 15], ["Cilindros de 45", 45]])

def usuario():
    while True:
        nombre = input("Ingrese su nombre, debe tener mínimo 3 letras: ")
        if nombre.isdecimal():
            print("Solo puede ingresar letras, vuelva a intentarlo.")
        elif len(nombre) >= 3:
            print("Nombre ingresado correctamente.")
            return nombre
        else:
            print("El nombre debe tener mínimo 3 letras")

def usuario_num():
    while True:
        telefono = input("Ingrese su número telefónico, debe tener entre 8 y 9 dígitos: ")
        if telefono.isdigit() and 8 <= len(telefono) <= 9:
            print("Telefono ingresado correctamente.")
            return telefono
        elif telefono.isalpha():
            print("No puede ingresar letras, vuelva a intentarlo")
        else:
            print("El número telefónico debe tener entre 8 y 9 dígitos, vuelva a intentarlo.")

def op_camiones():
    while True:
        try:
            cantCamiones = int(input("¿Cuantos camiones desea comprar?: "))
            if cantCamiones > 0:
                return cantCamiones
            else:
                print("Valor ingresado menor o igual a 0, vuelva a intentarlo")
        except ValueError:
                print("Valor ingresado no válido, vuelva a intentarlo")
        
def op_cilindros():
    with open("listaCilindros.csv", "r") as cilindros:
        cilindrosR = csv.reader(cilindros)
        next(cilindrosR)
        cilindrosInfo = list(cilindrosR)

    def cantCilindros(tipo):
        while True:
            try:
                cantidad = int(input(f"¿Cuantos cilindros de {tipo} kilos desea comprar?: "))
                return cantidad
            except ValueError:
                print("Valor ingresado no válido, vuelva a intentarlo")   
    cil5 = cantCilindros(5)
    cil15 = cantCilindros(15)
    cil45 = cantCilindros(45)                     
    cil5T = cil5 * int(cilindrosInfo[0][1])
    cil15T = cil15 * int(cilindrosInfo[1][1])
    cil45T = cil45 * int(cilindrosInfo[2][1])
    return cil5T + cil15T + cil45T

while pedido != 2:
    time.sleep(2) 
    os.system("cls")
    print("Bienvenido a la distribuidora de gas")
    nombre = usuario()
    telefono = usuario_num()
    while True:
        try:
            time.sleep(2)
            os.system("cls")
            print("_________________________________________\n")
            print("Eliga una opción:\n1. Compra de camiones\n2. Compra de cilindros de gas\n3. Imprimir boleta y terminar pedido")
            print("_________________________________________\n")
            op = int(input())               
            if op == 1:
                cantCamiones = op_camiones()
                kilosT += camion * cantCamiones 
                Total = (kilosT // camion) * 100000 + (kilosT % camion) * 1700
                continue                        
            elif op == 2:
                kilosT += op_cilindros()
                Total = (kilosT // camion) * 100000 + (kilosT % camion) * 1700
                continue                
            elif op == 3:
                if kilosT <= 0:
                    print("No puede imprimir boleta sin haber ordenado kilos.")
                    continue
                else:
                    cantCamiones = kilosT // camion if kilosT % camion == 0 else (kilosT // camion) + 1
                    print("_________________________________________\n")
                    print(f"Cliente: {nombre}\nTeléfono: {telefono}\nCantidad de kilos: {kilosT}\nCamiones: {cantCamiones}\nValor total: {Total}")
                    print("_________________________________________\n")
                    time.sleep(2)
                    break 
            else:
                print("Debe ingresar un número entre (1-3)")
                continue                   
        except ValueError:
                print("Valor ingresado no válido, vuelva a intentarlo")
                continue
    while True:
        try:
            time.sleep(2)
            os.system("cls")
            pedido = int(input("¿Desea hacer otro pedido?\n1. Sí \n2. No\n"))
            if pedido == 1:
                with open ("listaCilindros.csv", "w", newline="") as cilindros:
                    cilindrosW = csv.writer(cilindros)
                    cilindrosW.writerow(["Tipo de cilindro", "Capacidad (kilos)"])
                    cilindrosW.writerows([["Cilindros de 5", 5], ["Cilindros de 15", 15], ["Cilindros de 45", 45]])
                kilosT = 0
                total = 0
                break
            elif pedido == 2:
                print("Muchas gracias por usar nuestro programa.")
                break
            else:
                print("Debe ingresar un valor entre el rango (1-2)")
        except ValueError:
            print("Valor ingresado no válido, vuelva a intentarlo")