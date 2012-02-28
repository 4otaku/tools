# -*- coding: utf8 -*-

from PyQt4 import QtCore, QtGui
from lib.abstract import Abstract
from lib.error import Error

# ======================================================================
class Action_Abstract(Abstract):

    text = ''
    tip = ''

    def __init__(self, app, menu):
        Abstract.__init__(self, app)

        try:
            self._action = self.build_action()
            menu.addAction(self._action)

        except Exception as E:
            Error(E).display()

    def build_action(self):
        action = QtGui.QAction(self.get_window())
        action.setText(self.utf(self.text))

        if len(self.tip) > 0:
            action.setStatusTip(self.utf(self.tip))

        action.triggered.connect(self.execute)
        return action

    def execute(self):
        pass
