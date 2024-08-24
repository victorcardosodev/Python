def metade(p):
    return p / 2

def dobro(p):
    return p * 2

def aumentar(p, porcentagem):
    return p + ((p / 100) * porcentagem)

def diminuir(p, porcentagem):
    return p - ((p / 100) * porcentagem)

def moeda(p, monetario = 'R$'):
    return f'{monetario} {p:.2f}'.replace('.', ',')

def moedacomval(p, monetario = 'R$', formato=True):
    if formato:
        return f'{monetario} {p:.2f}'.replace('.', ',')
    else:
        return f'{p}'


def resumo(p, aumento, reducao):
    resumoval = dict()
    resumoval['Preço analisado'] = p
    resumoval['Dobro do preço'] = p * 2
    resumoval['Metade do preço'] = p / 2
    resumoval[f'Aumento de {aumento}%'] = p + ((p / 100) * aumento)
    resumoval[f'Redução de {reducao}%'] = p - ((p / 100) * reducao)
    for valor in resumoval:
         print(f'{valor}: R${resumoval[valor]:<5}')
#         res.append(f'{valor}: R${resumoval[valor]:.2f}')

 #   for item in res:
  #      print(f'{item:^5}')