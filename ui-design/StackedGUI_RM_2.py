# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'StackedGUI.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_guif_main(object):
    def setupUi(self, guif_main):
        guif_main.setObjectName("guif_main")
        guif_main.resize(1044, 912)
        guif_main.setWindowOpacity(1.0)
        self.guif_main_wid = QtWidgets.QWidget(guif_main)
        self.guif_main_wid.setObjectName("guif_main_wid")
        self.gridLayout = QtWidgets.QGridLayout(self.guif_main_wid)
        self.gridLayout.setObjectName("gridLayout")
        self.guif_main_grid = QtWidgets.QWidget(self.guif_main_wid)
        self.guif_main_grid.setObjectName("guif_main_grid")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.guif_main_grid)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.guif_mm_stacker = QtWidgets.QStackedWidget(self.guif_main_grid)
        self.guif_mm_stacker.setEnabled(True)
        self.guif_mm_stacker.setObjectName("guif_mm_stacker")
        self.guif_mainmenu = QtWidgets.QWidget()
        self.guif_mainmenu.setObjectName("guif_mainmenu")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.guif_mainmenu)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.guif_mm_grid = QtWidgets.QGridLayout()
        self.guif_mm_grid.setObjectName("guif_mm_grid")
        self.guif_mm_grid_btn = QtWidgets.QHBoxLayout()
        self.guif_mm_grid_btn.setObjectName("guif_mm_grid_btn")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.guif_mm_grid_btn.addItem(spacerItem)
        self.guif_mm_btn_login = QtWidgets.QPushButton(self.guif_mainmenu)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.guif_mm_btn_login.setFont(font)
        self.guif_mm_btn_login.setObjectName("guif_mm_btn_login")
        self.guif_mm_grid_btn.addWidget(self.guif_mm_btn_login)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.guif_mm_grid_btn.addItem(spacerItem1)
        self.guif_mm_btn_reg = QtWidgets.QPushButton(self.guif_mainmenu)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.guif_mm_btn_reg.setFont(font)
        self.guif_mm_btn_reg.setObjectName("guif_mm_btn_reg")
        self.guif_mm_grid_btn.addWidget(self.guif_mm_btn_reg)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.guif_mm_grid_btn.addItem(spacerItem2)
        self.guif_mm_grid.addLayout(self.guif_mm_grid_btn, 3, 0, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.guif_mm_grid.addItem(spacerItem3, 4, 0, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.guif_mm_grid.addItem(spacerItem4, 0, 0, 1, 1)
        self.guif_mm_title = QtWidgets.QLabel(self.guif_mainmenu)
        font = QtGui.QFont()
        font.setPointSize(60)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.guif_mm_title.setFont(font)
        self.guif_mm_title.setAlignment(QtCore.Qt.AlignCenter)
        self.guif_mm_title.setObjectName("guif_mm_title")
        self.guif_mm_grid.addWidget(self.guif_mm_title, 1, 0, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(20, 60, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.guif_mm_grid.addItem(spacerItem5, 2, 0, 1, 1)
        self.gridLayout_2.addLayout(self.guif_mm_grid, 1, 0, 1, 1)
        self.guif_mm_stacker.addWidget(self.guif_mainmenu)
        self.guif_loginmenu = QtWidgets.QWidget()
        self.guif_loginmenu.setObjectName("guif_loginmenu")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.guif_loginmenu)
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_6.setObjectName("gridLayout_6")
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_6.addItem(spacerItem6, 2, 1, 1, 1)
        self.guif_lm_grid = QtWidgets.QGridLayout()
        self.guif_lm_grid.setObjectName("guif_lm_grid")
        self.guif_lm_title_logo = QtWidgets.QLabel(self.guif_loginmenu)
        font = QtGui.QFont()
        font.setPointSize(60)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.guif_lm_title_logo.setFont(font)
        self.guif_lm_title_logo.setAlignment(QtCore.Qt.AlignCenter)
        self.guif_lm_title_logo.setObjectName("guif_lm_title_logo")
        self.guif_lm_grid.addWidget(self.guif_lm_title_logo, 0, 0, 1, 1)
        self.guif_lm_title_login = QtWidgets.QLabel(self.guif_loginmenu)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.guif_lm_title_login.setFont(font)
        self.guif_lm_title_login.setAlignment(QtCore.Qt.AlignCenter)
        self.guif_lm_title_login.setObjectName("guif_lm_title_login")
        self.guif_lm_grid.addWidget(self.guif_lm_title_login, 1, 0, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(20, 30, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.guif_lm_grid.addItem(spacerItem7, 2, 0, 1, 1)
        self.guif_lm_layout_btn = QtWidgets.QHBoxLayout()
        self.guif_lm_layout_btn.setObjectName("guif_lm_layout_btn")
        self.guif_lm_layout_btn_2 = QtWidgets.QGridLayout()
        self.guif_lm_layout_btn_2.setObjectName("guif_lm_layout_btn_2")
        self.guif_lm_lineEdit_pass = QtWidgets.QLineEdit(self.guif_loginmenu)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.guif_lm_lineEdit_pass.setFont(font)
        self.guif_lm_lineEdit_pass.setMaxLength(32)
        self.guif_lm_lineEdit_pass.setObjectName("guif_lm_lineEdit_pass")
        self.guif_lm_layout_btn_2.addWidget(self.guif_lm_lineEdit_pass, 1, 2, 1, 1)
        self.guif_lm_label_user = QtWidgets.QLabel(self.guif_loginmenu)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.guif_lm_label_user.setFont(font)
        self.guif_lm_label_user.setObjectName("guif_lm_label_user")
        self.guif_lm_layout_btn_2.addWidget(self.guif_lm_label_user, 0, 1, 1, 1)
        self.guif_lm_lineEdit_user = QtWidgets.QLineEdit(self.guif_loginmenu)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.guif_lm_lineEdit_user.setFont(font)
        self.guif_lm_lineEdit_user.setMaxLength(32)
        self.guif_lm_lineEdit_user.setObjectName("guif_lm_lineEdit_user")
        self.guif_lm_layout_btn_2.addWidget(self.guif_lm_lineEdit_user, 0, 2, 1, 1)
        spacerItem8 = QtWidgets.QSpacerItem(80, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.guif_lm_layout_btn_2.addItem(spacerItem8, 0, 3, 1, 1)
        spacerItem9 = QtWidgets.QSpacerItem(80, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.guif_lm_layout_btn_2.addItem(spacerItem9, 0, 0, 1, 1)
        self.guif_lm_label_pass = QtWidgets.QLabel(self.guif_loginmenu)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.guif_lm_label_pass.setFont(font)
        self.guif_lm_label_pass.setObjectName("guif_lm_label_pass")
        self.guif_lm_layout_btn_2.addWidget(self.guif_lm_label_pass, 1, 1, 1, 1)
        spacerItem10 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.guif_lm_layout_btn_2.addItem(spacerItem10, 2, 1, 1, 1)
        self.guif_lm_layout_btn.addLayout(self.guif_lm_layout_btn_2)
        self.guif_lm_grid.addLayout(self.guif_lm_layout_btn, 3, 0, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem11)
        self.guif_lm_btn_back = QtWidgets.QPushButton(self.guif_loginmenu)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.guif_lm_btn_back.setFont(font)
        self.guif_lm_btn_back.setObjectName("guif_lm_btn_back")
        self.horizontalLayout_4.addWidget(self.guif_lm_btn_back)
        spacerItem12 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem12)
        self.guif_lm_btn_login = QtWidgets.QPushButton(self.guif_loginmenu)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.guif_lm_btn_login.setFont(font)
        self.guif_lm_btn_login.setObjectName("guif_lm_btn_login")
        self.horizontalLayout_4.addWidget(self.guif_lm_btn_login)
        spacerItem13 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem13)
        self.guif_lm_grid.addLayout(self.horizontalLayout_4, 4, 0, 1, 1)
        self.gridLayout_6.addLayout(self.guif_lm_grid, 1, 1, 1, 1)
        spacerItem14 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_6.addItem(spacerItem14, 1, 2, 1, 1)
        spacerItem15 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_6.addItem(spacerItem15, 0, 1, 1, 1)
        spacerItem16 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_6.addItem(spacerItem16, 1, 0, 1, 1)
        self.guif_mm_stacker.addWidget(self.guif_loginmenu)
        self.guif_welcome = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.guif_welcome.sizePolicy().hasHeightForWidth())
        self.guif_welcome.setSizePolicy(sizePolicy)
        self.guif_welcome.setSizeIncrement(QtCore.QSize(0, 0))
        self.guif_welcome.setAutoFillBackground(False)
        self.guif_welcome.setObjectName("guif_welcome")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.guif_welcome)
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.guif_wm_grid = QtWidgets.QGridLayout()
        self.guif_wm_grid.setObjectName("guif_wm_grid")
        self.guif_wm_h_layout = QtWidgets.QHBoxLayout()
        self.guif_wm_h_layout.setObjectName("guif_wm_h_layout")
        self.guif_wm_btn_math = QtWidgets.QPushButton(self.guif_welcome)
        self.guif_wm_btn_math.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/welcomemenu/img/maths-logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.guif_wm_btn_math.setIcon(icon)
        self.guif_wm_btn_math.setIconSize(QtCore.QSize(200, 200))
        self.guif_wm_btn_math.setObjectName("guif_wm_btn_math")
        self.guif_wm_h_layout.addWidget(self.guif_wm_btn_math)
        spacerItem17 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.guif_wm_h_layout.addItem(spacerItem17)
        self.guif_wm_btn_comput = QtWidgets.QPushButton(self.guif_welcome)
        self.guif_wm_btn_comput.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/welcomemenu/img/computer-logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.guif_wm_btn_comput.setIcon(icon1)
        self.guif_wm_btn_comput.setIconSize(QtCore.QSize(200, 200))
        self.guif_wm_btn_comput.setFlat(False)
        self.guif_wm_btn_comput.setObjectName("guif_wm_btn_comput")
        self.guif_wm_h_layout.addWidget(self.guif_wm_btn_comput)
        spacerItem18 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.guif_wm_h_layout.addItem(spacerItem18)
        self.guif_wm_btn_history = QtWidgets.QPushButton(self.guif_welcome)
        self.guif_wm_btn_history.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/welcomemenu/img/History-logo.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.guif_wm_btn_history.setIcon(icon2)
        self.guif_wm_btn_history.setIconSize(QtCore.QSize(200, 200))
        self.guif_wm_btn_history.setFlat(False)
        self.guif_wm_btn_history.setObjectName("guif_wm_btn_history")
        self.guif_wm_h_layout.addWidget(self.guif_wm_btn_history)
        self.guif_wm_grid.addLayout(self.guif_wm_h_layout, 4, 1, 1, 1)
        self.guif_wm_label_name = QtWidgets.QLabel(self.guif_welcome)
        font = QtGui.QFont()
        font.setPointSize(30)
        self.guif_wm_label_name.setFont(font)
        self.guif_wm_label_name.setAlignment(QtCore.Qt.AlignCenter)
        self.guif_wm_label_name.setObjectName("guif_wm_label_name")
        self.guif_wm_grid.addWidget(self.guif_wm_label_name, 2, 1, 1, 1)
        spacerItem19 = QtWidgets.QSpacerItem(20, 150, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.guif_wm_grid.addItem(spacerItem19, 0, 1, 1, 1)
        spacerItem20 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.guif_wm_grid.addItem(spacerItem20, 3, 1, 1, 1)
        spacerItem21 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.guif_wm_grid.addItem(spacerItem21, 2, 0, 1, 1)
        spacerItem22 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.guif_wm_grid.addItem(spacerItem22, 2, 2, 1, 1)
        spacerItem23 = QtWidgets.QSpacerItem(20, 200, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.guif_wm_grid.addItem(spacerItem23, 7, 1, 1, 1)
        self.guif_wm_title = QtWidgets.QLabel(self.guif_welcome)
        font = QtGui.QFont()
        font.setPointSize(40)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.guif_wm_title.setFont(font)
        self.guif_wm_title.setAlignment(QtCore.Qt.AlignCenter)
        self.guif_wm_title.setObjectName("guif_wm_title")
        self.guif_wm_grid.addWidget(self.guif_wm_title, 1, 1, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem24 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem24)
        self.guif_wm_btn_set = QtWidgets.QPushButton(self.guif_welcome)
        font = QtGui.QFont()
        font.setPointSize(32)
        self.guif_wm_btn_set.setFont(font)
        self.guif_wm_btn_set.setObjectName("guif_wm_btn_set")
        self.horizontalLayout.addWidget(self.guif_wm_btn_set)
        spacerItem25 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem25)
        self.guif_wm_btn_logout = QtWidgets.QPushButton(self.guif_welcome)
        font = QtGui.QFont()
        font.setPointSize(32)
        self.guif_wm_btn_logout.setFont(font)
        self.guif_wm_btn_logout.setObjectName("guif_wm_btn_logout")
        self.horizontalLayout.addWidget(self.guif_wm_btn_logout)
        spacerItem26 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem26)
        self.guif_wm_grid.addLayout(self.horizontalLayout, 6, 1, 1, 1)
        spacerItem27 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.guif_wm_grid.addItem(spacerItem27, 5, 1, 1, 1)
        self.gridLayout_5.addLayout(self.guif_wm_grid, 0, 0, 1, 1)
        self.guif_mm_stacker.addWidget(self.guif_welcome)
        self.guif_register = QtWidgets.QWidget()
        self.guif_register.setObjectName("guif_register")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.guif_register)
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.guif_rm_grid = QtWidgets.QGridLayout()
        self.guif_rm_grid.setObjectName("guif_rm_grid")
        spacerItem28 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.guif_rm_grid.addItem(spacerItem28, 4, 0, 1, 1)
        self.guif_rm_title_reg = QtWidgets.QLabel(self.guif_register)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.guif_rm_title_reg.setFont(font)
        self.guif_rm_title_reg.setAlignment(QtCore.Qt.AlignCenter)
        self.guif_rm_title_reg.setObjectName("guif_rm_title_reg")
        self.guif_rm_grid.addWidget(self.guif_rm_title_reg, 1, 0, 1, 1)
        self.guif_rm_title = QtWidgets.QLabel(self.guif_register)
        font = QtGui.QFont()
        font.setPointSize(60)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.guif_rm_title.setFont(font)
        self.guif_rm_title.setAlignment(QtCore.Qt.AlignCenter)
        self.guif_rm_title.setObjectName("guif_rm_title")
        self.guif_rm_grid.addWidget(self.guif_rm_title, 0, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        spacerItem29 = QtWidgets.QSpacerItem(100, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem29, 0, 3, 1, 1)
        self.guif_rm_input_user = QtWidgets.QLineEdit(self.guif_register)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.guif_rm_input_user.setFont(font)
        self.guif_rm_input_user.setMaxLength(100)
        self.guif_rm_input_user.setObjectName("guif_rm_input_user")
        self.gridLayout_4.addWidget(self.guif_rm_input_user, 0, 2, 1, 1)
        self.guif_rm_label_user = QtWidgets.QLabel(self.guif_register)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.guif_rm_label_user.setFont(font)
        self.guif_rm_label_user.setObjectName("guif_rm_label_user")
        self.gridLayout_4.addWidget(self.guif_rm_label_user, 0, 1, 1, 1)
        spacerItem30 = QtWidgets.QSpacerItem(100, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem30, 0, 0, 1, 1)
        self.guif_rm_input_pass = QtWidgets.QLineEdit(self.guif_register)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.guif_rm_input_pass.setFont(font)
        self.guif_rm_input_pass.setMaxLength(100)
        self.guif_rm_input_pass.setObjectName("guif_rm_input_pass")
        self.gridLayout_4.addWidget(self.guif_rm_input_pass, 1, 2, 1, 1)
        self.guif_rm_label_pass = QtWidgets.QLabel(self.guif_register)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.guif_rm_label_pass.setFont(font)
        self.guif_rm_label_pass.setObjectName("guif_rm_label_pass")
        self.gridLayout_4.addWidget(self.guif_rm_label_pass, 1, 1, 1, 1)
        self.guif_rm_label_email = QtWidgets.QLabel(self.guif_register)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.guif_rm_label_email.setFont(font)
        self.guif_rm_label_email.setObjectName("guif_rm_label_email")
        self.gridLayout_4.addWidget(self.guif_rm_label_email, 2, 1, 1, 1)
        self.guif_rm_input_email = QtWidgets.QLineEdit(self.guif_register)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.guif_rm_input_email.setFont(font)
        self.guif_rm_input_email.setMaxLength(100)
        self.guif_rm_input_email.setObjectName("guif_rm_input_email")
        self.gridLayout_4.addWidget(self.guif_rm_input_email, 2, 2, 1, 1)
        self.guif_rm_label_dob = QtWidgets.QLabel(self.guif_register)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.guif_rm_label_dob.setFont(font)
        self.guif_rm_label_dob.setObjectName("guif_rm_label_dob")
        self.gridLayout_4.addWidget(self.guif_rm_label_dob, 3, 1, 1, 1)
        self.guif_rm_input_date = QtWidgets.QDateEdit(self.guif_register)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.guif_rm_input_date.setFont(font)
        self.guif_rm_input_date.setCalendarPopup(True)
        self.guif_rm_input_date.setObjectName("guif_rm_input_date")
        self.gridLayout_4.addWidget(self.guif_rm_input_date, 3, 2, 1, 1)
        self.horizontalLayout_2.addLayout(self.gridLayout_4)
        self.guif_rm_grid.addLayout(self.horizontalLayout_2, 3, 0, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem31 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem31)
        self.guif_rm_btn_back = QtWidgets.QPushButton(self.guif_register)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.guif_rm_btn_back.setFont(font)
        self.guif_rm_btn_back.setObjectName("guif_rm_btn_back")
        self.horizontalLayout_3.addWidget(self.guif_rm_btn_back)
        spacerItem32 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem32)
        self.guif_rm_btn_reg = QtWidgets.QPushButton(self.guif_register)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.guif_rm_btn_reg.setFont(font)
        self.guif_rm_btn_reg.setObjectName("guif_rm_btn_reg")
        self.horizontalLayout_3.addWidget(self.guif_rm_btn_reg)
        spacerItem33 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem33)
        self.guif_rm_grid.addLayout(self.horizontalLayout_3, 5, 0, 1, 1)
        self.guif_rm_label_invalid = QtWidgets.QLabel(self.guif_register)
        self.guif_rm_label_invalid.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.guif_rm_label_invalid.setFont(font)
        self.guif_rm_label_invalid.setStyleSheet("color: rgb(255, 0, 0);")
        self.guif_rm_label_invalid.setAlignment(QtCore.Qt.AlignCenter)
        self.guif_rm_label_invalid.setObjectName("guif_rm_label_invalid")
        self.guif_rm_grid.addWidget(self.guif_rm_label_invalid, 2, 0, 1, 1)
        self.gridLayout_7.addLayout(self.guif_rm_grid, 1, 1, 1, 1)
        spacerItem34 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_7.addItem(spacerItem34, 2, 1, 1, 1)
        spacerItem35 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_7.addItem(spacerItem35, 1, 0, 1, 1)
        spacerItem36 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_7.addItem(spacerItem36, 0, 1, 1, 1)
        spacerItem37 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_7.addItem(spacerItem37, 1, 2, 1, 1)
        self.guif_mm_stacker.addWidget(self.guif_register)
        self.gridLayout_3.addWidget(self.guif_mm_stacker, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.guif_main_grid, 0, 0, 1, 1)
        guif_main.setCentralWidget(self.guif_main_wid)

        self.retranslateUi(guif_main)
        self.guif_mm_stacker.setCurrentIndex(3)
        QtCore.QMetaObject.connectSlotsByName(guif_main)

    def retranslateUi(self, guif_main):
        _translate = QtCore.QCoreApplication.translate
        guif_main.setWindowTitle(_translate("guif_main", "EduSuite"))
        self.guif_mm_btn_login.setText(_translate("guif_main", "  Login  "))
        self.guif_mm_btn_reg.setText(_translate("guif_main", "Register"))
        self.guif_mm_title.setText(_translate("guif_main", "EduSuite"))
        self.guif_lm_title_logo.setText(_translate("guif_main", "EduSuite"))
        self.guif_lm_title_login.setText(_translate("guif_main", "Login"))
        self.guif_lm_label_user.setText(_translate("guif_main", "Username:"))
        self.guif_lm_label_pass.setText(_translate("guif_main", "Password:"))
        self.guif_lm_btn_back.setText(_translate("guif_main", "Back"))
        self.guif_lm_btn_login.setText(_translate("guif_main", "Login"))
        self.guif_wm_label_name.setText(_translate("guif_main", "Welcome {name}!"))
        self.guif_wm_title.setText(_translate("guif_main", "EduSuite"))
        self.guif_wm_btn_set.setText(_translate("guif_main", "Settings"))
        self.guif_wm_btn_logout.setText(_translate("guif_main", "Logout"))
        self.guif_rm_title_reg.setText(_translate("guif_main", "Register"))
        self.guif_rm_title.setText(_translate("guif_main", "EduSuite"))
        self.guif_rm_label_user.setText(_translate("guif_main", "Username:"))
        self.guif_rm_label_pass.setText(_translate("guif_main", "Password:"))
        self.guif_rm_label_email.setText(_translate("guif_main", "Email:"))
        self.guif_rm_label_dob.setText(_translate("guif_main", "Date of Birth:"))
        self.guif_rm_input_date.setDisplayFormat(_translate("guif_main", "dd-MMM-yyyy"))
        self.guif_rm_btn_back.setText(_translate("guif_main", "Back"))
        self.guif_rm_btn_reg.setText(_translate("guif_main", "Register"))
        self.guif_rm_label_invalid.setText(_translate("guif_main", "Invalid Details"))

import main_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    guif_main = QtWidgets.QMainWindow()
    ui = Ui_guif_main()
    ui.setupUi(guif_main)
    guif_main.show()
    sys.exit(app.exec_())

