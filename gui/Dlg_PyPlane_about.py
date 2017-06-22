# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 11:07:50 2015

@author: winkler
"""

import sys
from PyQt5 import QtWidgets
from PyQt5.QtCore import QT_VERSION_STR
from PyQt5.Qt import PYQT_VERSION_STR
import matplotlib as mp

from .Ui_PyPlane_about import Ui_DlgAbout


class AboutDialog(QtWidgets.QDialog, Ui_DlgAbout):
    def __init__(self, version, date):
        self.status = None
        QtWidgets.QDialog.__init__(self)

        self.setupUi(self)
        
        self.pyplane_version_info.setText(version)
        self.pyplane_date.setText(date)
        self.pyplane_platform.setText(sys.platform)

        self.python_version_info.setText(sys.version)
        self.qt_version_info.setText(QT_VERSION_STR)
        self.pyqt_version_info.setText(PYQT_VERSION_STR)
        self.matplotlib_version_info.setText(mp.__version__)

        self.show()
        self.buttonBox.button(QtWidgets.QDialogButtonBox.Ok).clicked.connect(self.close)
        self.exec_()