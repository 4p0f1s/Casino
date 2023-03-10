import time,os
cartalrev = "┌─────────┐\n│  P   P  │\n│   E E   │\n│    P    │\n│   E E   │\n│  s   s  │\n└─────────┘"

def carga():
    os.system("cls")
    print("""
                         __
                   _..-''--'----_.
                 ,''.-''| .---/ _`-._
               ,' \ \  ;| | ,/ / `-._`-.
             ,' ,',\ \( | |// /,-._  / /
             ;.`. `,\ \`| |/ / |   )/ /
            / /`_`.\_\ \| /_.-.'-''/ /
           / /_|_:.`. \ |;'`..')  / /
           `-._`-._`.`.;`.\  ,'  / /
               `-._`.`/    ,'-._/ /
                 : `-/     \`-.._/
                 |  :      ;._ (
                 :  |      \  ` \\
                  \         \   |
                   :        :   ;
                   |           /
                   ;         ,'
                  /         /
                 /         /
                          /
    """)

    for x in range(0,101, 4):
        print( "Cargando el juego",x,"%  de 100 %")
        time.sleep(0.75)
    os.system("cls")

def dibujos(mano):
    global cartalrev
    list = []

    cartas = {
        'A♠': '┌─────────┐\n│A        │\n│         │\n│    ♠    │\n│         │\n│        A│\n└─────────┘',
        '2♠': '┌─────────┐\n│2        │\n│  ♠      │\n│         │\n│      ♠  │\n│        2│\n└─────────┘',
        '3♠': '┌─────────┐\n│3        │\n│  ♠      │\n│    ♠    │\n│      ♠  │\n│        3│\n└─────────┘',
        '4♠': '┌─────────┐\n│4        │\n│  ♠   ♠  │\n│         │\n│  ♠   ♠  │\n│        4│\n└─────────┘',
        '5♠': '┌─────────┐\n│5        │\n│  ♠   ♠  │\n│    ♠    │\n│  ♠   ♠  │\n│        5│\n└─────────┘',
        '6♠': '┌─────────┐\n│6        │\n│  ♠   ♠  │\n│  ♠   ♠  │\n│  ♠   ♠  │\n│        6│\n└─────────┘',
        '7♠': '┌─────────┐\n│7   ♠    │\n│  ♠   ♠  │\n│    ♠    │\n│  ♠   ♠  │\n│    ♠   7│\n└─────────┘',
        '8♠': '┌─────────┐\n│8   ♠    │\n│  ♠   ♠  │\n│  ♠   ♠  │\n│  ♠   ♠  │\n│    ♠   8│\n└─────────┘',
        '9♠': '┌─────────┐\n│9        │\n│  ♠ ♠ ♠  │\n│  ♠ ♠ ♠  │\n│  ♠ ♠ ♠  │\n│        9│\n└─────────┘',
        '10♠': '┌─────────┐\n│10 ♠  ♠  │\n│  ♠  ♠   │\n│   ♠  ♠  │\n│   ♠  ♠  │\n│  ♠  ♠ 10│\n└─────────┘',
        'J♠': '┌─────────┐\n│J    ww  │\n│   ♠ {)  │\n│   | %   │\n│   | %   │\n│  __%%[ J│\n└─────────┘',
        'Q♠': '┌─────────┐\n│Q    ww  │\n│   ♠ {(  │\n│   | %%  │\n│   |%%%  │\n│  _%%%O Q│\n└─────────┘',
        'K♠': '┌─────────┐\n│K    WW  │\n│   ♠ {)  │\n│   | %%  │\n│   |%%%  │\n│  _%%%> K│\n└─────────┘',
        'A♦': '┌─────────┐\n│A        │\n│         │\n│    ♦    │\n│         │\n│        A│\n└─────────┘',
        '2♦': '┌─────────┐\n│2        │\n│  ♦      │\n│         │\n│      ♦  │\n│        2│\n└─────────┘',
        '3♦': '┌─────────┐\n│3        │\n│  ♦      │\n│    ♦    │\n│      ♦  │\n│        3│\n└─────────┘',
        '4♦': '┌─────────┐\n│4        │\n│  ♦   ♦  │\n│         │\n│  ♦   ♦  │\n│        4│\n└─────────┘',
        '5♦': '┌─────────┐\n│5        │\n│  ♦   ♦  │\n│    ♦    │\n│  ♦   ♦  │\n│        5│\n└─────────┘',
        '6♦': '┌─────────┐\n│6        │\n│  ♦   ♦  │\n│  ♦   ♦  │\n│  ♦   ♦  │\n│        6│\n└─────────┘',
        '7♦': '┌─────────┐\n│7   ♦    │\n│  ♦   ♦  │\n│    ♦    │\n│  ♦   ♦  │\n│    ♦   7│\n└─────────┘',
        '8♦': '┌─────────┐\n│8   ♦    │\n│  ♦   ♦  │\n│  ♦   ♦  │\n│  ♦   ♦  │\n│    ♦   8│\n└─────────┘',
        '9♦': '┌─────────┐\n│9        │\n│  ♦ ♦ ♦  │\n│  ♦ ♦ ♦  │\n│  ♦ ♦ ♦  │\n│        9│\n└─────────┘',
        '10♦': '┌─────────┐\n│10 ♦  ♦  │\n│  ♦  ♦   │\n│   ♦  ♦  │\n│   ♦  ♦  │\n│  ♦  ♦ 10│\n└─────────┘',
        'J♦': '┌─────────┐\n│J    ww  │\n│   ♦ {)  │\n│   | %   │\n│   | %   │\n│  __%%[ J│\n└─────────┘',
        'Q♦': '┌─────────┐\n│Q    ww  │\n│   ♦ {(  │\n│   | %%  │\n│   |%%%  │\n│  _%%%O Q│\n└─────────┘',
        'K♦': '┌─────────┐\n│K    WW  │\n│   ♦ {)  │\n│   | %%  │\n│   |%%%  │\n│  _%%%> K│\n└─────────┘',
        'A♥': '┌─────────┐\n│A        │\n│         │\n│    ♥    │\n│         │\n│        A│\n└─────────┘',
        '2♥': '┌─────────┐\n│2        │\n│  ♥      │\n│         │\n│      ♥  │\n│        2│\n└─────────┘',
        '3♥': '┌─────────┐\n│3        │\n│  ♥      │\n│    ♥    │\n│      ♥  │\n│        3│\n└─────────┘',
        '4♥': '┌─────────┐\n│4        │\n│  ♥   ♥  │\n│         │\n│  ♥   ♥  │\n│        4│\n└─────────┘',
        '5♥': '┌─────────┐\n│5        │\n│  ♥   ♥  │\n│    ♥    │\n│  ♥   ♥  │\n│        5│\n└─────────┘',
        '6♥': '┌─────────┐\n│6        │\n│  ♥   ♥  │\n│  ♥   ♥  │\n│  ♥   ♥  │\n│        6│\n└─────────┘',
        '7♥': '┌─────────┐\n│7   ♥    │\n│  ♥   ♥  │\n│    ♥    │\n│  ♥   ♥  │\n│    ♥   7│\n└─────────┘',
        '8♥': '┌─────────┐\n│8   ♥    │\n│  ♥   ♥  │\n│  ♥   ♥  │\n│  ♥   ♥  │\n│    ♥   8│\n└─────────┘',
        '9♥': '┌─────────┐\n│9        │\n│  ♥ ♥ ♥  │\n│  ♥ ♥ ♥  │\n│  ♥ ♥ ♥  │\n│        9│\n└─────────┘',
        '10♥': '┌─────────┐\n│10 ♥  ♥  │\n│  ♥  ♥   │\n│   ♥  ♥  │\n│   ♥  ♥  │\n│  ♥  ♥ 10│\n└─────────┘',
        'J♥': '┌─────────┐\n│J    ww  │\n│   ♥ {)  │\n│   | %   │\n│   | %   │\n│  __%%[ J│\n└─────────┘',
        'Q♥': '┌─────────┐\n│Q    ww  │\n│   ♥ {(  │\n│   | %%  │\n│   |%%%  │\n│  _%%%O Q│\n└─────────┘',
        'K♥': '┌─────────┐\n│K    WW  │\n│   ♥ {)  │\n│   | %%  │\n│   |%%%  │\n│  _%%%> K│\n└─────────┘',
        'A♣': '┌─────────┐\n│A        │\n│         │\n│    ♣    │\n│         │\n│        A│\n└─────────┘',
        '2♣': '┌─────────┐\n│2        │\n│  ♣      │\n│         │\n│      ♣  │\n│        2│\n└─────────┘',
        '3♣': '┌─────────┐\n│3        │\n│  ♣      │\n│    ♣    │\n│      ♣  │\n│        3│\n└─────────┘',
        '4♣': '┌─────────┐\n│4        │\n│  ♣   ♣  │\n│         │\n│  ♣   ♣  │\n│        4│\n└─────────┘',
        '5♣': '┌─────────┐\n│5        │\n│  ♣   ♣  │\n│    ♣    │\n│  ♣   ♣  │\n│        5│\n└─────────┘',
        '6♣': '┌─────────┐\n│6        │\n│  ♣   ♣  │\n│  ♣   ♣  │\n│  ♣   ♣  │\n│        6│\n└─────────┘',
        '7♣': '┌─────────┐\n│7   ♣    │\n│  ♣   ♣  │\n│    ♣    │\n│  ♣   ♣  │\n│    ♣   7│\n└─────────┘',
        '8♣': '┌─────────┐\n│8   ♣    │\n│  ♣   ♣  │\n│  ♣   ♣  │\n│  ♣   ♣  │\n│    ♣   8│\n└─────────┘',
        '9♣': '┌─────────┐\n│9        │\n│  ♣ ♣ ♣  │\n│  ♣ ♣ ♣  │\n│  ♣ ♣ ♣  │\n│        9│\n└─────────┘',
        '10♣': '┌─────────┐\n│10 ♣  ♣  │\n│  ♣  ♣   │\n│   ♣  ♣  │\n│   ♣  ♣  │\n│  ♣  ♣ 10│\n└─────────┘',
        'J♣': '┌─────────┐\n│J    ww  │\n│   ♣ {)  │\n│   | %   │\n│   | %   │\n│  __%%[ J│\n└─────────┘',
        'Q♣': '┌─────────┐\n│Q    ww  │\n│   ♣ {(  │\n│   | %%  │\n│   |%%%  │\n│  _%%%O Q│\n└─────────┘',
        'K♣': '┌─────────┐\n│K    WW  │\n│   ♣ {)  │\n│   | %%  │\n│   |%%%  │\n│  _%%%> K│\n└─────────┘'
        }
    for x in mano:
        for z,y in cartas.items():
            if x == z:
                list.append(y)

    return list
