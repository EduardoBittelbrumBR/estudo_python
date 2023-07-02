# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno,
# Cosseno e tangente

from math import cos, sin, tan

a = float(input('Digite o valor do ângulo: '))

print('Para o ângulo {} temos:'
      '\nCosseno: {:.2f}'
      '\nSeno: {:.2f}'
      '\n Tangente: {:.2f}'.format(a, cos(a), sin(a), tan(a)))
