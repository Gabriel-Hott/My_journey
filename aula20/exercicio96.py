#Criar um programa que tenha uma função chamara área(), que receba as dimensões de um terreno retangular (LARGURA e COMPRIMENTO) e mostre a área do terreno. AxB
def área(a, b):
    soma = a * b
    print(f'A partir das medidas {a:.2f}m e {b:.2f}m , a sua área calculada é {soma:.2f}²')

#Código principal
 
área(float(input('Digite a largura do terreno: ')), float(input('Qual o comprimento do terreno: ')))