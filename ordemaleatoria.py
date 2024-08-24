from random import shuffle

print('Digite o nome dos alunos que irão ser sorteados para apresentação do trabalho!')

aluno1 = input(('Aluno 1: '))
aluno2 = input(('Aluno 2: '))
aluno3 = input(('Aluno 3: '))
aluno4 = input(('Aluno 4: '))

lista = [aluno1, aluno2, aluno3, aluno4]
shuffle(lista)

print('A ordem de apresentação é \n{}'.format(lista))