import sqlite3

# Conecta ao banco (cria o arquivo loja.db se ele nao existir)
conexao = sqlite3.connect("loja.db")
cursor = conexao.cursor()

# Cria a tabela de produtos
cursor.execute("""
CREATE TABLE IF NOT EXISTS produtos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    preco REAL NOT NULL
)
""")

# Produtos a serem inseridos
produtos_iniciais = [
    ("Teclado Mecânico", 250.00),
    ("Mouse Gamer", 120.50),
    ("Monitor 24 polegadas", 799.90),
]

# Inserção segura utilizando placeholders ?
cursor.executemany(
    "INSERT INTO produtos (nome, preco) VALUES (?, ?)", produtos_iniciais
)

conexao.commit()
conexao.close()

print("Banco loja.db criado e 3 produtos inseridos com sucesso!")