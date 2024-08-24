nome = input('Digite seu nome completo: ').strip()

print('Seu nome com todas as letras maiúsculas fica {}'.format(nome.upper()))

print('Seu nome com todas as letras minúsculas fica {}'.format(nome.lower()))

print('Seu nome tem ao todo {} letras'.format((len(nome) - nome.count(' '))))

dividido = nome.split()

print('Seu primeiro nome tem {} letras'.format(len(dividido[0])))