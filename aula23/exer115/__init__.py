def topo(msg): #TOPO DO MENU
    print(30 * '-')
    print(f'{msg:^30}')
    print(30 * '-')

def menu(msg): #MENU DE OPÇÕES
    print(f'{'1 - Ver pessoas cadastradas':<40} \n'
          f'{'2 - Cadastrar nova pessoa':<40}\n'
          f'{'3 - Sair do sistema':<40}\n')
    print(30 * '-')
    while True:
        try:
            a = int(input(msg))
            if a >= 1 and a <= 3:
                break
            else:
                print(f'\033[31mO valor {a} não está nas opções do menu.\033[m')
        except (ValueError, TypeError):
            print('\33[31mValor digitado não e um NUMERO INTEIRO!!!\033[m')
    print(30 * '-')
    if a == 1:
        print(f'{'OPÇÂO 1':^30}')
    elif a == 2:
        print(f'{'OPÇÂO 2':^30}')
    else:
        print(f'{'OPÇÂO 3':^30}')
    print(30 * '-')