# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário com 15% de aumento

salary = float(input('Digite o salário: '))
print('O salário atual é: {}'
      '\nO novo salário é: {:.2f}'.format(salary, (15 / 100 * salary) + salary))
