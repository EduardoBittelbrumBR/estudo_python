# Crie um programa que receba o nome de 4 alunos e monte uma sequência de apresentação

from random import shuffle

student1 = input('Digite o nome do primeiro aluno: ')
student2 = input('Digite o nome do segundo aluno: ')
student3 = input('Digite o nome do terceiro aluno: ')
student4 = input('Digite o nome do quarto aluno: ')

lista = [student1, student2, student3, student4]
shuffle(lista)

print('A sequência para apresentação do trabalho é: {}'.format(lista))
