alunosenotas = []
alunos = alunosenotas[:]

while True:
    nome = str(input('Digite o nome do aluno: '))
    nota1 = float(input('Digite a primeira nota: '))
    nota2 = float(input('Digite a segunda nota: '))
    alunosenotas.append(nome)
    alunosenotas.append(nota1)
    alunosenotas.append(nota2)
    alunosenotas.append((nota1 + nota2) / 2)

    alunos.append(alunosenotas[:])
    alunosenotas.clear()

    escolha = str(input('Deseja continuar [S/N]: '))
    if escolha in 'Nn':
        break


for p, v in enumerate(alunos):
    print(f'{p:<5} {v[0]:<5} {v[3]:>5.1f}')

#print(alunos)

while True:
    escolha = int(input('Digite o número do aluno que deseja ver as notas ou 999 para sair do programa: '))

    if escolha == 999:
        break

    if escolha < len(alunos):
        print(f'as notas do aluno(a) {alunos[escolha][0]} foram: {alunos[escolha][1]} e {alunos[escolha][2]}')