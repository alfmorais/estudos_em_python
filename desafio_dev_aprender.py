import json
from pathlib import Path

caminho = 'D://11. CURSOS DE TI//15_CURSO_DE_PYTHON_DEV_APRENDER//pikachu.json'

arquivo = Path(caminho).read_text()
arquivo_json = json.loads(arquivo)


def funcao_ability(ability):
    resultado = "['abilities'][1]['ability']['name']"
    if resultado == 'lightning-rod':
        print(f'{ability} encontrada!')
    else:
        pass


for arquivo in arquivo_json:
    funcao_ability(arquivo)
