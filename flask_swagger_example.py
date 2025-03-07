from flask import Flask, jsonify, render_template
from flasgger import Swagger
from flask_swagger import swagger as swagger_spec_generator

app = Flask(__name__, template_folder="templates")
flasgger_swagger = Swagger(app)

@app.route("/")
def home():
    return render_template("swagger_example.html")

@app.route('/api/pokemon/<int:id>')
def get_pokemon(id):
    """
    Get a Pokemon
    ---
    parameters:
      - name: id
        in: path
        type: integer
        required: true
    responses:
      200:
        description: A single Pokemon test
        examples:
          application/json: { "id": 1, "name": "Pikachu" }
    """
    return jsonify({'id': id, 'name': 'Pikachu'})

@app.route("/spec")
def spec():
    swag = swagger_spec_generator(app)
    swag['info']['title'] = "Pokemon API"
    swag['info']['version'] = "1.0.0"
    return jsonify(swag)

if __name__ == '__main__':
    app.run(port=5001)
