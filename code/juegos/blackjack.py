import random, os, time
from juegos.dibujos.cartas import *

def preparacion():
    global cartas
    cartas = [
            '2♠', '3♠', '4♠', '5♠', '6♠', '7♠', '8♠', '9♠', '10♠', 'J♠', 'Q♠', 'K♠', 'A♠',
            '2♦', '3♦', '4♦', '5♦', '6♦', '7♦', '8♦', '9♦', '10♦', 'J♦', 'Q♦', 'K♦', 'A♦',
            '2♥', '3♥', '4♥', '5♥', '6♥', '7♥', '8♥', '9♥', '10♥', 'J♥', 'Q♥', 'K♥', 'A♥',
            '2♣', '3♣', '4♣', '5♣', '6♣', '7♣', '8♣', '9♣', '10♣', 'J♣', 'Q♣', 'K♣', 'A♣',
        ]
    random.shuffle(cartas)
    jugador.append(cartas.pop())
    crupier.append(cartas.pop())
    jugador.append(cartas.pop())
    crupier.append(cartas.pop())

def menu(puntos):
    carga()
    print("¡Bienvenido al Blackjack!\nUsted tiene esta cantidad de PEPEPOINTS: %s.\nLa cantidad de apuesta obligatoria minima de este juego es de 20.\n" %(puntos))
    salir = input("Quiere empezar a jugar o salir al menu principal? ")
    while salir != False and salir != True:
        if salir.lower() == "salir":
            salir = True
        elif salir.lower() == "jugar":
            salir = False
        else:
            salir = input("No ha respondido correctamente a la pregunta.\nVuelva a intentarlo: ")
    return salir

def juegoblack(puntos):
    global apuesta
    pepepoints = int(puntos)
    salir = menu(pepepoints)
    apuesta = 20
    while pepepoints != 0 and salir != True:
        time.sleep(1)
        os.system("cls")
        print('Esta es tu cantidad de pepepoints: %s \n' %(pepepoints))
        accion = int(input("1. Jugar\n2. Cambiar Apuesta\n0. Salir\n   Opcion: "))
        if accion == 1:
            pepepoints = juego(pepepoints)
            paus = input("Presiona enter para continuar...")
        elif accion == 2:
            apuesta = int(input('Introduce una apuesta: '))
            while apuesta % 2 != 0 and apuesta < 20:
                print('Introduce una apuesta valida: ' )
                apuesta = int(input('Introduce una apuesta: '))
                os.system('cls')
        elif accion == 0:
            salir = True
        else:
            print("No ha introducido una opcion valida, pruebe de nuevo...")
    return pepepoints

def calc(mano, quien):
    cartasEq = {
            '2♠' : 2, '3♠' : 3, '4♠' : 4, '5♠' : 5, '6♠' : 6, '7♠' : 7, '8♠' : 8, '9♠' : 9, '10♠' : 10, 'J♠' : 10, 'Q♠' : 10, 'K♠' : 10, 'A♠' : [1, 11],
            '2♦' : 2, '3♦' : 3, '4♦' : 4, '5♦' : 5, '6♦' : 6, '7♦' : 7, '8♦' : 8, '9♦' : 9, '10♦' : 10, 'J♦' : 10, 'Q♦' : 10, 'K♦' : 10, 'A♦' : [1, 11],
            '2♥' : 2, '3♥' : 3, '4♥' : 4, '5♥' : 5, '6♥' : 6, '7♥' : 7, '8♥' : 8, '9♥' : 9, '10♥' : 10, 'J♥' : 10, 'Q♥' : 10, 'K♥' : 10, 'A♥' : [1, 11],
            '2♣' : 2, '3♣' : 3, '4♣' : 4, '5♣' : 5, '6♣' : 6, '7♣' : 7, '8♣' : 8, '9♣' : 9, '10♣' : 10, 'J♣' : 10, 'Q♣' : 10, 'K♣' : 10, 'A♣' : [1, 11],
        }

    calc = 0
    if quien == 'jugador':
        if ((mano[0] == 'A♠' or mano[0] == 'A♣' or mano[0] == 'A♥' or mano[0] == 'A♦') and (mano[1] == '10♠' or mano[1] == '10♣' or mano[1] == '10♥' or mano[1] == '10♦' or mano[1] == 'J♠' or mano[1] == 'J♣' or mano[1] == 'J♥' or mano[1] == 'J♦' or mano[1] == 'Q♠' or mano[1] == 'Q♣' or mano[1] == 'Q♥' or mano[1] == 'Q♦' or mano[1] == 'K♠' or mano[1] == 'K♣' or mano[1] == 'K♥' or mano[1] == 'K♦')) or ((mano[1] == 'A♠' or mano[1] == 'A♣' or mano[1] == 'A♥' or mano[1] == 'A♦') and (mano[0] == '10♠' or mano[0] == '10♣' or mano[0] == '10♥' or mano[0] == '10♦' or mano[0] == 'J♠' or mano[0] == 'J♣' or mano[0] == 'J♥' or mano[0] == 'J♦' or mano[0] == 'Q♠' or mano[0] == 'Q♣' or mano[0] == 'Q♥' or mano[0] == 'Q♦' or mano[0] == 'K♠' or mano[0] == 'K♣' or mano[0] == 'K♥' or mano[0] == 'K♦')):
            calc += 21
        else:
            for x in mano:
                for z,k in cartasEq.items():
                    if z == x:
                        if x == 'A♠' or x == 'A♣' or x == 'A♥'  or x == 'A♦':
                            pregu = int(input('Cuanto quieres que valga A? 1 o 11 : '))
                            while pregu != 1 and pregu != 11:
                                print('Introduce un valor correcto')
                                pregu = int(input('Cuanto quieres que valga A? 1 o 11: '))
                            calc += pregu
                        else:
                            calc += k
    else:
        for x in mano:
            for z,k in cartasEq.items():
                if z == x:
                    if x == 'A♠' or x == 'A♣' or x == 'A♥'  or x == 'A♦':
                        calc += 1
                    else:
                        calc += k
    return calc

