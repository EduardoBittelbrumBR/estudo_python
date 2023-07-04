# Faça um programa que leia uma frase pelo teclado e mostre:
# Quantas vezes aparece a letra A
# Em que posição ela aparece pela primeira vez
# Em que posição ela aparece a última vez

phrase = str(input('Digite uma frase: ')).strip()

phraseUpper = phrase.upper()
countA = phraseUpper.count('A')
firstA = phraseUpper.index('A')
lastA = phraseUpper.rindex('A')

print('Quantidade letra A: {}'
      '\nPosição primeiro A: {}'
      '\nPosição último A: {}'.format(countA, firstA, lastA))
