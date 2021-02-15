num = int(input("Digite um num: "))

equ1 = 0
equ2 = 0
equ3 = 0

for n in range(0, num + 1):
	equ1 += n

for n in range(0, num + 1):
	equ2 += (2*n) - 1

print(equ1)
print(equ2)
