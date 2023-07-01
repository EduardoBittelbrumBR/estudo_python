# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade
# de tinta necessária para pinta-la, sabendo que cada litro de tinta pinta uma área de 2m2

height = float(input('Digite a altura em metros: '))
width = float(input('Digite a largura em metros: '))

area = height * width
calcInk = area / 2

print('Altura: {}'
      '\nLargura: {}'
      '\nÁrea: {}'
      '\nLitros de tinta necessários para pintar essa área: {}'.format(height, width, area, calcInk))
