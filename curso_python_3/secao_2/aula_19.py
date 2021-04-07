"""
Formatação de Strings
"""
nome = 'Alfredo'
idade = 28
altura = 1.58
peso = 85
imc = peso / altura ** 2

print(f'{nome}, tem {idade} anos e seu IMC é: {imc:.2f}')
print('{0} tem {1} anos de idade e seu IMC é: {:.2f}'.format(nome, idade, imc))

# Nomear os conchetes para identificar as variaveis.
