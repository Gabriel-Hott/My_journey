#Criar um programa que pergunte números ao usario e pergunte quando ele quer parar, ao final ele tera que mostrar a média dos numeros digitados, qual foi o menor número e o maior número.
print(35*'+=')
sair = 0
c = 0
tot = 0
while sair == 0:
    n = int(input('Digite um número: '))
    c += 1
    tot += n
    cont = str(input('Deseja continuar[S] sim [N] não: ')).upper()
    if cont == 'N':
        sair = 1
print('foram digitados o total de {} números, com uma media de {}'.format(c, tot/c))