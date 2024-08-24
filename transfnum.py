num = int(input('Digite o número que deseja converter: '))
print('Escolha uma das opções abaixo:')
print('[1] Converter para Binário')
print('[2] Converter para Octal')
print('[3] Converter para Hexadecimal')
opcao = int(input('Sua opção: '))

if opcao == 1:
    print(f'O número {num} em Binário é {bin(num)[2:]}')

elif opcao == 2:
    print(f'O número {num} em octal é {oct(num)[2:]}')

elif opcao == 3:
    print(f'O número {num} em Hexadecimal é {hex(num)[2:]}')

else:
    print('Opção inválida!')    