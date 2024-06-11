import os
import time
import json

ratingJuegos = {
    "Ajedrez": 0,
    "Super Mario Bros": 0,
    "DOOM": 0,
    "Half-Life": 0,
    "Fortnite": 0,
    "Minecraft": 0
}

ratingPelis = {
    "El Padrino": 0,
    "The Matrix": 0,
    "John Wick": 0,
    "Taxi Driver": 0,
    "Toy Story": 0
}



with open ("ratingJuegos.json", "w") as catalogoJuegos:
    json.dump(ratingJuegos, catalogoJuegos)

with open ("ratingPelis.json", "w") as catalogoPelis:
    json.dump(ratingPelis,  catalogoPelis)

def quizJuegos():
    for juego in ratingJuegos:
        while True:
            try:
                puntajeJ = int(input(f"Entregele un puntaje a {juego}: "))
                if 1 <= puntajeJ <= 10:
                    ratingJuegos[juego] = puntajeJ
                    break
                else:
                    print("Solo puede ingresar un valor entre 1-10, vuelva a intentarlo")
            except ValueError:
                print("Valor ingresado incorrecto, vuelva a intentarlo")  
    with open ("ratingJuegos.json", "w") as catalogoJuegos:
        json.dump(ratingJuegos, catalogoJuegos)

def quizPelis():
    for peli in ratingPelis:
        while True:
            try:
                puntajeP = int(input(f"Entregele un puntaje a {peli}: "))
                if 1 <= puntajeP <= 10:
                    ratingPelis[peli] = puntajeP
                    break
                else:
                    print("Solo puede ingresar un valor entre 1-10, vuelva a intentarlo")
            except ValueError:
                print("Valor ingresado incorrecto, vuelva a intentarlo")
    with open ("ratingPelis.json", "w") as catalogoPelis:
        json.dump(ratingPelis, catalogoPelis)
    
while True:
    try:
        time.sleep(2)
        print("Seleccione una opción: ")
        print("1. Evaluar juegos")
        print("2. Evaluar peliculas")
        print("3. Entregar ranking juegos")
        print("4. Entregar ranking peliculas")
        print("5. Salir")
        op = int(input())
        if op == 1:
            quizJuegos()
            continue
        elif op == 2:
            quizPelis()
            continue
        elif op == 3:
            with open ("ratingJuegos.json", "r") as catalogoJuegos:
                juegosL = json.load(catalogoJuegos)
                print(juegosL)
        elif op == 4:
            with open ("ratingPelis.json", "r") as catalogoPelis:
                pelisL = json.load(catalogoPelis)
                print(pelisL)
        elif op == 5:
            print("Gracias por usar el programa.")
            break
        elif op <= 0 or op >= 6:
            print("Solo puede elegir un número entre el rango (1-5), vuelva a intentarlo.")
    except ValueError:
        print("Valor incorrecto, vuelva a intentarlo.")