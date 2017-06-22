# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui/Ui_PyPlane_about.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_DlgAbout(object):
    def setupUi(self, DlgAbout):
        DlgAbout.setObjectName("DlgAbout")
        DlgAbout.resize(579, 422)
        self.buttonBox = QtWidgets.QDialogButtonBox(DlgAbout)
        self.buttonBox.setGeometry(QtCore.QRect(230, 390, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.grpInfo = QtWidgets.QGroupBox(DlgAbout)
        self.grpInfo.setGeometry(QtCore.QRect(10, 3, 561, 391))
        self.grpInfo.setObjectName("grpInfo")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.grpInfo)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 20, 541, 361))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setFieldGrowthPolicy(QtWidgets.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_2.setContentsMargins(-1, 12, -1, -1)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_pyplane_version = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_pyplane_version.setFont(font)
        self.label_pyplane_version.setObjectName("label_pyplane_version")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_pyplane_version)
        self.pyplane_version_info = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pyplane_version_info.setFont(font)
        self.pyplane_version_info.setObjectName("pyplane_version_info")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.pyplane_version_info)
        self.label_pyplane_date = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_pyplane_date.setFont(font)
        self.label_pyplane_date.setObjectName("label_pyplane_date")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_pyplane_date)
        self.pyplane_date = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pyplane_date.setFont(font)
        self.pyplane_date.setObjectName("pyplane_date")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.pyplane_date)
        self.label_platform = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_platform.setFont(font)
        self.label_platform.setObjectName("label_platform")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_platform)
        self.pyplane_platform = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pyplane_platform.setFont(font)
        self.pyplane_platform.setObjectName("pyplane_platform")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.pyplane_platform)
        self.verticalLayout_2.addLayout(self.formLayout_2)
        self.txtCopyright = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.txtCopyright.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.txtCopyright.setWordWrap(True)
        self.txtCopyright.setOpenExternalLinks(False)
        self.txtCopyright.setObjectName("txtCopyright")
        self.verticalLayout_2.addWidget(self.txtCopyright)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setMaximumSize(QtCore.QSize(200, 200))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/icons/pyplane_logo.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.txtGPL = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.txtGPL.setAlignment(QtCore.Qt.AlignCenter)
        self.txtGPL.setWordWrap(True)
        self.txtGPL.setOpenExternalLinks(False)
        self.txtGPL.setObjectName("txtGPL")
        self.verticalLayout.addWidget(self.txtGPL)
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setWordWrap(True)
        self.label_2.setOpenExternalLinks(False)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label_python_version = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_python_version.setObjectName("label_python_version")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_python_version)
        self.python_version_info = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.python_version_info.setObjectName("python_version_info")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.python_version_info)
        self.label_qt_version = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_qt_version.setObjectName("label_qt_version")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_qt_version)
        self.label_pyqt_version = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_pyqt_version.setObjectName("label_pyqt_version")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_pyqt_version)
        self.label_matplotlib_version = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_matplotlib_version.setObjectName("label_matplotlib_version")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_matplotlib_version)
        self.qt_version_info = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.qt_version_info.setObjectName("qt_version_info")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.qt_version_info)
        self.pyqt_version_info = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.pyqt_version_info.setObjectName("pyqt_version_info")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.pyqt_version_info)
        self.matplotlib_version_info = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.matplotlib_version_info.setObjectName("matplotlib_version_info")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.matplotlib_version_info)
        self.verticalLayout.addLayout(self.formLayout)

        self.retranslateUi(DlgAbout)
        self.buttonBox.accepted.connect(DlgAbout.accept)
        self.buttonBox.rejected.connect(DlgAbout.reject)
        QtCore.QMetaObject.connectSlotsByName(DlgAbout)

    def retranslateUi(self, DlgAbout):
        _translate = QtCore.QCoreApplication.translate
        DlgAbout.setWindowTitle(_translate("DlgAbout", "About"))
        self.grpInfo.setTitle(_translate("DlgAbout", "Information"))
        self.label_pyplane_version.setText(_translate("DlgAbout", "Version:"))
        self.pyplane_version_info.setText(_translate("DlgAbout", "TextLabel"))
        self.label_pyplane_date.setText(_translate("DlgAbout", "Date:"))
        self.pyplane_date.setText(_translate("DlgAbout", "TextLabel"))
        self.label_platform.setText(_translate("DlgAbout", "Platform:"))
        self.pyplane_platform.setText(_translate("DlgAbout", "TextLabel"))
        self.txtCopyright.setText(_translate("DlgAbout", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Copyright (C) 2013-2017</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">by Klemens Fritzsche and Jan Winkler</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Technische Universität Dresden</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Faculty of Electrical and Computer Engineering</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Institute of Control Theory</p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a href=\"http://www.tu-dresden.de/ing/elektrotechnik/rst?set_language=en\"><span style=\" text-decoration: underline; color:#0000ff;\">http://www.tu-dresden.de/ing/elektrotechnik/rst?set_language=en</span></a></p></body></html>"))
        self.txtGPL.setText(_translate("DlgAbout", "This program is free software, licensed under the terms of the GNU General Public License, Version 3\n"
"http://www.gnu.org/license/"))
        self.label_2.setText(_translate("DlgAbout", "Please consult\n"
"<https://github.com/TUD-RST/pyplane.git>\n"
" for updated versions of this program!"))
        self.label_python_version.setText(_translate("DlgAbout", "Python-Version:"))
        self.python_version_info.setText(_translate("DlgAbout", "TextLabel"))
        self.label_qt_version.setText(_translate("DlgAbout", "QT-Version:"))
        self.label_pyqt_version.setText(_translate("DlgAbout", "PyQT-Version:"))
        self.label_matplotlib_version.setText(_translate("DlgAbout", "Matplotlib-Version:"))
        self.qt_version_info.setText(_translate("DlgAbout", "TextLabel"))
        self.pyqt_version_info.setText(_translate("DlgAbout", "TextLabel"))
        self.matplotlib_version_info.setText(_translate("DlgAbout", "TextLabel"))

import icons_rc
