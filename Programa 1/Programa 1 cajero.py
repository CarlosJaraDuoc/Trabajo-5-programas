import os
import time
clean = "cls"
saldo = 1000
contador_Intentos = [1, 3] 
respuesta = 0
claveCajero = """abc"""
os.system(clean)
with open("UsuarioCajero.txt", "w") as contraseña:
    contraseña.write(claveCajero)
with open("UsuarioCajero.txt", "r") as contraseña:
    claveR = contraseña.read()
    while True:
        try:       
            clave = input(f"Escriba su contraseña, le quedan {contador_Intentos[1]} intentos: ")
            if clave == claveR:
                print("Sesión iniciada")
                break
            else:
                contador_Intentos[0] += 1
                contador_Intentos[1] -= 1
                if contador_Intentos[0] > 3:
                    print("has fallado los 3 intentos")
                    respuesta = 4
                    break
                else:
                    print("La contraseña es incorrecta, vuelva a intentarlo")
        except ValueError:
            print("Error encontrado, vuelva a intentarlo")
            continue

def menu():
    print("Bienvenido al Banco del País, seleccione una opción")
    print("1. Consultar Saldo")
    print("2. Depositar Dinero")
    print("3. Girar Dinero")
    print("4. Salir")

def consultarSaldo():
    print("Tu saldo actual es de: $", int(saldo), sep="")

def depositDinero():
    while True:
        try:
            global saldo
            cant_deposito = float(input("Ingrese la cantidad a depositar: $"))
            if cant_deposito <=0:
                print("No puede depositar 0 o menos")
                break
            saldo = cant_deposito + saldo
            print("Has depositado: $",int(cant_deposito),"\nNuevo saldo: $",int(saldo), sep="")
            return saldo
        except ValueError:
            print("Valor no válido, vuelva a intentar")
            continue

def girarDinero():
    while True:
        try:
            global saldo
            cant_retiro = float(input("Ingrese la cantidad a retirar: $"))
            if cant_retiro <= 0:
                print("No puede depositar 0 o menos")
                break
            elif cant_retiro <= saldo:
                saldo -= cant_retiro
                print("Has retirado: $",int(cant_retiro),"\nNuevo saldo: $",int(saldo), sep="")
                return saldo
            else:
                print("No es posible realizar el retiro, saldo insuficiente.")
                break
        except ValueError:
            print("Valor no válido, vuelva a intentar")
            continue

def salir():
    global respuesta
    print("Gracias por utilizar el cajero.")
    respuesta = 4

while respuesta != 4:
    try:
        time.sleep(3)
        os.system(clean)
        menu()
        op = int(input())
    except ValueError:
        print("Valor incorrecto, vuelva a intentarlo")
        continue
    if op == 1:
        consultarSaldo()
    elif op == 2:
        depositDinero()
    elif op == 3 and saldo <= 0:
        print("No puede girar con su cuenta en 0")
        continue
    elif op == 3 and saldo > 0:
        girarDinero()
    elif op == 4:
        salir()
        time.sleep(2)
    else:
        print("Opción no válida, eliga un valor entre (1-4)")
        continue