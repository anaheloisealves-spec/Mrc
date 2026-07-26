import sqlite3
from flask import Flask, jsonify, request

app = Flask(__name__)


def conectar():
    conexao = sqlite3.connect("loja.db")
    conexao.row_factory = sqlite3.Row
    return conexao

 
@app.route("/produtos/<int:id>", methods=["DELETE"])
def apagar(id):
    conexao = conectar()
    cursor = conexao.execute("DELETE FROM produtos WHERE id = ?", (id,))
    conexao.commit()
    afetadas = cursor.rowcount
    conexao.close()

    if afetadas == 0:
        return jsonify({"erro": "Produto nao encontrado"}), 404

    return jsonify({"mensagem": "Produto apagado com sucesso"})


if __name__ == "__main__":
    app.run(debug=True)
