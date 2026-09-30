from livros import Livros
from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile
import sys
from tela_pesquisar_livro import TelaPesquisarLivro

app = QApplication([])

tela_main = TelaPesquisarLivro()
app.exec()



