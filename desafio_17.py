# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo
# calcule e mostre o comprimento da hipotenusa

from math import pow, sqrt

co = float(input('Digite o valor do cateto oposto de um triangulo retângulo: '))
ca = float(input('Digite o valor do cateto adjacente de um triangulo retângulo: '))

h = sqrt((pow(co, 2)) + (pow(ca, 2)))

print('O valor da hipotenusa é: {}'.format(h))
