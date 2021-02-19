qtd = int(input("Quantas vezes você quer repetir?"))
soma = 0
lista = []

for num in range(1, qtd + 1):
	n = int(input(f'Digite {num}/{qtd}:'))
	soma = n + soma
	lista.append(n)	

print(f'Esse é o maior número digitado: {max(lista)}')

#Para a função de contar qde de vezes que número foi utilizado, usamos a função 'count'. 

print(f'Essa foi a quantidade que ele foi digitado: {lista.count(max(lista))}')
