aluno = str(input('Qual o nome do aluno: '))

nota1 = float(input('Digite a nota do primeiro bimestre do aluno {}: '.format(aluno)))
nota2 = float(input('Agora digite a nota do segundo bimestre: '))

media = (nota1 + nota2) / 2

if media > 10 or media < 0:
    print('A nota {} não é válida, por favor verifique as notas digitadas!'.format(media))
elif media >= 7:
    print('O(A) aluno(a) {} foi aprovado(a) com a nota {:.1f} de média!'.format(aluno, media))
elif media < 7 and media >= 5:
    print('O(A) aluno(a) {} irá precisar de recuperação pois terminou com a nota {} de média!'.format(aluno, media))
else:
    print('O(A) aluno(a) {} foi reprovado(a) com a nota {}'.format(aluno, media))