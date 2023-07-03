# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno,
# Cosseno e tangente

from math import cos, sin, tan, radians

a = float(input('Digite o valor do ângulo: '))

print('Para o ângulo {} temos:'
      '\nCosseno: {:.2f}'
      '\nSeno: {:.2f}'
      '\nTangente: {:.2f}'.format(a, cos(radians(a)), sin(radians(a)), tan(radians(a))))
