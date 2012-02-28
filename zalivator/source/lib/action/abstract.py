# -*- coding: utf8 -*-

from PyQt4 import QtCore, QtGui
from lib.abstract import Abstract
from lib.error import Error

# ======================================================================
class Action_Abstract(Abstract):

    object_name = ''
    text = ''

    def __init__(self, app, menu):
        Abstract.__init__(self, app)

        try:
            self._action = self.build_action()
            menu.addAction(self._action)

        except Exception as E:
            Error(E).display()

    def build_action(self):
        action = QtGui.QAction(self.get_window())
        action.setObjectName(self.object_name)
        action.setText(self.utf(self.text))
        return action
