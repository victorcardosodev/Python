def leiaDinheiro(p):
    valido = False
    while not valido:
        entrada = str(input(p))
        if entrada.isalpha():
            print(f'ERRO: "{entrada}" não é um número')
        else:
            valido = True
            return float(entrada)