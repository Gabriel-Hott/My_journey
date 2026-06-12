#Criar um programa que leia nome, idade e sexo de 4 pessoas, No final do programa mostre: a média da idade do grupo, nome do homem mais velho, e quantas mulheres têm menos de 20 anos.
media = 0
Menor = 0
velho = 0
for c in range (1, 5):
    nome = str(input('Digite se nome: '))
    ida = int(input('Digite o ano de seu nascimento [xxxx] '))
    sex = str(input('Qual é o seu sexo [m] [f]: ')).upper()
    media = media + (2026 - ida)
    if sex == 'M':
        if (2026 - ida) > velho:
            Hvelho = nome
    elif sex == 'F':
        if (2026 - ida) < 20:
            Menor = Menor + 1
print('A media de idade foi {} anos, O homem mais velho foi o Sr. {} é o número de mulheres abaixo de 20 anos foram {} pessoa'.format(media/4, Hvelho, Menor))