from random import randint

tupla = ()
menor = maior = 0

quant = int(input('Quantos valores serão digitados?: '))

for num in range(quant):
    num = randint(0, 100)

    tupla += (num,)
    #tupla = tupla + tuple([num])


print(tupla)
print(f'o Maior valor digitado foi {max(tupla)} e o menor foi {min(tupla)}')