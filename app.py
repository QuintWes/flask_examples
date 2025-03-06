from flask import Flask, render_template_string

app = Flask(__name__)

@app.route("/")
def index():
    return render_template_string("""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <title>API Package Examples</title>
        <style>
            body { font-family: Arial, sans-serif; padding: 50px; background-color: #f5f5f5; }
            h1 { margin-bottom: 30px; }
            a { display: block; padding: 15px; margin: 10px 0; background-color: #007bff; color: white; text-decoration: none; border-radius: 5px; width: 300px; text-align: center; }
            a:hover { background-color: #0056b3; }
        </style>
    </head>
    <body>
        <h1>Flask API Examples</h1>
        <a href="http://localhost:5001/api/pokemon/1">Flask-Swagger Example</a>
        <a href="http://localhost:5002/api/pokemon/1">Flask-RESTX Example</a>
        <a href="http://localhost:5003/api/pokemon/1">APIFairy Example</a>
        <a href="http://localhost:5005/api/pokemon/1">Connexion Example</a>
    </body>
    </html>
    """)

if __name__ == '__main__':
    app.run(port=5000)
