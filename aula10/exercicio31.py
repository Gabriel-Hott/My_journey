#criar um programa que pergunte a distacia de uma viagem em Km. Calcule o preço da passagem, cobrando R$0.50 por KM para viagens de até 200Km e R$0.45 para viagens mais logas.
dist = float(input('Qual a distancia pecorrida: '))
if dist <= 200:
    total = dist * 0.50
    print('O total a pagar da sua viagem de {}Km é {:.2f}R$'.format(dist, total))
else:
    total = dist * 0.45
    print('O total da sua viagem de {}Km é {:.2f}R$'.format(dist, total))
print('Fim programa')