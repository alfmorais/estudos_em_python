from datetime import *

# - Criar variáveis para nome(str), idade(int)
# - altura(float) e peso(float) de uma pessoa
# - Criar variável com o ano atual(int)
# - Obter o ano de nascimento da pessoa (baseado na idade e no ano atual)
# - Obter o IMC da pessoa com 2 casas decimas (peso e na altura da pessoa)
# - Exibir um texto com todos os valores na tela usando F-Strings(com as chaves)

# dados do exercicio
nome = 'Alfredo'
idade = 28
altura = 1.58589575
peso = 85.5698565
ano = datetime.today()
ano = int(ano.year)
nascimento = ano - idade
imc = peso / altura ** 2

# String Formatada
print('Meu nome é {}, tenho {} anos, minha altura {:.2f}, meu peso {:.2f}, eu nasci no ano {}, estamos no ano {} e continuo com o IMC = {:.2f}'.format(
    nome, idade, altura, peso, nascimento, ano, imc))
