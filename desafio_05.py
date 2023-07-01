# Faça um programa que leia um número inteiro e mostre em tela o seu sucessor e seu antecessor

number1 = int(input('Digite um número: '))

predecessor = number1 - 1
successor = number1 + 1

print('O antecessor do número é: {} \nO sucessor do número é {}'.format(predecessor, successor))
