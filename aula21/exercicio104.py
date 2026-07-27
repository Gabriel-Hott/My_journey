#Criar um programa que leia a função chamada leiaInt(), que vai funcionar de forma semelhante á função input() do python, só que fazendo a validação para aceitar apenas um valor numérico. Ex: n = leiaInt('Digite um n')
def leiaInt(a):
        while True:
            res = input('Digite um número: ')
            if res.isnumeric():
                return res
            else:
                print(f'{'\033[0;31mERRO, por favor digite um número!\033[m'}')

#Código principal


n = leiaInt('Digite um número')
print(f'Você digitou o número {n}')