palavras = 'aprender', 'programar', 'linguagem', 'python', 'curso', 'gratis', 'estudar', 'praticar', 'trabalhar', 'mercado', 'programador', 'futuro'

for p in palavras:
    print(f'\nNa palavra {p.upper()} temos as seguintes vogais: ', end=' ')
    for vogais in p:
        if vogais.lower() in 'aeiou':
            print(f'{vogais}', end=' ')