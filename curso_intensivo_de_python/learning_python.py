filename = 'aprendizado.txt'

with open(filename) as arquivo:
    linhas = arquivo.readlines()
    print('Monstrando o metodo 1: ')
    print(linhas)

print('Monstrando o metodo 2: ')
for linha in linhas:
    print(linha)

print('Monstrando o metodo 3: ')
print(linhas)
