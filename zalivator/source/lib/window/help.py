# -*- coding: utf8 -*-

from lib.window.text import Window_Text

# ======================================================================
class Window_Help(Window_Text):

    text = 'Добро пожаловать в заливтор чотаку. <br />' + \
        'Для начала работы выберите один из пунктов в меню "Залить".'

    def __init__(self, app):
        Window_Text.__init__(self, app)
