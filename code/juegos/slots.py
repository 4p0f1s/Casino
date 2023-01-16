import os, time, random
from juegos.dibujos.slotsd import *

def menu(puntos):
    global salir
    carga()
    print("¡Bienvenido a la maquina tragaperras!\nUsted tiene esta cantidad de PEPEPOINTS: %s.\nLa cantidad de apuesta obligatoria de este juego es de 10.\nAqui puede encontrar la tabla de ganancias dependiendo de la cantidad que este apostando.\n" %(puntos))
    tabla()
    salir = input("Quiere empezar a jugar o salir al menu principal? ")
    while salir != False and salir != True:
        if salir.lower() == "salir":
            salir = True
        elif salir.lower() == "jugar":
            salir = False
        else:
            salir = input("No ha respondido correctamente a la pregunta.\nVuelva a intentarlo: ")

def juegoslot(puntos):
    global salir, rueda1, rueda2, rueda3, apuesta
    pepepoints = puntos
    apuesta = 10
    menu(pepepoints)
    while pepepoints != 0 and salir != True:
        os.system("cls")
        print("Esta es la cantidad de puntos que tiene: %s ₱\n" %(pepepoints))
        accion = int(input("1. Jugar\n2. Mostrar tabla de ganancia\n3. Cambiar apuesta\n0. Salir\n   Opcion: "))
        if accion == 1:
            pepepoints = pepepoints - apuesta
            rueda1 = rueda()
            rueda2 = rueda()
            rueda3 = rueda()
            pepepoints = comprobacion(pepepoints)
        elif accion == 2:
            tabla()
            paus = input("Presiona enter para continuar...")
        elif accion == 3:
            apuesta = int(input("Introduzca la apuesta: "))
            while apuesta != 10 and apuesta != 25 and apuesta != 50:
                print("No ha introducido una apuesta valida!")
                apuesta = int(input("Introduzca la apuesta: "))
        elif accion == 0:
            salir = True
        else:
            print("No ha introducido una opcion valida, pruebe de nuevo...")
        paus = input("Presiona enter para continuar...")
        os.system("cls")
    return pepepoints

