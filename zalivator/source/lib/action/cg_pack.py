# -*- coding: utf8 -*-

from lib.action.abstract import Action_Abstract

# ======================================================================
class Action_Pack(Action_Abstract):

    text = 'CG пак'
    tip = ''

    def __init__(self, app, menu):
        Action_Abstract.__init__(self, app, menu)
