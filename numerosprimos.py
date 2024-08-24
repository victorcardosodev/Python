num = int(input('Digite um número inteiro: '))
divisor = 0
for c in range(1, num+1):
    if num % c == 0 :
        divisor += 1
if divisor == 2:
    print(f'O número {num} pode ser divido apenas {divisor} vezes: por 1 e pelo próprio {num}, logo é um número primo')
else:
    print(f'O número {num} pode ser divido {divisor} vezes, logo é número composto')