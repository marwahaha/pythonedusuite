'''
	Name: edugui.py
	Author: Rowan Macdonald
	Description: The Master GUI Handler for the application
'''
#IMPORT STANDARD LIBRARY
import sys, os, random, math, time
#IMPORT PyQt5
from PyQt5 import QtCore, QtGui, QtWidgets, uic
#IMPORT EduSuite Functions
import edufunctions
#IMPORT MAIN GUI
import main_rc
#IMPORT SETTINGS
import settings

class UI_MAIN(object):
	def setupUi(self, guif_main):
		guif_main.setObjectName("guif_main")
		guif_main.resize(999, 831)
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
		self.guif_mm_btn_login.clicked.connect(self.LoginMenu)
		self.guif_mm_grid_btn.addWidget(self.guif_mm_btn_login)
		spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
		self.guif_mm_grid_btn.addItem(spacerItem1)
		self.guif_mm_btn_reg = QtWidgets.QPushButton(self.guif_mainmenu)
		font = QtGui.QFont()
		font.setPointSize(20)
		self.guif_mm_btn_reg.setFont(font)
		self.guif_mm_btn_reg.setObjectName("guif_mm_btn_reg")
		self.guif_mm_btn_reg.clicked.connect(self.RegMenu)
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
		spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
		self.gridLayout_6.addItem(spacerItem6, 1, 2, 1, 1)
		spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
		self.gridLayout_6.addItem(spacerItem7, 1, 0, 1, 1)
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
		spacerItem8 = QtWidgets.QSpacerItem(20, 30, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
		self.guif_lm_grid.addItem(spacerItem8, 2, 0, 1, 1)
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
		spacerItem9 = QtWidgets.QSpacerItem(80, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
		self.guif_lm_layout_btn_2.addItem(spacerItem9, 0, 3, 1, 1)
		spacerItem10 = QtWidgets.QSpacerItem(80, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
		self.guif_lm_layout_btn_2.addItem(spacerItem10, 0, 0, 1, 1)
		self.guif_lm_label_pass = QtWidgets.QLabel(self.guif_loginmenu)
		font = QtGui.QFont()
		font.setPointSize(16)
		font.setBold(True)
		font.setWeight(75)
		self.guif_lm_label_pass.setFont(font)
		self.guif_lm_label_pass.setObjectName("guif_lm_label_pass")
		self.guif_lm_layout_btn_2.addWidget(self.guif_lm_label_pass, 1, 1, 1, 1)
		spacerItem11 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
		self.guif_lm_layout_btn_2.addItem(spacerItem11, 2, 1, 1, 1)
		self.guif_lm_layout_btn.addLayout(self.guif_lm_layout_btn_2)
		self.guif_lm_grid.addLayout(self.guif_lm_layout_btn, 3, 0, 1, 1)
		self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
		self.horizontalLayout_4.setContentsMargins(-1, 0, -1, -1)
		self.horizontalLayout_4.setObjectName("horizontalLayout_4")
		spacerItem12 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
		self.horizontalLayout_4.addItem(spacerItem12)
		self.guif_lm_btn_back = QtWidgets.QPushButton(self.guif_loginmenu)
		font = QtGui.QFont()
		font.setPointSize(16)
		self.guif_lm_btn_back.setFont(font)
		self.guif_lm_btn_back.setObjectName("guif_lm_btn_back")
		self.guif_lm_btn_back.clicked.connect(self.MainMenu)
		self.horizontalLayout_4.addWidget(self.guif_lm_btn_back)
		spacerItem13 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
		self.horizontalLayout_4.addItem(spacerItem13)
		self.guif_lm_btn_login = QtWidgets.QPushButton(self.guif_loginmenu)
		font = QtGui.QFont()
		font.setPointSize(16)
		self.guif_lm_btn_login.setFont(font)
		self.guif_lm_btn_login.setObjectName("guif_lm_btn_login")
		self.guif_lm_btn_login.clicked.connect(self.LoginCheck)
		self.horizontalLayout_4.addWidget(self.guif_lm_btn_login)
		spacerItem14 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
		self.horizontalLayout_4.addItem(spacerItem14)
		self.guif_lm_grid.addLayout(self.horizontalLayout_4, 4, 0, 1, 1)
		self.gridLayout_6.addLayout(self.guif_lm_grid, 1, 1, 1, 1)
		spacerItem15 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
		self.gridLayout_6.addItem(spacerItem15, 0, 1, 1, 1)
		spacerItem16 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
		self.gridLayout_6.addItem(spacerItem16, 2, 1, 1, 1)
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
		self.guif_wm_btn_logout.clicked.connect(self.MainMenu)
		self.horizontalLayout.addWidget(self.guif_wm_btn_logout)
		spacerItem26 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
		self.horizontalLayout.addItem(spacerItem26)
		self.guif_wm_grid.addLayout(self.horizontalLayout, 6, 1, 1, 1)
		spacerItem27 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
		self.guif_wm_grid.addItem(spacerItem27, 5, 1, 1, 1)
		self.gridLayout_5.addLayout(self.guif_wm_grid, 0, 0, 1, 1)
		self.guif_mm_stacker.addWidget(self.guif_welcome)
		self.gridLayout_3.addWidget(self.guif_mm_stacker, 0, 0, 1, 1)
		self.gridLayout.addWidget(self.guif_main_grid, 0, 0, 1, 1)
		guif_main.setCentralWidget(self.guif_main_wid)

		self.retranslateUi(guif_main)
		self.guif_mm_stacker.setCurrentIndex(0)
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
		self.guif_wm_title.setText(_translate("guif_main", "EduSuite"))
		self.guif_wm_btn_set.setText(_translate("guif_main", "Settings"))
		self.guif_wm_btn_logout.setText(_translate("guif_main", "Logout"))
	'''
		GUI CODE END | MENU NAV & FUNCTIONS START
	'''
	def init(self):
		#INIT _translate
		_translate = QtCore.QCoreApplication.translate
		#RESET TEXT BOXES
		self.guif_lm_lineEdit_user.setText("")
		self.guif_lm_lineEdit_pass.setText("")
		#RESET LABELS
		self.name = settings.name
		self.guif_wm_label_name.setText(_translate("guif_main", "Welcome " + self.name))

	def MainMenu(self):
		self.init()
		self.guif_mm_stacker.setCurrentIndex(0)
	
	def LoginMenu(self):
		self.init()
		self.guif_mm_stacker.setCurrentIndex(1)
		
	def LoginCheck(self):
		#PASSES SELF VAR TO VAR
		username = self.guif_lm_lineEdit_user.text()
		password = self.guif_lm_lineEdit_pass.text()
		#CHECK LENGTH TO MAKE SURE THEY ACTUALLY ENTERED SOMETHING
		if (len(username) > 0 and len(password) > 0):
			check = edufunctions.LoginCheck.init(username,password)
			if (check):
				self.WelcomeMenu()
			else:
				self.MainMenu()
		
	def WelcomeMenu(self):
		self.init()
		self.guif_mm_stacker.setCurrentIndex(2)
		
	def RegMenu(self):
		pass

	def InitWindow():
		app = QtWidgets.QApplication(sys.argv)
		guif_main = QtWidgets.QMainWindow()
		ui = UI_MAIN()
		ui.setupUi(guif_main)
		guif_main.show()
		sys.exit(app.exec_())
		
'''
	STACKER INDEX
	0 - MAIN MENU
	1 - LOGIN MENU
	2 - WELCOME MENU
'''
