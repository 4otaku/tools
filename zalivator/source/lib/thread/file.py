# -*- coding: utf8 -*-
# License avaiavle at zalivator_license.txt in "licenses" directory

from lib.thread.abstract import Thread_Abstract
from PyQt4 import QtCore, QtGui
from time import sleep
from os import stat
from math import ceil
from base64 import b64encode

# ======================================================================
class Thread_File(Thread_Abstract):

    def __init__(self, filename, parent = None):
        Thread_Abstract.__init__(self, parent)
        self.filename = filename

    def run(self):
        size = stat(self.filename).st_size
        block_count = int(ceil(size / 1023))

        ret = ''
        f = open(self.filename)
        for i in range(block_count):
            data = f.read(1023)
            data = b64encode(data)
            ret += data
            self.emit(QtCore.SIGNAL("progress"), round(i * 100 / block_count))

        self.emit(QtCore.SIGNAL("finished"), ret)
