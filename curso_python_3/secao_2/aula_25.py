"""
Operadores Lógicos

and    | True x True = True != return False
or     | True x False = True > False x False = return False
not    | Not included on collection
in     | Check if object are included on collection 
not in | Check if object not are included on collectiona = 2
b = 2
c = 3

condicao = a == b and b < c

if condicao == True:
    print('Verdadeiro')

else:
    print('Falso')

print(not True)

a = ''

if not a:
    print('Preencha a variavel A')
    


"""

usuario = input('Nome: ')
senha = input('Senha: ')

usuario_bd = 'Alfredo'
senha_bd = '123456'

if usuario == usuario_bd and senha == senha_bd:
    print('Logado')

else:
    print('Login Incorreto')



