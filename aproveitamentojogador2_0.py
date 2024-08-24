estatistica = dict()
listgols = list()
todosjogadores = list()

while True:
    estatistica['nome'] = str(input('Nome do jogador: '))
    estatistica['partidas'] = int(input(f'Quantas partidas {estatistica['nome']} jogou?: '))

    for partida in range(0, estatistica['partidas']):
        listgols.append(int(input(f'Quantos gols na partida {partida + 1}: ')))

        estatistica['gols'] = listgols[:]
        estatistica['total'] = sum(listgols)

    listgols.clear()

    print(f'''jogador: {estatistica['nome']}
    gols: {estatistica['gols']}
    total de gols: {estatistica['total']}''')       

    print(f'O jogador {estatistica['nome']} jogou {estatistica['partidas']} partidas')
    
    todosjogadores.append(estatistica.copy())

    escolha = str(input('Deseja continaur [S/N]: '))

    if escolha in 'Nn':
        break

for id, player in enumerate(todosjogadores):
    print(f'{id} {todosjogadores[id]['nome']} {todosjogadores[id]['gols']:} {todosjogadores[id]['total']}')

while True:
    escolha = int(input('Mostrar dados de qual jogador? (ou 999 para sair): '))
    if escolha == 999:
        break
    
    if escolha > len(todosjogadores):
        print('Escolha invalida')
    else:
        print(f'-- Levantamento do jogador {todosjogadores[escolha]["nome"]}')
        for p, g in enumerate(todosjogadores[escolha]['gols']):
            print(f'na partida {p + 1} ele fez {g}')

