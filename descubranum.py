from random import randint
from time import sleep

numsorteado = randint(0, 5)
numdigitado = int(input('Tente descobrir qual o número de 1 a 5 que o computador irá escolher: '))
print('Escolhendo o número...')
sleep(2)

if numdigitado == numsorteado:
    print('Parabéns, você acertou!!')
else:
    print('Que pena, você errou ! O número escolhido pelo computador foi {}'.format(numsorteado))