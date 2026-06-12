#Fazer um programa que leia o peso de 5 pessoas e diga qual foi a maior e o menor peso lido.
M = 0
m = 1000
for c in range (1, 6):
    peso = float(input('Digite seu peso [Kg]: '))
    if peso >  M:
        M = peso
    if peso < m:
        m = peso
print('O maior peso registrado foi {}Kg e o menor peso registrado foi {}Kg.'.format(M, m))