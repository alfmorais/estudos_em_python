print("Seção 5: Estruturas Lógicas e Condicionais em Python") 
"""
1) O que vamos aprender nessa seção
2) if, else, elif
3) AND, OR, NOT, IS
4) Recapitulando

* elif = (else + if)

"""

print("\nFunção IF")
idade = float(input("Digite sua idade: "))
if idade < 18:
	print("\nMenor de Idade")
elif idade == 18:
	print("\nTem 18 anos")
else: 
	print("\nMaior de Idade")

"""
Estrutura lógicas: and, or, not, is. 

Operadores Unários - not, is
Operadores Binários - and, or

"""

ativo = False
logado = True

if ativo or logado: 
	print("\nBem vindo usuário!")
else: 
	print("\nVocê precisa ativar sua conta. Por favor, cheque seu e-mail!")

if not ativo: 
	print("\nVocê precisa ativar sua conta. Por favor, cheque seu e-mail!")
else:
	print("\nBem vindo usuário!")

print(not True)
print(not False)

if ativo is False:
	print("\nVocê precisa ativar sua conta. Por favor, cheque seu e-mail!")
else:
	print("\nBem vindo usuário!")
print("\nPrograma Encerrado")


