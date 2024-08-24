nomemaior = ''
idademaior = 0

idademenor = 20
nomemenor = ''

somaidade = 0

for pessoa in range(1, 6):
    nome = str(input('Digite seu nome: '))
    idade = int(input('Digite sua idade: '))

    if idade > idademaior:
        idademaior = idade
        nomemaior = nome

    elif idade < idademenor:
        nomemenor = nome
        idademenor = idade

    somaidade += idade
media = somaidade / 5

print(f'A pessoa mais velha é {nomemaior} com {idademaior} de idade e a mais nova é {nomemenor} com {idademenor} de idade. A média de idade do grupo é {media}')