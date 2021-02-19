"""
LISTAS

Listas em Python funcional como vetores/matrizes (arrays) em outras linguagens,
como a diferença de serem DINÂMICO e também de podermos colocar QUALQUER tipos,
de dados. 

Linguagem C / JAVA

	- Possuem tamanho e tipo fixo: 
	Ou seja, nesta linguagem se você criar um array do tipo 'int' e com tamanho
	5, este array será SEMPRE do tipo inteiro e poderá ter SEMPRE, no maximo 5 
	valores. 

Já em Python: 

DINÂMICO: Não possuem tamanho fixo; ou seja, podemos criar a lista e simplesmen-
te ir adicionando elementos: 
QUALQUER tipo de dado: Não possuem tipo de dado fixo, ou seja, podemos colocar 
qualquer tipo de dado. 

As listas em Python são representadas por colchetes = []

"""

#print(type([]))

lista1 = [1, 99, 4, 27, 15, 22, 3, 1, 44, 42, 27]
#print(lista1)

lista2 = ['A', 'L', 'F', 'R', 'E', 'D', 'O']
#print(lista2)

lista3 = []
#print(lista3)

lista4 = list(range(11))
#print(lista4)

lista5 = list('ALFREDO')
#print(lista5)

#""" Podemos facilmente checar se determinado valor está contido na lista """
#num = 7
#if num in lista4:
#	print(f'Encotrei o {num}')

#else:
#	print(f'Não encontrei o {num}')

#""" Podemos facilmente order uma lista """
#lista1.sort()
#print(lista1)

#""" Podemos facilmente contar o número de ocorrências de um valor em uma lista """
#print(lista1.count(1))
#print(lista5.count('E'))

# Adicionando elementos numa lista
#""" Para adicionar elementos em listas, usamos a função append """

#print(lista1)
#lista1.append(101)
#print(lista1)

#""" OBS: com append, nós só conseguimos adicionar 1 elemento por vez 

#lista.append(101, 102, 103) = ERRO!!!
#"""

#""" Encontrando uma lista dentro de outra lista """

#lista1.append([8, 3, 1]) # coloca a lista como elemento unico (sublista)
#print(lista1)

#if [8, 3, 1] in lista1:
#	print('Encontrei na lista')
#else:
#	print('Não encontrei na lista')

#""" Adicionando elemento a lista """

#lista1.extend([102, 105, 106]) # coloca como elemento da lista como valor adicional a lista
#print(lista1)

# Podemos inserir um novo elemento na lista informando a  posição do indice. 
# OBS: Isso não substitui o valor inicial o mesmo será deslocado para a direita da lista

#lista1.insert(2, 'Alfredo')
#print(lista1)

# Podemos facilmente somar ou juntar duas listas diferentes de 'n' maneiras: 
# 1º Maneira: 
#lista6 = lista1 + lista2
#print(lista6)

# 2º Maneira:
#lista1 = lista1 + lista2
#print(lista1)

# 3º Maneira:
#lista1.extend(lista2)
#print(lista1)

# Invertendo os valores de uma lista 1º Maneira:
#lista4.reverse()
#lista5.reverse()
#print(lista4)
#print(lista5)

# Invertendo os valores de uma lista 2º Maneira:
#print(lista4[::-1])
#print(lista5[::-1])

"""# Copiando uma lista
print(lista4)
lista6 = lista4.copy()
print(lista6)"""

"""# Tamanho de Lista
print(len(lista4))
# Podemos contar quantos itens tem uma lista
"""

"""
# Podemos facilmente remover o ultimo componente de uma lista
print(lista5)
lista5.pop() # Remove e retorna o ultimo elemento da lista
print(lista5)

# Podemos remover um elemento pelo indice
print(lista1)
lista1.pop(5)
print(lista1)

# Os elementos da direita deste indice foi deslocado para a esquerda. 

OBS: Se não houver elemento no indice informado teremos o erro de indexerror
"""

'''
# Limpando a Lista
print(lista1)
lista1.clear()
print(lista1)
'''
"""
# Podemos repetir elementos de uma lista com a multiplicação

nova = [1, 2, 3]
print(nova)
nova = nova * 3
print(nova)
"""
"""
# Podemos converter uma string para uma lista
# Exemplo 1:
curso = 'Programação em Python Essencial'
print(curso)

curso = curso.split()
print(curso)

# Exemplo 2:
curso = 'Programação,em,Java'
print(curso)

curso = curso.split(',')
print(curso)

curso = 'Programação8em8Python:8Essencial'
print(curso)
curso = curso.split('8')
print(curso)

# Convertendo uma lista de uma string
lista6 = ['Programação', 'em', 'Python:', 'Essencial']
print(lista6)

# Abaixo estamos falando: Pega a lista6, coloca espaço entre cada elemento e transforma em string.
curso = ' '.join(lista6)
print(curso)

# Iterando sobre a lista
soma = 0
for elemento in lista1:
	print(elemento)
	soma = soma + elemento

print(soma)
"""

# Utilizando o While
'''
carrinho = []
produto = ''

while produto != 'sair':
	print("Adicione um produto na lista ou digite 'sair' para sair: ")
	produto = input()
	if produto != 'sair':
		carrinho.append(produto)

for produto in carrinho:
	print(produto)

print("Clique em finalizar a compra")
'''

# Acesso aos elementos de um lista de forma indexada
'''
cores = ['amarelo', 'verde', 'azul', 'branco']
''' 

'''
print(cores[0])
print(cores[1])
print(cores[2])
print(cores[3])
'''
# Acesso aos elementos de uma lista de forma indexada 
'''
print(cores[-1])
print(cores[-2])
print(cores[-3])
print(cores[-4])
'''
'''
for cor in cores:
	print(cor)

indice = 0
while indice < len(cores):
	print(cores[indice])
	indice = indice + 1

print("")
'''
'''
for indice, cor in enumerate(cores):
	print(indice, cor)

print('')
'''

# Outros meios de trabalhar com lista
# Encontrando um indice de um elemento na lista
'''
num = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Em qual indice da lista está o valor 7?
print(num.index(7))
print(num.index(4))

print(num.index(5, 2)) # onde está o número 5 buscando apartir do indice 2?
print(num.index(6, 0, 10)) # busca o número em uma faixa de range
'''

# Invertendo componentes da lista
nomes = ['Alfredo', 'Morais']

nomes[0], nomes[1] = nomes[1], nomes[0]

print(nomes)
