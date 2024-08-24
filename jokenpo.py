from random import randint
from time import sleep

opcoes = ['pedra', 'papel', 'tesoura']

print('''
bem-vindo ao jokenpo
[0] Pedra
[1] Papel
[2] Tesoura
''')
opcao = int(input('Digite uma opção de 0 a 2: '))

if opcao > 2 or opcao < 0:
    print('Opção inválida!')
else:
    print('Jo')
    sleep(1.2)

    print('Ken')
    sleep(1.2)

    print('po')
    sleep(0.35)

    comp = randint(0, 2)

    print(f'O computador escolheu {opcoes[comp]}')
    print(f'Você escolheu {opcoes[opcao]}')

    if opcao == 0 and comp == 0 or opcao == 1 and comp == 1 or opcao == 2 and comp == 2:
        print('Empate!')

    elif opcao == 0 and comp == 2 or opcao == 1 and comp == 0 or opcao == 2 and comp == 1:
        print('Você ganhou!')

    else:
        print('Você perdeu!')
