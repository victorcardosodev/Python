numero = int(input('Digite um número inteiro de 0 a 9999: '))

numero = str(numero)

if len(numero) == 4:
    unidade = numero[3]
    dezena = numero[2]
    centena = numero[1]
    milhar = numero[0]
    print('numero {}: \nunidade: {} \ndezena: {} \ncentena: {} \nmilhar: {}'.format(numero, unidade, dezena, centena, milhar))
    
elif len(numero) == 3:
    unidade = numero[2]
    dezena = numero[1]
    centena = numero[0]
    print('numero {}: \nunidade: {} \ndezena: {} \ncentena: {}'.format(numero, unidade, dezena, centena))

elif len(numero) == 2:
    unidade = numero[1]
    dezena = numero[0]
    print('numero {}: \nunidade: {} \ndezena: {}'.format(numero, unidade, dezena))

elif len(numero) == 1 :
    unidade = numero[0]
    print('numero {}: \nunidade: {}'.format(numero, unidade))

else:
    print('Número inválido!')