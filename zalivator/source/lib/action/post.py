# -*- coding: utf8 -*-

from lib.action.abstract import Action_Abstract

# ======================================================================
class Action_Post(Action_Abstract):

    object_name = 'Action_Post'
    text = 'Запись'

    def __init__(self, app, menu):
        Action_Abstract.__init__(self, app, menu)
