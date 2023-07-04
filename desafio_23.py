# Faça um programa que leia um número entre 0 e 9999
# Mostre na tela cada um dos dígitos separado

number = str(input('Digite um número entre 0 e 9999: '))
unit = number[3]
ten = number[2]
hundred = number[1]
thousand = number[0]

print('Unidade: {}'
      '\nDezena: {}'
      '\nCentena: {}'
      '\nMilhar: {}'.format(unit, ten, hundred, thousand))
