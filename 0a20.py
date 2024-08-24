numeral = 'zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte'

while True:
    numero = int(input('Digite um número de 0 a 20: '))
    if numero < 0 or numero > 20:
        print('Tente novamente. ', end='')
    else:
        break

print(f'Você digitou o número {numeral[numero]}')