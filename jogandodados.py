from random import randint
from time import sleep
from operator import itemgetter

maior = 0
ganhador = ''

listaderes = list()
resultados = dict()

for players in range(0, 4):
    resultados['nome'] = str(input(f'{players + 1}º jogador digite seu nome: '))
    resultados['valordado'] = randint(1, 6)
    if resultados['valordado'] > maior:
        maior = resultados['valordado']
        ganhador = resultados['nome']

    listaderes.append(resultados.copy())
    
ranking = list()

ranking = sorted(listaderes, key=itemgetter('valordado'), reverse=True)

for players in range(len(listaderes)):
    print('-'*35)
    print(f'o Jogador {listaderes[players]['nome']} recebeu o valor {listaderes[players]['valordado']}')
    sleep(1)

print('/'*40)
print(f'O ganhador foi: {ganhador} com o valor {maior}')
print('/'*40)

for n, v in enumerate(ranking):
    print(f'{n + 1}º lugar: {v['nome']} com o valor {v['valordado']}')
    print('=-'*25)
