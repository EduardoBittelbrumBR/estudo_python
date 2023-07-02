# Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção inteira
# Ex: Digite o número 6.127, o número tem a parte inteira 6

from math import floor

number = float(input('Digite um número real: '))

npi = floor(number)

print('A porção real do número {} é {}'.format(number, npi))
