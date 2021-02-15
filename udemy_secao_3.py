""" Aula 03/04/2020

DIR & HELP
Utilitários Python para te auxiliar na programação. 
DIR -> Apresenta todos os atributos/propriedades e funções/métodos disponiveis p/ determinação de dados ou variavel. 
dir(tipo de dado/variavel)
EX -> dir("geek")

HELP -> Apresenta a documentação/como utilizar os atributos/propriedades e funções/métodos disponiveis p/ determinação de dados ou variavel. 
help()

no caso estamos trabalhando com Geany
file:///C:/Program%20Files%20(x86)/Geany/share/doc/geany/html/index.html

"""
# Desse jeito eu consigo visualizar como utilizar essa variavel. 
# print(dir("Geek"))

""" Aula 04/04/2020

Recebendo dados do usuario

""" 
# Exemplo antigo de como colocar variavél em função do print
print("Qual é seu nome?")
name = input()
print("Seja Bem-vindo (a) %s" % name)

print("Quantos anos você tem?") 
anos = input()

print("O (A) %s tem %s anos" % (name, anos))

# Exemplo moderno
print("Seja Bem-vindo (a) {}, ele tem {} de idade!".format(name, anos))

# Exemplo atual
print(f'Seja Bem-vindo (a) {name}, ele tem {anos} de idade!')

print(f'A {name} nasceu em {2020 - int(anos)}')

""" 
input() -> todo dado recebido via input é do tipo String
Em Python, string é tudo que estiver entre: 
Aspas simples -> EX: 'alfredo'
Aspas duplas -> EX: "alfredo"
Aspas simples triplas -> EX: '''alfredo'''
"""
# Aspas duplas triplas -> EX: """alfredo"""




