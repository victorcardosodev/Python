limitetermos = 0
progressao = 0

termo = int(input('Digite o primeiro termo da progressão aritmética: '))
razao = int(input('Digite a razão da progressão aritmética: '))

while limitetermos < 10:
    conta = termo + razao
    termo = conta
    progressao +=1
    print(f'{progressao}º termo: {conta-razao}')
    limitetermos += 1