def comprobacionjug(valor):
    if valor > 21:
        print('Te has pasado, has perdido!')
        partida = False
        return partida

def comprobacion(jug, crup, puntos):
    pepepoints = puntos
    if crup > 21:
        print('El crupier pierde, tu ganas!')
        pepepoints = pepepoints + (apuesta * 2)
    elif jug == crup:
        print('Empate, nadie gana')
        pepepoints = pepepoints + apuesta
    elif jug > crup:
        print('Has ganado al crupier, tu ganas!')
        pepepoints = pepepoints + (apuesta * 2)
    else:
        print('Tu pierdes :(')
    partida = False
    return [partida, pepepoints]

def juego(puntos):
    global crupier,jugador
    pepepoints = puntos
    pepepoints = pepepoints - apuesta
    primera_mano = True
    quedarse = False
    partida = True
    crupier = []
    jugador = []
    preparacion()
    crupierCart = dibujos(crupier)
    jugadorCart = dibujos(jugador)

    crupier_calc = calc(crupier, 'crupier')
    jugador_calc = calc(jugador, 'jugador')

    while pepepoints != 0 and partida != False:

        if quedarse == True:
            print('Cartas del crupier: \n{} ({})'.format('\n'.join(crupierCart), crupier_calc))

            while crupier_calc <= 17:
                crupier.append(cartas.pop())
                crupierCart = dibujos(crupier)
                crupier_calc = calc(crupier, 'crupier')

            os.system('cls')
            print('Cartas del crupier: \n{} ({})'.format('\n'.join(crupierCart), crupier_calc))
            x = comprobacion(jugador_calc,crupier_calc, pepepoints)
            partida = x[0]
            pepepoints = x[1]

        else:
            os.system('cls')
            print('Cartas del crupier: \n{}'.format(crupierCart[0]+'\n'+ cartalrev))
        print('\nTus cartas:\n{} ({})'.format('\n'.join(jugadorCart), jugador_calc))

        while quedarse != True and partida != False:
            opcion = int(input('\nQue te gustaria hacer?\n1.Pedir carta\n2.Quedarse\n'))
            if opcion == 1:
                os.system('cls')
                jugador.append(cartas.pop())
                jugadorCart = dibujos(jugador)
                jugador_calc = calc(jugador, 'jugador')
                partida = comprobacionjug(jugador_calc)
                print('Cartas del crupier: \n{}'.format(crupierCart[0]+'\n'+ cartalrev))
                print('\nTus cartas:\n{} ({})'.format('\n'.join(jugadorCart), jugador_calc))
            elif opcion == 2:
                quedarse = True
                os.system('cls')
    return pepepoints
