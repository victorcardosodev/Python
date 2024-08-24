cidade = input('Digite o nome da sua cidade: ').strip()
cidade = cidade.split()
print('Verificamos se a sua cidade inicia com o nome "Santo" e a resposta é: {}'.format(cidade[0].lower() == 'santo'))