import os

# Criar uma pasta, ainda não existente
os.mkdir('Musicas')
os.makedirs('Videos' + os.sep + 'Ação')
os.makedirs('Músicas' + os.sep + 'Rock')

# path = caminho completo

print(os.path.isdir('Músicas'))

if os.path.isdir('Músicas') == False:
    os.mkdir('Músicas')
else:
    print('Diretório já existe')
