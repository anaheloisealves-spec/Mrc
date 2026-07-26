import sqlite3
from flask import Flask, jsonify, request

app = Flask(__name__)

def conectar():
    conexao = sqlite3.connect("loja.db")
    conexao.row_factory = sqlite3.Row
    return conexao


def criar_tabela():
    conexao = conectar()
    conexao.execute("""
    CREATE TABLE IF NOT EXISTS produtos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        preco REAL NOT NULL
    )
    """)
    conexao.commit()
    conexao.close()

@app.route("/produtos", methods=["GET"])
def listar_produtos():
    conexao = conectar()
    cursor = conexao.execute("SELECT * FROM produtos")
    produtos = [dict(linha) for linha in cursor.fetchall()]
    conexao.close()
    return jsonify(produtos)


@app.route("/produtos", methods=["POST"])
def criar_produto():
    novo = request.get_json()

   
        return jsonify({"erro": "O campo preco e obrigatorio"}), 400

    if "nome" not in novo:
        return jsonify({"erro": "O campo nome e obrigatorio"}), 400

    conexao = conectar()
    cursor = conexao.execute(
        "INSERT INTO produtos (nome, preco) VALUES (?, ?)",
        (novo["nome"], novo["preco"]),
    )
    conexao.commit()

    novo_id = cursor.lastrowid
    conexao.close()

    return jsonify({"id": novo_id, **novo}), 201


if __name__ == "__main__":
    criar_tabela()
    app.run(debug=True)
