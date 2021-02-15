""" 

Em matemática, o número harmônico designado por H(n) define-se como sendo a soma
da série harmônica: 

H(n) = 1 + 1/2 + 1/3 + ... 1/n

Faça um programa que leia um valor n inteiro e positivo e apresente o valor de 
H(n):

"""
num = int(input("Digite um número: "))

if num > 0:
	hnlista = [1]
	for n in range(1, num + 1):
		hn = 1/n
		hnlista.append(hn)

hnlist = sum(hnlista)
print(f'Essa é a soma harmônica: {hnlist}')
print(hnlista)

