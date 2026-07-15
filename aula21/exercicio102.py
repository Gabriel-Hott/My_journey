#Criar um programa que tenha uma função de fatorial() que receba dois parâmetros: o primero que indique o número a calcular e o outro chamado show, que será um valor lógico(opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial.

from time import sleep
from math import factorial
def fatorial(a, show=False):
    print(f'O fatorial de {a} é {factorial(a)}')
    if show == True:
        print(f'O calculo do fatorial {a} e feito: ',)
        sleep(1.9)
        for c in range(a, 0, -1):
            print(f'{c}', end=' ', flush=True)
            sleep(0.6)
            if c > 1:
                print('x', end=' ', flush=True)
                sleep(0.6)
            else:
                print(f'= {factorial(a)}', flush=True)
                sleep(0.6)
        
#Código principal

r1 = int(input('Fatorial: '))
r2 = str(input('Calculo: [S/N] '))
print(f'Calculando o fatorial de {r1}', flush=True)
sleep(1)
if r2 in 'Ss':
    r2 = True
    resp = fatorial(r1, r2)
else:
    resp = fatorial(r1)