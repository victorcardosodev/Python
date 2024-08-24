def tamanho(msg):
    tam = len(msg) + 4
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)


lista = list()

for i in range(0, 3):
    lista.append(str(input('Digite uma mensagem: ')))

for mensagem in lista:
    tamanho(mensagem)