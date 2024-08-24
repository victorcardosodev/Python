from datetime import date

anonas = int(input('Digite o ano de nascimento do atleta: '))
anoatual = date.today().year
idade = anoatual - anonas

print(f'A idade do atleta é: {idade} anos')

if 0 < idade <= 9:
    print('Categoria: MIRIM') 

elif 9 < idade <= 14:
    print('Categoria: INFANTIL')

elif 14 < idade <= 19:
    print('Categoria: JUNIOR')

elif 19 < idade <= 25:
    print('Categoria: Sênior')

elif idade > 25:
    print('Categoria: MASTER')

else:
    print('Idade invalida')