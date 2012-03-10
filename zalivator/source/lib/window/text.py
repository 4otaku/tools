# -*- coding: utf8 -*-

from lib.window.abstract import Window_Abstract
from PyQt4 import QtCore, QtGui

# ======================================================================
class Window_Text(Window_Abstract):

    text = ''

    def __init__(self, app):
        Window_Abstract.__init__(self, app)

        self._text = QtGui.QTextBrowser(self.get_box())
        self._text.setHtml(self.utf(self.text))
        self._text.setOpenExternalLinks(True)
        self._text.setFrameStyle(QtGui.QFrame.NoFrame)
        self._text.setWordWrapMode(QtGui.QTextOption.WrapAtWordBoundaryOrAnywhere)
        self._text.setReadOnly(True)

        self.get_layout().addWidget(self._text)
