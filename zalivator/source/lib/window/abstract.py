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
        except Exception as E:
            Error(E).display()
