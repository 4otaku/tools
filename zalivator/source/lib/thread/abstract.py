# -*- coding: utf8 -*-
# License avaiavle at zalivator_license.txt in "licenses" directory

from PyQt4 import QtCore, QtGui

# ======================================================================
class Thread_Abstract(QtCore.QThread):

    def __init__(self, parent = None):
        QtCore.QThread.__init__(self, parent)

    def run(self):
        pass
