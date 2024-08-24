termo = int(input('Digite o primeiro termo da progressão aritmética: '))
razao = int(input('Digite a razão da progressão aritmética: '))

for progressao in range(1, 11):
    conta = termo + razao
    termo = conta

    print(f'{progressao}º termo: {conta-razao}')