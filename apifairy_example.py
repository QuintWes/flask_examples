from flask import Flask
from apifairy import APIFairy
from marshmallow import Schema, fields

app = Flask(__name__)
apifairy = APIFairy(app)

class PokemonSchema(Schema):
    id = fields.Int()
    name = fields.Str()

@app.route('/api/pokemon/<int:id>')
@apifairy.response(PokemonSchema)
def get_pokemon(id):
    return {'id': id, 'name': 'Pikachu'}

if __name__ == '__main__':
    app.run(port=5003)
