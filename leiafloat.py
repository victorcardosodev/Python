def leiafloat(n):
    try:
        print(f'Você acabou de digitar o valor {float(n):.2f}')
    
    except Exception as erro:
        print(f'ERRO: {erro}')


num = input("DIgite um número: ")
leiafloat(num)