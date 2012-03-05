# -*- coding: utf8 -*-

from PyQt4 import QtCore, QtGui
from lib.abstract import Abstract
from lib.error import Error

# ======================================================================
class Window_Abstract(Abstract):

    def __init__(self, app):
        Abstract.__init__(self, app)

        try:
            widget = self.get_window().centralWidget()
            if widget:
                widget.close()

            self._box = QtGui.QGroupBox(self.get_window())
            self._box.setGeometry(0, 0, 600, 480)
            self.get_window().setCentralWidget(self._box)
        except Exception as E:
            Error(E).display()

    def get_box(self):
        return self._box
