#ajsknskna equisde no se que hacer uwu mala mia
import random #esto no se para que sirve, pero importa el modulo random

opciones = ["piedra", "papel", "tijera"] #esta es una lista wow
tu_puntaje = 0 #vamos a crear un marcador 
puntaje_computadora = 0
#Colores ANSI
BLANCO = "\033[37m"
ROJO = "\033[91m"
VERDE = "\033[32m"
AMARILLO = "\033[93m"
AZUL = "\033[34m"
MAGENTA = "\033[95m"
CYAN = "\033[36m"

while True:
    Turno_Computadora = random.choice(opciones) #una variable, elige una opcion aleatoriamente
    turno_del_jugador = input("Elige piedra, papel o tijera: ") .lower() #me costo entender esto, pero basicamente el input se puede guardar en una variable para guardar lo que el jugador escribe

    if turno_del_jugador not in opciones: #esto es para que si el jugador pone algo que no sea piedra, papel o tijera, le diga que no es valido
     print("Opcion no valida") 
     continue #esto es para que vuelva a preguntar al jugador, si no lo pones, el juego se termina

    else:
     print("Tu eleccion:", turno_del_jugador)
     print("Eleccion de la computadora:", Turno_Computadora) #ya sabes que es print, pero si pones comas puedes poner texto (strings) y la variable
     
     if turno_del_jugador == Turno_Computadora: #si el turno del jugador es igual a la compu es empate, con elif sera cuando gane y else para cuando pierda
        print(AMARILLO, "Empate")
     elif turno_del_jugador == "tijera" and Turno_Computadora == "papel": #also, aqui el and es para que se cumplan las dos condiciones, si el jugador elige tijera y la computadora papel, gana el jugador
         print(VERDE, "Ganaste")
         tu_puntaje += 1 #asi suma uno
     elif turno_del_jugador == "piedra" and Turno_Computadora == "tijera":
         print(VERDE, "Ganaste")
         tu_puntaje += 1
     elif turno_del_jugador == "papel" and Turno_Computadora == "piedra":
        print(VERDE, "Ganaste")
        tu_puntaje += 1
     else:
            print(ROJO, "Perdiste") #no tiene que poner condiciones, porque si no es empate ni gana el jugador, entonces pierde
            puntaje_computadora += 1
     print(f"Marcador: Tu {tu_puntaje} - Computadora {puntaje_computadora}") #la f es para que puedas poner variables dentro del print, y las llaves son para poner la variable
     print(BLANCO)
    while True:
        respuesta = input("Quieres jugar otra vez? (si/no): ").lower() #esto es para que el jugador pueda jugar otra vez, y si pone si, se reinicia el juego, si pone no, se termina
        if respuesta == "si":
            break #no es continue pq no funciona, no se pq
        elif respuesta == "no":
             break #esto es para que se termine el juego
    if respuesta == "no":
         break
print(MAGENTA, "Gracias por jugar :3")
print(BLANCO)

#recordar que si todo esta bien  y no funciona, muy probablemente se te duplico el codigo
#el while va antes de todo pq si no se vuelve loco con la pregunta
#q dolor de cabeza la sangria, recuerda que los primos if, else, elif, etc deben estar en la misma altura
#ya vi pq decian que los bucles como while son un dolor de cabeza
#teodiosangriayteamoperohoyteodio