frase = input('Digite uma frase qualquer: ')
frase = frase.upper()
vezes = frase.count('A')
primeira = frase.find('A')
ultima = frase.rfind('A')

print('A letra A aparece {} vezes na frase.'.format(vezes))
print('A primeira letra A aparece na posição {}'.format(primeira + 1))
print('A ultima letra A aparece na posição {}'.format(ultima + 1))