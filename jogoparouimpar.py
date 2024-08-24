from random import randint
escolha = ''
vitorias = 0

escolha = str(input('Escolha entre impar [I] ou par [P]: ')).upper()
if escolha != 'P' and escolha != 'I':
    while escolha != 'P' and escolha != 'I':
        print('Escolha inválida! Tente novamente.')
        escolha = str(input('Escolha entre impar [I] ou par [P]: ')).upper()


escolhanumero = int(input('Agora escolha um número inteiro: '))
while escolha == 'P' or escolha == 'I':

    escolhacomp = randint(0, 10)

    soma = escolhanumero + escolhacomp
    resto = soma % 2
    
    if resto == 0:
        resultado = 'P'
        print(f'Você jogou {escolhanumero} e o computador jogou {escolhacomp}, a soma deu {soma} e esse valor é par')
    
    else:
        resultado = 'I'
        print(f'Você jogou {escolhanumero} e o computador jogou {escolhacomp}, a soma deu {soma} e esse valor é impar')
    
    if escolha == resultado:
        print('Parabéns, você ganhou esta rodada!')
        vitorias += 1
    
    else:
        print(f'Que pena, você perdeu. A quantidade de rodadas vencidas foi: {vitorias}')
        break
    
    escolha = ''
    
    while escolha == '':
        escolha = str(input('Escolha entre impar [I] ou par [P]: ')).upper()
        
        if escolha != 'I' and escolha != 'P':
            while escolha != 'P' and escolha != 'I':
                print('Escolha inválida! Tente novamente.')
                escolha = str(input('Escolha entre impar [I] ou par [P]: ')).upper()
        escolhanumero = int(input('Agora escolha um número inteiro: '))