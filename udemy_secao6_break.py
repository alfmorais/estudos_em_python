""" 
Funciona da mesma forma da linguagem C, Java. 

Utilizamos o break para sair de loops, de maneira forçada. 

Ou de maneira planejada. 

"""

#Exemplo 1: 
for numero in range(11):
	if numero == 6:
		break
	else:
		print(numero)

print("Sai do Loop Infinito")

#Exemplo 2:
while True:
	comando = input("Digite sair p/ sair: ")
	if comando.upper() == 'SAIR':
		break

print("Sai do Loop Infinito")

