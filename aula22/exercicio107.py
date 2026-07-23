#Criar um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade(). Fazer também um programa que importe  esse módulo e use algumas das funções.
from utilexer import moeda

r = int(input('Digite um número: '))
print(f'Se aumentar 10% do {r} dará {moeda.aumen(r)}')
print(f'Se diminuir 10% do {r} dará {moeda.dimin(r)}')
print(f'Se dobra o valor {r} dará {moeda.dobro(r)}')
print(f'Se pegarmos metade de {r} dará {moeda.meta(r)}')