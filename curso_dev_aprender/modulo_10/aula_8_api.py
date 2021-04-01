# NOSSO 1º API - FLASK E DJANGO
# DUAS MANEIRAS
# 1) FLASK
# 2) FLASK RESTFUL

from flask import Flask, jsonify, request

api = Flask(__name__)

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

# ROTA PADRÃO


@api.route('/')
def obter_postagens():
    """

    """
    return jsonify(postagens)


api.run(port=5000, host='localhost', debug=True)
