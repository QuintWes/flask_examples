from flask import Flask, render_template
from flask_restx import Api, Resource

app = Flask(__name__, template_folder="templates")
api = Api(app)

@app.route("/")
def home():
    return render_template("restx_example.html")

@api.route('/api/pokemon/<int:id>')
class Pokemon(Resource):
    def get(self, id):
        return {'id': id, 'name': 'Pikachu'}

if __name__ == '__main__':
    app.run(port=5002)
