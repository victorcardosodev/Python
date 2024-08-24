from time import sleep

progressao = 0

termo = int(input('Digite o primeiro termo da progressão aritmética: '))
razao = int(input('Digite a razão da progressão aritmética: '))
quanttermos = int(input('Insira a quantidade de termos que deseja que seja apresentado: '))

while quanttermos != 0 and progressao < quanttermos:
    conta = termo + razao
    termo = conta
    progressao +=1
    print(f'{progressao}º termo: {conta-razao}')
    if progressao == quanttermos:
        quanttermos += int(input('Deseja mostrar mais termos dessa progressão aritmética? se sim, digite a quantidade ou digite 0 para encerrar: '))

print('Encerrando programa...')
sleep(1)