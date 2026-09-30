import sys
from PySide6.QtWidgets import QWidget
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile

class TelaPesquisarLivro(QMainWindow):
    def __init__(self):
        super.__init__()

        self.caminho_tela = 'pesquisar_livro.ui'
        self.tela = QFile(self.caminho_tela)
        self.tela.open(QFile.ReadOnly)

        self.loader = QUiLoader()
        self.loader.load(self.tela)

        self.open_window = self.loader.load(self.tela)
        self.open_window.show()


        self.open_window.ButtonPesquisar.clicked(self.pesquisar)


    def pesquisar(self):
        print('teste')