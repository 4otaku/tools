# -*- coding: utf8 -*-
# License avaiavle at zalivator_license.txt in "licenses" directory

from PyQt4 import QtCore, QtGui
from lib.abstract import Abstract
from lib.action.cg_pack import Action_Pack
from lib.action.quit import Action_Quit
from lib.action.about import Action_About
from lib.action.help import Action_Help

# ======================================================================
class Menu(Abstract):

    actions = {}

    def __init__(self, app):
        Abstract.__init__(self, app)

        window = self.get_app().get_window()

        menubar = QtGui.QMenuBar(window)
        menubar.setGeometry(QtCore.QRect(0, 0, 800, 24))
        menubar.setObjectName("menubar")

        menu_upload = QtGui.QMenu(menubar)
        menu_upload.setObjectName("menu_upload")

    #            self.actions['art'] = Action_Art(app, menu_upload)
        self.actions['cg_pack'] = Action_Pack(app, menu_upload)
    #            self.actions['post'] = post.Action_Post(app, menu_upload)
        self.actions['quit'] = Action_Quit(app, menu_upload)

        menu_upload.setTitle(self.utf('Залить'))
        menubar.addAction(menu_upload.menuAction())

        menu_about = QtGui.QMenu(menubar)
        menu_about.setObjectName("menu_upload")

        self.actions['about'] = Action_About(app, menu_about)
        self.actions['help'] = Action_Help(app, menu_about)

        menu_about.setTitle(self.utf('Помощь'))
        menubar.addAction(menu_about.menuAction())

        window.setMenuBar(menubar)
