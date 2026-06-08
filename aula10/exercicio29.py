#escrever um programa que leia a velocidade de um carro, se ele ultrapassar 80km/h. mostrar ele que foi multado e a multa por cada Km acima do limite vai custa 7.00R$
velo = int(input('Em qual velocidade você está trafegando? '))
if velo <= 80:
    print('Você esta dentro do limite da velocidade, PARABENS')
else:
    print('Você esta acima da velocidade permitida de 80Km/h')
    multa = float((velo - 80) * 7)
    print('Sua multa é de {:.2f}R$'.format(multa))