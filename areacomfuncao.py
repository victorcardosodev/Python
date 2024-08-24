def area(a, l):
    area = a * l
    print(f'O valor da área de um terreno {l:.1f}m² x {a:.1f}m² é: {area:.1f}m²')


# Programa principal
a = float(input('Digite o valor da altura: '))
l = float(input('Digite o valor da largura: '))

area(a, l)
