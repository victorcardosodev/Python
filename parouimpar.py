num = int(input('Digite um número inteiro: '))
resto = num % 2

if resto == 0:
    print('O número que você digitou "{}" é par'.format(num))
else:
    print('O número que você digitou "{}" é impar'.format(num))