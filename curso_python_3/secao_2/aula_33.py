""" 
while em Python
utilizando para realizar ações enquanto 
uma condição for verdadeira

requisitos: entender condições e operadores


while True:
    nome = input("Qual é o seu nome?")
    print(f'Olá {nome}')
    break

print('Não será executado')

# Fazendo um contador
x = 0
while x <= 100:
    print(x)
    x = x + 1

print('Acabou!')

# usando a função continue
y = 0
while y < 10:
    if y == 3:
        y += 1
        continue
    print(y)
    y += 1

# usando uma tabela
x = 0
while x < 10:
    y = 0
    while y < 5:
        print(f'X vale {x} e Y vale {y}')
        y += 1
    x += 1

print('Acabou!')
"""

while True:
    print()
    num_1 = input('Digite um número: ')
    num_2 = input('Digite outro número: ')
    operador = input('Digite um operador: ')

    if not num_1.isnumeric() or not num_2.isnumeric():
        print('Você precisa digitar um número.')
        print('Encerrando o programa!')
        break

    num_1 = int(num_1)
    num_2 = int(num_2)

    if operador == '+':
        print(num_1 + num_2)
    elif operador == '-':
        print(num_1 - num_2)
    elif operador == '/':
        print(num_1 / num_2)
    elif operador == '*':
        print(num_1 * num_2)
    else:
        print('Operador Invalido, digite novamente!')
