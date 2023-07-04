# Crie um programa que leia o nome de uma cidade e e diga se ela começa ou não com o nome SANTO

city = str(input('Digite o nome de uma cidade: '))

cityUpper = city.upper()
citySplit = cityUpper.split()

cityFind = citySplit[0].find('SANTO')

if cityFind == -1:
    print('O nome da cidade não contem SANTO')
else:
    print('O nome da cidade contem SANTO')
