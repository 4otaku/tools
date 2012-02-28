# -*- coding: utf8 -*-

from lib.action.abstract import Action_Abstract

# ======================================================================
class Action_Art(Action_Abstract):

    text = 'Арт'
    tip = ''

    def __init__(self, app, menu):
        Action_Abstract.__init__(self, app, menu)

    def execute(self):
        self.get_app().set_mode('art')
