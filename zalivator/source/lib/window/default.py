# -*- coding: utf8 -*-

from lib.window.text import Window_Text
from PyQt4 import QtCore, QtGui

# ======================================================================
class Window_Default(Window_Text):

    text = '<br /><br /><br /><br /><br /><br />' + \
        'Добро пожаловать в заливатор для 4отаку. <br />' + \
        'Для начала работы выберите один из пунктов в меню "Залить".'

    def __init__(self, app):
        Window_Text.__init__(self, app)

        self._text.setAlignment(QtCore.Qt.AlignCenter)
