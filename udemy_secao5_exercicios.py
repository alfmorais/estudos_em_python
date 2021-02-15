"""
#1

n1 = float(input("\nDigite 1º nº: "))
n2 = float(input("\nDigite 2º nº: "))

if n1 == n2:
	print("\nn1 = n2")
	print("\nNúmeros Iguais!")

elif n1 > n2:
	print("\nn1 > n2")
	print("\nO número maior é: " + str(n1))

else:
	print("\nn2 > n1")
	print("\nO número maior é: " + str(n2))

print("\nFIM!")

#2
import math
n1 = float(input("\nDigite 1 nº: "))

if n1 < 0:
	print("\nNúmero invalido!")

else:
	r1 = math.sqrt(n1)
	print("\nO nº digitado foi: " + str(n1))
	print("\nRaiz desse nº é: " + str(r1))

print("\nFim!")

#3
n1 = float(input("\nDigite 1 nº: "))

if n1 <0: 
	print("\nO nº é invalido!")

else: 
	n2 = n1 ** 2
	print("\nEsse é o valor do nº escolhido ao quadrado: " + str(n2))

print("\nFim!")

#4
import math
n1 = float(input("Digite 1 nº: "))

if n1 <0: 
	print("\nO nº é invalido!")

else: 
	n2 = n1 ** 2
	n3 = math.sqrt(n1)
	print("O nº digitado ao quadrado: " + str(n2))
	print("O nº digitado com raiz quadrada: " + str(n3))

print("\nFim!")

#5
n1 = int(input("Digite 1 nº: "))
if n1%2 == 0: #Quando usado o % ele usa o resto da divisão. 
	print("\nO número é par!")

else:
	print("\nO número é impar!")

print("\nFim!")

#6
n1 = float(input("Digite 1º nº: "))
n2 = float(input("Digite 2º nº: "))

if n1 > n2: 
	print("O 1º nº digitado é maior!")

elif n2 > n1:
	print("O 2º nº digitado é maior!")

else:
	print("Os nº's são iguais!")

n3 = ((n1) - (n2)) * (-1)
print("A diferença entre eles são " + str(n3) + " unidades!")

#7
n1 = float(input("Digite 1º nº: "))
n2 = float(input("Digite 2º nº: "))

if n1 > n2:
	print("Esse é o número maior: " + str(n1))

elif n2 > n1:
	print("Esse é o número maior: " + str(n2))

else:
	print("Os números são iguais!")

print("\nFim!")

#8
n1 = float(input("Digite nota 1: "))
n2 = float(input("Digite nota 2: "))

if n1 >10: 
	print("Nota invalida")

elif n1 < 0: 
	print("Nota invalida")

elif n2 >10: 
	print("Nota invalida")

elif n2 < 0: 
	print("Nota invalida")

else:
	print("A média do aluno é = " + str((n1+n2)/2))

print("\nFim")

#9
s1 = float(input("Digite seu salário bruto: "))
e1 = float(input("Digite o valor do emprestimo: ")) 

s2 = ((s1 / 10 ) *2)
if e1 > s2:
	print("Emprestimo não disponivél!") 

else: 
	print("Emprestimo disponivél!")

print("\nFim!")

#10 
sexo = input("Aspas tripla"
Digite o seu sexo: 
M = Masculino
F = Feminino 
"Aspas tripla")

if sexo.upper() == "M": 
	h = float(input("Digite sua altura: "))
	peso = ((72.7 * h) - 58.0)
	print("Seu peso ideal é: %.2f" %(peso))

else: 
	h = float(input("Digite sua altura: "))
	peso = ((62.1 * h) - 44.7)
	print("Seu peso ideal é: %.2f" %(peso))

print("\nFim!")

"""
"""
#11 (não conseguir fazer o número 11)
n = input('Digite um numero inteiro: ')
i = 0
s = 0
while i < len(n):
 s = s + int(n[i])
 i+=1
print(s)

#12
import math
n = int(input("Digite um número: "))
if n < 0:
	print("Número Invalido!")

else:
	print("Esse é o logaritmo do número digitado:")
	print(math.log10(n))

print("Fim!")

#13
print("\nVamos calcular a média ponderada do aluno!")
n1 = float(input("\nDigite N1: "))
n2 = float(input("\nDigite N2: "))
n3 = float(input("\nDigite N3: "))
p1, p2, p3 = 1, 1, 2
mp = ((n1 * p1)+(n2 * p2)+(n3 * p3))/4
print("\nMédia Ponderada = " + str(mp))
if mp >= 6.0:
	print("Aluno aprovado")
	print("Não fez mais que sua obrigação!")

else:
	print("Aluno reprovado")
	print("Se fudeu!")

print("\nFim!")

#14 (Não Consegui Funcionar) 

n1 = float(input("Digite a nota do trabalho de laboratório: "))
n2 = float(input("Digite a nota da avaliação semestral: "))
n3 = float(input("Digite a nota do exame final: "))
p1, p2, p3 = 2, 3, 5

mp = ((n1 * p1) + (n2 * p2) + (n3 * p3))/ (p1 + p2 + p3)

if n1 > 10:
	print("Valor invalido!")

elif n1 < 0: 
	print("Valor invalido!")

elif n2 > 10:
	print("Valor invalido!")

elif n2 < 0: 
	print("Valor invalido!")

elif n3 > 10:
	print("Valor invalido!")

elif n3 < 0: 
	print("Valor invalido!")

else: 
	print("Sua média é: " + str(mp))
	if mp in range(0, 2.9):
		print("Aluno Reprovado")
	
	elif mp in range(3, 4.9):
		print("Aluno em Recuperação")
	
	else:
		print("Aluno Aprovado")

print("\nFim!")

#15 
n = int(input("Digite 1 nº de 1 a 7: "))
if n == 1: 
	print("Hoje é Domingo!")
elif n == 2:
	print("Hoje é Segunda!")
elif n == 3:
	print("Hoje é Terça!")
elif n == 4: 
	print("Hoje é Quarta!")
elif n == 5:
	print("Hoje é Quinta!")
elif n == 6: 
	print("Hoje é Sexta!")
elif n == 7: 
	print("Hoje é Sabádo!")
elif n > 7: 
	print("Número Invalido!")
else: 
	print("Número Invalido!")

print("\nFIM!")

# 16
mes = int(input("Digite 1 nº de 1 a 12: "))

if mes == 1: 
	print("Janeiro")
elif mes == 2:
	print("Fevereiro")
elif mes == 3:
	print("Março")
elif mes == 4:
	print("Abril")
elif mes == 5:
	print("Maio")
elif mes == 6:
	print("Junho")
elif mes == 7:
	print("Julho")
elif mes == 8:
	print("Agosto")
elif mes == 9:
	print("Setembro")
elif mes == 10:
	print("Outubro")
elif mes == 11:
	print("Novembro")
elif mes == 12:
	print("Dezembro")
elif mes > 12:
	print("Número Invalido!")
else:
	print("Número Invalido!")

print("\nFim!")

#17
bmenor = float(input("Digite a medida da base menor: "))
bmaior = float(input("Digite a medida da base maior: "))
altura = float(input("Digite a medida da altura: "))

if bmenor < 0: 
	print("Base Menor = Valor Invalído!")
	print("Executar o programa novamente")
elif bmaior < 0:
	print("Base Maior = Valor Invalído!")
	print("Executar o programa novamente")
elif altura < 0: 
	print("Altura = Valor Invalída!")
	print("Executar o programa novamente")
else:
	print("\nVamos calcular a área de um trapézio!")
	area = (((bmaior + bmenor) * altura) / 2)
	print("\nArea do Trapézio = " + str(area))

print("\nFim")

#18
#Definindo o código como uma função ou bloco
def calculadora():
#	operation = input
Por favor digite a operação que deseja realizar: 
+ para adição
- para subtração
* para multiplicação
/ para divisão


	number_1 = float(input("Entre seu primeiro número: "))
	number_2 = float(input("Entre seu segundo número: "))

#Adição
	if operation == "+":
		print("{} + {} = ".format(number_1, number_2))
		print(number_1 + number_2)

#Subtração
	elif operation == "-":
		print("{} - {} = ".format(number_1, number_2))
		print(number_1 - number_2)

#Multiplicação
	elif operation == "*":
		print("{} * {} = ".format(number_1, number_2))
		print(number_1 * number_2)

#Divisão
	elif operation == "/":
		print("{} / {} = ".format(number_1, number_2))
		print(number_1 / number_2)

#Mostra a mensagem de simbolo invalido
	else:
		print("Você escolheu uma operação invalida")

	again()
#Define a função again() que repete o bloco calculadora
def again():

	calculadora_novamente = input (
Você gostaria de usar a calculadora novamente? 
Digite "S" para -> SIM
Digite "N" para -> NÃO
)
	if calculadora_novamente.upper() == "S":
		calculadora()
		
	elif calculadora_novamente.upper() == "N": 
		print("Ok. Muito Obrigado por utilizar a calculadora")
		
	else:
		again()

calculadora()

#19 
n = float(input("Digite 1 nº: "))
n1 = n % 3
n2 = n % 5
n3 = n1 + n2

if n3 == 0:
	print("O número digitado é dividido por '3' & '5'.")
elif n2 == 0:
	print("O número digitado é dividido por '5', mas não por '3'.")
elif n1 == 0:
	print("O número digitado é dividido por '3', mas não por '5'.")
else: 
	print("Os números são tem divisão exata pelos números '3' & '5'.")

print("\nFim!")

#20

a = float(input("Digite o valor de A: "))
b = float(input("Digite o valor de B: "))
c = float(input("Digite o valor de C: "))

d = a * b * c

if d <= 0: 
	print("Informação Invalida!")

elif a == b == c: 
	print("Triangulo Equilátero!")
	print("Isto é: possui três lados iguais.")

elif a != b != c: 
	print("Triangulo Escaleno!")
	print("Isto é: não possui lados iguais.")

else: 
	print("Triangulo Isósceles!")
	print("Isto é: possui dois lados iguais.")

print("\nFim!")

#21
def calculadora():
	problema = input(
Escolha a opção: 
1 = Soma 2 números; 
2 = Diferença entre 2 números (maior pelo menor);
3 = Produto entre os números; 
4 = Divisão entre os números (o denominador não pode ser zero).

)

	if problema == "1": 
		n1 = float(input("Digite o Nº1: "))
		n2 = float(input("Digite o Nº2: "))
		print("{} + {} ".format(n1, n2))
		print(n1 + n2)

	elif problema == "2":
		n1 = float(input("Digite o Nº1: "))
		n2 = float(input("Digite o Nº2: "))
		if n1 > n2: 
			print("{} - {} ".format(n1, n2))
			print(n1 - n2)
		else: 
			print("{} - {} ".format(n2, n1))
			print(n2 - n1)

	elif problema == "3": 
		n1 = float(input("Digite o Nº1: "))
		n2 = float(input("Digite o Nº2: "))
		print("{} * {} ".format(n1, n2))
		print(n1 * n2)

	elif problema == "4": 
		n1 = float(input("Digite o Nº1: "))
		n2 = float(input("Digite o Nº2: "))
		print("{} / {} ".format(n1, n2))
		print(n1 / n2)

	else:
		print("Valor digitado não corresponde a nenhuma ação")
		calculadora()
	again()
def again(): 
	a = input(
Gostaria de usar a calculadora novamente: 
S = Sim 
N = Não 
)
	if a.upper() == "S": 
		calculadora()
	elif a.upper() == "N": 
		print("Obrigado por utilizar a nossa calculadora!")
	else: 
		print("Digito invalido")
		again()

calculadora()

# 22
print("\nVamos descobrir se é possivel você se aponsentar: ")
idade = int(input("\nQual é sua idade? "))
anost = int(input("\nQuantos anos você trabalhou? "))

if idade == 65:
	print("Você pode se aposentar!")
elif anost == 30: 
	print("Você pode se aponsentar!")
elif idade == 60: 
	if anost == 25:
		print("Você pode se aposentar!") 
	else: 
		print("Não pode se aposentar!")
else: 
	print("Não pode se aposentar!")

print("\nFim!")

#23
ano = int(input("Digite o ano: "))
bi = ano % 4

if bi == 0: 
	print("Esse é um ano Bissexto!")
else: 
	print("Esse não é um ano Bissexto!")

print("\nFim!")

#24 
valor = float(input("Digite o valor do produto sem imposto: "))
estado = input(
Digite qual é o estado que vocês está querendo vender? 
MG = Minas Gerais 
SP = São Paulo
RJ = Rio de Janeiro
MS = Mato Grosso do Sul
) 

if estado.upper() == "MG":
	print("Valor do Produto com imposto para MG = " + str(valor * 1.07))
elif estado.upper() == "SP": 
	print("Valor do Produto com imposto para SP = " + str(valor * 1.12))
elif estado.upper() == "RJ":
	print("Valor do Produto com imposto para RJ = " + str(valor * 1.15))
elif estado.upper() == "MS":
	print("Valor do Produto com imposto para MS = " + str(valor * 1.08))
else: 
	print("Valor digitado não corresponde a nenhum estado programado!")
print("\nFim")

# 25
a = float(input("Digite o valor de A: "))
b = float(input("Digite o valor de B: "))
c = float(input("Digite o valor de C: "))

delta = int((b ** 2) - (4 * a * c))
raizd = delta ** (1/2)
raiz1 = (- b + raizd) / (2 * a)
raiz2 = (- b - raizd) / (2 * a)

if delta < 0: 
	print("Não existe raiz")

elif delta == 0: 
	print("Raiz única")

else:
	print("Esta é raiz x1 = " + str(raiz1))
	print("Esta é raiz x2 = " + str(raiz2))

print("\nFIM!")

#26 
km = float(input("Digite a distancia em 'km': "))
gs = float(input("Digite a QTY de gasolina no tanque: "))
 
consumo = km / gs
if consumo <= 8: 
	print("Venda seu carro!")
	print(consumo)

elif 8 < consumo == 14: 
	print("Seu carro é economico!") 
	print(consumo)

elif consumo > 14: 
	print("Seu carro é super economico!")
	print(consumo)

print("\nFim!")

# 27
age = int(input("Digite sua idade: "))

if age in range(5, 8): 
	print("Infantil A")
elif age in range(8, 11): 
	print("Infantil B")
elif age in range(11, 14):
	print("Juvenil A")
elif age in range(14, 18): 
	print("Juvenil B")
elif age >= 18:
	print("Sêniors")
else: 
	print("Sem classificação")
print("\nFim!")

# 28
x = float(input("Digite o valor de X: "))
y = float(input("Digite o valor de Y: "))
z = float(input("Digite o valor de Z: "))

g = (( x * y * z )** (1/3))
p = ((x) + (2 * y) + (3 * z)) / 6
h = (( 1 ) / (1 / x) + (1 / y) + (1 / z))
a = (x + y + z) / (3)

print("Cálculo de Média Geométrica = " + str(g))
print("Cálculo de Média Ponderada = " + str(p))
print("Cálculo de Média Harmônica = " + str(h))
print("Cálculo de Média Aritmética = " + str(a)) 


#Prova de Matematica
print("\nOlá Alunos, iremos realizar uma prova de Matematica!") 
print(

Questão 1) Resolva as equações de soma abaixo: 

a) 54 + 68 = 
b) 25 + 36 = 
c) 45 + 67 = 
d) 38 + 43 = 
e) 11 + 98 = 

) 

a = int(input("Qual é a resposta correta da Questão 1a): "))
b = int(input("Qual é a resposta correta da Questão 1b): "))
c = int(input("Qual é a resposta correta da Questão 1c): "))
d = int(input("Qual é a resposta correta da Questão 1d): "))
e = int(input("Qual é a resposta correta da Questão 1e): "))

nota = []
print("\nCorreção da Prova: ")
if a == 122:
	nota.append(1)
	print("1a = Certo")
else:
	print("1a = Errado")
if b == 61:
	nota.append(1)
	print("1b = Certo")
else:
	print("1b = Errado")
if c == 112:
	nota.append(1)
	print("1c = Certo")
else:
	print("1c = Errado")
if d == 81:
	nota.append(1)
	print("1d = Certo")
else:
	print("1d = Errado")
if e == 109:
	nota.append(1)
	print("1e = Certo")
else:
	print("1e = Errado")

if len(nota) == 5:
	print("\nVocê tirou 10")
elif len(nota) == 4:
	print("\nVocê tirou 8")
elif len(nota) == 3:
	print("\nVocê tirou 6")
elif len(nota) == 2:
	print("\nVocê tirou 4")
elif len(nota) == 1:
	print("\nVocê tirou 2")
elif len(nota) == 0: 
	print("\nVocê não acertou nenhuma questão!")
print("\nFim")

#30
n1 = int(input("Digite qualquer número: "))
n2 = int(input("Digite qualquer número: "))
n3 = int(input("Digite qualquer número: "))

lista1 = [n1, n2, n3]
lista2 = sorted(lista1)
print("\nOs números em ordem crescente são: ")
print(lista2)

#31 Não Consegui
peso = float(input("Digite seu peso: "))
halt = float(input("Digite sua altura: ")) 
str(peso)
str(halt)
if peso <= 60: 
	if halt < 1.20: 
		print("Classificação A")
	elif halt in range(1.20, 1.80):
		print("Classificação B")
	else:
		print("Classificação C")

elif peso in range(60, 100):
	if halt < 1.20: 
		print("Classificação D")
	elif halt in range(1.20, 1.80):
		print("Classificação E")
	else:
		print("Classificação F")

else: 
	if halt < 1.20: 
		print("Classificação G")
	elif halt in range(1.20, 1.80):
		print("Classificação H")
	else:
		print("Classificação I")

print("\nFim!")

lanches = int(input("Qual foi o codigo do lanche? "))
quantd1 = int(input("Qual foi a quantidade pedida? "))
bebidas = int(input("Qual foi o codigo da bebida? "))
quantd2 = int(input("Qual foi a quantidade pedida? "))

if lanches == 100:
	print("Você pediu o cachorro quente, custa 1.20.")
	print("{} * {}".format(1.20, quantd1))
	totala = (1.20 * quantd1)
	print(totala)

elif lanches == 101:
	print("Você pediu o Bauru Simples, custa 1.30.")
	print("{} * {}".format(1.30, quantd1))
	totala = (1.30 * quantd1)
	print(totala)

elif lanches == 102:
	print("Você pediu o Bauru com Ovo, custa 1.50.")
	print("{} * {}".format(1.50, quantd1))
	totala = (1.50 * quantd1)
	print(totala)

elif lanches == 103:
	print("Você pediu o Hamburguer, custa 1.20.")
	print("{} * {}".format(1.20, quantd1))
	totala = (1.20 * quantd1)
	print(totala)

elif lanches == 104:
	print("Você pediu o Cheeseburguer, custa 1.70.")
	print("{} * {}".format(1.70, quantd1))
	totala = (1.70 * quantd1)
	print(totala)

else:
	print("Você digitou o código errado")

if bebidas == 105:
	print("Você pediu o Suco, custa 2.20.")
	print("{} * {}".format(2.20, quantd2))
	totalb = (2.20 * quantd2)
	print(totalb)

elif bebidas == 106:
	print("Você pediu o Refrigerante, custa 1.00.")
	print("{} * {}".format(1.00, quantd2))
	totalb = (1.00 * quantd2)
	print(totalb)

else:
	print("Você digitou o código errado")

print("Total da sua conta foi: ")
print(totala + totalb)

produto = int(input("Digite o preço do produto: "))

if produto < 50:
	produto2 = produto * 1.05
	print("\nAumento de 5%: " + str(produto2))

elif produto in range(50, 101):
	produto2 = produto * 1.10
	print("\nAumento de 10%: " + str(produto2))

else:
	produto2 = produto * 1.15
	print("\nAumento de 15%: " + str(produto2))

if produto2 < 80:
	print("\nProduto Barato")

elif produto2 in range(80, 121):
	print("\nProduto Normal")

elif produto2 in range(120, 201):
	print("\nProduto Caro")

else: 
	print("\nProduto Super Caro")

print("Bem-Vindo a Crise do COVID-19")

#34 (NÃO CONSIGUI FAZER)

nota = int(input("Qual é a nota do aluno? "))
falt = int(input("Quantas faltas o aluno possui? "))

if falt <= 20:
	if nota in range(0, 4):
		print("Conceito E")
	elif nota in range(4, 5):
		print("Conceito D")
	elif nota in range(5, 7.6):
		print("Conceito C")
	elif nota in range(7.5, 9):
		print("Conceito B")
	else:
		print("Conceito A")

else:
	if nota in range(0, 4):
		print("Conceito E")
	elif nota in range(4, 5):
		print("Conceito E")
	elif nota in range(5, 7.6):
		print("Conceito D")
	elif nota in range(7.5, 9):
		print("Conceito C")
	else:
		print("Conceito B")

print("\nFIM")

#36

vendas = int(input("Digite o valor das vendas mensais: "))

print("\nO valor da sua comissão é: ")
if vendas >= 100_000:
	com = 700 + (vendas * 0.16)
	print(com)
elif vendas in range(80_000, 100_001):
	com = 650 + (vendas * 0.14)
	print(com)
elif vendas in range(60_000, 80_001): 
	com = 600 + (vendas * 0.14)
	print(com)
elif vendas in range(40_000, 60_001):
	com = 550 + (vendas * 0.14)
	print(com)
elif vendas in range(20_000, 40_001):
	com = 500 + (vendas * 0.14)
	print(com)
else:
	com = 400 + (vendas * 0.14)
	print(com)

print("\nFIM")
"""

salf = int(input("Digite o salário do funcionário: "))
anos = int(input("Digite o tempo de serviço desse funcionário: "))

print("Seu novo salário: ")

if salf <= 500:
	salatual = (salf * 1.25)
	print(salatual)

elif salf in range(500, 1001):
	salatual = (salf * 1.20)
	print(salatual)

elif salf in range(1001, 1501):
	salatual = (salf * 1.15)
	print(salatual)

elif salf in range(1501, 2001):
	salatual = (salf * 1.10)
	print(salatual)

else: 
	salatual = salf
	print(salatual)

print("Seu Bônus será: ")

if anos <= 1:
	print("Não tem bônus disponivel")

elif anos in range(1, 4):
	bonus = 100
	print("{} + {} ".format(bonus, salatual))
	print(bonus + salatual)

elif anos in range(4, 7):
	bonus = 200
	print("{} + {} ".format(bonus, salatual))
	print(bonus + salatual)

elif anos in range(7, 11): 
	bonus = 300
	print("{} + {} ".format(bonus, salatual))
	print(bonus + salatual)

else: 
	bonus = 500
	print("{} + {} ".format(bonus, salatual))
	print(bonus + salatual)

print("\nFIM")













