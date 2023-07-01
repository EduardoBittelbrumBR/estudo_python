# Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada

number1 = float(input('Digite um número: '))

double = number1 * 2
triple = number1 * 3
sr = number1 ** (1/2)

print('Dobro: {} \nTriplo: {}\nRaiz quadrada: {:.2f}'.format(double, triple, sr))
