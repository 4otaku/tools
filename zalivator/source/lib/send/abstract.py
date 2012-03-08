# -*- coding: utf8 -*-

from PyQt4 import QtCore, QtGui
from lib.window.abstract import Window_Abstract
from lib.error import Error

# ======================================================================
class Send_Abstract(Window_Abstract):

    bars = {}
    inited_bars = {}

    def __init__(self, app):
        Window_Abstract.__init__(self, app)

        try:
            for key, bar in self.bars.iteritems():
                print key
                print bar
                self.init_bar(key, bar)

        except Exception as E:
            Error(E).display()

    def init_bar(self, key, config):
        bar = QtGui.QProgressBar(self.get_box())
        bar.setMinimum(0)
        bar.setMaximum(100)
        for a in range(100):
            sleep(1)
            bar.setValue(a)
