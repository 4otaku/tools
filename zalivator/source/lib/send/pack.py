# -*- coding: utf8 -*-

from lib.send.abstract import Send_Abstract
from PyQt4 import QtCore, QtGui

# ======================================================================
class Send_Pack(Send_Abstract):

    bars = {
        'send': 'Отсылаю запрос',
        'file': 'Подготавливаю архив'
    }

    def process_request(self):
        data = {}

        data['title'] = self.data['title']
        data['text'] = self.data['text']

        data['file'] = self.prepare_file(self.data['filename'], self.get_bar('file'))
