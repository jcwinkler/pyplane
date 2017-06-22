# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui/Ui_PyPlane.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_pyplane(object):
    def setupUi(self, pyplane):
        pyplane.setObjectName("pyplane")
        pyplane.resize(770, 757)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(pyplane.sizePolicy().hasHeightForWidth())
        pyplane.setSizePolicy(sizePolicy)
        pyplane.setMinimumSize(QtCore.QSize(770, 757))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/pyplane_logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        pyplane.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(pyplane)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.full = QtWidgets.QVBoxLayout()
        self.full.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.full.setSpacing(1)
        self.full.setObjectName("full")
        self.inputBox = QtWidgets.QHBoxLayout()
        self.inputBox.setObjectName("inputBox")
        self.syst = QtWidgets.QVBoxLayout()
        self.syst.setObjectName("syst")
        self.title = QtWidgets.QLabel(self.centralwidget)
        self.title.setObjectName("title")
        self.syst.addWidget(self.title)
        self.xDotBox = QtWidgets.QHBoxLayout()
        self.xDotBox.setObjectName("xDotBox")
        self.xDotLabel = QtWidgets.QLabel(self.centralwidget)
        self.xDotLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.xDotLabel.setObjectName("xDotLabel")
        self.xDotBox.addWidget(self.xDotLabel)
        self.xDotLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.xDotLineEdit.setObjectName("xDotLineEdit")
        self.xDotBox.addWidget(self.xDotLineEdit)
        self.submitButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.submitButton.sizePolicy().hasHeightForWidth())
        self.submitButton.setSizePolicy(sizePolicy)
        self.submitButton.setMinimumSize(QtCore.QSize(0, 0))
        self.submitButton.setMaximumSize(QtCore.QSize(100, 16777215))
        self.submitButton.setObjectName("submitButton")
        self.xDotBox.addWidget(self.submitButton)
        self.syst.addLayout(self.xDotBox)
        self.yDotBox = QtWidgets.QHBoxLayout()
        self.yDotBox.setObjectName("yDotBox")
        self.yDotLabel = QtWidgets.QLabel(self.centralwidget)
        self.yDotLabel.setObjectName("yDotLabel")
        self.yDotBox.addWidget(self.yDotLabel)
        self.yDotLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.yDotLineEdit.setObjectName("yDotLineEdit")
        self.yDotBox.addWidget(self.yDotLineEdit)
        self.clearButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.clearButton.sizePolicy().hasHeightForWidth())
        self.clearButton.setSizePolicy(sizePolicy)
        self.clearButton.setMinimumSize(QtCore.QSize(0, 0))
        self.clearButton.setMaximumSize(QtCore.QSize(100, 16777215))
        self.clearButton.setObjectName("clearButton")
        self.yDotBox.addWidget(self.clearButton)
        self.syst.addLayout(self.yDotBox)
        self.inputBox.addLayout(self.syst)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.inputBox.addWidget(self.line)
        self.funcBox = QtWidgets.QVBoxLayout()
        self.funcBox.setObjectName("funcBox")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.funcBox.addWidget(self.label)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.yLabel = QtWidgets.QLabel(self.centralwidget)
        self.yLabel.setObjectName("yLabel")
        self.horizontalLayout_6.addWidget(self.yLabel)
        self.yLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.yLineEdit.setObjectName("yLineEdit")
        self.horizontalLayout_6.addWidget(self.yLineEdit)
        self.FctPlotButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.FctPlotButton.sizePolicy().hasHeightForWidth())
        self.FctPlotButton.setSizePolicy(sizePolicy)
        self.FctPlotButton.setMinimumSize(QtCore.QSize(0, 0))
        self.FctPlotButton.setMaximumSize(QtCore.QSize(100, 16777215))
        self.FctPlotButton.setObjectName("FctPlotButton")
        self.horizontalLayout_6.addWidget(self.FctPlotButton)
        self.funcBox.addLayout(self.horizontalLayout_6)
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem)
        self.FctClearButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.FctClearButton.sizePolicy().hasHeightForWidth())
        self.FctClearButton.setSizePolicy(sizePolicy)
        self.FctClearButton.setMinimumSize(QtCore.QSize(0, 0))
        self.FctClearButton.setMaximumSize(QtCore.QSize(100, 16777215))
        self.FctClearButton.setObjectName("FctClearButton")
        self.horizontalLayout_8.addWidget(self.FctClearButton)
        self.verticalLayout_10.addLayout(self.horizontalLayout_8)
        self.funcBox.addLayout(self.verticalLayout_10)
        self.inputBox.addLayout(self.funcBox)
        self.full.addLayout(self.inputBox)
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.West)
        self.tabWidget.setDocumentMode(True)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setMaximumSize(QtCore.QSize(720, 16777215))
        self.tab.setObjectName("tab")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.tab)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.SettingsLayout = QtWidgets.QVBoxLayout()
        self.SettingsLayout.setObjectName("SettingsLayout")
        self.SettingsWidgetPlaceholder = QtWidgets.QWidget(self.tab)
        self.SettingsWidgetPlaceholder.setObjectName("SettingsWidgetPlaceholder")
        self.SettingsLayout.addWidget(self.SettingsWidgetPlaceholder)
        self.verticalLayout_3.addLayout(self.SettingsLayout)
        self.tabWidget.addTab(self.tab, "")
        self.full.addWidget(self.tabWidget)
        self.logField = QtWidgets.QTextEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.logField.sizePolicy().hasHeightForWidth())
        self.logField.setSizePolicy(sizePolicy)
        self.logField.setMinimumSize(QtCore.QSize(0, 0))
        self.logField.setMaximumSize(QtCore.QSize(16777215, 100))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.logField.setFont(font)
        self.logField.setMouseTracking(False)
        self.logField.setAutoFillBackground(True)
        self.logField.setStyleSheet("QTextEdit { background-color: rgb(0, 0, 0) }")
        self.logField.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.logField.setFrameShadow(QtWidgets.QFrame.Plain)
        self.logField.setLineWidth(0)
        self.logField.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.logField.setTextInteractionFlags(QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.logField.setObjectName("logField")
        self.full.addWidget(self.logField)
        self.gridLayout.addLayout(self.full, 0, 0, 1, 1)
        pyplane.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(pyplane)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 770, 21))
        self.menubar.setObjectName("menubar")
        pyplane.setMenuBar(self.menubar)
        self.actionNew = QtWidgets.QAction(pyplane)
        self.actionNew.setObjectName("actionNew")
        self.actionOpen = QtWidgets.QAction(pyplane)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave = QtWidgets.QAction(pyplane)
        self.actionSave.setObjectName("actionSave")
        self.actionQuit = QtWidgets.QAction(pyplane)
        self.actionQuit.setObjectName("actionQuit")
        self.actionNullclines = QtWidgets.QAction(pyplane)
        self.actionNullclines.setObjectName("actionNullclines")
        self.action = QtWidgets.QAction(pyplane)
        self.action.setObjectName("action")
        self.action_2 = QtWidgets.QAction(pyplane)
        self.action_2.setObjectName("action_2")
        self.actionPyPlane_Help = QtWidgets.QAction(pyplane)
        self.actionPyPlane_Help.setObjectName("actionPyPlane_Help")
        self.actionAbout = QtWidgets.QAction(pyplane)
        self.actionAbout.setObjectName("actionAbout")

        self.retranslateUi(pyplane)
        self.tabWidget.setCurrentIndex(0)
        self.actionQuit.triggered.connect(pyplane.close)
        QtCore.QMetaObject.connectSlotsByName(pyplane)

    def retranslateUi(self, pyplane):
        _translate = QtCore.QCoreApplication.translate
        pyplane.setWindowTitle(_translate("pyplane", "MainWindow"))
        self.title.setText(_translate("pyplane", "Dynamical System"))
        self.xDotLabel.setText(_translate("pyplane", "x\' = "))
        self.xDotLineEdit.setPlaceholderText(_translate("pyplane", "y"))
        self.submitButton.setText(_translate("pyplane", "Submit"))
        self.yDotLabel.setText(_translate("pyplane", "y\' = "))
        self.yDotLineEdit.setPlaceholderText(_translate("pyplane", "x-x**3"))
        self.clearButton.setText(_translate("pyplane", "Clear Trajectories"))
        self.label.setText(_translate("pyplane", "Additional Function:"))
        self.yLabel.setText(_translate("pyplane", "0 = f(x,y) ="))
        self.yLineEdit.setPlaceholderText(_translate("pyplane", "x**2+y**2-4"))
        self.FctPlotButton.setText(_translate("pyplane", "Plot"))
        self.FctClearButton.setText(_translate("pyplane", "Clear Plots"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("pyplane", "Settings"))
        self.actionNew.setText(_translate("pyplane", "New"))
        self.actionOpen.setText(_translate("pyplane", "Open"))
        self.actionSave.setText(_translate("pyplane", "Save"))
        self.actionQuit.setText(_translate("pyplane", "Quit"))
        self.actionNullclines.setText(_translate("pyplane", "Nullclines"))
        self.action.setText(_translate("pyplane", "Vector Field"))
        self.action_2.setText(_translate("pyplane", "..."))
        self.actionPyPlane_Help.setText(_translate("pyplane", "PyPlane Help"))
        self.actionAbout.setText(_translate("pyplane", "About"))

import gui.icons_rc
