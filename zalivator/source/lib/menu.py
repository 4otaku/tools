# -*- coding: utf8 -*-

from PyQt4 import QtCore, QtGui

# ======================================================================
class Menu():

  def __init__(self, app):
    try:
      window = app.get_window()

      menubar = QtGui.QMenuBar(window)
      menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
      menubar.setObjectName("menubar")

      menu_upload = QtGui.QMenu(menubar)
      menu_upload.setObjectName("menu_upload")
      window.setMenuBar(menubar)

#      actionupdateall = QtGui.QAction(window)
#      actionupdateall.setObjectName("actionupdateall")
#      actionupdateall.setText("Whee")

#      menu_upload.addSeparator()
#      menu_upload.addAction(actionupdateall)
      menubar.addAction(menu_upload.menuAction())

      menu_upload.setTitle(app.utf('Залить'))
    except Exception as E:
      print E
