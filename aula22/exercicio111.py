#Criar um pacote chamdo utilidadesCeV que tenha dois módulos internos chamados moeda e dado. Transfira todas as funções utilizadas nos exercicios 107, 108, 109 para o primeiro pacote e mantenha tudo funcionando.

from utilidadesCeV import moeda

r = float(input('Digite um valor: R$'))
moeda.resumo(r, 25, 30)