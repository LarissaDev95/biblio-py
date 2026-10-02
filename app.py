from PySide6.QtWidgets import QApplication
from pesquisar_livro import Pesquisar_Livro

app = QApplication([])

tela_main = Pesquisar_Livro()
tela_main.show()

app.exec()



# Livros.create({
#     'titulo' : 'cronicas de narnia',
#     'isbn' : 1234567891234,
#     'autor' : 'autor',
#     'editora' : 'editora ltda',
#     'genero_literario': 'fantasia',
#     'data_lancamento' : '2026-09-28'
# })

# listLivros = Livros.find_all()
# print(listLivros)
# uniqueLivros = Livros.find_one({'id' : 7})
# print(dict(uniqueLivros))

# Livros.update(data={'titulo':'titulo atualizado'}, id=7)
# uniqueLivros = Livros.find_one({'id' : 7})
# print(dict(uniqueLivros))

# Livros.delete(id=1)
# uniqueLivros = Livros.find_one(rules={'id' : 1})
# print(dict(uniqueLivros))
