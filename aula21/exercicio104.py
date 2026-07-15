#Criar um programa que leia a função chamada leiaInt(), que vai funcionar de forma semelhante á função input() do python, só que fazendo a validação para aceitar apenas um valor numérico. Ex: n = leiaInt('Digite um n')
def leiaInt(a):
    while True:
        res = input('Digite um número: ')
        if res >= 0 or res <0:
            break

#Código principal


n = leiaInt('Digite um número')
print(f'Você digitou o número {n}')