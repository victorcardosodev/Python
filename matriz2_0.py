numeros = []
matrizmontada = []

somaterceiracol = 0
maiorvalor2l = 0
somapares = 0
linhavertical = 0
linhahorizontal = 0

for matriz in range(0, 9):
    
    num = int(input(f'Digite o valor da matriz [{linhavertical}, {linhahorizontal}]: '))
    numeros.append(num)
    linhahorizontal += 1

    if num % 2 == 0:
        somapares += num

    if linhahorizontal == 3:
        somaterceiracol += num
        matrizmontada.append(numeros[:])
        numeros.clear()
        linhavertical += 1
        linhahorizontal = 0

for p, v in enumerate(matrizmontada):
    print(f'[{v[0]:^5}] [{v[1]:^5}] [{v[2]:^5}]')


print(f'a soma da segunda linha é: {matrizmontada[1][0] + matrizmontada[1][1] + matrizmontada[1][2]}')
print(f'o resultado da soma dos valores pares digitados é: {somapares}')
print(f'a soma da terceira coluna resultado no valor: {somaterceiracol}')