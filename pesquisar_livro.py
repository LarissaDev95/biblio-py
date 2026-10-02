from ui_pesquisar_livro import Ui_PesquisarLivro
from PySide6.QtWidgets import QMainWindow
from livros import Livros

class Pesquisar_Livro(QMainWindow):
    def __init__(self):
        super(Pesquisar_Livro, self).__init__()
        self.ui = Ui_PesquisarLivro()

        self.ui.setupUi(self)

        self.ui.ButtonPesquisar.clicked.connect(self.pesquisar)

    def pesquisar(self):
        livros_encontrados = Livros.find_all({
                'autor': self.ui.InputAutor.toPlainText()
            })

        self.ui.InputTitulo.setPlainText( livros_encontrados[0].titulo)
        