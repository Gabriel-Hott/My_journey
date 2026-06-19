#criar um programa que tenha um tupla totalmente preenchida com uma contagem por extenso (nome do número), de 0 ate 20. O programa deverá ler um número pelo teclado(entre 0 e 20) e mostrá-lo por extenso.
nome = 'Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco',
'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onde', 'Doze',
'Treze', 'Catorze', 'Quize', 'Dezesseis', 'Dezessete',
'Dezoito', 'Dezenove', 'Vinte'
while True:
    nun = int(input('Digite um número de 0 até 20: '))
    if nun >= 0 and nun <= 20:
        print(f'Você digitou o número {nome[nun]}')
        break
    else:
        print('Por favor tente novamente,', end=' ')