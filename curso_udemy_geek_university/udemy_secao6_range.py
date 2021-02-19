""" Entendendo e Explorando os Ranges:

	- Precisamos conhecer o loop for para usar os ranges. 
	- Precisamos conhecer o range para trabalhar com loops for. 

Os ranges são utilizados para gerar sequências númericas, não de forma aleatória
mais sim de maneira especificada.

#Forma 1
range(valor_de_parada)

OBS: valor_de_parada não inclusive o ultimo número. 

#Forma 2
range(valor_de_inicio, valor_de_parada)

OBS: valor_de_parada não inclusive o ultimo número. 

#Forma 3
range(valor_de_inicio, valor_de_parada, passo)

OBS: valor_de_parada não inclusive o ultimo número. 

#Forma 4 = Forma 3 (Inversa)
range(valor_de_inicio, valor_de_parada, passo)

OBS: valor_de_parada não inclusive (inicio especificado pelo usuário, e passo especificado pelo usuario.

"""

for num in range(1000, -5, -5):
	print(num)
