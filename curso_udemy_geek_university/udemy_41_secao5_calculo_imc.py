altura = float(input("Digite sua altura: "))
pesokg = float(input("Digite seu peso: "))

imc = (pesokg) / (altura * altura)
print(imc)

if imc <= 18.5:
	print("Abaixo do Peso")

elif imc in range(18.6, 24.9):
	print("Saudável")

elif imc in range(25.0, 29.9):
	print("Peso em excesso")

elif imc in range(30.0, 34.9):
	print("Obesidade Grau I")

elif imc in range(35.0, 39.9):
	print("Obesidade Grau II")

else: 
	print("Obesidade Grau III")

print("\nFIM")
