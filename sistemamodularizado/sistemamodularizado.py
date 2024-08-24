from time import sleep
from funcoes import *


cadastro = dict()
pessoas = [
    {'nome': 'fernando', 'idade': 26},
    {'nome': 'Pereira', 'idade': 23},
    {'nome': 'Sergio', 'idade': 53},
    {'nome': 'Rodinei', 'idade': 78},
    {'nome': 'Magrão', 'idade': 18},
    {'nome': 'Gabriela', 'idade': 33}
]


#Menu Principal
while True:
    titulo('Menu principal')
    print('''1 - Ver pessoas cadastradas
2 - Cadastrar nova pessoa
3 - Sair do sistema
    ''')
    escolha = funcaoEscolha(input('Sua opção: '))
    

    if escolha == 1:
        if len(pessoas) == 0:
            print('Ainda não há pessoas cadastradas')
        
        else:
            titulo('Pessoas cadastradas')

            for _, p in enumerate(pessoas):
                print(f'nome: {p['nome']:28} {p['idade']:>10} anos')

            sleep(2)

    elif escolha == 2:
        titulo('Novo cadastro')
        cadastro['nome'] = cadastrarNome()
        cadastro['idade'] = cadastrarIdade()
        pessoas.append(cadastro.copy())
        cadastro.clear()

    elif escolha == 3:
        titulo('Saindo do sistema... Até logo!')
        sleep(1)
        break