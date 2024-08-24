estatistica = dict()
listgols = list()

estatistica['nome'] = str(input('Nome do jogador: '))
estatistica['partidas'] = int(input(f'Quantas partidas {estatistica['nome']} jogou?: '))

for partida in range(0, estatistica['partidas']):
    listgols.append(int(input(f'Quantos gols na partida {partida + 1}: ')))
    estatistica['gols'] = listgols
    estatistica['total'] = sum(listgols)

print(f'''jogador: {estatistica['nome']}
gols: {estatistica['gols']}
total de gols: {estatistica['total']}''')       

print(f'O jogador {estatistica['nome']} jogou {estatistica['partidas']} partidas')

for p, g in enumerate(listgols):
    print(f'=> Na partida {p + 1} fez {listgols[p]} gols')
print(f'Foi um total de {estatistica['total']} gols')