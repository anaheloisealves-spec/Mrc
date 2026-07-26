import sqlite3

conexao = sqlite3.connect("loja.db")

conexao.row_factory = sqlite3.Row
cursor = conexao.cursor()

cursor.execute("SELECT * FROM produtos")
produtos = cursor.fetchall()

print("--- Lista de Produtos ---")
for linha in produtos:
    produto = dict(linha)
    print(
        f"ID: {produto['id']} | Nome: {produto['nome']} | Preço: R$ {produto['preco']:.2f}"
    )

conexao.close()
