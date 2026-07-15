#Criar um programa que tenha uma lista chamada 'números' e duas funções chamadas sorteia() e somaPar(). A primeira função vai sortear 5 números e vai colocálas dentro da lista e a segunda função vai mostrar a soma entre todo os valores PARES sorteados pela função anterior.
from random import randint
from time import sleep
numeros = list()

def cabeçalho():
    print(15* '+=')
    print(f'{'SORTEIO DE NÚMEROS':^30}')
    print(15* '+=')

def sorteia():
    for c in range(0, 5):
        numeros.append(randint(0, 100))
    for c in numeros:
        print(c, end=', ', flush=True)
        sleep(0.8)
    print()

def somaPar():
    soma = 0
    for c in numeros:
        if c % 2 == 0:
            soma += c
            print(c, end=', ', flush=True)
            sleep(0.8)
    sleep(0.8)
    print(f'A soma de todos os números pares foi {soma}', flush=True)

#Código principal

cabeçalho()
print('Os 5 números sorteados foram... ', end='', flush=True)
sorteia()
print('Os números pares são... ', end='', flush=True)
somaPar()
print('FIM DO PROGRAMA')