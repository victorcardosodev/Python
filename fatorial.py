valor = int(input('Digite um número para que seu fatorial seja calculado: '))
num = valor
fator = num - 1
calculo = 1

escolha = int(input('Digite um número para escolher como fazer: [1] While ou [2] For: '))

if escolha == 1:    
    while fator != 0:
        calculo *= num
        fator -= 1
        num -= 1

    print(f'O resultado de {valor}! (fatorial) é: {calculo}')

elif escolha == 2:
    for fator in range (num, 1, -1):
        calculo *= fator
        num -= 1

    print(f'O resultado de {valor}! (fatorial) é: {calculo}')

else:
    print('Opção inválida!')