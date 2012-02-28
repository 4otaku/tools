# -*- coding: utf8 -*-

from lib.action.abstract import Action_Abstract

# ======================================================================
class Action_Quit(Action_Abstract):

    object_name = 'Action_Quit'
    text = 'Выйти'

    def __init__(self, app, menu):
        Action_Abstract.__init__(self, app, menu)
