#escrever um programa que pergunte qual o salario de um usuario e calcule seu aumento, para salarios superiores a R$1.250.00, calcule um aumento de 10%.
#para os inferiores 15%
sal = float(input('Digite seu salario: R$'))
if sal <= 1250:
    nov = (sal / 100) * 15
    tota = sal + nov
    print('Seu salario de R${} recebeu um aumento de 15% (R${:.2f}) dando um total de R${:.2f}'.format(sal, nov, tota))
else:
    nov = (sal / 100) * 10
    tota = sal + nov
    print('Seu salario de R${} vai receber um aumento de 10% (R${:.2f}) totalizando R${}'.format(sal, nov, tota))
print('Fim programa') 