produto = float(input('Digite o valor do produto que será comprado: '))
formpag = int(input('''Os números correspondente a forma de pagamento
                    \n1 = à vista
                    \n2 = à vista no cartão
                    \n3 = em até 2x no cartão
                    \n4 = 3x ou mais no cartão
                    \nDigite a forma de pagamento escolhida: '''))

if formpag == 1:
    valorfinal = produto * 0.9
    print(f'O valor final do produto é R${valorfinal:.2f}')
elif formpag == 2:
    valorfinal = produto * 0.95
    print(f'O valor final do produto é R${valorfinal:.2f}')
elif formpag == 3:
    print(f'O valor da compra é R${produto:.2f}')
elif formpag == 4:
    valorfinal = produto * 1.20
    print(f'O valor final do produto ficará em R${valorfinal:.2f}')
else:
    print('Opção inválida!')