def comprobacion(pepepoints):
    print("%s %s %s" %(dslots(rueda1),dslots(rueda2),dslots(rueda3)))
    if apuesta == 10:
        if (rueda1 == "pepe" and rueda2 == "pepe" and rueda3 == "pepe"):
            pepepoints = pepepoints + 1500
        elif (rueda1 == "seven" and rueda2 == "seven" and rueda3 == "seven") or (rueda1 == "pepe" and rueda2 == "seven" and rueda3 == "seven") or (rueda1 == "seven" and rueda2 == "pepe" and rueda3 == "seven") or (rueda1 == "seven" and rueda2 == "seven" and rueda3 == "pepe") or (rueda1 == "pepe" and rueda2 == "pepe" and rueda3 == "seven") or (rueda1 == "seven" and rueda2 == "pepe" and rueda3 == "pepe") or (rueda1 == "pepe" and rueda2 == "seven" and rueda3 == "pepe"):
            pepepoints = pepepoints + 500
        elif (rueda1 == "bar" and rueda2 == "bar" and rueda3 == "bar") or (rueda1 == "pepe" and rueda2 == "bar" and rueda3 == "bar") or (rueda1 == "bar" and rueda2 == "pepe" and rueda3 == "bar") or (rueda1 == "bar" and rueda2 == "bar" and rueda3 == "pepe") or (rueda1 == "pepe" and rueda2 == "pepe" and rueda3 == "bar") or (rueda1 == "bar" and rueda2 == "pepe" and rueda3 == "pepe") or (rueda1 == "pepe" and rueda2 == "bar" and rueda3 == "pepe"):
            pepepoints = pepepoints + 200
        elif (rueda1 == "bell" and rueda2 == "bell" and rueda3 == "bell") or (rueda1 == "pepe" and rueda2 == "bell" and rueda3 == "bell") or (rueda1 == "bell" and rueda2 == "pepe" and rueda3 == "bell") or (rueda1 == "bell" and rueda2 == "bell" and rueda3 == "pepe") or (rueda1 == "pepe" and rueda2 == "pepe" and rueda3 == "bell") or (rueda1 == "bell" and rueda2 == "pepe" and rueda3 == "pepe") or (rueda1 == "pepe" and rueda2 == "bell" and rueda3 == "pepe"):
            pepepoints = pepepoints + 150
        elif (rueda1 == "limon" and rueda2 == "limon" and rueda3 == "limon") or (rueda1 == "pepe" and rueda2 == "limon" and rueda3 == "limon") or (rueda1 == "limon" and rueda2 == "pepe" and rueda3 == "limon") or (rueda1 == "limon" and rueda2 == "limon" and rueda3 == "pepe") or (rueda1 == "pepe" and rueda2 == "pepe" and rueda3 == "limon") or (rueda1 == "limon" and rueda2 == "pepe" and rueda3 == "pepe") or (rueda1 == "pepe" and rueda2 == "limon" and rueda3 == "pepe"):
            pepepoints = pepepoints + 90
        elif (rueda1 == "naranja" and rueda2 == "naranja" and rueda3 == "naranja") or (rueda1 == "pepe" and rueda2 == "naranja" and rueda3 == "naranja") or (rueda1 == "naranja" and rueda2 == "pepe" and rueda3 == "naranja") or (rueda1 == "naranja" and rueda2 == "naranja" and rueda3 == "pepe") or (rueda1 == "pepe" and rueda2 == "pepe" and rueda3 == "naranja") or (rueda1 == "naranja" and rueda2 == "pepe" and rueda3 == "pepe") or (rueda1 == "pepe" and rueda2 == "naranja" and rueda3 == "pepe"):
            pepepoints = pepepoints + 60
        elif (rueda1 == "cereza" and rueda2 == "cereza" and rueda3 == "cereza") or (rueda1 == "pepe" and rueda2 == "cereza" and rueda3 == "cereza") or (rueda1 == "cereza" and rueda2 == "pepe" and rueda3 == "cereza") or (rueda1 == "cereza" and rueda2 == "cereza" and rueda3 == "pepe") or (rueda1 == "pepe" and rueda2 == "pepe" and rueda3 == "cereza") or (rueda1 == "cereza" and rueda2 == "pepe" and rueda3 == "pepe") or (rueda1 == "pepe" and rueda2 == "cereza" and rueda3 == "pepe"):
            pepepoints = pepepoints + 30
    elif apuesta == 25:
        if (rueda1 == "pepe" and rueda2 == "pepe" and rueda3 == "pepe"):
            pepepoints += 3000
        elif (rueda1 == "seven" and rueda2 == "seven" and rueda3 == "seven") or (rueda1 == "pepe" and rueda2 == "seven" and rueda3 == "seven") or (rueda1 == "seven" and rueda2 == "pepe" and rueda3 == "seven") or (rueda1 == "seven" and rueda2 == "seven" and rueda3 == "pepe") or (rueda1 == "pepe" and rueda2 == "pepe" and rueda3 == "seven") or (rueda1 == "seven" and rueda2 == "pepe" and rueda3 == "pepe") or (rueda1 == "pepe" and rueda2 == "seven" and rueda3 == "pepe"):
            pepepoints += 1250
        elif (rueda1 == "bar" and rueda2 == "bar" and rueda3 == "bar") or (rueda1 == "pepe" and rueda2 == "bar" and rueda3 == "bar") or (rueda1 == "bar" and rueda2 == "pepe" and rueda3 == "bar") or (rueda1 == "bar" and rueda2 == "bar" and rueda3 == "pepe") or (rueda1 == "pepe" and rueda2 == "pepe" and rueda3 == "bar") or (rueda1 == "bar" and rueda2 == "pepe" and rueda3 == "pepe") or (rueda1 == "pepe" and rueda2 == "bar" and rueda3 == "pepe"):
            pepepoints += 500
        elif (rueda1 == "bell" and rueda2 == "bell" and rueda3 == "bell") or (rueda1 == "pepe" and rueda2 == "bell" and rueda3 == "bell") or (rueda1 == "bell" and rueda2 == "pepe" and rueda3 == "bell") or (rueda1 == "bell" and rueda2 == "bell" and rueda3 == "pepe") or (rueda1 == "pepe" and rueda2 == "pepe" and rueda3 == "bell") or (rueda1 == "bell" and rueda2 == "pepe" and rueda3 == "pepe") or (rueda1 == "pepe" and rueda2 == "bell" and rueda3 == "pepe"):
            pepepoints += 300
        elif (rueda1 == "limon" and rueda2 == "limon" and rueda3 == "limon") or (rueda1 == "pepe" and rueda2 == "limon" and rueda3 == "limon") or (rueda1 == "limon" and rueda2 == "pepe" and rueda3 == "limon") or (rueda1 == "limon" and rueda2 == "limon" and rueda3 == "pepe") or (rueda1 == "pepe" and rueda2 == "pepe" and rueda3 == "limon") or (rueda1 == "limon" and rueda2 == "pepe" and rueda3 == "pepe") or (rueda1 == "pepe" and rueda2 == "limon" and rueda3 == "pepe"):
            pepepoints += 150
        elif (rueda1 == "naranja" and rueda2 == "naranja" and rueda3 == "naranja") or (rueda1 == "pepe" and rueda2 == "naranja" and rueda3 == "naranja") or (rueda1 == "naranja" and rueda2 == "pepe" and rueda3 == "naranja") or (rueda1 == "naranja" and rueda2 == "naranja" and rueda3 == "pepe") or (rueda1 == "pepe" and rueda2 == "pepe" and rueda3 == "naranja") or (rueda1 == "naranja" and rueda2 == "pepe" and rueda3 == "pepe") or (rueda1 == "pepe" and rueda2 == "naranja" and rueda3 == "pepe"):
            pepepoints += 100
        elif (rueda1 == "cereza" and rueda2 == "cereza" and rueda3 == "cereza") or (rueda1 == "pepe" and rueda2 == "cereza" and rueda3 == "cereza") or (rueda1 == "cereza" and rueda2 == "pepe" and rueda3 == "cereza") or (rueda1 == "cereza" and rueda2 == "cereza" and rueda3 == "pepe") or (rueda1 == "pepe" and rueda2 == "pepe" and rueda3 == "cereza") or (rueda1 == "cereza" and rueda2 == "pepe" and rueda3 == "pepe") or (rueda1 == "pepe" and rueda2 == "cereza" and rueda3 == "pepe"):
            pepepoints += 50
    else:
        if (rueda1 == "pepe" and rueda2 == "pepe" and rueda3 == "pepe"):
            pepepoints += 6000
        elif (rueda1 == "seven" and rueda2 == "seven" and rueda3 == "seven") or (rueda1 == "pepe" and rueda2 == "seven" and rueda3 == "seven") or (rueda1 == "seven" and rueda2 == "pepe" and rueda3 == "seven") or (rueda1 == "seven" and rueda2 == "seven" and rueda3 == "pepe") or (rueda1 == "pepe" and rueda2 == "pepe" and rueda3 == "seven") or (rueda1 == "seven" and rueda2 == "pepe" and rueda3 == "pepe") or (rueda1 == "pepe" and rueda2 == "seven" and rueda3 == "pepe"):
            pepepoints += 2500
        elif (rueda1 == "bar" and rueda2 == "bar" and rueda3 == "bar") or (rueda1 == "pepe" and rueda2 == "bar" and rueda3 == "bar") or (rueda1 == "bar" and rueda2 == "pepe" and rueda3 == "bar") or (rueda1 == "bar" and rueda2 == "bar" and rueda3 == "pepe") or (rueda1 == "pepe" and rueda2 == "pepe" and rueda3 == "bar") or (rueda1 == "bar" and rueda2 == "pepe" and rueda3 == "pepe") or (rueda1 == "pepe" and rueda2 == "bar" and rueda3 == "pepe"):
            pepepoints += 1000
        elif (rueda1 == "bell" and rueda2 == "bell" and rueda3 == "bell") or (rueda1 == "pepe" and rueda2 == "bell" and rueda3 == "bell") or (rueda1 == "bell" and rueda2 == "pepe" and rueda3 == "bell") or (rueda1 == "bell" and rueda2 == "bell" and rueda3 == "pepe") or (rueda1 == "pepe" and rueda2 == "pepe" and rueda3 == "bell") or (rueda1 == "bell" and rueda2 == "pepe" and rueda3 == "pepe") or (rueda1 == "pepe" and rueda2 == "bell" and rueda3 == "pepe"):
            pepepoints += 600
        elif (rueda1 == "limon" and rueda2 == "limon" and rueda3 == "limon") or (rueda1 == "pepe" and rueda2 == "limon" and rueda3 == "limon") or (rueda1 == "limon" and rueda2 == "pepe" and rueda3 == "limon") or (rueda1 == "limon" and rueda2 == "limon" and rueda3 == "pepe") or (rueda1 == "pepe" and rueda2 == "pepe" and rueda3 == "limon") or (rueda1 == "limon" and rueda2 == "pepe" and rueda3 == "pepe") or (rueda1 == "pepe" and rueda2 == "limon" and rueda3 == "pepe"):
            pepepoints += 300
        elif (rueda1 == "naranja" and rueda2 == "naranja" and rueda3 == "naranja") or (rueda1 == "pepe" and rueda2 == "naranja" and rueda3 == "naranja") or (rueda1 == "naranja" and rueda2 == "pepe" and rueda3 == "naranja") or (rueda1 == "naranja" and rueda2 == "naranja" and rueda3 == "pepe") or (rueda1 == "pepe" and rueda2 == "pepe" and rueda3 == "naranja") or (rueda1 == "naranja" and rueda2 == "pepe" and rueda3 == "pepe") or (rueda1 == "pepe" and rueda2 == "naranja" and rueda3 == "pepe"):
            pepepoints += 200
        elif (rueda1 == "cereza" and rueda2 == "cereza" and rueda3 == "cereza") or (rueda1 == "pepe" and rueda2 == "cereza" and rueda3 == "cereza") or (rueda1 == "cereza" and rueda2 == "pepe" and rueda3 == "cereza") or (rueda1 == "cereza" and rueda2 == "cereza" and rueda3 == "pepe") or (rueda1 == "pepe" and rueda2 == "pepe" and rueda3 == "cereza") or (rueda1 == "cereza" and rueda2 == "pepe" and rueda3 == "pepe") or (rueda1 == "pepe" and rueda2 == "cereza" and rueda3 == "pepe"):
            pepepoints += 100
    return pepepoints

def rueda():
    return random.choice(["seven", "bar", "bell", "limon", "naranja", "cereza", "pepe"])
