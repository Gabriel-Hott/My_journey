#Crie um programa que leia a idade e o sexo de varias pessoas, A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final mostre: 1 - Quantas pessoas tem mais de 18 anos. 2 - quantos são homens. 3 - quantas são mulheres com menos de 20 anos. 
idade = masc = Mul= 0
while True:
    ida = int(input('Qual é a idade da pessoa: '))
    sex = str(input('Qual é o sexo da pessoa [M/F]: ')).upper().strip()[0]
    if sex == 'M' or sex == 'F':
        if ida > 18:
            idade += 1
        if ida < 20 and sex == 'F':
            Mul += 1
        if sex == 'M':
            masc += 1
        esc = str(input('Deseja continuar [S/N]: ')).upper().strip()[0]
        if esc == 'N':
            break
        elif esc != 'S':
            print('Opção INVALIDA, por favor reinicie.')
    else:
        print('Opção INVALIDA, por favor reinicie.')
   
print(f'Ao todo {idade} são pessoas maiores de 18.')
print(f'Foram digitados o total de {masc} homens.')
print (f'È ao todo foram {Mul} mulheres com menos de 20 anos')