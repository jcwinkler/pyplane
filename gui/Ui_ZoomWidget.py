# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui/Ui_ZoomWidget.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_ZoomWidget(object):
    def setupUi(self, ZoomWidget):
        ZoomWidget.setObjectName(_fromUtf8("ZoomWidget"))
        ZoomWidget.resize(795, 587)
        self.horizontalLayout = QtGui.QHBoxLayout(ZoomWidget)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setSizeConstraint(QtGui.QLayout.SetMinAndMaxSize)
        self.verticalLayout.setSpacing(2)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label_9 = QtGui.QLabel(ZoomWidget)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.verticalLayout.addWidget(self.label_9)
        self.label = QtGui.QLabel(ZoomWidget)
        font = QtGui.QFont()
        font.setPointSize(7)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.xminLineEdit = QtGui.QLineEdit(ZoomWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.xminLineEdit.sizePolicy().hasHeightForWidth())
        self.xminLineEdit.setSizePolicy(sizePolicy)
        self.xminLineEdit.setMinimumSize(QtCore.QSize(100, 22))
        self.xminLineEdit.setObjectName(_fromUtf8("xminLineEdit"))
        self.verticalLayout.addWidget(self.xminLineEdit)
        self.label_2 = QtGui.QLabel(ZoomWidget)
        font = QtGui.QFont()
        font.setPointSize(7)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout.addWidget(self.label_2)
        self.xmaxLineEdit = QtGui.QLineEdit(ZoomWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.xmaxLineEdit.sizePolicy().hasHeightForWidth())
        self.xmaxLineEdit.setSizePolicy(sizePolicy)
        self.xmaxLineEdit.setMinimumSize(QtCore.QSize(0, 22))
        self.xmaxLineEdit.setObjectName(_fromUtf8("xmaxLineEdit"))
        self.verticalLayout.addWidget(self.xmaxLineEdit)
        self.label_3 = QtGui.QLabel(ZoomWidget)
        font = QtGui.QFont()
        font.setPointSize(7)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.verticalLayout.addWidget(self.label_3)
        self.yminLineEdit = QtGui.QLineEdit(ZoomWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.yminLineEdit.sizePolicy().hasHeightForWidth())
        self.yminLineEdit.setSizePolicy(sizePolicy)
        self.yminLineEdit.setMinimumSize(QtCore.QSize(0, 22))
        self.yminLineEdit.setObjectName(_fromUtf8("yminLineEdit"))
        self.verticalLayout.addWidget(self.yminLineEdit)
        self.label_4 = QtGui.QLabel(ZoomWidget)
        font = QtGui.QFont()
        font.setPointSize(7)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.verticalLayout.addWidget(self.label_4)
        self.ymaxLineEdit = QtGui.QLineEdit(ZoomWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ymaxLineEdit.sizePolicy().hasHeightForWidth())
        self.ymaxLineEdit.setSizePolicy(sizePolicy)
        self.ymaxLineEdit.setMinimumSize(QtCore.QSize(100, 22))
        self.ymaxLineEdit.setObjectName(_fromUtf8("ymaxLineEdit"))
        self.verticalLayout.addWidget(self.ymaxLineEdit)
        self.SetButton = QtGui.QPushButton(ZoomWidget)
        self.SetButton.setObjectName(_fromUtf8("SetButton"))
        self.verticalLayout.addWidget(self.SetButton)
        self.ZoomButton = QtGui.QPushButton(ZoomWidget)
        self.ZoomButton.setObjectName(_fromUtf8("ZoomButton"))
        self.verticalLayout.addWidget(self.ZoomButton)
        self.RefreshButton = QtGui.QPushButton(ZoomWidget)
        self.RefreshButton.setObjectName(_fromUtf8("RefreshButton"))
        self.verticalLayout.addWidget(self.RefreshButton)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.label_5 = QtGui.QLabel(ZoomWidget)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.verticalLayout.addWidget(self.label_5)
        self.forwardCheckbox = QtGui.QCheckBox(ZoomWidget)
        font = QtGui.QFont()
        font.setPointSize(7)
        self.forwardCheckbox.setFont(font)
        self.forwardCheckbox.setObjectName(_fromUtf8("forwardCheckbox"))
        self.verticalLayout.addWidget(self.forwardCheckbox)
        self.backwardCheckbox = QtGui.QCheckBox(ZoomWidget)
        font = QtGui.QFont()
        font.setPointSize(7)
        self.backwardCheckbox.setFont(font)
        self.backwardCheckbox.setObjectName(_fromUtf8("backwardCheckbox"))
        self.verticalLayout.addWidget(self.backwardCheckbox)
        spacerItem1 = QtGui.QSpacerItem(20, 10, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem1)
        self.label_6 = QtGui.QLabel(ZoomWidget)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.verticalLayout.addWidget(self.label_6)
        self.label_7 = QtGui.QLabel(ZoomWidget)
        font = QtGui.QFont()
        font.setPointSize(7)
        self.label_7.setFont(font)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.verticalLayout.addWidget(self.label_7)
        self.xinitLineEdit = QtGui.QLineEdit(ZoomWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.xinitLineEdit.sizePolicy().hasHeightForWidth())
        self.xinitLineEdit.setSizePolicy(sizePolicy)
        self.xinitLineEdit.setObjectName(_fromUtf8("xinitLineEdit"))
        self.verticalLayout.addWidget(self.xinitLineEdit)
        self.label_8 = QtGui.QLabel(ZoomWidget)
        font = QtGui.QFont()
        font.setPointSize(7)
        self.label_8.setFont(font)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.verticalLayout.addWidget(self.label_8)
        self.yinitLineEdit = QtGui.QLineEdit(ZoomWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.yinitLineEdit.sizePolicy().hasHeightForWidth())
        self.yinitLineEdit.setSizePolicy(sizePolicy)
        self.yinitLineEdit.setObjectName(_fromUtf8("yinitLineEdit"))
        self.verticalLayout.addWidget(self.yinitLineEdit)
        self.CreateTrajectoryButton = QtGui.QPushButton(ZoomWidget)
        self.CreateTrajectoryButton.setObjectName(_fromUtf8("CreateTrajectoryButton"))
        self.verticalLayout.addWidget(self.CreateTrajectoryButton)
        spacerItem2 = QtGui.QSpacerItem(20, 10, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem2)
        self.linLabel = QtGui.QLabel(ZoomWidget)
        self.linLabel.setObjectName(_fromUtf8("linLabel"))
        self.verticalLayout.addWidget(self.linLabel)
        self.linBox = QtGui.QComboBox(ZoomWidget)
        self.linBox.setMaximumSize(QtCore.QSize(110, 16777215))
        self.linBox.setObjectName(_fromUtf8("linBox"))
        self.verticalLayout.addWidget(self.linBox)
        self.linButton = QtGui.QPushButton(ZoomWidget)
        self.linButton.setMaximumSize(QtCore.QSize(110, 16777215))
        self.linButton.setObjectName(_fromUtf8("linButton"))
        self.verticalLayout.addWidget(self.linButton)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.mpl_layout = QtGui.QVBoxLayout()
        self.mpl_layout.setObjectName(_fromUtf8("mpl_layout"))
        self.frame = QtGui.QWidget(ZoomWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMinimumSize(QtCore.QSize(444, 0))
        self.frame.setObjectName(_fromUtf8("frame"))
        self.mpl_layout.addWidget(self.frame)
        self.horizontalLayout.addLayout(self.mpl_layout)

        self.retranslateUi(ZoomWidget)
        QtCore.QMetaObject.connectSlotsByName(ZoomWidget)

    def retranslateUi(self, ZoomWidget):
        ZoomWidget.setWindowTitle(_translate("ZoomWidget", "Form", None))
        self.label_9.setText(_translate("ZoomWidget", "Window Range", None))
        self.label.setText(_translate("ZoomWidget", "xmin", None))
        self.label_2.setText(_translate("ZoomWidget", "xmax", None))
        self.label_3.setText(_translate("ZoomWidget", "ymin", None))
        self.label_4.setText(_translate("ZoomWidget", "ymax", None))
        self.SetButton.setText(_translate("ZoomWidget", "Set", None))
        self.ZoomButton.setText(_translate("ZoomWidget", "Zoom", None))
        self.RefreshButton.setText(_translate("ZoomWidget", "Refresh", None))
        self.label_5.setText(_translate("ZoomWidget", "Integration", None))
        self.forwardCheckbox.setText(_translate("ZoomWidget", "Forward", None))
        self.backwardCheckbox.setText(_translate("ZoomWidget", "Backward", None))
        self.label_6.setText(_translate("ZoomWidget", "Initial Condition", None))
        self.label_7.setText(_translate("ZoomWidget", "x-Coordinate", None))
        self.label_8.setText(_translate("ZoomWidget", "y-Coordinate", None))
        self.CreateTrajectoryButton.setText(_translate("ZoomWidget", "Create", None))
        self.linLabel.setText(_translate("ZoomWidget", "Linearization", None))
        self.linButton.setText(_translate("ZoomWidget", "Linearize", None))

