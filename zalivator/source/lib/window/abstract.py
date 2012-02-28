# -*- coding: utf8 -*-

from PyQt4 import QtCore, QtGui
from lib.abstract import Abstract
from lib.error import Error

# ======================================================================
class Window_Abstract(Abstract):

    def __init__(self, app):
        Abstract.__init__(self, app)

        try:
            pass
        except Exception as E:
            Error(E).display()
