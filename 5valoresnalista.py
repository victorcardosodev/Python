valores = []

for num in range (0, 5):
    valores.append(int(input('Digite um valor: ')))

for posicao, valor in enumerate(valores):
    print(f'Na posição {posicao} está o valor {valor}')

print(f'o valor mais alto digitado foi: {max(valores)} e o menor foi: {min(valores)}')