#fazer um programa que leia duas notas de um aluno e faca a sua média
nome = str(input('Qual é o nome do Aluno: '))
n1 = float(input('Digite a primeira nota do aluno: '))
n2 = float(input('Digite a segunda nota do aluno: '))
media = (n1 + n2) /2
print('O aluno {} obteve uma media de {:.1f} com a primeira nota sendo {} e a segunda sendo {}.'.format(nome, media, n1, n2))