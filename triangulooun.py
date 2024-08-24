print('Analisando triângulos')

r1 = float(input('Digite o valor do primeiro segmento: '))
r2 = float(input('Digite o valor do segundo segmento: '))
r3 = float(input('Digite o valor do terceiro segmento: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima PODEM FORMAR um triângulo', end=' ')
    if r1 == r2 == r3:
        print('e é um triângulo EQUILÁTERO')
    elif r1 != r2 != r3 != r1:
        print('e é um triângulo ESCALENO')
    else:
        print('e é um triângulo ISÓSCELES')
else:
    print('Baseado nos valores digitados os segmentos não podem formar um triângulo')