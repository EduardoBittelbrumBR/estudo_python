# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros

meters = float(input('Digite valor em metros: '))

cm = meters * 100
mm = meters * 1000

print('Metros: {} \nCentimetros: {}\nMilimetros: {}'.format(meters, cm, mm))
