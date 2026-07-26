from flask import Flask, jsonify

app = Flask(__name__)

produtos = [
    {"id": 1, "nome": "Teclado Mecânico", "preco": 250.00, "disponivel": True},
    {"id": 2, "nome": "Mouse Gamer", "preco": 120.50, "disponivel": False},
    {
        "id": 3,
        "nome": "Monitor 24 polegadas",
        "preco": 799.90,
        "disponivel": True,
    },
    {"id": 4, "nome": "Headset USB", "preco": 180.00, "disponivel": True},
]


@app.route("/produtos/<int:id>")
def buscar_produto(id):
    for produto in produtos:
        if produto["id"] == id:
            return jsonify(produto)

    # Caso não encontre nenhum produto com o ID especificado
    return jsonify({"erro": "Produto nao encontrado"}), 404


if __name__ == "__main__":
    app.run(debug=True)