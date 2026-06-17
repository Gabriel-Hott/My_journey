#Fazer um programa que mostre a tabuada de varios números. um de cada vez. para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.
c = 0
while True:
    n = int(input('Digite um número para ver sua tabuada: '))
    c = 1
    if n > 0:
        while c <= 10:
            print(f'{c:^2} X {n:^3} = {c*n:^4}')
            c += 1
    else:
        break
print('FIM PROGRAMA')