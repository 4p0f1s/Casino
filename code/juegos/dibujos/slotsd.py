import os, time
def carga():
    os.system("cls")
    print("""
                                         .-------.
                                         |Jackpot|
                             ____________|_______|_____________
                            |  __    __    ___  _____    __    |
                            | / _\  / /   /___\/__   \  / _\   |
                            | \ \  / /   //  //  / /\ \ \ \  25|
                            | _\ \/ /___/ \_//  / /  \/ _\ \ []|
                            | \__/\____/\___/   \/      \__/ []|
                            |===_______===_______===_______====|
                            ||*|\_     |*| _____ |*|\_     | *||
                            ||*|| \ _  |*||     ||*|| \ _  | *||
                            ||*| \_(_) |*||*BAR*||*| \_(_) | *||
                            ||*| (_)   |*||_____||*| (_)   | *|| __
                            ||*|_______|*|_______|*|_______| *||(__)
                            |===_______===_______===_______====| ||
                            ||*| _____ |*|\_     |*|  ___  | *|| ||
                            ||*||     ||*|| \ _  |*| |_  | | *|| ||
                            ||*||*BAR*||*| \_(_) |*|  / /  | *|| ||
                            ||*||_____||*| (_)   |*| /_/   | *|| ||
                            ||*|_______|*|_______|*|_______| *||_//
                            |===_______===_______===_______====|_/
                            ||*|  ___  |*|   |   |*| _____ | *||
                            ||*| |_  | |*|  / \  |*||     || *||
                            ||*|  / /  |*| /_ _\ |*||*BAR*|| *||
                            ||*| /_/   |*|   O   |*||_____|| *||
                            ||*|_______|*|_______|*|_______| *||
                            |lc=___________________________====|
                            |  /___________________________\   |
                            |   |                         |    |
                           _|    \_______________________/     |_
                          (______________________________________)\n""")

    for x in range(0,101, 4):
        print( "Cargando el juego",x,"%  de 100 %")
        time.sleep(0.75)
    os.system("cls")

def tabla():
    print("""
       ┌──────────────────────────────────────────────────────────────────────┐
       |                      TABLA DE GANANCIA / APUESTA                     |
       |──────────────────────────────────────────────────────────────────────|
       |        COMBINACION      | APUESTA 10 ₱ | APUESTA 25 ₱ | APUESTA 50 ₱ |
       |──────────────────────────────────────────────────────────────────────|
       |      PEPE PEPE PEPE     |    1500 ₱    |   3000 ₱     |    6000 ₱    |
       |         7  7  7         |     500 ₱    |   1250 ₱     |    2500 ₱    |
       |       BAR BAR BAR       |     200 ₱    |    500 ₱     |    1000 ₱    |
       |      BELL BELL BELL     |     150 ₱    |    300 ₱     |     600 ₱    |
       |    LIMON LIMON LIMON    |      90 ₱    |    150 ₱     |     300 ₱    |
       | NARANJA NARANJA NARANJA |      60 ₱    |    100 ₱     |     200 ₱    |
       |  CEREZA CEREZA CEREZA   |      30 ₱    |     50 ₱     |     100 ₱    |
       |        PEPE * *         |     Premio igual a la combinacion de *     |
       |        PEPE PEPE *      |     Premio igual a la combinacion de *     |
       └──────────────────────────────────────────────────────────────────────┘""")

def dslots(sel):
    global dibujoslots
    dibujoslots = { "seven":".-------.\n|   _   '\n`-' /  /\n   .  /\n  /  /\n `--'",
    "bar":" ______          __       _______\n|_   _ \        /  \     |_   __ \ \n  | |_) |      / /\ \      | |__) |\n  |  __'.     / ____ \     |  __ /\n _| |__) |  _/ /    \ \_  _| |  \ \_\n|_______/  |____|  |____ |____| |___|",
    "bell":"       ______\n      (      )\n       |    |\n     .'''8o'''.\n    /          \ \n    |_.--''--._|\n    )          (\n   /_..------.._\ \n   `-.___||___.-'\n         ()",
    "limon": "             \x1b[1;33;40m*&&&&&&.\x1b[0m\n         \x1b[1;32;40m/# ""\x1b[1;33;40m/##%%%%##%%%%.\x1b[0m\x1b[0m\n       \x1b[1;32;40m&#*#*""\x1b[1;33;40m,,,,,,,,,******\x1b[0m\n    \x1b[1;32;40m%%%%**\x1b[1;33;40m#/*,,,,,,,,,,,,*****\x1b[0m\n  \x1b[1;32;40m#%%%%/*\x1b[1;33;40m/#(**,,,,,,,,,,,,,***/*\x1b[0m\n \x1b[1;32;40m*%%%%#""\x1b[1;33;40m(/###/****,,,,,,,,,,****/*\x1b[0m\n \x1b[1;32;40m*%%%%#""\x1b[1;33;40m(##%#//*****************//*\x1b[0m\n  \x1b[1;32;40m#%%##""\x1b[1;33;40m#%###(///************//////\x1b[0m\n   \x1b[1;32;40m#%#\x1b[1;33;40m#/((((((/////////////////(//\x1b[0m\n    \x1b[1;32;40m#\x1b[0m    \x1b[1;33;40m/((((((/////////((((((((/\x1b[0m\n          \x1b[1;33;40m,/(((((((((((((((((##((\x1b[0m\n                 \x1b[1;33;40m*/((((((((((*\x1b[0m",
    "naranja":"                   ██████████\n                 ██▓▓▓▓▒▒▒▒▒▒██\n           ███████▒▒▒▒▓▓▓████\n        ███   ░░░ ██████\n      ██░░░░░░░░░░░██░░██\n     ██░░  ░░░░░░░░░░░░░██\n     ██░░░░░░░░░░░░░░░░░██\n      ██░░░░░░░░░░░░░░██\n        ██░░░░░░░░░░██\n          ██████████",
    "cereza" : "__.--~~.,-.__\n'~-._.-('-.__'-.\n        \    '~~'\n    .--./ \ \n   /#   \  \.--.\n   \    /  /#   \ \n    '--'   \    /\n            '--' ",
    "pepe" : "@@@@  @@@@@ @@@@  @@@@@\n@   @ @     @   @ @\n@@@@  @@@@  @@@@  @@@@\n@     @     @     @\n@     @@@@@ @     @@@@@"}

    for x,y in dibujoslots.items():
        if sel == x:
            print(y)