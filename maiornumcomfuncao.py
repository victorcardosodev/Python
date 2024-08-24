numeros = list()

def maiornum(num):
    maior = max(numeros)
    print(maior)

while True:
    num = int(input('Digite um número: '))
    numeros.append(num)
    
    escolha = str(input('Deseja continuar ? [S/N]: '))
    if escolha in 'Nn':
        break

maiornum(numeros)