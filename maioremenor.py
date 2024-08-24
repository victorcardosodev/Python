print('Nesse programa será necessário que seja digitado 3 números inteiros')

num1 = int(input('Primeiro número: '))
num2 = int(input('Segundo número: '))
num3 = int(input('Terceiro número: '))

lista = sorted([num1, num2, num3])
print('O maior número digitado foi: {} e o menor número foi: {}'.format(lista[2], lista[0]))