# -*- coding: utf8 -*-

from lib.window.abstract import Window_Abstract
from PyQt4 import QtCore, QtGui

# ======================================================================
class Window_Default(Window_Abstract):

    welcome_text = 'Добро пожаловать в заливтор чотаку. <br />' + \
        'Для начала работы выберите один из пунктов в меню "Залить".'

    def __init__(self, app):
        Window_Abstract.__init__(self, app)

        self._text = QtGui.QLabel(self.utf(self.welcome_text), self.get_window())
        self._text.setGeometry(0, 0, 600, 400)
        self._text.setTextInteractionFlags(QtCore.Qt.TextBrowserInteraction)
        self._text.setAlignment(QtCore.Qt.AlignCenter)
