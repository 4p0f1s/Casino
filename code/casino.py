#pip install https://github.com/orokusaki/pycard/archive/master.zip
import os, time, pycard
from intro import *
from juegos.blackjack import *
from juegos.slots import *
from creditos import *
from juegos.ruleta import *
def intro():
    global nom, trato, jugar
    animacion()
    nomape = input('BIENVENID@, a nuestro casino, "CASINOS PEPE", con quien tenemos el gusto de tratar?\nNombre y Apellido: ').split(" ")
    nom = nomape[0]
    while nom == '':
        print('Introduce un nombre correcto')
        nomape = input().split(" ")
        nom = nomape[0]
        os.system('cls')
    trato = input("Como deberiamos de referirnos a usted?\nComo Sr, Sra, Srita, Srito o Cosa?\n")
    while trato.lower() != 'sr' and trato.lower() != 'sra' and trato.lower() != 'srita' and trato.lower() != 'srito' and trato.lower() != 'cosa':
        os.system('cls')
        print('No ha introducido una opcion correcta!')
        trato = input("Como deberiamos de referirnos a usted?\nComo Sr, Sra, Srita, Srito o Cosa?\n")

    if trato.lower() == 'cosa':
        jugar = input('%s quiere entrar a nuestro casino a jugar? ' %(trato.upper()[0]+trato[1:]))
        while jugar.lower() != 'si' and jugar.lower() != 'no':
            os.system('cls')
            print('No ha introducido una respuesta correcta!')
            jugar = input('%s quiere entrar a nuestro casino a jugar? ' %(trato.upper()[0]+trato[1:]))

        if jugar.lower() == "si":
            print("Procedamos a iniciar el processo!")
            os.system("start https://ok.ru/video/205784418888")
            processo()
            pepepoints = creditos()
            menu_principal(pepepoints)
        else:
            despedida()

    elif trato.lower() == 'sr' or trato.lower() == 'sra' or trato.lower() == 'srita' or trato.lower() == 'srito':
        jugar = input('%s %s quiere entrar a nuestro casino a jugar? ' %(trato.upper()[0]+trato[1:], nom.upper()[0]+nom[1:]))
        while jugar.lower() != 'si' and jugar.lower() != 'no':
            os.system('cls')
            print('No ha introducido una respuesta correcta!')
            jugar = input('%s quiere entrar a nuestro casino a jugar? ' %(trato.upper()[0]+trato[1:]))
        if jugar.lower() == "si":
            print("Procedamos a iniciar el processo!")
            proces = processo()
            if proces == True:
                pepepoints = creditos()
                menu_principal(pepepoints)
        else:
            despedida()

def processo():
    global terms
    terms = True
    while terms != False:
        os.system("cls")
        terms = input('Para poder proceder a jugar, necesitara "PEPEPOINTS".\nPara conseguir de estos, necesitara introducir su tarjeta de credito...\nEsta de acuerdo con esto? ')
        if terms.lower() == "si":
            veri_tarjeta()
            time.sleep(1)
            terms = False
            return True
        elif terms.lower() == "no":
            terms = False
            despedida()
        else:
            print("\nPerdone no le he entendido, puede volver a introducir si esta de acuerdo o no? ")
            time.sleep(1)

def despedida():
    print("\nRegresa cuando quieras.")

def veri_tarjeta():
    global tarjeta
    tarjeta = False
    while tarjeta != True:
        os.system("cls")
        numero = input('Introduzca el numero de su tarjeta de credito: ')
        mes = int(input('Introduzca el mes de caducidad de su tarjeta de credito: '))
        ano = int(input('Introduzca el año de caducidad de su tarjeta de credito: '))
        cvc = int(input('Introduzca el cvc de su tarjeta de credito: '))
        tarjeta = pycard.Card(numero,mes,ano,cvc)
        if tarjeta.is_valid == True:
            print('\nLa tarjeta introducida es valida!')
            time.sleep(1.75)
            tarjeta = True
        else:
            print("\nLa tarjeta introducida no es valida, introduce una tarjeta valida!")
            time.sleep(1.75)

def menu_principal(puntos):
    os.system("cls")
    pepepoints = puntos
    accion = int(input("%s %s a que quiere jugar?\n\n1. Blackjack\n2. SLOTS\n3. Ruleta\n0. Salir\n   Opcion: " %(trato.upper()[0]+trato[1:], nom.upper()[0]+nom[1:])))
    while accion != 0:
        if accion == 1:
            os.system("cls")
            pepepoints = juegoblack(pepepoints)

        elif accion == 2:
            os.system("cls")
            pepepoints = juegoslot(pepepoints)

        elif accion == 3:
            os.system("cls")
            pepepoints = juegoruleta(pepepoints)

        accion = int(input("\n%s %s a que quiere jugar?\n\n1. Blackjack\n2. SLOTS\n3. Ruleta\n0. Salir\n   Opcion: " %(trato.upper()[0]+trato[1:], nom.upper()[0]+nom[1:])))
    despedida()

intro()
