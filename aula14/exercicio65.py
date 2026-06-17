#Criar um programa que pergunte números ao usario e pergunte quando ele quer parar, ao final ele tera que mostrar a média dos numeros digitados, qual foi o menor número e o maior número.
print(35*'+=')
sair = 0
c = 0
tot = 0
maior = 0
menor = 0
while sair == 0:
    n = int(input('Digite um número: '))
    c += 1
    tot += n
    cont = str(input('Deseja continuar[S] sim [N] não: ')).upper()
    if cont == 'N':
        sair = 1
    if c == 1:
        maior = menor = n
    else:
        if maior < n:
            maior = n
        if menor > n:
            menor = n
print('foram digitados o total de {} números, com uma media de {:.2f}'.format(c, tot/c))
print ('O maior número digitado foi {} e o menor número foi {}'.format(maior, menor))