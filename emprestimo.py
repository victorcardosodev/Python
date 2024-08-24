casa = float(input('Digite o valor da casa: '))
salario = float(input('Digite o valor do seu salario: '))
anos = int(input('Planeja quitar em quantos anos: '))

meses = anos * 12
prestacao = casa / meses
partsal = salario * 30 / 100

if prestacao > partsal:
    input('O empréstimo foi negado pois o valor da prestação (R${:.2f}) é maior que 30% do seu salário'.format(prestacao))
else:
    input('Parabéns, seu empréstimo de R${:.2f} foi aprovado !! O valor das parcelas ficaram em R${:.2f}'.format(casa, prestacao))