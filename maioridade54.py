from datetime import date

maior = 0
menor = 0

print('Digite o ano de nascimento de 7 pessoas')
for pessoa in range(1, 8):
    anonasc = int(input(f'Digite o ano de nascimento da {pessoa}º pessoa: '))
    if date.today().year - anonasc > 18:
        maior += 1
    else:
        menor += 1
print(f'A quantidade de pessoas maiores de idade é {maior} e de menores de idade é {menor}')
    