# Arquivos JSON

import json
from pathlib import Path

carros = [
    {'Marca': 'Nissan', 'Preço': 45.000, 'Cor': 'Azul'},
    {'Marca': 'Ford', 'Preço': 75.000, 'Cor': 'Verde'},
    {'Marca': 'BMW', 'Preço': 117.000, 'Cor': 'Amarelo'}
]

carros_json = json.dumps(carros)
Path('D://11. CURSOS DE TI//15_CURSO_DE_PYTHON_DEV_APRENDER\carros.json').write_text(carros_json)

arquivo = Path(
    'D://11. CURSOS DE TI//15_CURSO_DE_PYTHON_DEV_APRENDER\carros.json').read_text()
arquivo_json = json.loads(arquivo)
print(arquivo_json[0]['Marca'] + ' ' + str(arquivo_json[0]['Preço']))
print(arquivo_json[1]['Marca'] + ' ' + str(arquivo_json[1]['Preço']))
