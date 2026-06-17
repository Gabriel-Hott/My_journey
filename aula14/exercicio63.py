#Criar um programa que pegunte um número(x) inteiro, e mostre os (x) termos da sequencia de fibonacci
n = int(input('Quantos termos dejesa ver da sequencia de fibonacci: '))
c = 3
print(40*'+=')
n1 = 0
n2 = 1
print('{} » {}'.format(n1, n2), end='')
while c <= n:
    n3 = n1 + n2
    print(' » {}'.format(n3), end='') 
    n1 = n2
    n2 = n3
    c += 1
print(' » fim')