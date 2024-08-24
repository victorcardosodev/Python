valores = []
escolha = 'S'

while escolha == 'S':
    num = int(input('Digite um valor: '))
    if num in valores:
        print('Valor duplicado! Não vou adicionar...')
    else:
        valores.append(num)
        print('Valor adicionado com sucesso...')

        escolha = str(input('Deseja continuar adicionando valores na lista ? [S/N]: ')).strip().upper()[0]
        
        while escolha != 'N' and escolha != 'S':
            print('Opção inválida...')
            escolha = str(input('Deseja continuar adicionando valores na lista ? [S/N]: ')).strip().upper()[0]
      
valores.sort()      
print(valores)




