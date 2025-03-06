import connexion

app = connexion.App(__name__, specification_dir="./openapi/")
app.add_api("pokemon_api.yaml")

if __name__ == "__main__":
    app.run(port=5004)
