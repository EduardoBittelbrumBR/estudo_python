# Faça um programa que leia o nome completo de uma pessoa
# mostrando em seguida o primeiro e último nome
# separadamente

name = str(input('Digite um nome: ')).strip()

split = name.split()
firstName = split[0]
convertSplit = len(split)
int(convertSplit)
positionLastName = convertSplit - 1
lastname = split[positionLastName]

print('Nome completo: {}'.format(name.title()))
print('Primeiro nome: {}'.format(firstName.title()))
print('Último nome: {}'.format(lastname.title()))
