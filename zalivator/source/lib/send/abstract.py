# -*- coding: utf8 -*-

from PyQt4 import QtCore, QtGui
from lib.window.abstract import Window_Abstract
from lib.error import Error
from time import sleep

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
        bar.setValue(0)

        self.inited_bars.key = bar

    def get_bar(self, key):
        return self.inited_bars.key
