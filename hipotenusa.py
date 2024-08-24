from math import hypot

catoposto = float(input('Digite o valor do cateto oposto: '))
catadjacente = float(input('Digite o valor do cateto adjacente: '))

hipotenusa = hypot(catoposto, catadjacente)

print('Você digitou que o cateto adjacente é {:.2f} e o cateto oposto é {:.2f}, o resultado da hipotenusa foi {:.2f}'.format(catadjacente, catoposto, hipotenusa))