def voto(ano):
    from datetime import date
    
    idade = date.today().year - ano
    if idade < 16:
        return 'Direito de voto negado'
    
    elif idade >= 16 and idade < 18:
        return 'Seu voto é opcional !!'
    
    elif idade >= 18 and idade < 65:
        return 'Seu voto é obrigatório !!'
    
    elif idade >= 65:
        return 'Seu voto é opcional !!'

anonas = int(input('Digite o ano do seu nascimento: '))

print(voto(anonas))