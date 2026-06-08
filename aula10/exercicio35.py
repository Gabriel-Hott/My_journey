#fazer um programa que leia um comprimento de 3 retas e diga se podem forma um triângulo ou não, necessario pesquisar o principio matematico para ser feito.
p1 = float(input('Digite a primeira linha do triâgulo: '))
p2 = float(input('Digite a segunda linha do triângulo: '))
p3 = float(input('Digite a terceira linha do triângulo: '))
if p1 < p2 + p3 and p2 < p1 + p3 and p3 < p1 + p2:
    print('Os seguimento acima pode forma um triângulo')
else: 
    print('Os seguimento acima não podem forma um triângulo')