# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_mm_login_menu(object):
    def setupUi(self, mm_login_menu):
        mm_login_menu.setObjectName("mm_login_menu")
        mm_login_menu.resize(796, 600)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(mm_login_menu.sizePolicy().hasHeightForWidth())
        mm_login_menu.setSizePolicy(sizePolicy)
        mm_login_menu.setIconSize(QtCore.QSize(24, 24))
        self.centralwidget = QtWidgets.QWidget(mm_login_menu)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.mm_label_user = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.mm_label_user.setFont(font)
        self.mm_label_user.setObjectName("mm_label_user")
        self.horizontalLayout.addWidget(self.mm_label_user)
        self.mm_login_box = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.mm_login_box.setFont(font)
        self.mm_login_box.setObjectName("mm_login_box")
        self.horizontalLayout.addWidget(self.mm_login_box)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.gridLayout.addLayout(self.horizontalLayout, 2, 1, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.mm_label_pass = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.mm_label_pass.setFont(font)
        self.mm_label_pass.setObjectName("mm_label_pass")
        self.horizontalLayout_2.addWidget(self.mm_label_pass)
        self.mm_password_box = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.mm_password_box.setFont(font)
        self.mm_password_box.setObjectName("mm_password_box")
        self.horizontalLayout_2.addWidget(self.mm_password_box)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.gridLayout.addLayout(self.horizontalLayout_2, 3, 1, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem4)
        self.mm_login_button = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(24)
        self.mm_login_button.setFont(font)
        self.mm_login_button.setObjectName("mm_login_button")
        self.horizontalLayout_3.addWidget(self.mm_login_button)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem5)
        self.gridLayout.addLayout(self.horizontalLayout_3, 4, 1, 1, 1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setContentsMargins(-1, -1, -1, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.mm_title = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(40)
        self.mm_title.setFont(font)
        self.mm_title.setAlignment(QtCore.Qt.AlignCenter)
        self.mm_title.setObjectName("mm_title")
        self.verticalLayout_2.addWidget(self.mm_title)
        self.gridLayout.addLayout(self.verticalLayout_2, 1, 1, 1, 1)
        mm_login_menu.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(mm_login_menu)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 796, 21))
        self.menubar.setObjectName("menubar")
        mm_login_menu.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(mm_login_menu)
        self.statusbar.setObjectName("statusbar")
        mm_login_menu.setStatusBar(self.statusbar)

        Ui_mm_login_menu.retranslateUi(self,mm_login_menu)
        QtCore.QMetaObject.connectSlotsByName(mm_login_menu)

    def retranslateUi(self, mm_login_menu):
        _translate = QtCore.QCoreApplication.translate
        mm_login_menu.setWindowTitle(_translate("mm_login_menu", "EduSuite"))
        self.mm_label_user.setText(_translate("mm_login_menu", "Username:"))
        self.mm_label_pass.setText(_translate("mm_login_menu", "Password"))
        self.mm_login_button.setText(_translate("mm_login_menu", "  Login  "))
        self.mm_title.setText(_translate("mm_login_menu", "EduSuite"))

