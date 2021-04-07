"""
Operadores Relacionais

== | igualdade
>  | maior que
>= | maior ou igual que
<  | menor que
<= | menor ou igual que
!= | diferente de
"""

num_1 = int(input('Digite num_1: '))
num_2 = int(input('Digite num_2: '))

if num_1 == num_2:
    print(True)
elif num_1 != num_2:
    print(False)

print('num_1 == num_2: ' + str(num_1 == num_2))
print('num_1 > num_2: ' + str(num_1 > num_2))
print('num_1 >= num_2: ' + str(num_1 >= num_2))
print('num_1 < num_2: ' + str(num_1 < num_2))
print('num_1 <= num_2: ' + str(num_1 <= num_2))
print('num_1 != num_2: ' + str(num_1 != num_2))

nome = input('Qual é o seu nome? ')
idade = input('Qual é a sua idade? ')

idade_limite = 18
idade_maxima = 25

if int(idade) >= idade_limite and int(idade) <= idade_maxima:
    print(f'{nome} pode pegar o emprestimo!')

else:
    print(f'{nome} não pode pegar o emprestimo!')

    
