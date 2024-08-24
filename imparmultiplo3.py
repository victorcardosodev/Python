soma = 0
for num in range(1+2, 501, 3):
    parimpar = num % 2
    if parimpar == 1:
        soma += num
        print (soma)