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
        try:
            size = stat(self.filename).st_size
            block_count = int(ceil(size / 1023))

            ret = ''
            f = open(self.filename)
            i = 0
            while True:
                data = f.read(1023)
                if len(data) == 0:
                    break

                i += 1
                data = b64encode(data)
                ret += data
                self.emit(QtCore.SIGNAL("progress"), round(i * 100 / block_count))

            self.emit(QtCore.SIGNAL("finished"), ret)

        except Exception as E:
            self.emit(QtCore.SIGNAL("error"))
