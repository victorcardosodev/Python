lista = [[],[]]


for val in range(0, 7):
    num = int(input(f'Digite o {val + 1}° valor: '))

    if num % 2 == 0:
        lista[0].append(num)
    else:
        lista[1].append(num)

lista[0].sort()
lista[1].sort()

print(f'Os valores pares foram os {lista[0]}')
print(f'Os valores ímpares foram os {lista[1]}')