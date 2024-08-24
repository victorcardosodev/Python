from time import sleep

def contagem(i, f, p):
    for contador in range(i, f, p):
        sleep(0.5)
        print(contador, end=' ')


inicio = int(input('Inicio: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))


if passo == 0 and inicio < fim:
    passo = 1
elif passo == 0 and inicio > fim:
    passo = -1

if inicio > fim and passo > 0:
    passo = passo - passo - passo

print(f'A contagem de {inicio} até {fim} de {passo} em {passo} é: ')
contagem(inicio, fim + passo, passo)
print('FIM !!')