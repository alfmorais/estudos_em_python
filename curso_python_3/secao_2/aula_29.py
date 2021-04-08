'''
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou impar. Caso o usuário não digite um número inteiro, 
informe que não é um número inteiro
'''
numero = input('Digite um número: ')

if numero.isnumeric():
    numero = int(numero)
    if numero % 2 == 0:
        print(f'{numero} é par!')
    else:
        print(f'{numero} é impar!')

else:
    print('Você digitou um caractere não valido. Vamos encerrar o programa.')

'''
Faça um programa que pergunte a hora ao usuario e baseando-se no horário
descrito, exiba a saudação apropriado. Ex:
bom dia 0-11, boa tarde 12-17, boa noite 18-23
'''
hora = input('Digite a hora (0 a 23): ')

if hora.isdigit():
    hora = int(hora)
    if hora >= 0 and hora <= 11:
        print('Bom dia')
    elif hora >= 12 and hora <= 17:
        print('Boa tarde')
    elif hora >= 18 and hora <= 23:
        print('Boa noite')
    else:
        print('Digito invalido')

else:
    print('Você digitou um caractere não valido. Vamos encerrar o programa.')

'''
faça um programa que peça o primeiro nome do usuário. se o nome tiver 4 letras ou 
menos escreva "seu nome é curto", se tiver entre 5 a 6 letras, escreva: "seu nome é normal"
maior que 6 escreva: "seu nome é muito grande"
'''
nome = input('Digite seu nome: ')
tamanho = len(nome)

if nome.isdigit():
    if tamanho <= 4:
        print('seu nome é curto')
    elif tamanho >= 5 and tamanho <= 6:
        print('seu nome é normal')
    else:
        print('seu nome é muito grande')

else:
    print('Você digitou um caractere não valido. Vamos encerrar o programa.')
