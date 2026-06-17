#fazer um programa que leia algo que o usuario digitou e mostre na tela o tipo primitivo e todas as informações possiveis sobre ela com a função 'n.is...'
# print('Digite algo e vamos conferir como ele e lido pelo Python')
# n = input('Digite aqui: ')
# print('Oque você digitou é Alfa numerico:{}, ele é um número:{}, ele é uma palavra:{}, ele é printavel(e possivel exibir na tela):{}'.format(n.isalnum(), n.isdigit(), n.isascii(), n.isprintable()))
#concluido Obs. tive que olhar a explicação pois não vi que ele necessitava de (), ele é uma função então e claro que necessitava de parenteses.

#refazendo

print('Digite algo e vamos conferir como ele e lido pelo Python')
n = input('Digite oque quiser:')
print('Oque você digitou é do tipo primitivo:', type(n))
print('Oque você digitou é um número:', n.isnumeric())
print('Oque você digitou tem espaços:', n.isspace)
print('Oque você digitou é Alfabetico:', n.isalpha)
print('Oque você digitou é Alfanúmerico:', n.isalnum())
print('Oque você digitou está em Maiúscula:', n.isupper)
print('Oque você digitou está em Minúscula:', n.islower)
print('Oque você digitou está Capitalizado:', n.istitle())