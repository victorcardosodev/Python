lista = []

for numero in range(0, 5):
    num = int(input('Digite um número aleatório: '))
    if num in lista:
        while num in lista:
            num = int(input('Valor duplicado, digite outro valor: '))
            if num not in lista:
                break
    
    if numero == 0 or num > lista[-1]:
        lista.append(num)
        print('Valor adicionado ao final da lista! ')
    else:
        pos = 0
        while pos < len(lista):
            if num < lista[pos]:
                lista.insert(pos, num)
                break
        print(f'valor adicionado na posição {pos}')
        pos += 1
    
print(lista)