# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_ui.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(988, 737)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 60, 169, 31))
        self.label.setMaximumSize(QtCore.QSize(169, 91))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 10, 169, 31))
        self.label_2.setMaximumSize(QtCore.QSize(169, 91))
        self.label_2.setObjectName("label_2")
        self.outputDirLabel = QtWidgets.QLabel(self.centralwidget)
        self.outputDirLabel.setGeometry(QtCore.QRect(20, 110, 169, 31))
        self.outputDirLabel.setMaximumSize(QtCore.QSize(169, 91))
        self.outputDirLabel.setObjectName("outputDirLabel")
        self.resamplingAlgorithms = QtWidgets.QComboBox(self.centralwidget)
        self.resamplingAlgorithms.setEnabled(False)
        self.resamplingAlgorithms.setGeometry(QtCore.QRect(200, 60, 211, 31))
        self.resamplingAlgorithms.setObjectName("resamplingAlgorithms")
        self.datasetButton = QtWidgets.QPushButton(self.centralwidget)
        self.datasetButton.setGeometry(QtCore.QRect(200, 10, 121, 34))
        self.datasetButton.setObjectName("datasetButton")
        self.outputDirectoryButton = QtWidgets.QPushButton(self.centralwidget)
        self.outputDirectoryButton.setEnabled(False)
        self.outputDirectoryButton.setGeometry(QtCore.QRect(200, 110, 121, 34))
        self.outputDirectoryButton.setObjectName("outputDirectoryButton")
        self.datasetPickedLabel = QtWidgets.QLabel(self.centralwidget)
        self.datasetPickedLabel.setGeometry(QtCore.QRect(440, 10, 531, 31))
        self.datasetPickedLabel.setText("")
        self.datasetPickedLabel.setObjectName("datasetPickedLabel")
        self.outputDirectoryPickedLabel = QtWidgets.QLabel(self.centralwidget)
        self.outputDirectoryPickedLabel.setGeometry(QtCore.QRect(440, 110, 531, 31))
        self.outputDirectoryPickedLabel.setText("")
        self.outputDirectoryPickedLabel.setObjectName("outputDirectoryPickedLabel")
        self.startButton = QtWidgets.QPushButton(self.centralwidget)
        self.startButton.setEnabled(False)
        self.startButton.setGeometry(QtCore.QRect(20, 170, 112, 34))
        self.startButton.setObjectName("startButton")
        self.datasetProgressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.datasetProgressBar.setGeometry(QtCore.QRect(330, 12, 101, 31))
        self.datasetProgressBar.setMaximum(336)
        self.datasetProgressBar.setProperty("value", 0)
        self.datasetProgressBar.setObjectName("datasetProgressBar")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 988, 21))
        self.menubar.setObjectName("menubar")
        self.menuAsd = QtWidgets.QMenu(self.menubar)
        self.menuAsd.setObjectName("menuAsd")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionQqq = QtWidgets.QAction(MainWindow)
        self.actionQqq.setObjectName("actionQqq")
        self.menuAsd.addSeparator()
        self.menuAsd.addSeparator()
        self.menuAsd.addAction(self.actionQqq)
        self.menubar.addAction(self.menuAsd.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Resampling Algorithm:"))
        self.label_2.setToolTip(_translate("MainWindow", "Only csv datasets are acceptable!"))
        self.label_2.setText(_translate("MainWindow", "Dataset:"))
        self.outputDirLabel.setText(_translate("MainWindow", "Output directory:"))
        self.datasetButton.setText(_translate("MainWindow", "Choose..."))
        self.outputDirectoryButton.setText(_translate("MainWindow", "Choose..."))
        self.startButton.setText(_translate("MainWindow", "Start"))
        self.menuAsd.setTitle(_translate("MainWindow", "File"))
        self.actionQqq.setText(_translate("MainWindow", "Test"))

