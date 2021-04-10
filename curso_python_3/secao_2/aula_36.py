""" 
for in em python
iterando strings com for
função range(start=0, stop, step=1)
"""
texto = 'Python'

for letra in texto:
    print(letra)

for i, letra in enumerate(texto):
    print(i, letra)

for numero in range(10):
    print(numero)

nova_string = ''

for letra in texto:
    if letra == 't':
        nova_string = nova_string + letra.upper()
    elif letra == 'h':
        nova_string += letra.upper()
    else:
        nova_string += letra

print(nova_string)
