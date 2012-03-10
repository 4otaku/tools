# -*- coding: utf8 -*-
# License avaiavle at zalivator_license.txt in "licenses" directory

from lib.action.abstract import Action_Abstract
from PyQt4 import QtGui

# ======================================================================
class Action_Quit(Action_Abstract):

    text = 'Выйти'
    tip = ''

    def __init__(self, app, menu):
        Action_Abstract.__init__(self, app, menu)

    def execute(self):
        QtGui.qApp.quit()
