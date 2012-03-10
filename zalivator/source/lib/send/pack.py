# -*- coding: utf8 -*-

from lib.send.abstract import Send_Abstract
from PyQt4 import QtCore, QtGui

# ======================================================================
class Send_Pack(Send_Abstract):

    bars = {
        'send': 'Отсылаю запрос',
        'file': 'Подготавливаю архив'
    }
    _url = '/api/create/art/pack'

    def process_request(self):
        self.send_data = {}

        self.send_data['title'] = self.data['title']
        self.send_data['text'] = self.data['text']

        self.prepare_file(self.data['filename'], self.get_bar('file'))

    def on_file_finish(self, data):
        self.send_data['archive'] = data
        Send_Abstract.on_file_finish(self, data)

    def test_send_ready(self):
        return self.get_bar('file')['ready']

    def start_send(self):
        self.send(self.get_bar('send'))

    def on_send_finish(self, data):
        print data
