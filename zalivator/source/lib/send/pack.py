# -*- coding: utf8 -*-
# License avaiavle at zalivator_license.txt in "licenses" directory

from lib.send.abstract import Send_Abstract
from PyQt4 import QtCore, QtGui
import os

# ======================================================================
class Send_Pack(Send_Abstract):

    bars = {
        'send': 'Отсылаю запрос',
        'file': 'Подготавливаю архив'
    }
    _url = '/api/create/art/pack'
    _success_text = 'Ваш CG-пак успешно добавлен и появится по адресу ' + \
        '<a href="{0}/art/pack/{1}">{0}/art/pack/{1}</a>, ' + \
        'когда арты будут обработаны. Это может занять до нескольких часов.<br />' + \
        'В общем списке ваш пак появится, когда будет проверен модератором. ' + \
        'Приносим извинения за неудобства'

    def process_request(self):
        self.send_data = {}

        self.send_data['title'] = self.data['title']
        self.send_data['text'] = self.data['text']
        self.send_data['filename'] = os.path.basename(self.data['filename'])

        self.prepare_file(self.data['filename'], self.get_bar('file'))

    def on_file_finish(self, data):
        self.send_data['archive'] = data
        Send_Abstract.on_file_finish(self, data)

    def test_send_ready(self):
        return self.get_bar('file')['ready']

    def start_send(self):
        self.send(self.get_bar('send'))

    def on_send_finish(self, data):
        if data['success']:
            text = self.success_text(data['id'])
        else:
            text = 'Ошибка.<br /><br />'.decode('utf-8') + self.error_text(data)

        self._result_box.setHtml(self.utf(text))

    def success_text(self, item_id):
        return self._success_text.format(self._domain, item_id)

    def error_text(self, data):
        if 'large' in data and data['large']:
            return 'Выбранный вами файл превышает 125 мегабайт.'.decode('utf-8')

        if 'errors' in data:
            error = data['errors'].pop()
            ret = self.translate_error_code(error['code']).decode('utf-8')
            if 'message' in error:
                ret += '<br />'.decode('utf-8') + error['message'].decode('utf-8')
            if 'id' in data:
                ret += '<a href="{0}/art/pack/{1}">{0}/art/pack/{1}</a>'.format(self._domain, data['id'])
            return ret

        return 'Природу ошибки определить не удалось.'.decode('utf-8')
