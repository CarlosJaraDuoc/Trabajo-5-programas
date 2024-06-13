import os
import time
import json
clean = "cls"
sushi = 0
total = 0
descuento = 0
respuesta = 1
cantP = 0
cantO = 0
cantV = 0
cantA = 0
volver = ""

catalogoSushis = [
    ["PikaRoll", 4500],
    ["OtakuRoll", 5000],
    ["PulpoRoll", 5200],
    ["AnguilaRoll", 4800]
]

contadorSushis = [
    ["sushiP", 1],
    ["sushiO", 1],
    ["sushiV", 1],
    ["sushiA", 1]
]

with open ("SushiMenu.json", "w") as catalogo:
    json.dump(catalogoSushis,catalogo)

with open ("SushiMenu.json","r", newline="") as catalogo:
    catalogoL = json.load(catalogo)

with open ("SushiContadores.json", "w") as contador:
    json.dump(contadorSushis, contador)

with open ("SushiContadores.json", "r", newline="") as contador:
    contadorL = json.load(contador)

def menu():
    print("Bienvenido al delivery de Sushis")
    print("Seleccione el tipo de Sushi: ")
    print("1. Pikachu Roll $4500 ")
    print("2. Otaku Roll $5000 ")
    print("3. Pulpo Venenoso Roll $5200 ")
    print("4. Anguila Eléctrica Roll $4800 ")
    print("5. Proceder a pago")

def pikachu():
    global sushi, total, cantP
    total += catalogoL[0][1]
    sushi += 1
    cantP += contadorL[0][1]
    return (sushi, cantP, total)

def otaku():
    global sushi, total, cantO
    total += catalogoL[1][1]
    sushi += 1
    cantO += contadorL[1][1]
    return (sushi, cantO, total)

def pulpo():
    global sushi, total, cantV
    total += catalogoL[2][1]
    sushi += 1
    cantV += contadorL[2][1]
    return (sushi, cantV, total)

def anguila():
    global sushi, total, cantA
    total += catalogoL[3][1]
    sushi += 1
    cantA += contadorL[3][1]
    return (sushi, cantA, total)

def menuDescuento():
    print("¿Posee código de descuento?")
    print("1. Si")
    print("2. No")

def boleta():
    global total, descuento
    print ("******************************")
    print(f"TOTAL PRODUCTOS:{sushi}")
    print ("******************************")
    print(f"Pikachu Roll : {cantP}")
    print(f"Otaku Roll : {cantO}")
    print(f"Pulpo Venenoso Roll : {cantV}")
    print(f"Anguila Eléctrica Roll : {cantA}")
    print ("******************************")
    print(f"Subtotal por pagar: ${total}")
    print("Descuento por código: $",int(descuento))
    total -= descuento
    print("TOTAL: $",int(total))

def desc():
    global descuento, codigo, total, nomDescuento, volver
    while codigo == 1:
        try:
            os.system(clean)
            time.sleep(1)
            nomDescuento = input("Ingrese el código de descuento: ")
            if nomDescuento == "soyotaku":
                descuento = total * 0.10
                print (f"Ha obtenido un 10% de descuento")
                break
            else:
                print("código no válido")
                while True:
                    print("¿Desea reingresar el código?")
                    print ("V = Sí")
                    print ("X = Volver al menú")
                    volver = input("")
                    volver = volver.upper()
                    if volver == "V":
                        break
                    elif volver == "X":
                        break
                    elif volver.isnumeric():
                        print("No puedes ingresar números")
                        continue
                    else:
                        print("Valor inválido, vuelva a intentarlo")
                        continue
                if volver == "V":
                        continue
                elif volver == "X":
                        break
        except ValueError:
            print("No ha ingresado un valor correcto")
            continue
    else:
        os.system(clean)
        time.sleep(1)

while respuesta != 2:
    try:
        time.sleep(2)
        os.system(clean)
        menu()
        tipo = int(input())
        if tipo == 1:
            pikachu()
            continue
        elif tipo == 2:
            otaku()
            continue
        elif tipo == 3:
            pulpo()
            continue
        elif tipo == 4:
            anguila()
            continue
        elif tipo == 5 and total <= 0:
            print("No puede realizar un pedido con la canasta vacia, vuelva a intentarlo.")
            continue
        elif tipo == 5 and total > 0:
            print("Procesando pedido...")
        else:
            print("Ingrese un valor dentro del rango (1-5)")
            continue
        while True:
            try:
                menuDescuento()
                codigo = int(input())
                if codigo <= 0 or codigo >=3:
                    print("Ingrese un valor dentro del rango (1-2)")
                    continue
                else:
                    break
            except ValueError:
                print("Ingrese un valor correcto")
                continue
    except ValueError:
        print("Ingrese un número válido")
        continue
    os.system(clean)
    time.sleep(2)
    if codigo == 1: 
        desc()
    if volver == "X":
        continue
    boleta()
    
    while respuesta != 2:
        try:
            print("¿Desea realizar otro pedido?")
            print("1. Si")
            print("2. No")
            respuesta = int(input())
            if respuesta == 2:
                print("Gracias por usar el programa.")
            elif respuesta == 1:
                os.system(clean)
                time.sleep(1)
                sushi = 0
                total = 0
                descuento = 0
                respuesta = 1
                cantP = 0
                cantO = 0
                cantV = 0
                cantA = 0
                volver = ""
                break
            else:
                print("Ingrese un número dentro del rango (1 - 2)")
                continue
        except ValueError:
            print("Ingrese un número válido")
            continue