#Criar um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.
tul = 'casa', 'onibus', 'verdura', 'calça', 'mesa'
for c in tul: #Ele vai pegar cada item da lista na posição C
    print(f'\n A palavra è {c.upper()} e as vogais são ', end='')
    for x in c: #O X vai analisar cada letra dentro da palavra
        if x.lower() in 'aeiou':
            print(x, end=' ')