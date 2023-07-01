# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar
# Cotação dolar 1 = 4,79

money = float(input('Quanto dinheiro você tem na carteira?: '))

convertDolar = money / 4.79

print('Você pode comprar {:.2f} dólares'.format(convertDolar))
