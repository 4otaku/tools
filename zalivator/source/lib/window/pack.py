# -*- coding: utf8 -*-

from lib.window.abstract import Window_Abstract
from PyQt4 import QtCore, QtGui

# ======================================================================
class Window_Pack(Window_Abstract):

    stateIndex = 2

    def __init__(self, app):
        Window_Abstract.__init__(self, app)

        self._button = QtGui.QPushButton("Выберите файл", self.get_window())
        self._button.show()

#        self.fileDialog = QtGui.QFileDialog(self.get_window())
#        self.fileDialog.show()

    def select_file():
        lineEdit.setText(QFileDialog.getOpenFileName())
