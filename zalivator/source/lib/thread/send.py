# -*- coding: utf8 -*-
# License avaiavle at zalivator_license.txt in "licenses" directory

from lib.thread.abstract import Thread_Abstract
from lib.util.file_callback import Util_File_Callback
from PyQt4 import QtCore, QtGui
import urllib2, urllib
import json

# ======================================================================
class Thread_Send(Thread_Abstract):

    def __init__(self, data, url, parent = None):

        Thread_Abstract.__init__(self, parent)
        self._sent = 0
        self._url = url
        self._data = data

        self._file = QtCore.QTemporaryFile(self)
        self._file.setAutoRemove(True)
        self._file.open()
        self._filename = self._file.fileName()

    def run(self):
        try:
            body = [('format', 'json')]
            for key, value in self._data.iteritems():
                body.append((key, value.encode('UTF-8')))

            f = open(self._filename, 'w')
            body = urllib.urlencode(body).encode('UTF-8')
            total = len(body)
            written = 0
            while len(body) > 0:
                part = body[:1024000]
                f.write(part)
                written += 1024000
                pct = 5 + (written * 25 / total)
                self.emit(QtCore.SIGNAL("progress"), round(pct))
                body = body[1024000:]
            f.close()
            print self._filename

            stream = Util_File_Callback(self._filename, 'rb', self.update, self._filename)
            req = urllib2.Request(self._url, stream)
            res = urllib2.urlopen(req)

            del self._file

            try:
                self.emit(QtCore.SIGNAL("finished"), json.load(res))
            except Exception as E:
                self.emit(QtCore.SIGNAL("finished"), {'success': False, 'large': True})

        except Exception as E:
            self.emit(QtCore.SIGNAL("error"))

    def update(self, total, size, name):
        self._sent += size
        pct = 30 + (self._sent * 70 / total)
        self.emit(QtCore.SIGNAL("progress"), round(pct))
