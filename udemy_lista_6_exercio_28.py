""" 

Exercicio abaixo proposto pela GEEK UNIVERSITY tem como objetivo usar o calculo fatorial. 
FONTE: https://matematicabasica.net/fatorial/
FONTE PYTHON: https://www.pythonprogressivo.net/2018/05/Calcular-Fatorial-Python-FOR-WHILE.html

"""

num = int(input("Digite um número: "))
resultado = 1
lista = [1]

for n in range(1, num + 1):
	resultado *= n
	s = 1 / resultado
	lista.append(s)

print(f'A soma fatorial é: {sum(lista)}')
print(f'{lista}')

'''
num = int(input("Digite um número: "))
resultado = 1

for n in range(1, num + 1):
	resultado *= n
print(f'Essa é possibilidades de números da mega sena {resultado}')
'''
