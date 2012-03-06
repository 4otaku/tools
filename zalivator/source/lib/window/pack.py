# -*- coding: utf8 -*-

from lib.window.abstract import Window_Abstract
from PyQt4 import QtCore, QtGui

# ======================================================================
class Window_Pack(Window_Abstract):

    def __init__(self, app):
        Window_Abstract.__init__(self, app)

        layout = QtGui.QHBoxLayout()

        self._button = QtGui.QGroupBox(self.get_box())
        self._button.setLayout(layout)

        button = QtGui.QPushButton(self.utf("Выберите файл"), self._button)
        button.clicked.connect(self.select_file)

        layout.addWidget(button)

        self._label = QtGui.QLabel(self.utf("Файл не выбран"), self._button)
        self._label.setTextInteractionFlags(QtCore.Qt.TextBrowserInteraction)

        layout.addWidget(self._label)

        self.get_layout().addWidget(self._button)

        self._title = QtGui.QLineEdit(QtCore.QString(self.utf('Введите заголовок')), self.get_box())
        self.get_layout().addWidget(self._title)

        self._text = QtGui.QTextEdit(QtCore.QString(self.utf('Введите описание')), self.get_box())
        self.get_layout().addWidget(self._text)

        self._send = QtGui.QPushButton(self.utf("Отправить"), self.get_box())
        self._send.clicked.connect(self.send_file)
        self.get_layout().addWidget(self._send)

    def select_file(self, data):
        file_name = QtGui.QFileDialog.getOpenFileName(None, self.utf("Выберите архив"),
            "", self.utf("Архив в формате zip(*.zip)"))
        if file_name.length():
            if file_name.length() > 55:
                file_name = file_name.left(20) + QtCore.QString(".....") + file_name.right(30)

            self._label.setText(file_name)

    def send_file(self, data):
        self._file_dialog = QtGui.QFileDialog(self.get_window())
        self._file_dialog.show()
