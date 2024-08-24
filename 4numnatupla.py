tupla = ()
tuplapar = ()

for loop in range(4):
    num = int(input(f'Digite o {loop + 1}º loop: '))

    tupla = tupla + (num,)

    if num % 2 == 0:
        tuplapar = tuplapar + (num,)


quantnove = tupla.count(9)
print(f'A quantidade de números nove digitado foi {quantnove}')

if 3 in tupla:
    wherethree = tupla.index(3)
    print(f'o primeiro número 3 foi guardado na posição {wherethree} da memória')
else:
    print('O número 3 não foi digitado')

print(tupla)

print(f'Esses foram os números pares {tuplapar}')