import connexion
from flask import render_template

app = connexion.App(__name__, specification_dir="./openapi/")
flask_app = app.app
flask_app.template_folder = "templates"

app.add_api("pokemon_api.yaml")

@flask_app.route("/")
def home():
    return render_template("connexion_example.html")

if __name__ == "__main__":
    app.run(port=5004)
