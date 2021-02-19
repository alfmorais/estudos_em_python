# Conversão entre tipos

# STR -> INT
idade = int(input('Digite a sua idade: '))
print(idade > 17)

# INT -> STR
ano_publicacao = 2020
print('Este livro foi criado em ' + str(ano_publicacao))

# STR -> FLOAT
altura = input('Altura da Parede?')
print(float(altura) > 2.50)

# Conversões entre coleções
saudacao = 'Hello'
print(list(saudacao))  # STR -> LIST
print(set(saudacao))  # STR -> SET
print(tuple(saudacao))  # STR -> TUPLE
print(list(range(30)))  # RANGE -> LIST

# Conversões entre lista
numeros = [10, 20, 30, 40]
print(set(numeros))
print(tuple(numeros))
print(type(numeros))
