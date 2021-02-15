def comando():
	num = int(input("Digite um número entre 100 a 999: "))
	

	if num in range(100, 1000):
		for num2 in num:
			print(num2)
	else:
		print("Valor digitado não corresponde com a ordem!")
		print("Digite novamente!")
		comando()

comando()
