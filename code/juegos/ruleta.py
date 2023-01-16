import os, time, random
from juegos.dibujos.ruletad import *
listaNumero = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31", "32", "33", "34", "35", "36", "00"]
listaFila = {"1a fila" : ["1","4", "7", "10", "13", "16", "19", "22", "25", "28", "31", "34"], "2a fila" : ["2", "5", "8", "11", "14", "17", "20", "23", "26", "29", "32", "35"], "3a fila" : ["3", "6", "9", "12", "15", "18", "21", "24", "27", "30", "33", "36"]}
listaDoce = {"1a docena" : ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"] , "2a docena" : ["13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24"], "3a docena" : ["25", "26", "27", "28", "29", "30", "31", "32", "33", "34", "35", "36"]}
listaColor = {"rojo" : ["1", "3", "5", "7", "9", "12", "14", "16", "18", "19", "21", "23", "25", "27", "30", "32", "34", "36"], "negro" : ["2", "4", "6", "8", "10", "11", "13", "15", "17", "20", "22", "24", "26", "28", "29", "31", "33", "35"]}
listaMit = {"1-18" : ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18"], "19-36" : ["19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31", "32", "33", "34", "35", "36"]}
listaPar = {"par" : ["2", "4","6" ,"8","10","12","14","16","18","20", "22","24","26", "28","30","32","34","36"], "impar" : ["1","3","5","7","9","11","13","15","17","19","21","23","25","27","29","31","33","35"]}
def menu(puntos):
    global salir
    carga()
    print("¡Bienvenido a la ruleta!\nUsted tiene esta cantidad de PEPEPOINTS: %s.\nLa cantidad de apuesta obligatoria de este juego es de 20.\nAqui puede encontrar la tabla de apuesta.\n" %(puntos))
    tabla()
    salir = input("Quiere empezar a jugar o salir al menu principal? ")
    while salir != False and salir != True:
        if salir.lower() == "salir":
            salir = True
        elif salir.lower() == "jugar":
            salir = False
        else:
            salir = input("No ha respondido correctamente a la pregunta.\nVuelva a intentarlo: ")

def juego(puntos):
    global listaApuesta
    pepepoints = puntos
    listaApuesta = {}
    segapu = ""
    while segapu.lower() != "no" and pepepoints != 0:
        os.system("cls")
        print("Esta es la cantidad de puntos que tiene: %s ₱\n" %(pepepoints))
        apostar = input("Introduzca una apuesta.\n(1a docena/ 2a docena/ 3a docena/ 1a fila/ 2a fila/ 3a fila/ numero/ color/ par / impar/ 1-18 / 19-36): ")
        while apostar not in listaNumero and apostar not in listaFila and apostar not in listaDoce and apostar not in listaColor and apostar not in listaMit and apostar not in listaPar:
            print('Introduce una apuesta valida.')
            apostar = input("Introduzca una apuesta.\n(1a docena/ 2a docena/ 3a docena/ 1a fila/ 2a fila/ 3a fila/ numero/ color/ par / impar/ 1-18 / 19-36): ")
        apuesta = input("Introduzca la apuesta, minimo 20: ")

        if apuesta == '':
            while apuesta == '':
                print('Introduzca una apuesta valida')
                apuesta = input("Introduzca la apuesta, minimo 20: ")
            apuesta = int(apuesta)

        elif int(apuesta) < 20:
            while int(apuesta) < 20:
                print('Introduzca una apuesta valida')
                apuesta = input("Introduzca la apuesta, minimo 20: ")
            apuesta = int(apuesta)
        apuesta = int(apuesta)
        while (apuesta < 20) or (apuesta > pepepoints):
            apuesta = int(input("Introduzca una apuesta valida: "))
        listaApuesta[apostar] = apuesta
        pepepoints -= apuesta
        segapu = input("\n¿Quieres seguir apostando? ")
        while segapu.lower() != "no" and segapu.lower() != "si":
            print('Introduce una opcion valida, si o no.')
            segapu = input("\n¿Quieres seguir apostando? ")
    segapu = input("\n¿Quiere ver su apuesta? ")
    while segapu.lower() != "no" and segapu.lower() != "si":
        segapu = input("\nIntroduzca una respuesta valida: ")
    if segapu.lower() == "si":
        for x,y in listaApuesta.items():
            print("\nApuesta: %s \nPuntos apostados: %s" %(x, y))
    pepepoints = comprobacion(pepepoints)
    return pepepoints

def juegoruleta(puntos):
    global salir
    pepepoints = puntos
    menu(pepepoints)
    while pepepoints != 0 and salir != True:
        time.sleep(1)
        os.system("cls")
        accion = int(input("1. Jugar\n2. Mostrar tabla de apuesta\n0. Salir\n   Opcion: "))
        if accion == 1:
            pepepoints = juego(pepepoints)
            paus = input("Presiona enter para continuar...")
        elif accion == 2:
            tabla()
            paus = input("Presiona enter para continuar...")
        elif accion == 0:
            salir = True
        else:
            print("No ha introducido una opcion valida, pruebe de nuevo...")
    return pepepoints

def comprobacion(puntos):
    pepepoints = puntos
    totalganado = 0
    time.sleep(2)
    os.system("cls")
    ruleta = random.choice(listaNumero)
    print("Este es el numero en el que ha caido la bola %s.\n" %(ruleta))
    for x,y in listaApuesta.items():
        if x in listaNumero:
            if x == ruleta:
                totalganado = totalganado + ( float(y) * 37)
                print("Has ganado %s con tu apuesta.\n" %(( float(y) * 37)))
            else:
                print("No has Ganado nada con tu apuesta: %s." %(x))
        elif x in listaFila:
            if x == "1a fila" and str(ruleta) in listaFila["1a fila"]:
                totalganado = totalganado + ( float(y) * 12)
                print("Has ganado %s con tu apuesta.\n" %(( float(y) * 12)))
            elif x == "2a fila" and str(ruleta) in listaFila["2a fila"]:
                totalganado = totalganado + ( float(y) * 12)
                print("Has ganado %s con tu apuesta.\n" %(( float(y) * 12)))
            elif x == "3a fila" and str(ruleta) in listaFila["3a fila"]:
                totalganado = totalganado + ( float(y) * 12)
                print("Has ganado %s con tu apuesta.\n" %(( float(y) * 12)))
            else:
                print("No has Ganado nada con tu apuesta: %s." %(x))
        elif x in listaDoce:
            if x == "1a docena" and str(ruleta) in listaDoce["1a docena"]:
                totalganado = totalganado + ( float(y) * 3)
                print("Has ganado %s con tu apuesta.\n" %(( float(y) * 3)))
            elif x == "2a docena" and str(ruleta) in listaDoce["2a docena"]:
                totalganado = totalganado + ( float(y) * 3)
                print("Has ganado %s con tu apuesta.\n" %(( float(y) * 3)))
            elif x == "3a docena" and str(ruleta) in listaDoce["3a docena"]:
                totalganado = totalganado + ( float(y) * 3)
                print("Has ganado %s con tu apuesta.\n" %(( float(y) * 3)))
            else:
                print("No has Ganado nada con tu apuesta: %s." %(x))
        elif x in listaColor:
            if x == "rojo" and str(ruleta) in listaColor["rojo"]:
                totalganado = totalganado + ( float(y) * 2)
                print("Has ganado %s con tu apuesta.\n" %(( float(y) * 2)))
            elif x == "negro" and str(ruleta) in listaColor["negro"]:
                totalganado = totalganado + ( float(y) * 2)
                print("Has ganado %s con tu apuesta.\n" %(( float(y) * 2)))
            else:
                print("No has Ganado nada con tu apuesta: %s." %(x))
        elif x in listaMit:
            if x == "1-18" and str(ruleta) in listaMit["1-18"]:
                totalganado = totalganado + ( float(y) * 2)
                print("Has ganado %s con tu apuesta.\n" %(( float(y) * 2)))
            elif x == "19-36" and str(ruleta) in listaMit["19-36"]:
                totalganado = totalganado + ( float(y) * 2)
                print("Has ganado %s con tu apuesta.\n" %(( float(y) * 2)))
            else:
                print("No has Ganado nada con tu apuesta: %s." %(x))
        elif x in listaPar:
            if x == "par" and str(ruleta) in listaPar["par"]:
                totalganado = totalganado + ( float(y) * 2)
                print("Has ganado %s con tu apuesta.\n" %(( float(y) * 2)))
            elif x == "par" and str(ruleta) in listaPar["par"]:
                totalganado = totalganado + ( float(y) * 2)
                print("Has ganado %s con tu apuesta.\n" %(( float(y) * 2)))
            else:
                print("No has Ganado nada con tu apuesta: %s." %(x))
    pepepoints = pepepoints + totalganado
    return pepepoints
