import sqlite3
from flask import Flask, jsonify, request

app = Flask(__name__)


def conectar():
    conexao = sqlite3.connect("tarefas.db")
    conexao.row_factory = sqlite3.Row
    return conexao


 
@app.route("/tarefas", methods=["GET"])
def listar():
    conexao = conectar()
    cursor = conexao.execute("SELECT * FROM tarefas")
    tarefas = [dict(l) for l in cursor.fetchall()]
    conexao.close()
    return jsonify(tarefas)


 
@app.route("/tarefas", methods=["POST"])
def criar():
    novo = request.get_json()
    conexao = conectar()
    cursor = conexao.execute(
        "INSERT INTO tarefas (titulo, feita) VALUES (?, ?)",
        (novo["titulo"], novo.get("feita", 0)),
    )
    conexao.commit()
    novo_id = cursor.lastrowid
    conexao.close()
    return jsonify({"id": novo_id, **novo}), 201


 
@app.route("/tarefas/<int:id>", methods=["PUT"])
def atualizar(id):
    dados = request.get_json()
    conexao = conectar()
    cursor = conexao.execute(
        "UPDATE tarefas SET titulo = ?, feita = ? WHERE id = ?",
        (dados["titulo"], dados.get("feita"), id),
    )
    conexao.commit()
    afetadas = cursor.rowcount
    conexao.close()

    if afetadas == 0:
        return jsonify({"erro": "Tarefa nao encontrada"}), 404

    return jsonify({"id": id, **dados})


 
@app.route("/tarefas/<int:id>", methods=["DELETE"])
def apagar(id):
    conexao = conectar()
    cursor = conexao.execute("DELETE FROM tarefas WHERE id = ?", (id,))
    conexao.commit()
    afetadas = cursor.rowcount
    conexao.close()

    if afetadas == 0:
        return jsonify({"erro": "Tarefa nao encontrada"}), 404

    return jsonify({"mensagem": "Tarefa apagada com sucesso"})


if __name__ == "__main__":
    app.run(debug=True)
