import random
p1 = str(input('Digite o nome no primeiro aluno: '))
p2 = str(input('Digite o nome do segundo aluno: '))
p3 = str(input('Digite o nome do terceiro aluno: '))
p4 = str(input('Digite o nome do quarto aluno: '))
lista = [p1, p2, p3, p4]
Escolha = random.choice(lista)
print(Escolha)
