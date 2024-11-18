from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QApplication,QMainWindow,QMenuBar,QMenu,QFileDialog

from main import display_all_cells
import sys


class Window(QMainWindow):
    def __init__(self):
        super(Window,self).__init__()

        self.setWindowTitle('Редактор')
        self.setGeometry(100,250,650,500)

        self.text_edit = QtWidgets.QTextEdit(self)
        self.setCentralWidget(self.text_edit)

        self.createMenuBar()
    def createMenuBar(self):
        self.menuBar = QMenuBar(self)
        self.setMenuBar(self.menuBar)

        fileMenu = QMenu("&Файл ",self)
        self.menuBar.addMenu(fileMenu)

        # show_all = fileMenu.addMenu("&Показать все")
        # show_full = fileMenu.addMenu("&Показать все +")
        # show_minus = fileMenu.addMenu("&Показать все -")
        fileMenu.addAction('save',self.action_clicked)
        fileMenu.addAction('open', self.action_clicked)

        fileMenu_show = QMenu("&Показать ", self)
        self.menuBar.addMenu(fileMenu_show)
        fileMenu_show.addAction('show_all',self.action_clicked)

    @QtCore.pyqtSlot()
    def action_clicked(self):
        action = self.sender()
        # print(f'Action + {action.text()}')
        if action.text() == 'save':
            print(f'save')
            fname = QFileDialog.getSaveFileName(self)[0]
            try:
                f = open(fname,'w')
                text = self.text_edit.toPlainText()
                f.write(text)
                f.close()
            except FileNotFoundError:
                print('file not found')


        elif action.text() == 'open':
            print(f'open')
            fname = QFileDialog.getOpenFileName(self)[0]

            try:
                f = open(fname,'r')
                with f:
                    data = f.read()
                    self.text_edit.setText(data)
                f.close()
            except FileNotFoundError:
                print('file not found')
        elif action.text() == 'show_all':
            print('show_all')
            info = display_all_cells()
            self.text_edit.setText(info)



def application():
    app = QApplication(sys.argv)
    window = Window()

    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    application()