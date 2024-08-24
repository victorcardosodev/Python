def titulo(msg):
    msg = msg.upper()
    print('-'*50)
    print(msg.center(50))
    print('-'*50)


def funcaoEscolha(n):
    try:
        n = int(n)
        return n
        
    except ValueError:
        return print('ERRO: Digite um número inteiro entre 1 e 3 !')
    
def cadastrarNome():
        try:
            nome = input('Digite o nome de usuário: ')
            return nome
        except (ValueError, TypeError):
            print('Erro ao digitar o nome de usuário.')

def cadastrarIdade():
    while True:
        try:
            idade = input('Digite a idade: ')
            idade = int(idade)
            return idade
        except:
            print('Erro ao digitar a idade')