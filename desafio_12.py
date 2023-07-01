#Faça um programa que leia o preço de um produto e mostre seu novo preço, com 5% de desconto

price = float(input('Digite o valor do produto: '))
print('O valor atual do produto é: {}'
      '\nO novo valor do produto é: {:.2f}'.format(price, price - (5 / 100 * price)))
