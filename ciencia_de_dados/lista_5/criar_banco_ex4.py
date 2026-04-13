import sqlite3

conn = sqlite3.connect("meu_banco.db")
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS produtos (
        id INTEGER PRIMARY KEY,
        nome TEXT,
        preco REAL,
        estoque INTEGER
    )
""")

cursor.executemany("INSERT INTO produtos (nome, preco, estoque) VALUES (?, ?, ?)", [
    ("Televisão", 1500.00, 30),
    ("Celular", 899.90, 45),
    ("Notebook", 3200.50, 18),
    ("Tablet", 899.90, 12),
    ("Fone de Ouvido", 150.00, 60),
    ("Smart Watch", 320.00, 55),
    ("Caixa de Som", 175.30, 20),
    ("Monitor", 1200.00, 38),
])

conn.commit()
conn.close()