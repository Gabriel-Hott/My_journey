#Fazer um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final. 1 - Média abaixo de 5.0(REPROVADO), 2 - Média entre 5.0 e 6.9(RECUPERAÇÂO), 3 - Média 7.0 ou superior(APROVADO).
print(30*'=')
print('ESCOLA BEM SUCESSO')
print(30*'=')
print('Notas escolares')
n1 = float(input('Digite a primera nota do aluno(a): '))
n2 = float(input('Digite a segunda nota do aluno(a): '))
if ((n1 + n2)/2) < 5:
    print('Com nota {} e {} a sua média foi de {:.2f} com isso voce está REPROVADO.'.format(n1, n2, (n1 + n2)/2))
elif((n1+n2)/2) < 6.9:
    print('Com nota {} e {} a sua média foi de {:.2f} é com isso você está de RECUPERAÇÂO.'.format(n1, n2, (n1 + n2)/2)) 
else:
    print('Com nota {} e {} a sua média é {:.2f} e está APROVADO.'.format(n1, n2, (n1 + n2)/2))