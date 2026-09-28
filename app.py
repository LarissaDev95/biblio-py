import mysql.connector

conector = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "biblioteca_py",
    
)

cursor = conector.cursor()

cursor.execute("INSERT INTO livro(isbn, autor, titulo, data_lancamento, genero_literario, editora) VALUES (123435, 'machado de assis', 'dom casmurro'. '1899-02-25', 'romance', 'livaria')")

conector.commit()