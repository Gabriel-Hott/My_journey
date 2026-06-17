#Criar um programa que simule um funcionamento de um caixa eletronico. No inicio ele devera solicitar o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues. (O CAIXA POSSUI VALORES DE R$01, R$10, R$20 É R$50)
print(40 * '-')
print(f'{'BANCO JUNIN':^40}')
print(40 * '-')
valor = int(input('Qual valor deseja sacar: R$'))
cedula = 50
totCedula = 0
while True:
    if valor >= cedula:
        valor -= cedula
        totCedula += 1
    else:
        if totCedula > 0:
            print(f'Total de {totCedula} cédulas de RS{cedula}')
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        totCedula = 0
        if valor == 0:
            break
print(40 * '-')
print('FIM PROGRAMA')