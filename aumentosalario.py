salarioatual = float(input('Digite seu salário atual: '))
aumento = float(input('Digite a porcentagem do aumento: '))

novosalario = salarioatual+(salarioatual*(aumento/100))

print('Com o aumento de {}% no seu salário, ele passa de R${:.2f} para R${:.2f}'.format(aumento, salarioatual, novosalario))