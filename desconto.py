preco = float(input('Digite o valor do produto: '))
desconto = float(input('Digite a porcentagem do desconto: '))

novopreco = preco-(preco*(desconto/100))

print('O preco do produto deixou de ser R${:.2f} e com o desconto de {}% passou a ser R${:.2f}'.format(preco, desconto, novopreco))