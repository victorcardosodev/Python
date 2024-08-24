def leiaint(n_int):
    while True:
        try:
            print(f'Você acabou de digitar o valor INTEIRO {int(n_int)}')
            break
        
        except (ValueError, TypeError):
            print('numero invalido')
            n_int = input('digite um valor inteiro: ')

        except (KeyboardInterrupt):
            print('operação interrompida')
            return 0


def leiafloat(n_float):
    while True:
        try:
            print(f'Você acabou de digitar o valor REAL {float(n_float):.2f}')
            break
        
        except (ValueError, TypeError):
            print('número invalido')
            n_float = input(f'Digite um valor Real: ')

        except (KeyboardInterrupt):
            print('operação interrompida')
            return 0


numint = input("DIgite um número inteiro: ")
leiaint(numint)

numfloat = input('Digite um número real: ')
leiafloat(numfloat)