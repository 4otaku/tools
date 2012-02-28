# -*- coding: utf8 -*-

import sys
from PyQt4 import QtCore, QtGui
from lib.menu import Menu
from lib.error import Error

# ======================================================================
class App():

    def __init__(self):
        try:
            self._qt_app = QtGui.QApplication(sys.argv)
            self._window = QtGui.QMainWindow()

            Menu(self)
        except Exception as E:
            Error(E).display()

    def execute(self):
        try:
            self.get_window().show()
            self.get_qt_app().exec_()
        except Exception as E:
            Error(E).display()

    def get_window(self):
        return self._window

    def get_qt_app(self):
        return self._qt_app

    def utf(self, string):
        return QtCore.QObject.trUtf8(self.get_window(), string)
