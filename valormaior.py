num1 = int(input('Digite um número inteiro qualquer: '))
num2 = int(input('Digite outro número inteiro qualquer: '))

if num1 > num2:
    print('O primeiro número ({}) é maior que o segundo ({})'.format(num1, num2))
elif num2 > num1:
    print('O segundo número ({}) é maior que o primeiro ({})'.format(num2, num1))
else:
    print('Os dois números são iguais')