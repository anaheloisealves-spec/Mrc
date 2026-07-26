from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/produto")
def produto():
    dados_produto = {
        "id": 1,
        "nome": "Teclado Mecânico",
        "preco": 250.00,
        "disponivel": True,
    }
    return jsonify(dados_produto)


if __name__ == "__main__":
    app.run(debug=True)