boletimgeral = list()
informacoesaluno = dict()

print('Cadastro de aluno e notas')

while True:
    informacoesaluno['nome'] = str(input('Digite o nome do aluno: '))
    informacoesaluno['media'] = float(input('Digite a média do aluno: '))
    if informacoesaluno['media'] > 5:
        informacoesaluno['resultado'] = 'Aprovado(a)'
    else:
        informacoesaluno['resultado'] = 'Reprovado(a)'

    boletimgeral.append(informacoesaluno.copy())

    escolha = str(input('Deseja cadastrar mais alunos [S/N]: '))
    if escolha in 'Nn':
        break

for aluno in range(len(boletimgeral)):
    print(f'O aluno(a) {boletimgeral[aluno]["nome"]} teve uma média de {boletimgeral[aluno]["media"]} e o resultado foi: {boletimgeral[aluno]["resultado"]}')