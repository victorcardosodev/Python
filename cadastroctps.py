from datetime import date

pessoa = dict()

pessoa['nome'] = str(input('Digite seu nome: '))
pessoa['idade'] = date.today().year - int(input('Digite o ano do seu nascimento: '))
pessoa['CTPS'] = int(input('Digite sua carteira de trabalho ( ou se não tiver digite 0 ): '))

if pessoa['CTPS'] != 0:
    pessoa['anocontratacao'] = int(input('Digite o ano da sua contratação: '))
    pessoa['salario'] = float(input('Qaul o seu salário: '))
    pessoa['anoaposentadoria'] = pessoa['idade'] + (35 - (date.today().year - pessoa['anocontratacao']))
    
    print(f'olá {pessoa["nome"]}, você tem {pessoa["idade"]} anos, o número da sua carteira de trabalho é {pessoa["CTPS"]}, a sua contratação foi em {pessoa["anocontratacao"]} com salário de {pessoa["salario"]} e a idade mínima da sua aposentaria é com {pessoa["anoaposentadoria"]} anos')
else:
    print(f'olá {pessoa["nome"]}, você tem {pessoa["idade"]} anos e não tem carteira de trabalho cadastrada')