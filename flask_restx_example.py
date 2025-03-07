from flask import Flask, render_template
from flask_restx import Api, Resource, Namespace

app = Flask(__name__, template_folder="templates")
api = Api(app, doc='/docs', title="Pokemon API", version="1.0", description="Simple Pokemon API")

# Create a namespace
pokemon_ns = Namespace('pokemon', description='Pokemon operations')

@app.route("/")
def home():
    return render_template("restx_example.html")

# Add route to the namespace
@pokemon_ns.route('/<int:id>')
class Pokemon(Resource):
    def get(self, id):
        """Get a Pokemon by its ID"""
        return {'id': id, 'name': 'Pikachu'}

# Add the namespace to the API
api.add_namespace(pokemon_ns, path="/api/pokemon")

if __name__ == '__main__':
    app.run(port=5002)
