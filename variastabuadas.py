from time import sleep

tabuada = int(input('Digite o número da tabuada que deseja ou digite um número negativo para fechar o programa: '))

max = 0

while tabuada >= 0:
    print(f'A tabuada de {tabuada} é:')
    while max <= 10:
        print(f'{tabuada} x {max} = {tabuada * max}')
        max += 1
    max = 0
    tabuada = int(input('Digite outro valor ou um número negativo pra fechar um programa: '))
    if tabuada < 0:
        break
print('Fechando o programa...')
sleep()