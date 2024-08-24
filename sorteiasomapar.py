from random import randint

def sorteia():
    global sorteio
    sorteio = list()
    for _ in range(0, 5):
        sorteio.append(randint(1, 10))

    print(sorteio)


def soma(lista):
    somapar = 0
    for valor in lista:
        if valor % 2 == 0:
            somapar += valor
    
    print(somapar)

sorteia()
soma(sorteio)