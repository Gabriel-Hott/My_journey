#Reescrever o exercicio 104 ( leiaint() ), incluindo agora uma  a possibilidade de escrever um número inválido, Criar também um função leiaFloat() com a mesma funcionalidade.  

def leiaInt(a):
    while True:
        try:
            a = int(input('Digite um número inteiro: '))
        except (TypeError, ValueError):
            print('\033[0;31mPor favor digite um valor INTEIRO!!!\033[m')
        except KeyboardInterrupt:
            print('O usúario não quis informar um número.')
            return 0
        else:
            return a

def LeiaFloat(a):
    while True:
        try:
            a = float(input('Digite um número Real: '))
        except (TypeError, ValueError):
            print(f'\033[0;31mO valor digitado não e um número Realz\033[m')
        except KeyboardInterrupt:
            print('O usúario não quis informar um número.')
            return 0
        else:
            return a

#Código principal

res = leiaInt('Digite um número inteiro: ')
res2 = LeiaFloat('Digite um número Real: ')
print(f'{res} é um número inteiro')
print(f'{res2} é um número Real')