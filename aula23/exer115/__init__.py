from time import sleep

def topo(msg): #TOPO DO MENU
    sleep(0.8)
    print(35 * '-')
    print(f'\033[34m{msg:^35}\033[m')
    print(35 * '-')

def menu(lista, msg): #MENU DE OPÇÕES
    c = 1
    for i in lista:
        sleep(0.3)
        print(f'\033[33m{c}\033[m - \033[32m{i}\033[m')
        c += 1
    print(35 * '-')
    while True:
        try:
            a = int(input(msg)) - 1
            if a >= 0 and a <= (len(lista) - 1):
                return a
            else:
                print(f'\033[31mOpção {a} não e uma opção valida\033[m')
        except (ValueError, TypeError):
            print('\033[31mA opção escolhida não é um número inteiro\033[m')