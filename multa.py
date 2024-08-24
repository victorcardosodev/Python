velmax = 80
velcarro = float(input('Digite a velocidade que seu carro estava: '))
if velcarro > 80:
    multa = (velcarro - 80) * 7
    print('você foi multado no valor de R${:.2f}'.format(multa))