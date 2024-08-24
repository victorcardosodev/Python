num = int(input('Digite um valor inteiro: '))

quantidade = 0
maior = num
menor = num
soma = 0

while num != -1:
    quantidade +=1
    soma += num
    media = soma / quantidade

    if num > maior:
        maior = num
    
    elif num < menor:
        menor = num

    num = int(input('Digite outro outro número, ou se desejar sair digite "-1" para sair: '))

print(f'A quantidade de números digitados foi {quantidade}, a média foi de {media}, o maior número foi {maior} e o menor foi {menor}')