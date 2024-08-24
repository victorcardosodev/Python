def ficha(n, g):
    
    print(f'O jogador {n} marcou {g} gol(s) no campeonato')


nome = str(input('Digite o nome do jogador: '))
if not nome:
    nome = '<desconhecido>'

gols = input('Qual a quantidade de gols que ele marcou: ')
if not gols:
    gols = 0
elif gols.isnumeric():
    gols = int(gols)
else:
    gols = 0

ficha(nome, gols)