# Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
# Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido

from random import choice

student1 = input('Digite o nome do primeiro aluno: ')
student2 = input('Digite o nome do segundo aluno: ')
student3 = input('Digite o nome do terceiro aluno: ')
student4 = input('Digite o nome do quarto aluno: ')

rc = [student1, student2, student3, student4]

print('O aluno que irá apagar o quadro é: {}'.format(choice(rc)))
