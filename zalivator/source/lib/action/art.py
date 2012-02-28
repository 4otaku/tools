# -*- coding: utf8 -*-

from lib.action.abstract import Action_Abstract

# ======================================================================
class Action_Art(Action_Abstract):

    object_name = 'Action_Art'
    text = 'Арт'

    def __init__(self, app, menu):
        Action_Abstract.__init__(self, app, menu)
