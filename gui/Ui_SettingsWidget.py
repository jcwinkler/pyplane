# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui/Ui_SettingsWidget.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SettingsWidget(object):
    def setupUi(self, SettingsWidget):
        SettingsWidget.setObjectName("SettingsWidget")
        SettingsWidget.resize(513, 413)
        self.verticalLayout = QtWidgets.QVBoxLayout(SettingsWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.SectionListView = QtWidgets.QListView(SettingsWidget)
        self.SectionListView.setMinimumSize(QtCore.QSize(100, 0))
        self.SectionListView.setMaximumSize(QtCore.QSize(100, 16777215))
        self.SectionListView.setObjectName("SectionListView")
        self.horizontalLayout_2.addWidget(self.SectionListView)
        self.SectionLayout = QtWidgets.QFormLayout()
        self.SectionLayout.setObjectName("SectionLayout")
        self.SetupSectionTitle = QtWidgets.QLabel(SettingsWidget)
        self.SetupSectionTitle.setMinimumSize(QtCore.QSize(200, 30))
        self.SetupSectionTitle.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.SetupSectionTitle.setFont(font)
        self.SetupSectionTitle.setText("")
        self.SetupSectionTitle.setObjectName("SetupSectionTitle")
        self.SectionLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.SetupSectionTitle)
        self.horizontalLayout_2.addLayout(self.SectionLayout)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.SetupApplyButton = QtWidgets.QPushButton(SettingsWidget)
        self.SetupApplyButton.setMinimumSize(QtCore.QSize(100, 0))
        self.SetupApplyButton.setMaximumSize(QtCore.QSize(100, 16777215))
        self.SetupApplyButton.setObjectName("SetupApplyButton")
        self.horizontalLayout.addWidget(self.SetupApplyButton)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(SettingsWidget)
        QtCore.QMetaObject.connectSlotsByName(SettingsWidget)

    def retranslateUi(self, SettingsWidget):
        _translate = QtCore.QCoreApplication.translate
        SettingsWidget.setWindowTitle(_translate("SettingsWidget", "Form"))
        self.SetupApplyButton.setText(_translate("SettingsWidget", "Apply"))

