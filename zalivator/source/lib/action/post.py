# -*- coding: utf8 -*-

from lib.action.abstract import Action_Abstract

# ======================================================================
class Action_Post(Action_Abstract):

    text = 'Запись'
    tip = ''

    def __init__(self, app, menu):
        Action_Abstract.__init__(self, app, menu)

    def execute(self):
        self.get_app().set_mode('post')
