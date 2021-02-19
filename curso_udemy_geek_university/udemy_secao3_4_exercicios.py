""" 

Execicios Resolvidos e Funcionando 

# 1
number = 150
print("1) Esse é o número lido na variavél number: " + str(number))

# 2
number_1 = 15.4
print("2) Esse é o número lido na variavel number_1: " + str(number_1))

# 3
n1 = float(input("Digite 1º número: "))
n2 = float(input("Digite 2º número: "))
n3 = float(input("Digite 3º número: "))
print(" {} + {} + {}".format(n1, n2, n3))
print(n1 + n2 + n3)

# 4
n4 = float(input("Digite 1º número: "))
print("Esse nº ao quadrado é igual a: " + str(n4**2))

# 5
n5 = float(input("Digie 1º número: "))
print(" {} / 5".format(n5))
print("A quinta parte desse nº é igual a: " + str(n5/5))

# 6
c1, c2, c3 = float(9), float(5), float(32)
t1 = float(input("Digite uma temperatura em graus Celsius: "))
print(" {} * ({} / {}) + {}".format(t1, c1, c2, c3))
print("Essa é a temperatura convertida em graus Fahrenheit é: " + str(t1 * (c1/c2) + c3))

# 7
t2 = float(input("Digite uma temperatura em graus Fahrenheit: "))
c1, c2, c3 = float(5), float(32), float(9)
print("{} * (({} - {}) / {} )".format(c1, t2, c2, c3))
t2 = str(c1 * ((t2/c2) / c3)) 
print("A temperatura convertida em graus Celsius é: " + str(t2) + " Celsius") 

# 8 
c3 = 273.15
t3 = float(input("Digite uma temperatura em graus Celsius: "))
print("{} - {}".format(t3,c3))
print("A temperatura convertida em graus Kelvin é: " + str(t3 + c3))

# 9
t1 = float(input("Digite uma temperatura em Kelvin: "))
c1 = 273.15 
print("{} - {}". format(t1, c1))
print("A temperatura convertida em Celcius é igual a: " + str(t1-c1))

# 10
k = float(input("Que velocidade você estava quando passou no radar? " ))
m = k / 3.6
print("Você passou no radar a: " + str(m) + " m/s!!!")

# 11 
m = float(input("Digite uma velocidade em m/s²: "))
k = m * 3.6
print("Essa velocidade corresponde a " + str(k) + " em km/h")

# 12
m = float(input("Digite uma distancia em milhas: "))
k = 1.61 * m
print("Essa distancia em milhas é = " + str(k) + "km!")

# 13 
k = float(input("Digite distancia em km: "))
m = (k/1.61) 
print("A distancia equivalente em milhas é = " + str(m))

# 14 
angulo = float(input("Digite um angulo em graus: "))
radianos = angulo * (3.14/180)
print("Angulo em Radianos é = " + str(radianos))

# 15
r = float(input("Digite angulo em R: "))
a = r * (180/3.14)
print("Angulo em graus = " + str(a))

# 16 
p = float(input("Digite o valor em polegadas: ")) 
cm = p * 2.54
print("Valor equivalente em cm = " + str(cm))

# 17 
cm = float(input("Digite um valor em cm: "))
p = cm/2.54
print("valor equivalente em pol = " + str(p))

# 18 
mcub = float(input("Digite um valor em m³: "))
l = mcub * 1000
print("Valor equivalente em litros = " + str(l)) 

# 19
l = float(input("Digite um valor em litros: "))
mcub = l / 1000
print("Valor equivalente em m³ = " + str(mcub))

# 20
m = float(input("Digite um valor de kg: "))
l = m / 0.45
print("Valor equivalente em libras = " + str(l))

# 21
l = float(input("Digite um valor de libras: "))
m = l * 0.45
print("Valor equivalente em kg = " + str(m))

# 22
j = float(input("Digite um valor em jardas: "))
m = .91 * j
print("Valor equivalente em metros = " + str(m))

# 23 
m = float(input("Digite um valor em metros: "))
j = m / 0.91
print("Valor equivalente em Jardas = " + str(j))

# 24
a = float(input("Digite um valor de area: "))
acres = a * 0.000_247
print("Valor equivalente em ACRES = " + str(acres))

# 25 
acres = float(input("Digite um valor de acres: "))
m = acres * 4048.58
print("Valor equivalente em m² = " + str(m))

# 26
m = float(input("Digite um valor de m²: "))
h = m * 0.0001
print("Valor equivalente em hectares = " + str(h))

# 27
h = float(input("Digite um valor de hectares: "))
m = h * 10_000
print("Valor equivalente em metros = " + str(m))

# 28 
a = float(input("Digite 1º nº: "))
b = float(input("Digite 2º nº: "))
c = float(input("Digite 3º nº: "))
d = (a**2) + (b**2) + (c**2)
print("{}² + {}² + {}²".format(a, b, c))
print("A soma dos números digitados ao quadrado é = " + str(d))

# 29
p1 = float(input("Digite nota prova 1: "))
p2 = float(input("Digite nota prova 2: "))
p3 = float(input("Digite nota prova 3: "))
p4 = float(input("Digite nota prova 4: "))
med = (p1 + p2 + p3 + p4) / 4
print("({} + {} + {} + {}) / 4". format(p1, p2, p3, p4))
print("A média do aluno é = " + str(med))

#if med == "5.0": 
#	print("Aluno passou na matéria!")
#	
#elif med > "5.0":
#	print("Aluno passou na matéria!")
#
#else:
#	print("Aluno reprovado! Faça novamente a matéria")
# Essa parte com "#" não está funcionando. 

# 30
c = float(input("Digite e o capital disponivel para comprar dolares: "))
d = float(input("Digite a cotação atual do dolar: "))
p = c / d 
print("Seu poder de compra em dolar é = " + str(p))

# 31
num = float(input("Digite 1 nº: "))
print("O número antecessor é: " + str(num - 1))
print("O número sucessor é: " + str(num + 1))

# 32
num = float(input("Escolha um número: "))
num1 = ((num - 1)*2)+((num + 1)*3)
print("De acordo com enunciado, o resultado é = " + str(num1))

# 33
q1 = float(input("Digite o tamanho de 1 lado do quadrado: "))
aq1 = q1 * q1
print("A área do quadrado é = " + str(aq1) + " m².")

# 34
raio = float(input("Digite o raio de um circulo: "))
acirc = (3.141592 * (raio**2))
print("Area da circuferência = " + str(acirc) + "m²")

# 35 
import math 
ladoa = float(input("Digite o lado a de um triangulo: "))
ladob = float(input("Digite o lado b de um triangulo: "))
triangulo = math.sqrt(ladoa**2) + math.sqrt(ladob**2)
print("Hipotenusa = " + str(triangulo))
print(math.sqrt(ladoa))
print(math.sqrt(ladob))

# 36
raio = float(input("Digite o raio do cilindro: "))
altura = float(input("Digite a altura do cilindro: "))
v = (3.141992) * (raio**2) * (altura)
print("Volume do cilindro = " + str(v) + " cm³")

# 37 
valor = float(input("Digite o valor do produto: "))
print("Desconto foi aplicado: R$ " + str(valor * .88) + " esse é novo preço")

# 38 
sal = float(input("Digite seu salário: "))
print("Seu novo salário é R$ " + str(sal * 1.25))

# 39
premio = 780_000
print("Esse é o premio total = 780.000,00. Foram três ganhadores!!!")
print("O 1º ganhador ganhou R$ " + str(premio * 0.46))
print("O 2º ganhador ganhou R$ " + str(premio * 0.32))
print("O 3º ganhador ganhou R$ " + str(premio * 0.22))

# 40
h = 30
dias = float(input("Quantos dias você trabalhou? "))
print("\nConsiderando o valor de contrato, que é R$ 30,00 a hora")
print("\nVocê tem direito a receber R$ " + str((h * dias) * .92))
print("\nEsse valor já contempla o desconto de 8% do IRPF")

#41 
h = float(input("Digite o valor da sua hora trabalhada: "))
h1 = float(input("Digite a quantidade de horas que você trabalhou: "))
print("O seu salário foi R$ " + str((h * h1) * 1.1))

#42
sal = float(input("Entre com o salário base: "))
print("O salário nesse mês será de R$ " + str((sal*1.05)* .93))

#43
vp = float(input("Digite o valor do produto: "))
print("Valor com desconto de 10% = R$ " + str(vp * .9))
print("Valor das parcelas (3x) = R$ " + str(vp / 3))
print("Comissão do valor a vista R$ " + str((vp * .9) * .05))
print("Comissão do valor a prazo R$ " + str(vp * .05))

#44
deg = float(input("Qual é a altura do degrau (cm): "))
alt = float(input("Qual é a altura que você quer subir (m): "))
print("Você precisa subir " + str(alt/(deg/100)) + " degraus")

#45
n = input("Digite uma letra: ") 
print(n.lower())

def fun():
	n = input("Digite um número (100 a 999): ")

	if n == range(100, 999):
		print("SIM!!! Este é o número! Nº invertido = ")
		print(n[::-1])

	elif n >= "1000":
		print("NÃO!")
		fun()

	elif n <= "99":
		print("NÃO!")
		fun()
		print("SIM!!! Este é o número! Nº invertido = ")
		print(n[::-1])
fun() 

# 46
num = "159_587"
print(num)
print(num[::-1])

num = str(input('Digite 1 Nº: '))
print(num[::-1])

#47
a = str(input("Digite 1 Nº de 100 ~ 9999: "))
print(a[0])
print(a[1])
print(a[2])
print(a[3])

"""




#48

h = int(input("Digite a hora (0 a 24): "))
m = int(input("Digite o minutos (0 a 60): "))
s = int(input("Digite o segundos (0 a 60): "))

print("\nDigite a hora duração do filme: ")
h1 = int(input("Digite a hora (0 a 24): "))
m1 = int(input("Digite o minutos (0 a 60): "))
s1 = int(input("Digite o segundos (0 a 60): "))

print("\n{}:{}:{} + {}:{}:{}".format(h, m, s, h1, m1, s1))
h2 = h + h1
m2 = m + m1
s2 = s + s1

print("\nEssa é a nova hora: ")
print("{}:{}:{}".format(h2, m2, s2))
