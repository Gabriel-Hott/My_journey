#fazer um programa que leia largura e altura de uma parede em metros, Calcule sua área e a quantidade necessaria de tinta para pintala, sabendo que um litro de tinta pinta uma área de 2m2.
l = float(input('Qual a largura de sua parede: '))
al = float(input('Qual a altura de sua parede: '))
area = l * al
tinta = area / 2
print('Se sua parede com as medidas de {} largura e {} altura totalizando {:.2f}m quadrados, você precisara aproximadamente de {:.2f}L de tinta'.format(l, al, area, tinta))