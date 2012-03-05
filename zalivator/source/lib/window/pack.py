# -*- coding: utf8 -*-

from lib.window.abstract import Window_Abstract
from PyQt4 import QtCore, QtGui

# ======================================================================
class Window_Pack(Window_Abstract):

    def __init__(self, app):
        Window_Abstract.__init__(self, app)

        layout = QtGui.QHBoxLayout()

        self._button = QtGui.QGroupBox(self.get_box())
        self._button.setGeometry(0, 0, 600, 40)
        self._button.setLayout(layout)

        button = QtGui.QPushButton(self.utf("Выберите файл"), self._button)
        button.setGeometry(0, 0, 100, 40)
        button.clicked.connect(self.select_file)

        layout.addWidget(button)

        self._label = QtGui.QLabel('', self._button)
        self._label.setGeometry(100, 0, 600, 40)
        self._label.setTextInteractionFlags(QtCore.Qt.TextBrowserInteraction)

        self.get_layout().addWidget(self._button)

        self._title = QtGui.QLineEdit(QtCore.QString(self.utf('Введите заголовок')), self.get_box())
        self.get_layout().addWidget(self._title)

        self._text = QtGui.QTextEdit(QtCore.QString(self.utf('Введите описание')), self.get_box())
        self.get_layout().addWidget(self._text)

        self._send = QtGui.QPushButton(self.utf("Отправить"), self.get_box())
        self._send.clicked.connect(self.send_file)
        self.get_layout().addWidget(self._send)

    def select_file(self, data):
        self._file_dialog = QtGui.QFileDialog(self.get_window())
        self._file_dialog.show()
#        lineEdit.setText(QFileDialog.getOpenFileName())

    def send_file(self, data):
        self._file_dialog = QtGui.QFileDialog(self.get_window())
        self._file_dialog.show()
