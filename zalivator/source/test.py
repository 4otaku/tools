import sys
from PyQt4 import QtCore, QtGui

app = QtGui.QApplication(sys.argv)

MainWindow = QtGui.QMainWindow()
menubar = QtGui.QMenuBar(MainWindow)
menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
menubar.setObjectName("menubar")

menuFile = QtGui.QMenu(menubar)
menuFile.setObjectName("menuFile")
MainWindow.setMenuBar(menubar)

actionupdateall = QtGui.QAction(MainWindow)
actionupdateall.setObjectName("actionupdateall")
actionupdateall.setText("Whee")

menuFile.addSeparator()
menuFile.addAction(actionupdateall)
menubar.addAction(menuFile.menuAction())

menuFile.setTitle(QtGui.QApplication.translate("MainWindow", "File", None, QtGui.QApplication.UnicodeUTF8))

button = QtGui.QPushButton("Hello World", MainWindow)
button.show()

MainWindow.show()

sys.exit(app.exec_())
