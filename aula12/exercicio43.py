#Fazer um programa que leia o peso e a altura de uma pessoa, e qualcule seu IMC e mostre seu status, de acordo com a tabela. 1 - Abaixo de 18.5: abaixo do peso, 2 - entre 18.5 e 25: peso ideal, 3 - 25 até 30: sobrepeso, 4 - 30 até 40: obesidade, 5 - acima de 40: obesidade mórbida.
print('Calculo de Indice de Massa Corporal - IMC')
peso = float(input('Qual é o seu peso [Kg]: '))
alt = float(input('Qual é a sua altura [cm]: '))
alt = alt / 100
IMC = peso / (alt ** 2)
print('Seu IMC é {:.2f} com isso '.format(IMC), end='')
if IMC < 18.5:
    print('você está abaixo do peso')
elif IMC < 25:
    print('você está no peso ideal')
elif IMC < 30:
    print('voce está com sobrepeso')
elif IMC < 40:
    print('você está obeso')
else:
    print('você está com obesidade mórbida')