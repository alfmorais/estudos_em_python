""" LOOP WHILE

Forma geral:

while expressão booleana:
	//execução de loop

o bloco do while será repetido enquanto a expressão booleana for verdadeira. 

Expressão booleana é toda expressão onde o resultado é verdadeiro ou falso. 

Exemplos: 

num = 5 

num < 5

Em um loop while é importante que cuidamos do número de parada. 

"""

num = 1

while num < 11: 
	print(num)
	num = num + 1

resposta = ''

while resposta != 'sim':
	resposta = input("Já acabou Jéssica?")

print("")
