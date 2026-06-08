n1 = float(input('Qual a sua primeira nota: '))
n2 = float(input('Qual a sua segunda nota: '))
nota = (n1 + n2) / 2
print('A sua media foi de {:.2f}'.format(nota))
if nota >= 6.0:
    print('Sua media esta otima PARABENS.')
else:
    print('Sua media esta ruim ESTUDE mais.')