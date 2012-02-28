# -*- coding: utf8 -*-

# ======================================================================
class Error():

  def __init__(self, error):
    self._error = error

  def display(self):
    print self._error
