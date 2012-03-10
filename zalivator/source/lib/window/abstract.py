# -*- coding: utf8 -*-

from PyQt4 import QtCore, QtGui
from lib.abstract import Abstract

# ======================================================================
class Window_Abstract(Abstract):

    def __init__(self, app):
        Abstract.__init__(self, app)

        widget = self.get_window().centralWidget()
        if widget:
            widget.close()

        self._layout = QtGui.QVBoxLayout()

        self._box = QtGui.QGroupBox(self.get_window())
        self._box.setGeometry(0, 0, 600, 480)
        self._box.setLayout(self._layout)

        self.get_window().setCentralWidget(self._box)

    def get_box(self):
        return self._box

    def get_layout(self):
        return self._layout
