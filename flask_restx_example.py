from flask import Flask
from flask_restx import Api, Resource

app = Flask(__name__)
api = Api(app)

@api.route('/api/pokemon/<int:id>')
class Pokemon(Resource):
    def get(self, id):
        return {'id': id, 'name': 'Pikachu'}

if __name__ == '__main__':
    app.run(port=5002)
