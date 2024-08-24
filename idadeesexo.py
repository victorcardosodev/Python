mais18 = 0
homens = 0
mulheresmenos20 = 0
escolha = ''

while escolha != 'N':
    idade = int(input('Digite a idade da pessoa: '))
    sexo = str(input('SEXO: [F/M]: ')).upper()
    if sexo != 'F' and sexo != 'M':
        print('ERRO! Digite apenas F ou M')
        continue

    if idade >= 18:
        mais18 += 1

    if sexo == 'M':
        homens += 1
    
    if sexo == 'F' and idade < 20:
        mulheresmenos20 += 1
    
    while escolha != 'N' and escolha != 'S':
        escolha = str(input('Deseja continuar [S/N]: ')).upper()
        if escolha == 'N':
            break
        elif escolha != 'S' and escolha != 'N':
            print('ERRO! Digite apenas S ou N')
            

print(f'''
Pessoas com mais de 18 anos: {mais18}
Quantidade de homens cadastrados: {homens}
Mulheres com menos de 20 anos {mulheresmenos20}''')