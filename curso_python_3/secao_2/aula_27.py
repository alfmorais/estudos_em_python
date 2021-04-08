# Leia a documentação
num1 = input('Digite numero 1: ')
num2 = input('Digite numero 2: ')

# isnumeric
print(num1.isnumeric())
print(num2.isnumeric())

# isdigit
print(num1.isdigit())
print(num2.isdigit())

# isdecimal
print(num1.isdecimal())
print(num2.isdecimal())

if num1.isdigit() and num2.isdigit():
    num1 = int(num1)
    num2 = int(num2)

    num = num1 + num2

    print(f'Soma dos dois números: {num}')

else:
    print('Você digitou um caractere invalido.')
