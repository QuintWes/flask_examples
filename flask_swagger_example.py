from flask import Flask, jsonify, render_template
from flask_swagger import swagger

app = Flask(__name__, template_folder="templates")

@app.route("/")
def home():
    return render_template("swagger_example.html")

@app.route('/api/pokemon/<int:id>')
def get_pokemon(id):
    return jsonify({'id': id, 'name': 'Pikachu'})

@app.route("/spec")
def spec():
    return jsonify(swagger(app))

if __name__ == '__main__':
    app.run(port=5001)
