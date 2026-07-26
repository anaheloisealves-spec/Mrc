from flask import Flask, jsonify, request

app = Flask(__name__)

# Banco de dados em memória
produtos = [
    {"id": 1, "nome": "Teclado Mecânico", "preco": 250.0},
    {"id": 2, "nome": "Mouse Gamer", "preco": 120.0},
]


@app.route("/produtos", methods=["GET"])
def listar_produtos():
    return jsonify(produtos)


@app.route("/produtos", methods=["POST"])
def criar_produto():
    novo_produto = request.get_json()
    produtos.append(novo_produto)
    return jsonify(novo_produto), 201


if __name__ == "__main__":
    app.run(debug=True)