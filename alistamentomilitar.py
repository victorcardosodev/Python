from datetime import date

anonasc = int(input('Digite o seu ano de nascimento: '))

idade = date.today().year - anonasc

if idade == 18:
    print('Você precisa se alistar!')
elif idade < 18:
    print('Ainda não é possivel se alistar!')
else:
    print('A idade obrigatoria de alistamento foi ultrapassada, entre em contato com o exercito brasileiro urgente!')