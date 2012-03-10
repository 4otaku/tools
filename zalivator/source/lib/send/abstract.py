# -*- coding: utf8 -*-

from PyQt4 import QtCore, QtGui
from lib.window.abstract import Window_Abstract
from lib.thread.file import Thread_File
from lib.thread.send import Thread_Send
from lib.error import Error
from time import sleep
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

        self.inited_bars[key] = {'bar': bar, 'ready': False}

    def get_bar(self, key):
        return self.inited_bars[key]

    def process_request(self):
        pass

    def prepare_file(self, filename, bar):
        self.parser = Thread_File(filename, self.get_box())
        self.active_bar = bar
        self.get_box().connect(self.parser, QtCore.SIGNAL("parsed"), self.on_file_parse)
        self.get_box().connect(self.parser, QtCore.SIGNAL("finished"), self.on_file_finish)
        self.parser.start()

    def on_file_parse(self, count):
        self.active_bar['bar'].setValue(count)

    def on_file_finish(self, data):
        self.active_bar['ready'] = True
        self.active_bar['bar'].setValue(100)
        if self.test_send_ready():
            self.start_send()

    def test_send_ready(self):
        return True

    def start_send(self):
        pass
