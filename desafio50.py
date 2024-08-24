soma = 0
for num in range(1, 7):
    num = int(input(f'Digite o {num}º número : '))
    if num % 2 == 0:
        soma += num
print(f'O resultado final da soma dos pares foi: {soma}')