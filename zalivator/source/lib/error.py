# -*- coding: utf8 -*-

import sys
from PyQt4 import QtCore, QtGui

# ======================================================================
class Error():

    def __init__(self, error):
        self._error = error

    def display(self):

        self.window = QtGui.QWidget()
        self.window.setGeometry(QtCore.QRect(100, 100, 400, 200))

        self.layout = QtGui.QVBoxLayout()
        self.window.setLayout(self.layout)

        label = QtGui.QLabel(self.utf(self._error), self.window)
        label.setTextInteractionFlags(QtCore.Qt.TextBrowserInteraction)

        self.layout.addWidget(label)

        self.window.show()
        self.window.exec_()

    def utf(self, string):
        return QtCore.QObject.trUtf8(self.window, string)


