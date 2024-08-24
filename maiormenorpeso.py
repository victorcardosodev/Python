maiorpeso = 0.0
menorpeso = 1000.0

for pessoas in range(1, 6):
    peso = float(input(f'Digite o {pessoas}º peso: '))
    if peso > maiorpeso:
        maiorpeso = peso
    elif peso < menorpeso:
        menorpeso = peso
print(f'O maior peso foi de {maiorpeso:.2f}KG e o menor {menorpeso:.2f}KG')