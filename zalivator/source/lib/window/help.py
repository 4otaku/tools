# -*- coding: utf8 -*-
# License avaiavle at zalivator_license.txt in "licenses" directory

from lib.window.text import Window_Text
from PyQt4 import QtCore, QtGui
import os, sys

# ======================================================================
class Window_Help(Window_Text):

    text = 'Последняя версия справки доступна по адресу: ' + \
        '<a href="http://wiki.4otaku.ru/Zalivator">http://wiki.4otaku.ru/Zalivator</a>.'

    def __init__(self, app):
        Window_Text.__init__(self, app)

        self._help = QtGui.QTextBrowser(self.get_box())

        path = os.path.abspath(os.path.dirname(sys.argv[0]))

        f = open(path + os.sep + 'help.txt', 'r')
        data = f.read()
        f.close()

        self._help.setHtml(self.utf(data))

        self._help.setOpenExternalLinks(True)
        self._help.setFrameStyle(QtGui.QFrame.NoFrame)
        self._help.setWordWrapMode(QtGui.QTextOption.WrapAtWordBoundaryOrAnywhere)
        self._help.setReadOnly(True)

        self.get_layout().addWidget(self._help, 100)
