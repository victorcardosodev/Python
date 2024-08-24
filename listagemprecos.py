listagem = 'Lápis', 1.75, 'Borracha', 2, 'Caderno', 15.9, 'Estojo', 25, 'Transferidor', 4.2, 'Compasso', 9.99, 'Mochila', 120.32, 'Canetas', 22.3, 'Livro', 34.9

#precos = 1
tamanho = len(listagem)

for produtos in range(0, tamanho):
    if produtos % 2 == 0:
        print(f'{listagem[produtos]:.<30}', end='')
    else:
        print(f'R${listagem[produtos]:>7.2f}')
    
#    print(f'R$ {listagem[precos]:.2f}')
#    precos += 2