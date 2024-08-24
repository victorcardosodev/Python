maismil = 0

produto = str(input('Nome do produto: '))
preco = float(input('Preço do produto: '))

maisbarato = produto
precomaisbarato = preco
totalgasto = preco

if preco > 1000: maismil += 1

confirmacao = str(input('Gostaria de continuar [S/N]: ')).upper()

while confirmacao == 'S':
    produto = str(input('Nome do produto: '))
    preco = float(input('Preço do produto: '))
    
    totalgasto += preco

    if preco > 1000:
        maismil += 1

    if preco < precomaisbarato:
        precomaisbarato = preco
        maisbarato = produto

    confirmacao = str(input('Gostaria de continuar [S/N]: ')).upper()

print(f'O valor total gasto na compra foi de R$ {totalgasto}')
print(f'Produtos com valor maior que R$ 1000,00: {maismil}')
print(f'Produto com menor valor: {maisbarato} ')