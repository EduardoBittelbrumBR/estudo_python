# Crie um programa que leia o nome completo de uma pessoa e mostre:
# O nome com todas as letras maiusculas
# O nome com todas as letras minusculas
# Quantas letras ao todo (sem considerar espaço)
# Quantas letras tem o primeiro nome

name = str(input('Digite seu nome: '))

nameUpper = name.upper()
nameLower = name.lower()
removeBlank = name.replace(" ", "")
firstName = name.split()

print('Nome completo em letra maiúscula: {}'.format(nameUpper))
print('Nome completo em letra minúscula: {}'.format(nameLower))
print('Quantidade de letras sem espaço {}'.format(len(removeBlank)))
print('O primeiro nome tem {} letras'.format(len(firstName[0])))
