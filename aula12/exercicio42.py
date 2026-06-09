#Refazer o desafio 35, mas acrescentando o recurso de mostrar que tipo de triâgulo séra formado: 1 - EQUILATERO-todos os lados iguais, 2 - ISÓSCELES-dois lados iguais, 3 - ESCALENO-Todos os lados diferentes 
print('Informe as retas para saber se formam um triângulo')
a = float(input('Digite a primeira linha: '))
b = float(input('Digite a segunda linha: '))
c = float(input('Digite a terceira linha: '))
if a < b + c and b < a + c and c < a + b:
    print('Os segmentos formam um triângulo')
    if a == b and b == c:
        print('O triângulo formado e um triângulo equilatero')
    elif a == c or b == a or b == c:
        print('O triângulo formado é um triângulo isóceles')
    else:
        print('O triângulo formado é um triãngulo escaleno')
else:
    print('Os segmentos não formam um triângulo')