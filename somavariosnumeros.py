soma = 0
digitados = 0

num = int(input('Digite um numero para soma ou digite 999 pra sair do programa: '))

while num != 999:
    soma += num
    digitados += 1

    num = int(input('Digite um numero para soma ou digite 999 pra sair do programa: '))

print(f'A quantidade de números digitados foi {digitados} e a soma total entre eles foi de {soma}')