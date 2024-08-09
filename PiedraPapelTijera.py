
from random import randint

def jugar():
    opciones = ["Piedra", "Papel", "Tijera"]

    while True:
        valor_aleatorio = randint(0, 2)
        juego_computador = opciones[valor_aleatorio]

        juego_usuario = input("¿Qué eliges? Piedra, Papel, Tijera (o 'salir' para terminar): ").capitalize()

        if juego_usuario == "Salir":
            print("Gracias por jugar. ¡Hasta la próxima!")
            break
        elif juego_usuario not in opciones:
            print("Opción no válida, por favor elige entre Piedra, Papel o Tijera.")
            continue

        print(f"Computadora eligió: {juego_computador}")

        if juego_usuario == juego_computador:
            print("¡Es un empate!")
        elif juego_usuario == "Piedra":
            if juego_computador == "Papel":
                print("¡Perdiste!", juego_computador, "cubre", juego_usuario)
            else:
                print("¡Ganaste!", juego_usuario, "aplasta", juego_computador)
        elif juego_usuario == "Papel":
            if juego_computador == "Tijera":
                print("¡Perdiste!", juego_computador, "corta", juego_usuario)
            else:
                print("¡Ganaste!", juego_usuario, "cubre", juego_computador)
        elif juego_usuario == "Tijera":
            if juego_computador == "Piedra":
                print("¡Perdiste!", juego_computador, "aplasta", juego_usuario)
            else:
                print("¡Ganaste!", juego_usuario, "corta", juego_computador)


jugar()

