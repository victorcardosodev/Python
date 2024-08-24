from time import sleep

print('Digite dois valores')
num1 = int(input('Primeiro valor: '))
num2 = int(input('Segundo valor: '))

sleep(0.5)
print('''\nOpções de ações com os valores digitados
      
[ 1 ] Somar
[ 2 ] Multiplicar
[ 3 ] Maior
[ 4 ] Novos números
[ 5 ] Sair do programa''')

opcao = int(input('\nSua escolha: '))

if opcao > 0 and opcao < 6:
    while opcao != 5:
        if opcao == 1:
            print(f'A soma entre {num1} e {num2} é {num1 + num2}')
            opcao = 6
        elif opcao == 2:
            print(f'O produto entre {num1} e {num2} é {num1 * num2}')
            opcao = 6
        elif opcao == 3:
            if num1 > num2:
                print(f'O maior valor é {num1}')
            else:
                print(f'O maior valor é {num2}')
            opcao = 6
        elif opcao == 4:
            num1 = int(input('Informe o novo valor para o primeiro número: '))
            num2 = int(input('Informe o novo valor para o segundo número: '))
            
            print('''\nQual ação deseja fazer com os novos valores?: 
[ 1 ] Somar
[ 2 ] Multiplicar
[ 3 ] Maior
[ 4 ] Novos números
[ 5 ] Sair do programa''')
        
            opcao = int(input('\nSua escolha: '))

        if opcao == 6:
            sleep(3)
            print('''\nDeseja fazer mais alguma ação? se sim, digite a opção: 
[ 1 ] Somar
[ 2 ] Multiplicar
[ 3 ] Maior
[ 4 ] Novos números
[ 5 ] Sair do programa''')
        
            opcao = int(input('\nSua escolha: '))

print('\nSaindo do programa...')
sleep(2)

print('\nObrigado e até a próxima!!')
sleep(1)