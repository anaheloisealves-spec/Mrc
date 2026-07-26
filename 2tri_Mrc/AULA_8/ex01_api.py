from flask import Flask

app = Flask(__name__)


@app.route("/")
def inicio():
    # Substitua pelo seu nome completo
    return "Aninha"


if __name__ == "__main__":
    app.run(debug=True)