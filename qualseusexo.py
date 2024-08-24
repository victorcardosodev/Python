sexo = str(input('Qual seu sexo?[F/M]: ')).upper()


while sexo != 'M' and sexo != 'F':
    sexo = str(input('Por favor, digite um valor válido correspondente ao seu sexo [F/M]: ')).upper()
if sexo == 'M':
    print('Você é do sexo masculino')
else:
    print('Você é do sexo feminino')