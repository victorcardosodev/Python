from utilidadesCeV.moedamod.moeda import *

p = float(input('Digite o preço: R$'))

print(f'A metade de {moedacomval(p, 'U$')} é {moedacomval(metade(p))}')
print(f'O dobro de {moedacomval(p, False)} é {moedacomval(dobro(p))}')
print(f'Aumentando 10%, temos {moedacomval(aumentar(p, 10),formato=False)}')
print(f'Reduzindo 13%, temos {moedacomval(diminuir(p, 13))}')