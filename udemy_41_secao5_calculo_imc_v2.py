altura = float(input("Digite sua altura: "))
pesokg = float(input("Digite seu peso: "))

imc = (pesokg) / (altura * altura)
print(imc)

if imc < 18:
	print("Abaixo do Peso")

elif imc in range(18, 25):
	print("Saudável")

elif imc in range(25, 30):
	print("Peso em excesso")

elif imc in range(30, 35):
	print("Obesidade Grau I")

elif imc in range(35, 40):
	print("Obesidade Grau II")

else: 
	print("Obesidade Grau III")

print("\nFIM")

