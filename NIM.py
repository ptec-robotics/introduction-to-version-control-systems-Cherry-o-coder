import colorama
print(colorama.Fore.GREEN+"")
name = input('NAME:')
turn = 0
coins = 13

def p1_turn():
    print(f"{name} there are {coins} coins(s) remaining")
    n = input("How many coins do you remove?")

def p2_turn():
    pass

while coins>0:
    if turn % 2 == 0:
        pass
    if turn % 2 == 1:
        pass #player 2 turn