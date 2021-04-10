""" 
lista em python:
- fatiamento
- append
- insert
- pop
- del
- clear
- extend
- min 
- max
- range

lista = ['A', 'Bacana', 'C', 'D', 'E', 10.5]
string = 'ABCDE'

# acessando item de uma string
print(string[1])

# acessando item de uma lista
print(lista[1])

# vendo uma lista inteira
print(lista)

# usando o valor de uma lista
print(lista[5])
valor = lista[5]
print(type(valor))

l1 = [1, 2, 3]
l2 = [4, 5, 6]

print(l1)
print(l2)

# somando as listas
l3 = l1 + l2
print(l3)

# função insert
l4 = l3.insert(0, 'banana')
print(l4)

# função delete
lista = list(range(10))
del(lista[2:5])
print(lista)

lista = list(range(13))
print(max(lista))
print(min(lista))

"""
# fogo da forca

secreto = 'perfume'
digitadas = []
chances = 3
while chances >= 1:
    letra = input('Digite uma letra: ')

    if len(letra) > 1:
        print('Não pode digitar mais que uma letra!')
        continue

    digitadas.append(letra)
    if letra in secreto:
        print(f'{letra} existe na palavra secreta!')
    else:
        print(f'{letra} não existe na palavra secreta!')
        digitadas.pop()

    secreto_temp = ''
    for letra_secreta in secreto:
        if letra_secreta in digitadas:
            secreto_temp += letra_secreta
        else:
            secreto_temp += '*'

    if secreto_temp == secreto:
        print('GANHOU')
        print(f'Palavra {secreto_temp}')
        break
    else:
        print(f'Palavra secreta {secreto_temp}')

    if letra not in secreto:
        chances -= 1
        print(f'você tem {chances} chances.')
        if chances == 0:
            print('PERDEU')
            break
