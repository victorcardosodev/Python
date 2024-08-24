expressao = list(input('Digite uma expressão númerica: '))
abertos = expressao.count('(')
fechados = expressao.count(')')

if abertos == fechados:
    print('Sua expressão está correta!')
else:
    print('Sua expressão está errada!')
    
print(fechados)
print(abertos)
print(expressao)