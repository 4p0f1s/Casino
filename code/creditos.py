import os, time
def creditos():
    global eur, rep
    pepepoints = 0
    creditosdicc = {5 : 50, 10: 100, 15 : 225, 25 : 550, 35 : 900 , 45 : 1250, 50 : 2000}
    totalgastado = 0
    os.system("cls")
    print("   ┌─────────────────────────┐\n   |TABLA DE VALOR PEPEPOINTS|\n   |─────────────────────────|\n   |EUROS       | PEPEPOINTS |\n   |─────────────────────────|\n   |5 €         |     50 ₱   |\n   |10 €        |    100 ₱   |\n   |15 €        |  200 + 25 ₱|\n   |25 €        | 450 + 100 ₱|\n   |35 €        | 750 + 150 ₱|\n   |45 €        |1000 + 250 ₱|\n   |50 €        |1500 + 500 ₱|\n   └─────────────────────────┘")
    rep = ''
    while rep.lower() != "no":
        eur = int(input("\n\nIntroduce una cantidad de euros: "))
        while eur != 5 and eur != 10 and eur != 15 and eur != 25 and eur != 35 and eur != 45 and eur != 50:
            print("La cantidad seleccionada no es valida, introduzca una cantidad valida")
            eur = int(input("\n\nIntroduce una cantidad de euros: "))
        totalgastado += eur
        if eur != 0:
            for x,y in creditosdicc.items():
                if eur == x:
                    pepepoints = pepepoints + int(y)
        print("Esta es la cantidad de PEPEPOINTS que tiene: %s ₱ " %(pepepoints))
        limitacion_dia(totalgastado)
        if rep.lower() == "no":
            print("Muchas Gracias por su compra!")
            time.sleep(2)
    os.system("cls")
    return pepepoints

def limitacion_dia(dinerogastado):
    global eur, rep
    rep = input("\nTe gustaria comprar mas PEPEPOINTS? ")
    while rep.lower() != "si" and rep.lower() != "no":
        print("No ha introducido una opcion valida!")
        rep = input("\nTe gustaria comprar mas PEPEPOINTS? ")
    if rep.lower() == "si":
        if dinerogastado >= 100:
            print("Usted a superado la limitacion de dinero gastado por dia!")
            rep = "no"
            eur = 0
    elif rep.lower() == "no":
        time.sleep(0.1)
