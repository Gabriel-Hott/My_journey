#Crie um programa que leie um número e mostre o seu faorial.
n = int(input('Digite um número que deseja ver o fatorial: '))
c = n
f = 1
while c > 0:
    print('{}'.format(c), end=' ')
    print(' x ' if c > 1 else ' = ', end=' ')
    f *= c
    c -= 1
print('{}'.format(f))