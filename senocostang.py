from math import sin, cos, tan, radians

angulo = float(input('Digite o valor do ângulo que deseja descobrir as medidas de seno, cosseno e tangente: '))
sen = sin(radians(angulo))
cost = cos(radians(angulo))
tang = tan(radians(angulo))

print('as medidas do angulos de {}° é: \nseno: {:.3f} \ncosseno: {:.3f} \ntangente: {:.3f}'.format(angulo, sen, cost, tang))