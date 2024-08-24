def notas(* nota, sit=False):

    """
    *nota: esse parametro pega todo valor digitado e tranforma meio que em uma lista
    sit: esse parametro se estiver como true mostrará a situação da media da turma se está boa ou ruim
    resp: recebe e organiza todas as respostas para que eu possa retornar na tela do usuario
    """

    global resp
    resp = dict()

    resp['maiornota'] = max(nota)
    resp['menornota'] = min(nota)
    resp['quantnotas'] = len(nota)
    resp['mediaturma'] = sum(nota) / resp['quantnotas']
    
    if sit:
        resp['situação'] = ''
        if resp['mediaturma'] >= 7:
            resp['situação'] = 'Boa'
        
        elif resp['mediaturma'] >= 5 and resp['mediaturma'] < 7:
            resp['situação'] = 'Razoável'
            
        else:
            resp['situação'] = 'Ruim'
    
    return resp


notas(3,2,7,6,7,8, sit=True)
print(resp)