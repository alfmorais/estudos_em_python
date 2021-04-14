""" 
Funções (def) em Python - return
"""


def funcao(var):
    return(var)


funcao('Valor que eu quero')
variavel = funcao('Valor que eu quero')

if variavel:
    print(variavel)
else:
    print('Nenhum valor.')


def divisao(n1, n2):
    try:
        return n1 / n2
    except ZeroDivisionError:
        print('Insira um denominador válido')


divide = divisao(8, 0)
print(divide)
