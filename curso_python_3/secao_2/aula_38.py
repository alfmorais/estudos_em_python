# for / else em python

lista = ['Alf', 'Mor', 'Neto']

for valor in lista:
    if valor.startswith('A'):
        print('Começa com A')
    else:
        print('Não começa com A')

comeca_com_a = False

for valor in lista:
    if valor.startswith('A'):
        comeca_com_a = True

if comeca_com_a == True:
    print('Exista palavra que começa com A')
else:
    print('Não existe')
