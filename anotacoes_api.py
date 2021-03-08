from flask import Flask, jsonify, request
import json
app = Flask(__name__)

# Receber parâmetro na URL: http://localhost:5000/100
# @app.route("/<number>", methods=['GET', 'POST'])
# Definir o tipo do parâmetro
# @app.route("/<int:number>", methods=['GET', 'POST'])

#def hello(number):
#  return 'Olá mundo! {}'.format(number)

@app.route("/<int:id>", methods=['GET', 'POST'])

# GET http://localhost:5000/1
def hello(id):
  if id == 1:
    return jsonify({
      'id': 1,
      'nome': 'Fabio Soares',
      'idade': 24
    })
  else:
    return jsonify({'error': 'Not found'})

# Utilizando uma lib
# pip3 install requests
# >>> import requests
# >>> response = requests.get('http://localhost:5000/1')
# >>> print(response.text)
# {
#   "id": 1,
#   "idade": 24,
#   "nome": "Fabio Soares"
# }

# caso seja POST...
# >>> import json
# >>> response = requests.post('http://localhost:5000/soma', json={"valores": [10,20]})
# >>> print(response.json())
# {'soma': 30}

@app.route("/soma", methods=['POST'])

# POST http://localhost:5000/soma
# body:
# {"valores": [10,20]}
def soma():
  numbers = sum(json.loads(request.data)['valores'])
  return jsonify({'soma': numbers})

@app.route("/developers/<int:id>", methods=['PUT', 'GET'])

# POST http://localhost:5000/developers/1
# body:
# {"valores": [10,20]}

DEVELOPERS = [
  {
    'id': 1,
    'name': 'Fabio Soares',
    'skills': ['Python', 'Ruby']
  },
  {
    'id': 2,
    'name': 'Teste Teste',
    'skills': ['Java', 'ShellScript']
  }
]

def developers(id):
  if request.method == 'PUT':
    data = json.loads(request.data)
    DEVELOPERS[id] = data
    return jsonify(DEVELOPERS[id])
  elif request.method == 'GET':
    return jsonify(DEVELOPERS[id])
  else:
    return jsonify({'error': 'Method POST not implemented'})

if __name__ == "__main__":
  # Usar o debug apenas em dev
  app.run(debug=True)
  #app.run()
