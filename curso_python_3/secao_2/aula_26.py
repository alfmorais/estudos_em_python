# Função Len

usuario = input('Digite seu usuário: ')
quantidade = len(usuario)

print(usuario, quantidade, type(quantidade))

if quantidade < 6:
    print('digite mais que 6 caracteres')
else:
    print('cadastro com sucesso')

nome = 'alfredo'
sobrenome = 'morais'
completo = nome + ' ' + sobrenome

print(completo, len(completo), type(completo))
