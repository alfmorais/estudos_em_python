'''
Como criar e modificar arquivos:
'w'  -> Usado somente para escrever algo
'a'  -> Usado para acrescentar algo
'r'  -> Usado somente para ler algo
'r+' -> Usado para ler e escrever algo

'''
import os

with open('celulares.txt', 'w') as arquivo:
    arquivo.write('Celular 1')

''' Esse codigo cria um arquivo do zero com o metodo 'a'
de apendice, quer dizer que ele adiciona o codigo em cima 
outro arquivo'''

nomes = ['Alfredo', 'Denise', 'Joaquim', 'Helena', 'Antonela']
with open('nomes.txt', 'a', newline='') as arquivo:
    for nome in nomes:
        arquivo.write(nome + os.linesep)

numeros = list(range(100000))
with open('numeros.txt', 'a', newline='') as arquivo:
    for numero in numeros:
        arquivo.write(str(numero) + os.linesep)

with open('nomes.txt', 'r') as arquivo:
    for linha in arquivo:
        print(linha)

with open('numeros.txt', 'r+') as arquivo:
    for linha in arquivo:
        print(linha)
