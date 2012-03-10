# -*- coding: utf8 -*-
# License avaiavle at zalivator_license.txt in "licenses" directory

from PyQt4 import QtCore, QtGui
from lib.window.abstract import Window_Abstract
from lib.thread.file import Thread_File
from lib.thread.send import Thread_Send
from time import sleep

# ======================================================================
class Send_Abstract(Window_Abstract):

    bars = {}
    data = {}
    inited_bars = {}

    _domain = 'http://4otaku.ru'
    _url = ''

    def __init__(self, app, data):
        Window_Abstract.__init__(self, app)

        for key, bar in self.bars.iteritems():
            self.init_bar(key, bar)

        label = QtGui.QLabel(self.utf('Результат:'), self.get_box())
        label.setTextInteractionFlags(QtCore.Qt.TextBrowserInteraction)
        self.get_layout().addWidget(label)

        self._result_box = QtGui.QTextEdit('', self.get_box())
        self._result_box.setReadOnly(True)
        self.get_layout().addWidget(self._result_box)

        self.data = data

        self.process_request()

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
        self.get_box().connect(self.parser, QtCore.SIGNAL("progress"), self.on_file_parse)
        self.get_box().connect(self.parser, QtCore.SIGNAL("finished"), self.on_file_finish)
        self.get_box().connect(self.parser, QtCore.SIGNAL("error"), self.trigger_error)
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

    def send(self, bar):
        self.sender = Thread_Send(self.send_data, self._domain + self._url, self.get_box())
        self.active_bar = bar
        self.get_box().connect(self.sender, QtCore.SIGNAL("progress"), self.on_send_progress)
        self.get_box().connect(self.sender, QtCore.SIGNAL("finished"), self.on_send_finish)
        self.get_box().connect(self.sender, QtCore.SIGNAL("error"), self.trigger_error)

        bar['bar'].setValue(5)

        self.sender.start()

    def on_send_progress(self, count):
        self.active_bar['bar'].setValue(count)

    def on_send_finish(self, data):
        self.active_bar['ready'] = True
        self.active_bar['bar'].setValue(100)

    def trigger_error(self):
        self.get_app().trigger_error()

    def translate_error_code(self, code):
        if code == 420 or code == 430:
            return 'Некорректные данные.'

        if code == 30:
            return 'CG-пак с таким названием уже добавлен.'

        if code == 10:
            return 'Выбранный вами файл превышает 125 мегабайт.'
