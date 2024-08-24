def fatorial(f=1, show=False):

    """
    Calculo de fatorial
    resultado: a variável 'resultado' armazena o resultado
    valor: a variável 'valor' armazena o valor da contagem do for que se inicia no 'f'
    f: o parametro 'f' recebe o número escolhido pelo usuário para ter o fatorial calculado
    show: o parametro 'show' é uma flag para mostrar ou não o processo de calculo
    """

    global resultado
    resultado = 1
    
    for valor in range(f, 0, -1):
        if show == True:
            if valor > 1:
                print(f'{valor} x', end=' ')

            else:
                print(valor, end=' = ')
            
        resultado *= valor
    return resultado

num = int(input('Digite um número para ser calculado o fatorial: '))
if num < 0:
    print('Não existe fatorial de número negativo, então por padrão, o valor será 1')
    num = 1

show = int(input('Gostaria que o calculo fosse mostrado [1 = Sim / 0 = Não]: '))

if show == 1:
    show = True

else: 
    show = False

fatorial(num, show)
print(resultado)
