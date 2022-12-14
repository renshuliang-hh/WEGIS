# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DatabasemMainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DataBaseMainWindow(object):
    def setupUi(self, DataBaseMainWindow):
        DataBaseMainWindow.setObjectName("DataBaseMainWindow")
        DataBaseMainWindow.resize(878, 599)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("postgis.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        DataBaseMainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(DataBaseMainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.connectButton = QtWidgets.QPushButton(self.centralwidget)
        self.connectButton.setGeometry(QtCore.QRect(30, 120, 121, 51))
        self.connectButton.setObjectName("connectButton")
        self.newdbButton = QtWidgets.QPushButton(self.centralwidget)
        self.newdbButton.setGeometry(QtCore.QRect(30, 40, 121, 51))
        self.newdbButton.setObjectName("newdbButton")
        self.browseButton = QtWidgets.QPushButton(self.centralwidget)
        self.browseButton.setGeometry(QtCore.QRect(30, 290, 121, 51))
        self.browseButton.setObjectName("browseButton")
        self.deleteButton = QtWidgets.QPushButton(self.centralwidget)
        self.deleteButton.setGeometry(QtCore.QRect(30, 410, 121, 51))
        self.deleteButton.setObjectName("deleteButton")
        self.layer2proButton = QtWidgets.QPushButton(self.centralwidget)
        self.layer2proButton.setGeometry(QtCore.QRect(590, 500, 181, 51))
        self.layer2proButton.setObjectName("layer2proButton")
        self.layer2fileButton = QtWidgets.QPushButton(self.centralwidget)
        self.layer2fileButton.setGeometry(QtCore.QRect(240, 500, 181, 51))
        self.layer2fileButton.setObjectName("layer2fileButton")
        self.newlayerButton = QtWidgets.QPushButton(self.centralwidget)
        self.newlayerButton.setGeometry(QtCore.QRect(30, 350, 121, 51))
        self.newlayerButton.setObjectName("newlayerButton")
        self.removebdButton = QtWidgets.QPushButton(self.centralwidget)
        self.removebdButton.setGeometry(QtCore.QRect(30, 190, 121, 51))
        self.removebdButton.setObjectName("removebdButton")
        self.dbtableView = QtWidgets.QTableView(self.centralwidget)
        self.dbtableView.setGeometry(QtCore.QRect(180, 40, 681, 431))
        self.dbtableView.setObjectName("dbtableView")
        DataBaseMainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(DataBaseMainWindow)
        self.statusbar.setObjectName("statusbar")
        DataBaseMainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(DataBaseMainWindow)
        QtCore.QMetaObject.connectSlotsByName(DataBaseMainWindow)

    def retranslateUi(self, DataBaseMainWindow):
        _translate = QtCore.QCoreApplication.translate
        DataBaseMainWindow.setWindowTitle(_translate("DataBaseMainWindow", "Database Operation"))
        self.connectButton.setText(_translate("DataBaseMainWindow", "Connect Database"))
        self.newdbButton.setText(_translate("DataBaseMainWindow", "New Database"))
        self.browseButton.setText(_translate("DataBaseMainWindow", " Browse Data"))
        self.deleteButton.setText(_translate("DataBaseMainWindow", "Delete Layer"))
        self.layer2proButton.setText(_translate("DataBaseMainWindow", "Add Layer to project"))
        self.layer2fileButton.setText(_translate("DataBaseMainWindow", "Export Layer to file"))
        self.newlayerButton.setText(_translate("DataBaseMainWindow", "New Layer"))
        self.removebdButton.setText(_translate("DataBaseMainWindow", "Remove Connection"))
