distancia = float(input('Digite em KM qual a distância que será essa viagem: '))

if distancia <= 200:
    print('Sua passagem custará R${:.2f}'.format(distancia*0.50))
else:
    print('Sua passagem custará R${:.2f}'.format(distancia*0.45))