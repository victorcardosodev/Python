numeros = []
matrizmontada = []
linhavertical = 0
linhahorizontal = 0

for matriz in range(0, 9):
    
    num = int(input(f'Digite o valor da matriz [{linhavertical}, {linhahorizontal}]: '))
    numeros.append(num)
    linhahorizontal += 1
    
    if linhahorizontal == 3:
        matrizmontada.append(numeros[:])
        numeros.clear()
        linhavertical += 1
        linhahorizontal = 0

for p, v in enumerate(matrizmontada):
    print(f'[{v[0]:^5}] [{v[1]:^5}] [{v[2]:^5}]')