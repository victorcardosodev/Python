from random import randint
from time import sleep

numuser = int(input('tente adivinhar o número que o computador vai escolher 0 a 10: '))
numcomp = randint(0, 10)
tentativas = 0

while numuser != numcomp:
    if numuser < 0 or numuser > 10:
        numuser = int(input('número invalido, tente um outro número: '))
    else:
        print('processando...')
        sleep(1)
        numuser = int(input('Você errou, tente um outro número: '))
        tentativas += 1
print(f'Parabéns, você acertou, foram necessário {tentativas+1} tentativa(s)')