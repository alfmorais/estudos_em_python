# NOSSO 1º API - FLASK E DJANGO
# DUAS MANEIRAS
# 1) FLASK
# 2) FLASK RESTFUL

from flask import Flask, jsonify, request

app = Flask(__name__)

'''
1 - Definir o objetivo da API:
    Ex: Iremos montar uma API de blog, onde eu poderei consultar,
    editar, criar e excluir postagens em um blog usando a API.

2 - Qual será a URL base da API?
    Ex: Quando você cria uma aplicação local ela terá um URL tipo
    http://localhost:5000, porém quando você for subir isso para nuvem, 
    você terá que comprar ou usar um dominio como URL base, vamos imaginar
    um exemplo: devaprender.com.br/api/

3 - Quais são os endpoints? 
    Ex: Se seu requesito é de poder consultar, criar e excluir, você terá que
    disponibilizar os endpoints para essas questões
            >/postagens

4 - Quais recursos será disponibilizado pelo API: 
    Informações sobre as postagens

5 - Quais verbos http serão disponibilizados?
    - GET
    - POST
    - PUT
    - DELETE

6 - Quais são os URL completos para cada um?
    - GET: http://localhost:5000/postagens
    - GET id: http://localhost:5000/postagens/1
    - POST id: http://localhost:5000/postagens
    - PUT id: http://localhost:5000/postagens/1
    - DELETE id: http://localhost:5000/postagens
'''

postagens = [
    {
        'título': 'Minha História',
        'autor': 'Amanda Dias'
    },
    {
        'título': 'Novo Dispositivo Sony',
        'autor': 'Howard Stringer'
    },
    {
        'título': 'Lançamento do Ano',
        'autor': 'Jeff Bezos'
    }
]

# Rota padrão - GET https://localhost:5000


@app.route('/')
def obter_postagens():
    return jsonify(postagens)

# Obter postagem por id - GET https://localhost:5000/postagem/1


@app.route('/postagem/<int:indice>', methods=['GET'])
def obter_postagem_por_indice(indice):
    return jsonify(postagens[indice])

# Criar uma nova postagem - POST https://localhost:5000/postagem


@app.route('/postagem', methods=['POST'])
def nova_postagem():
    postagem = request.get_json()
    postagens.append(postagem)

    return jsonify(postagem, 200)

# Alterar uma postagem existente - PUT https://localhost:5000/postagem/1


@app.route('/postagem/<int:indice>', methods=['PUT'])
def alterar_postagem(indice):
    postagem_alterada = request.get_json()
    postagens[indice].update(postagem_alterada)

    return jsonify(postagens[indice], 200)

# Excluir uma postagem - DELETE - https://localhost:5000/postagem/1


@app.route('/postagens/<int:indice>', methods=['DELETE'])
def excluir_postagem(indice):
    try:
        if postagens[indice] is not None:
            del postagens[indice]
            return jsonify(f'Foi excluído a postagem {postagens[indice]}', 200)
    except:
        return jsonify('Não foi possível encontrar a postagem para exclusão', 404)


app.run(port=5000, host='localhost', debug=True)
