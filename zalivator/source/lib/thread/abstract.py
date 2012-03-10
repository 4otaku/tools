# -*- coding: utf8 -*-

from PyQt4 import QtCore, QtGui
from lib.error import Error

# ======================================================================
class Thread_Abstract(QtCore.QThread):

    def __init__(self, parent = None):
        QtCore.QThread.__init__(self, parent)

    def run(self):
        pass
