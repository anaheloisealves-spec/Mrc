import sqlite3
from flask import Flask, jsonify, request

app = Flask(__name__)


def conectar():
    conexao = sqlite3.connect("loja.db")
    conexao.row_factory = sqlite3.Row
    return conexao


# READ - listar
@app.route("/produtos", methods=["GET"])
def listar():
    conexao = conectar()
    cursor = conexao.execute("SELECT * FROM produtos")
    produtos = [dict(l) for l in cursor.fetchall()]
    conexao.close()
    return jsonify(produtos)


# UPDATE - atualizar
@app.route("/produtos/<int:id>", methods=["PUT"])
def atualizar(id):
    dados = request.get_json()
    conexao = conectar()
    cursor = conexao.execute(
        "UPDATE produtos SET nome = ?, preco = ? WHERE id = ?",
        (dados["nome"], dados.get("preco"), id),
    )
    conexao.commit()
    afetadas = cursor.rowcount
    conexao.close()

    if afetadas == 0:
        return jsonify({"erro": "Produto nao encontrado"}), 404

    return jsonify({"id": id, **dados})


if __name__ == "__main__":
    app.run(debug=True)