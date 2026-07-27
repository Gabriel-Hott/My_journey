#Adicionar ao módulo moeda() criado anteriormente, uma função chamada resumo(), que mostre na tela algumas informações geradas pela funções que já temos no módulo criado.
from utilidadesCeV import moeda

p = float(input('Digite um valor: R$'))
moeda.resumo(p, 30, 45)