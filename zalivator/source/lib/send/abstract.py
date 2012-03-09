# -*- coding: utf8 -*-

from PyQt4 import QtCore, QtGui
from lib.window.abstract import Window_Abstract
from lib.error import Error
from time import sleep
from os import stat
from math import ceil
from base64 import b64encode
#import urllib.request
#from urllib.parse import urlencode
#import http.client
#import json

# ======================================================================
class Send_Abstract(Window_Abstract):

    bars = {}
    data = {}
    inited_bars = {}

    def __init__(self, app, data):
        Window_Abstract.__init__(self, app)

        try:
            for key, bar in self.bars.iteritems():
                self.init_bar(key, bar)

            self.data = data

            sleep(0.001)
            self.process_request()

        except Exception as E:
            Error(E).display()

    def init_bar(self, key, config):
        layout = QtGui.QHBoxLayout()

        progress_bar = QtGui.QGroupBox(self.get_box())
        progress_bar.setLayout(layout)

        label = QtGui.QLabel(self.utf(config), progress_bar)
        label.setTextInteractionFlags(QtCore.Qt.TextBrowserInteraction)

        layout.addWidget(label)

        bar = QtGui.QProgressBar(progress_bar)
        bar.text = config
        bar.setMinimum(0)
        bar.setMaximum(100)
        bar.setValue(0)

        layout.addWidget(bar)

        self.get_layout().addWidget(progress_bar)

        self.inited_bars[key] = bar

    def get_bar(self, key):
        return self.inited_bars[key]

    def process_request(self):
        pass

    def prepare_file(self, filename, bar):
        size = stat(filename).st_size
        block_count = int(ceil(size / 1023))

        ret = ''
        f = open(filename)
        for i in range(block_count):
            data = f.read(1023)
            data = b64encode(data)
            ret += data
            sleep(1)
            bar.setValue(round(i * 100 / block_count))

        bar.setValue(100)

        return ret
