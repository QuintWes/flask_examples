from flask import Flask, render_template
from apifairy import APIFairy
from marshmallow import Schema, fields

app = Flask(__name__, template_folder="templates")
apifairy = APIFairy(app)

class PokemonSchema(Schema):
    id = fields.Int()
    name = fields.Str()

@app.route("/")
def home():
    return render_template("apifairy_example.html")

@app.route('/api/pokemon/<int:id>')
@apifairy.response(PokemonSchema)
def get_pokemon(id):
    return {'id': id, 'name': 'Pikachu'}

if __name__ == '__main__':
    app.run(port=5003)
