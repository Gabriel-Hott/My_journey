#escreva um programa que leia um número inteiro e peça para qe o usuário escolha qual será a base de conversão. 1 - Binario, 2  - Octal, 3 - Hexadecimal.
print(30*'=')
esc = (int(input('Conversor de bases Numéricas, escolha qual conversor deseja usar \n'
      '1 - Para BINARIO \n'
      '2 - Para OCTAL \n'
      '3 - Para HEXADECIMAL \n')))
if  esc == 1:
    N = int(input('Qual valor você deseja converter para BINARIO: '))
    res =  bin(N)
    print('Sua conversao do número {}Decimal para Binario é {}.'.format(N, res[2:]))
elif esc == 2:
    N = int(input('Qual valor você deseja converter para OCTAL: '))
    res = oct(N)
    print('Sua conversão de número {} em Decimal para Octal é {}.'.format(N, res[2:]))
elif esc == 3:
    N = int(input('Qual valor você dejesa converter para HEXADECIMAL: '))
    res = hex(N)
    print('Sua conversão do número Decimal {} para Hexadecimal é {}.'.format(N, res[2:]))
else:
    print('Escolha invalida, O programa será encerrado.')