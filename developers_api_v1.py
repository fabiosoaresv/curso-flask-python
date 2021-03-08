from flask import Flask, jsonify, request
import json

app = Flask(__name__)

developers_array = [
  {'id': '1','name': 'Fabio Soares','skills': ['Python', 'Ruby']},
  {'id': '2','name': 'Teste Teste','skills': ['Java', 'Shell Script']}
]

@app.route("/developers/<int:id>", methods=['PUT', 'GET', 'POST', 'DELETE'])

def developers(id):
  if request.method == 'PUT':
    data = json.loads(request.data)
    developers_array[id] = data
    return jsonify(developers_array[id])
  elif request.method == 'GET':
    try:
      response = developers_array[id]
    except IndexError:
      response = {'error': 'Developer ID not found!'}
    except Exception:
      response = {'error': 'Error unknown'}
    return jsonify(response)
  elif request.method == 'POST':
    return jsonify({'error': 'Method POST not implemented'})
  elif request.method == 'DELETE':
    developers_array.pop(id)
    return jsonify({'success': True, 'message': 'Developer deleted!'})

if __name__ == "__main__":
  app.run(debug=True)
