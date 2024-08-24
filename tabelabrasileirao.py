classificacao = 'Botafogo','Palmeiras', 'Flamengo', 'São Paulo', 'Bahia', 'Cruzeiro', 'Fortaleza', 'Athletico-PR', 'Vasco da Gama', 'Bragantino', 'Atlético-MG', 'Juventude', 'Internacional', 'Criciúma', 'Cuiabá', 'Vitória', 'Corinthians', 'Grêmio', 'Atlético-GO', 'Fluminense'


fiveprimeiros = classificacao[:5]
print(fiveprimeiros)
print('')

ultimos = classificacao[-4:]
print(ultimos)
print('')

classificacaoalfabetica = sorted(classificacao)
print(classificacaoalfabetica)
print('')

corinthians = classificacao.index('Corinthians')
print(f'O corinthians se encontra na posição de memória {corinthians} e no campeonato {corinthians+1}º')