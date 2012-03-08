# -*- coding: utf8 -*-

from lib.send.abstract import Send_Abstract
from PyQt4 import QtCore, QtGui

# ======================================================================
class Send_Pack(Send_Abstract):

    bars = {
        'file': 'Подготавливаю архив',
        'send': 'Отсылаю запрос'
    }
