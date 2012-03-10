# -*- coding: utf8 -*-

from PyQt4 import QtCore, QtGui

# ======================================================================
class Thread_Abstract(QtCore.QThread):

    def __init__(self, parent = None):
        QtCore.QThread.__init__(self, parent)

    def run(self):
        pass
