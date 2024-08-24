lista = []
escolha = 'S'
num = int(input('Digite um número: '))

while escolha == 'S':
    lista.append(num)

    escolha = str(input('Deseja continuar? [S/N]: ')).strip().upper()
    if escolha != 'S' and escolha != 'N':
        print('Tente novamente!')
        escolha = str(input('Deseja continuar? [S/N]: ')).strip().upper()
    if escolha == 'N':
        break

    num = int(input('Digite um número: '))

if 5 in lista:
    print(f'O primeiro valor 5 foi encontrado na lista no indice {lista.index(5)}!')
else:
    print('O valor 5 não foi encontrado na lista!')

print(f'A lista na ordem digitada: {lista}')
print(f'A quantidade de números digitados foi de: {len(lista)}')
lista.sort(reverse=True)
print(f'A lista em ordem decrescente ficou dessa forma: {lista}')