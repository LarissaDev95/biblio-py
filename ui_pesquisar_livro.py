# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pesquisar_livro.ui'
##
## Created by: Qt User Interface Compiler version 6.11.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QMenu,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QTextEdit, QVBoxLayout, QWidget)

class Ui_PesquisarLivro(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(0, 0, 791, 551))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setSpacing(50)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 26, 16, 26)
        self.Titulo = QLabel(self.verticalLayoutWidget)
        self.Titulo.setObjectName(u"Titulo")

        self.verticalLayout.addWidget(self.Titulo)

        self.InputTitulo = QTextEdit(self.verticalLayoutWidget)
        self.InputTitulo.setObjectName(u"InputTitulo")

        self.verticalLayout.addWidget(self.InputTitulo)

        self.Autor = QLabel(self.verticalLayoutWidget)
        self.Autor.setObjectName(u"Autor")

        self.verticalLayout.addWidget(self.Autor)

        self.InputAutor = QTextEdit(self.verticalLayoutWidget)
        self.InputAutor.setObjectName(u"InputAutor")

        self.verticalLayout.addWidget(self.InputAutor)

        self.ButtonPesquisar = QPushButton(self.verticalLayoutWidget)
        self.ButtonPesquisar.setObjectName(u"ButtonPesquisar")

        self.verticalLayout.addWidget(self.ButtonPesquisar)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 22))
        self.menuPesquisar_Livro = QMenu(self.menubar)
        self.menuPesquisar_Livro.setObjectName(u"menuPesquisar_Livro")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuPesquisar_Livro.menuAction())

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.Titulo.setText(QCoreApplication.translate("MainWindow", u"Titulo", None))
        self.Autor.setText(QCoreApplication.translate("MainWindow", u"Autor", None))
        self.ButtonPesquisar.setText(QCoreApplication.translate("MainWindow", u"Pesquisar", None))
        self.menuPesquisar_Livro.setTitle(QCoreApplication.translate("MainWindow", u"Pesquisar Livro", None))
    # retranslateUi

