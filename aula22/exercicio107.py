#Criar um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade(). Fazer também um programa que importe  esse módulo e use algumas das funções.
from utilidadesCeV import moeda

r = float(input('Digite um valor: R$'))
print(f'Se aumentar 10% do R${r} dará {moeda.aumentar(r, 10)}')
print(f'Se diminuir 10% do R${r} dará {moeda.diminuir(r, 10)}')
print(f'Se dobra o valor R${r} dará {moeda.dobro(r)}')
print(f'Se pegarmos metade de R${r} dará {moeda.metade(r)}')