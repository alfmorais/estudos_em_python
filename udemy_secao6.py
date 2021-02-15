""" Seção 6: Estruturas de Repetição em Python """
"""
loop for
loop = Estrutura de repetição. 
for = uma dessas estruturas

C ou Java

for(int i = 0; i < 10; i++){
	//execução do loop
}

Python

foi item in iteravel: 
	//execução do loop
Utilizamos loops para iterar sobre sequências ou sobre valores iteráveis

exemplos de iteráveis:
	String
	nome = 'Geek University'
	Lista
	lista [1, 2, 3, 4]
	Range
	numeros = range(1, 10)


nome = 'Alfredo de Morais Neto'
lista = [1, 3, 5, 7, 9]
numeros = range(1, 10) #Temos que transformar em uma lista

Exemplos de for 1 (Iterando em uma String)
for letra in nome:
	print(letra)

Exemplos de for 2 (Iterando sobre uma lista)
for numero in lista:
	print(numero)

Exemplos de for 3 (Iterando sobre uma range)
for numero in range(1, 10):
	print(numero)


range(valor_inicial, valor_final)

OBS: último número não é incluido na range. 

range(1, 10) 
range vai até o valor 9. 

nome2 = 'Denise Morais'
for i, v in enumerate(nome2):
	print(nome2[i])

OBS: Quando não precisamos de um valor, pode-se descartar usando o "_". 

nome2 = 'Denise Morais'
for _, v in enumerate(nome2):
	print(nome2)

contador: 
qtd = int(input("Digite um valor de loop: "))
for n in range(1, qtd + 1):
	print(f'Imprimindo {n}')

Outro programa que soma os números: 
qtd = int(input("Digite um valor de loop: "))
soma = 0

for n in range(1, qtd + 1):
	num = int(input(f'Informe o {n}/{qtd} valor: '))
	soma = soma + num

print(f'A soma é {soma}')

# multiplar string
nome2 = nome * 300
print(nome2)

nome = 'Alfredo de Morais'
for letra in nome: 
	print(letra, end='') #Não pula uma linha no final do print

print("")

nome = 'Alfredo '
for num in range(1, 11):
	print(nome * num)

emoji = 'U0001F60D'

for num in range(1, 11):
	print(f'{emoji} * {num}')
print("")
"""
for _ in range(3):
	for num in range(1, 11):
		print("\U0001F60D" * num)

