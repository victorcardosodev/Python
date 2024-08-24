

def leiaint(n):
    try:
        print(f'Você acabou de digitar o valor {int(n)}')
        return n
    
    except ValueError:
        print('numero invalido')

    finally:
        print('Fim do programa')

    #if n.isnumeric():
    #    print(f'Você acabou de digitar o número {n}')
    #else:
    #    while True:
    #        n = input('\033[0;31mVocê precisa digitar um número inteiro. #Por favor, tente novamente: \033[m')
    #        if n.isnumeric():
    #            leiaint(n)
    #            break

num = input('Digite um número inteiro: ')
leiaint(num)