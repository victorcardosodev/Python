galera = []
pessoa = []
pesos = []
vezes = 0

maiorpeso = menorpeso = 0
cadastrados = 0

while True:
    nome = input('Digite o nome da pessoa: ')
    peso = float(input('Digite o peso: '))

    pessoa.append(nome)
    pessoa.append(peso)

    galera.append(pessoa[:])
    pessoa.clear()

    cadastrados += 1

    escolha = str(input('Quer continuar [S/N]: '))
    if escolha in 'Nn':
        break

for pes in galera:
    pesos.append(galera[vezes][1])
    vezes += 1




print(f'A quantidade de pessoas cadastradas foi de: {cadastrados}')
print(galera)
print(f'O maior peso foi {max(pesos)} e o menor foi {min(pesos)}')