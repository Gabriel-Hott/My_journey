#Cria um programa que gere números aleatorios e colocar em uma tupla. Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.
from random import randint
tul = randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10)
Maior = 0
Menor = 0
for c in range (0 ,len(tul)):
    if c == 0:
        Maior = tul[c]
        Menor = tul[c]
    if tul[c] > Maior:
        Maior = tul[c]
    elif tul[c] < Menor:
        Menor = tul[c] 
print(f'A lista aleátoria foi {tul} sendo o maior número {Maior} é o menor {Menor}')