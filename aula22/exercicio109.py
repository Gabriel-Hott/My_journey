#Modificar as funções do desafio 107 para que elas aceitem um parâmetro a mais, informando se o valor retornado pro elas vai ser ou não formatado pela função moeda(), desenvolvido no exercicio 108.

from utilidadesCeV import moeda

p = float(input('Digite um valor: R$'))
print(f'A metade de {moeda.format(p)} dará {moeda.metade(p, True)}')
print(f'O dobro de {moeda.format(p)} resultara em {moeda.dobro(p, True)}')
print(f'Se aumentar {moeda.format(p)} em 10% dará em {moeda.aumentar(p, 10, True)}')
print(f'Se dominuir {moeda.format(p)} em 10% dará em {moeda.diminuir(p, 10, True)}')