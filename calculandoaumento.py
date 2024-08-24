salario = float(input('Digite o valor do seu salário: '))

if salario >= 1250:
    novosal = salario + (salario/10)
    print('O seu novo salário é de R${:.2f}'.format(novosal))
else:
    novosal = salario + (salario/100*15)
    print('O seu novo salário é de R${:.2f}'.format(novosal))