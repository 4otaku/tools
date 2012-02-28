# -*- coding: utf8 -*-

from lib.action.abstract import Action_Abstract

# ======================================================================
class Action_About(Action_Abstract):

    text = 'О программе'
    tip = ''

    def __init__(self, app, menu):
        Action_Abstract.__init__(self, app, menu)
