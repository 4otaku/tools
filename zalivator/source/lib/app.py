# -*- coding: utf8 -*-
# License avaiavle at zalivator_license.txt in "licenses" directory

import sys
from PyQt4 import QtCore, QtGui
from lib.menu import Menu
from lib.error import Error
from lib.window.default import Window_Default
from lib.window.about import Window_About
from lib.window.help import Window_Help
from lib.window.pack import Window_Pack
from lib.send.pack import Send_Pack

# ======================================================================
class App():

    def __init__(self):
        try:
            self._qt_app = QtGui.QApplication(sys.argv)
            self._window = QtGui.QMainWindow()

            self._window.resize(600, 480)
            self._menu = Menu(self)

        except Exception as E:
            self._window.hide()
            self._error = Error(E).display()

    def execute(self, mode):
        try:
            self.set_mode(mode)
            self.get_window().show()
            self.get_qt_app().exec_()
        except Exception as E:
            self._window.hide()
            self._error = Error(E).display()

    def get_window(self):
        return self._window

    def get_qt_app(self):
        return self._qt_app

    def utf(self, string):
        return QtCore.QObject.trUtf8(self.get_window(), string)

    def set_mode(self, mode):
        try:
            if mode == 'default':
                self._mode_instance = Window_Default(self)
                return

            if mode == 'help':
                self._mode_instance = Window_Help(self)
                return

            if mode == 'about':
                self._mode_instance = Window_About(self)
                return

            if mode == 'pack':
                self._mode_instance = Window_Pack(self)
                return
        except Exception as E:
            self._window.hide()
            self._error = Error(E).display()

    def start_send(self, mode, data):
        try:
            if mode == 'pack':
                self._mode_instance = Send_Pack(self, data)
                return

        except Exception as E:
            self._window.hide()
            self._error = Error(E).display()

    def trigger_error(self):

        self._window.hide()
        self._error = Error(Exception()).display()

