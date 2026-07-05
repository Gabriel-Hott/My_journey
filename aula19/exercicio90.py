#Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário, No final, mostre o conteúdo da estrutura a tela. 7+ aprovado
aluno = dict()
aluno['nome'] = str(input('Qual é o nome do aluno: '))
aluno['média'] = float(input(f'Qual a média do aluno {aluno["nome"]}: '))
if aluno['média'] >= 7:
    aluno['situação'] = 'APROVADO'
elif aluno['média'] > 5:
    aluno['situação'] = 'RECUPERAÇÂO'
else:
    aluno['situação'] = 'REPROVADO'
print(40 * '=+')
for k, i in aluno.items():
    print(f' - {k} é igual a {i}')