from time import sleep

def linhas(mensagem):
    tam = len(mensagem) + 4
    print('~' * tam)
    print(f'  {mensagem}')
    print('~' * tam)

while True:

    linhas('SISTEMA DE AJUDA PyHELP')
    
    sleep(0.5)

    comando = str(input('Função ou biblioteca > '))
    if comando.lower() == 'fim':
        break

    linhas(f"Acessando o manual do comando '{comando}'")

    sleep(1.5)

    help(comando)
    sleep(1.5)
    
linhas('Até logo')