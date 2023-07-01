# Desenvolva um algoritmo que leia as duas notas de um aluno, calcule e mostre a sua média

number1 = float(input('Digite a primeira nota: '))
number2 = float(input('Digite a segunda nota: '))

average = (number1 + number2) / 2

print('Nota 1: {} \nNota 2: {}\nMédia: {:.1f}'.format(number1, number1, average))
