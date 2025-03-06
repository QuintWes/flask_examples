from flask import Flask, jsonify
from flask_swagger import swagger

app = Flask(__name__)

@app.route('/api/pokemon/<int:id>')
def get_pokemon(id):
    return jsonify({'id': id, 'name': 'Pikachu'})

@app.route("/spec")
def spec():
    return jsonify(swagger(app))

if __name__ == '__main__':
    app.run(port=5001)
