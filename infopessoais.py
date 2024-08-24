infos = dict()

pessoas = list()
mulheres = list()
acimamedia = list()

quantpessoas = idadetotal = mediaidade = 0

while True:
    print("\nCadastro de informações pessoais")

    infos['nome'] = str(input('Digite o nome: '))
    infos['idade'] = int(input('Digite a idade: '))
    while True:
        infos['sexo'] = str(input('Digite o sexo (M/F): ')).upper()
        if infos['sexo'] in 'MF':
            break
        print('ERRO: Por favor, digite apenas "M" ou "F"')
    
    if infos['sexo'] == 'F':
        mulheres.append(infos['nome'])
        infos['sexo'] = 'Feminino'
    elif infos['sexo'] == 'M':
        infos['sexo'] = 'Masculino'


    pessoas.append(infos.copy())

    quantpessoas += 1

    idadetotal += infos['idade']
    mediaidade = idadetotal / quantpessoas

    while True:
        escolha = str(input('Gostaria de adicionar mais alguém? [S/N]: ')).upper()

        if escolha not in 'NS':
            print('ERRO: Por favor, digite apenas "S" ou "N"')
        else:
            break

    if escolha in 'Nn':
        print('-'*50)
        break

for p, i in enumerate(pessoas):
    if i['idade'] > mediaidade:
        acimamedia.append(i['nome'])

for i, p in enumerate(pessoas):
    print(f'{i + 1} - {p['nome']} de {p['idade']} anos do sexo: {p['sexo']}')
    print('-'*50)

print(f'lista de mulheres:', end=' ')
for p, m in enumerate(mulheres):
    print(m, end=' ')

print(f'\nA média de idade do grupo é: {mediaidade:.2f} anos')

print(f'Pessoas que estão acima da média:', end=' ')
for p, a in enumerate(acimamedia):
    print(a, end=' ')