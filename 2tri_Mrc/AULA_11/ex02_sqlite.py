import sqlite3

conexao = sqlite3.connect("loja.db")

# row_factory faz com que as linhas venham no formato de dicionário
conexao.row_factory = sqlite3.Row
cursor = conexao.cursor()

# Busca todos os produtos
cursor.execute("SELECT * FROM produtos")
produtos = cursor.fetchall()

print("--- Lista de Produtos ---")
for linha in produtos:
    produto = dict(linha)
    print(
        f"ID: {produto['id']} | Nome: {produto['nome']} | Preço: R$ {produto['preco']:.2f}"
    )

conexao.close()