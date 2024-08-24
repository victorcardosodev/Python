from random import randint
jogo = []
jogos = []
cont = 0

quantjogos = int(input('Digite a quantidade de jogos que deseja: '))
for _ in range(0, quantjogos):
    while True:
        num = randint(1, 60)
        if num not in jogo:
            jogo.append(num)
            cont += 1
        
        if cont >= 6:
            break
    
    jogo.sort()
    jogos.append(jogo[:])
    jogo.clear()
    cont = 0

for gerados in range(0, quantjogos):
    print(f'Jogo {gerados+1}: {jogos[gerados]}')