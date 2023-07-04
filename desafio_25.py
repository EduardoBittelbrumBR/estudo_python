# Crie um programa que leia o nome de uma pessoa e diga se ela tem SILVA no nome

name = str(input('Digite seu nome: '))

# Convert variable name to UPPER

nameUpper = name.upper()

nameFind = nameUpper.find('SILVA')

print(nameFind)

if nameFind == -1:
    print('O nome não contem SILVA')
else:
    print('O nome contem SILVA')
