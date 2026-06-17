#c = 1
#while True:
#    print(c,' →', end='')
#    c += 1
#print('Acabou')
n = s = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    s += n
print(f'A soma dos números foi {s}')  #f strings