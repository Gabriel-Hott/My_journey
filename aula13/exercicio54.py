#Criar um programa que léie a data de nascimento de 7 pessoas, e no final mostre quantas pessoas não atigiram a maior idade e quantas já são maiores de idade.(maior idade 21 anos)
import time
totM = 0
totm = 0
for c in range (1, 8):
    nasc = int(input('Digite o ano de seu nascimento: '))
    if time.localtime().tm_year - nasc >= 21:
        totM = totM + 1
    else:
        totm = totm + 1
print('O total de pessoas adutas foi {} é o total de pessoas menores foi {}'.format(totM, totm))