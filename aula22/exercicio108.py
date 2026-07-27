#Adicionar ao módulo do exercicio 107 a função chamada moeda() que consiga mostrar os valores como valor monetário formatado. 

from utilidadesCeV import moeda, dados

r = float(input('Digite um valor: R$'))
print(f'Se aumentar 10% do {moeda.format(r)} dará {moeda.aumentar(r,10, True)}')
print(f'Se diminuir 10% do {moeda.format(r)} dará {moeda.diminuir(r, 10, True)}')
print(f'Se dobra o valor {moeda.format(r)} dará {moeda.dobro(r, True)}')
print(f'Se pegarmos metade de {moeda.format(r)} dará {moeda.metade(r, True)}')