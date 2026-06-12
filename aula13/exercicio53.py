#Criar um programa que leie uma frase e diga se ela é palindromo, desconsiderando espaços. (frases/palavras que podem ser lidas de trás para frente)
for c in range (1, 6):
    frase = str(input('Digite uma frase e vejá se ela e PALINDROMA: ')).upper()
    test = frase.replace(' ','')
    if test == test[::-1]:
        print('Essa frase {} é um POLINDROMO.'.format(frase))