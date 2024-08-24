lista = []
listaimpar = []
listapar = []
escolha = 'S'

num = int(input('Digite um número: '))

while escolha == 'S':
    lista.append(num)
    if num % 2 == 1:
        listaimpar.append(num)
    else:
        listapar.append(num)

    escolha = str(input('Deseja continuar? [S/N]: ')).strip().upper()
    if escolha != 'S' and escolha != 'N':
        print('Tente novamente!')
        escolha = str(input('Deseja continuar? [S/N]: ')).strip().upper()
    if escolha == 'N':
        break

    num = int(input('Digite um número: '))

print(f'A lista com todos os números ficou assim: {lista}')
print(f'A lista com números impares: {listaimpar}')
print(f'A lista com números pares: {listapar}')