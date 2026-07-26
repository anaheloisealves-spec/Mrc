import sqlite3

conexao = sqlite3.connect("loja.db")
cursor = conexao.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS produtos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    preco REAL NOT NULL
)
""")

produtos_iniciais = [
    ("Teclado Mecânico", 250.00),
    ("Mouse Gamer", 120.50),
    ("Monitor 24 polegadas", 799.90),
]
cursor.executemany(
    "INSERT INTO produtos (nome, preco) VALUES (?, ?)", produtos_iniciais
)

conexao.commit()
conexao.close()

print("Banco loja.db criado e 3 produtos inseridos com sucesso!")
