# -*- coding: utf8 -*-

# ======================================================================
class Abstract():

    def __init__(self, app):
         self._app = app

    def get_app(self):
         return self._app

    def get_window(self):
         return self.get_app().get_window()

    def utf(self, string):
        return self.get_app().utf(string)
