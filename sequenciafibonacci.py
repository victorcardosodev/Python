limite = 0
x = 0
y = 0
z = 1
num = int(input('Digite um número inteiro qualquer: '))

while limite < num:
    limite += 1
    x = y
    y = z
    print(f'{limite}º termo: {z}')
    z = y + x
    