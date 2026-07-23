#Criar um programa que tenha uma função chamada 'contador()', que receba três parâmetros: inicio, fim e passo e realize a contagem. O programa tem que realizar três contagens através da função criada: 1 - De 1 até 10, de 1 em 1, 2 - de 10 até 0, de 2 em 2, 3 - uma contagem personalizada.

from time import sleep

def contador(a, b, c):
    print(f'Contagem de {a} até {b} pulando de {c} em {c}.')
    sleep(1.2)
    if a > b and c > 0:
        for v in range(a, b, - c):
            print(v, end=', ', flush=True)
            sleep(0.6)
        print(v + c, 'FIM')
    elif a < 0:
        for v in range(a, b, + c):
            print(v, end=', ', flush=True)
            sleep(0.6)
        print(v + c, 'FIM')
    else:
        for v in range(a, b, c):
            print(v, end=', ', flush=True)
            sleep(0.6)
        print(v + c, 'FIM')

#Código principal

contador(int(input('1° número: ')), int(input('2° número: ')), int(input('passo: ')))