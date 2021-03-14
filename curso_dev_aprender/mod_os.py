import os

# Retorna o sistema operacional
os.name

# Retorna os arquivos no diretório
os.listdir()

# Retorna o separador nativo para o windos
os.sep

# Qual diretorio estamos?
os.getcwd()

# Montando um caminho para um arquivo.
# MUITO IMPORTANTE
os.path.join(os.getcwd() + os.sep + 'senhas.txt')
return 'C:\\Users\\Alfredo\\github\\estudos_em_python\\senhas.txt'

# Entrar dentro de uma pasta e acessar um documento
os.path.join(os.getcwd() + os.sep + 'documentos' + os.sep + 'senhas.txt')

# Extrair partes de um diretorio:
caminho = os.path.join(os.getcwd() + os.sep + 'senhas.txt')
print(os.path.dirname(caminho))  # obter um diretorio de path
print(os.path.basename(caminho))  # obter arquivo de um path

os.path.exists(os.getcwd() + os.sep + 'documentos')  # Retorna True | False
