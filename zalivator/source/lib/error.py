# -*- coding: utf8 -*-

import sys
import traceback
from PyQt4 import QtCore, QtGui

# ======================================================================
class Error():

    error_text = 'Произошла фатальная ошибка. Передайте разработчику следующие данные:'

    def __init__(self, error):
        self._error = str(self.error_text) + '\r\n\r\n' + str(error) + '\r\n' + \
            ''.join(traceback.format_stack())

    def display(self):

        self.window = QtGui.QWidget()
        self.window.setGeometry(QtCore.QRect(100, 100, 400, 200))

        self.layout = QtGui.QVBoxLayout()
        self.window.setLayout(self.layout)

        label = QtGui.QLabel(self.utf(self._error), self.window)
        label.setTextInteractionFlags(QtCore.Qt.TextBrowserInteraction)

        self.layout.addWidget(label)

        self.window.show()

        return self

    def utf(self, string):
        return QtCore.QObject.trUtf8(self.window, string)


