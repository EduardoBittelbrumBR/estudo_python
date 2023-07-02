# import biblioteca matemática
# importa biblioteca random

from math import sqrt
import random
import emoji

number = int(input('Digite um número: '))

sqr = sqrt(number)

print('A raiz quadrada de {} é {}'.format(number, sqr))

# printa número aleatório em tela

number2 = random.random()
print(number2)

# gera número aleatório entre 1 e 10

number3 = random.randint(1, 10)
print(number3)

# Printa um emoji em tela

print(emoji.emojize("Hello world :sunglasses:"))
