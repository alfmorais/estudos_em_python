'''
Formatando valores com modificadores

:s - Texto(strings)
:d - Inteiros(int)
:f - Números de ponto flutuante (float)
:.(NÚMERO)f - Quantidade de casas decimais (float)
:(CARACTERE)(> ou < ou ^)(Quantidade)(Tipo - s, d ou f)

> - Esquerda
< - Direita
^ - Centro

'''
num_1 = 10
num_2 = 3
divisao = num_1 / num_2

print('sem formatação = ' + str(divisao))
print('formatação com função format :.2f = {:.2f}'.format(divisao))
print(f'formatação com f e :.2f = {divisao:.2f}')

num = 1
print(f'{num:0>10}')

num_3 = 1150
print(f'{num_3:0^10}')
print(f'{num_3:.2f}')

nome = 'Alfredo de Morais'

print(50 - len(nome)/2)
print(f'{nome:#^50}')

nome_formatado = '{}'.format(nome)
print(nome_formatado)
nome_formatado = '{:@>50}'.format(nome)
print(nome_formatado)
