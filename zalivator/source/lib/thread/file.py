# -*- coding: utf8 -*-

from lib.thread.abstract import Thread_Abstract
from PyQt4 import QtCore, QtGui

# ======================================================================
class Thread_File(Thread_Abstract):

    def __init__(self, parent = None):
        Thread_Abstract.__init__(self, parent)
