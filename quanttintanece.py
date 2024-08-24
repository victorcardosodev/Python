largura = float(input('Digite em metros a largura da parede que será pintada: '))
altura = float(input('Agora digite em metros a altura: '))
area = largura*altura
litrostinta = area/2

print('A quantidade de litros de tinta para pintar uma área de {}m² é de {} litros'.format(area, litrostinta))