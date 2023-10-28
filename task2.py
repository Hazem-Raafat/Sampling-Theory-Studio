# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'task2.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 750)
        MainWindow.setMinimumSize(QtCore.QSize(1000, 700))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setMinimumSize(QtCore.QSize(1000, 700))
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.WindowTabs = QtWidgets.QTabWidget(self.centralwidget)
        self.WindowTabs.setObjectName("WindowTabs")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.tab)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.tab1 = QtWidgets.QFrame(self.tab)
        self.tab1.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.tab1.setFrameShape(QtWidgets.QFrame.Box)
        self.tab1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.tab1.setLineWidth(1)
        self.tab1.setObjectName("tab1")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.tab1)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.primary_plot = PlotWidget(self.tab1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.primary_plot.sizePolicy().hasHeightForWidth())
        self.primary_plot.setSizePolicy(sizePolicy)
        self.primary_plot.setMinimumSize(QtCore.QSize(0, 0))
        self.primary_plot.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.primary_plot.setAutoFillBackground(False)
        self.primary_plot.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"margin: 3px;\n"
"")
        self.primary_plot.setObjectName("primary_plot")
        self.verticalLayout_2.addWidget(self.primary_plot)
        self.reconstructed_plot = PlotWidget(self.tab1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.reconstructed_plot.sizePolicy().hasHeightForWidth())
        self.reconstructed_plot.setSizePolicy(sizePolicy)
        self.reconstructed_plot.setMinimumSize(QtCore.QSize(0, 0))
        self.reconstructed_plot.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.reconstructed_plot.setAutoFillBackground(False)
        self.reconstructed_plot.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"margin: 3px;\n"
"")
        self.reconstructed_plot.setObjectName("reconstructed_plot")
        self.verticalLayout_2.addWidget(self.reconstructed_plot)
        self.error_plot = PlotWidget(self.tab1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.error_plot.sizePolicy().hasHeightForWidth())
        self.error_plot.setSizePolicy(sizePolicy)
        self.error_plot.setMinimumSize(QtCore.QSize(0, 0))
        self.error_plot.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.error_plot.setAutoFillBackground(False)
        self.error_plot.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"margin: 3px;\n"
"")
        self.error_plot.setObjectName("error_plot")
        self.verticalLayout_2.addWidget(self.error_plot)
        self.controls = QtWidgets.QFrame(self.tab1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.controls.sizePolicy().hasHeightForWidth())
        self.controls.setSizePolicy(sizePolicy)
        self.controls.setMinimumSize(QtCore.QSize(0, 0))
        self.controls.setMaximumSize(QtCore.QSize(16777215, 100))
        self.controls.setFrameShape(QtWidgets.QFrame.Box)
        self.controls.setFrameShadow(QtWidgets.QFrame.Raised)
        self.controls.setObjectName("controls")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.controls)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.frame_3 = QtWidgets.QFrame(self.controls)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        self.frame_3.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(15)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_4 = QtWidgets.QLabel(self.frame_3)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)
        self.sampling_slider = QtWidgets.QSlider(self.frame_3)
        self.sampling_slider.setOrientation(QtCore.Qt.Horizontal)
        self.sampling_slider.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.sampling_slider.setObjectName("sampling_slider")
        self.horizontalLayout_4.addWidget(self.sampling_slider)
        self.sampling_lcd = QtWidgets.QLCDNumber(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sampling_lcd.sizePolicy().hasHeightForWidth())
        self.sampling_lcd.setSizePolicy(sizePolicy)
        self.sampling_lcd.setMaximumSize(QtCore.QSize(75, 35))
        self.sampling_lcd.setSmallDecimalPoint(False)
        self.sampling_lcd.setObjectName("sampling_lcd")
        self.horizontalLayout_4.addWidget(self.sampling_lcd)
        self.space_2 = QtWidgets.QFrame(self.frame_3)
        self.space_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.space_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.space_2.setObjectName("space_2")
        self.horizontalLayout_4.addWidget(self.space_2)
        self.label_3 = QtWidgets.QLabel(self.frame_3)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_4.addWidget(self.label_3)
        self.noise_slider = QtWidgets.QSlider(self.frame_3)
        self.noise_slider.setOrientation(QtCore.Qt.Horizontal)
        self.noise_slider.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.noise_slider.setObjectName("noise_slider")
        self.horizontalLayout_4.addWidget(self.noise_slider)
        self.noise_lcd = QtWidgets.QLCDNumber(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.noise_lcd.sizePolicy().hasHeightForWidth())
        self.noise_lcd.setSizePolicy(sizePolicy)
        self.noise_lcd.setMaximumSize(QtCore.QSize(75, 35))
        self.noise_lcd.setSmallDecimalPoint(False)
        self.noise_lcd.setObjectName("noise_lcd")
        self.horizontalLayout_4.addWidget(self.noise_lcd)
        self.space = QtWidgets.QFrame(self.frame_3)
        self.space.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.space.setFrameShadow(QtWidgets.QFrame.Raised)
        self.space.setObjectName("space")
        self.horizontalLayout_4.addWidget(self.space)
        self.import_btn = QtWidgets.QPushButton(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.import_btn.sizePolicy().hasHeightForWidth())
        self.import_btn.setSizePolicy(sizePolicy)
        self.import_btn.setMinimumSize(QtCore.QSize(0, 0))
        self.import_btn.setMaximumSize(QtCore.QSize(140, 40))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.import_btn.setFont(font)
        self.import_btn.setStyleSheet("\n"
"\n"
"QPushButton {\n"
"    background-color: rgb(0, 85, 255);\n"
"color:rgb(255, 255, 255);\n"
"border-radius:5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(0, 50, 150);\n"
"}\n"
"")
        self.import_btn.setObjectName("import_btn")
        self.horizontalLayout_4.addWidget(self.import_btn)
        self.clear_btn = QtWidgets.QPushButton(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.clear_btn.sizePolicy().hasHeightForWidth())
        self.clear_btn.setSizePolicy(sizePolicy)
        self.clear_btn.setMinimumSize(QtCore.QSize(0, 0))
        self.clear_btn.setMaximumSize(QtCore.QSize(140, 40))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.clear_btn.setFont(font)
        self.clear_btn.setStyleSheet("QPushButton {\n"
"    background-color: rgb(240, 0, 0);\n"
"color:rgb(255, 255, 255);\n"
"border-radius:5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(189, 0, 0);\n"
"}\n"
"")
        self.clear_btn.setObjectName("clear_btn")
        self.horizontalLayout_4.addWidget(self.clear_btn)
        self.label_8 = QtWidgets.QLabel(self.frame_3)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_4.addWidget(self.label_8)
        self.horizontalLayout_3.addWidget(self.frame_3)
        self.fmaxLCD = QtWidgets.QLCDNumber(self.controls)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fmaxLCD.sizePolicy().hasHeightForWidth())
        self.fmaxLCD.setSizePolicy(sizePolicy)
        self.fmaxLCD.setMaximumSize(QtCore.QSize(75, 35))
        self.fmaxLCD.setSmallDecimalPoint(False)
        self.fmaxLCD.setObjectName("fmaxLCD")
        self.horizontalLayout_3.addWidget(self.fmaxLCD)
        self.verticalLayout_2.addWidget(self.controls)
        self.horizontalLayout_2.addWidget(self.tab1)
        self.WindowTabs.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.tab_2)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.tab1_2 = QtWidgets.QFrame(self.tab_2)
        self.tab1_2.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.tab1_2.setFrameShape(QtWidgets.QFrame.Box)
        self.tab1_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.tab1_2.setLineWidth(1)
        self.tab1_2.setObjectName("tab1_2")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.tab1_2)
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.frame_21 = QtWidgets.QFrame(self.tab1_2)
        self.frame_21.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_21.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_21.setObjectName("frame_21")
        self.verticalLayout_16 = QtWidgets.QVBoxLayout(self.frame_21)
        self.verticalLayout_16.setContentsMargins(2, 2, 2, 2)
        self.verticalLayout_16.setSpacing(5)
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.sinusoidal_main_plot = PlotWidget(self.frame_21)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sinusoidal_main_plot.sizePolicy().hasHeightForWidth())
        self.sinusoidal_main_plot.setSizePolicy(sizePolicy)
        self.sinusoidal_main_plot.setMinimumSize(QtCore.QSize(0, 0))
        self.sinusoidal_main_plot.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.sinusoidal_main_plot.setAutoFillBackground(False)
        self.sinusoidal_main_plot.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"margin: 3px;\n"
"")
        self.sinusoidal_main_plot.setObjectName("sinusoidal_main_plot")
        self.verticalLayout_16.addWidget(self.sinusoidal_main_plot)
        self.sinusoidal_secondary_plot = PlotWidget(self.frame_21)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sinusoidal_secondary_plot.sizePolicy().hasHeightForWidth())
        self.sinusoidal_secondary_plot.setSizePolicy(sizePolicy)
        self.sinusoidal_secondary_plot.setMinimumSize(QtCore.QSize(0, 0))
        self.sinusoidal_secondary_plot.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.sinusoidal_secondary_plot.setAutoFillBackground(False)
        self.sinusoidal_secondary_plot.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"margin: 3px;\n"
"")
        self.sinusoidal_secondary_plot.setObjectName("sinusoidal_secondary_plot")
        self.verticalLayout_16.addWidget(self.sinusoidal_secondary_plot)
        self.frame = QtWidgets.QFrame(self.frame_21)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMaximumSize(QtCore.QSize(16777215, 120))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame_4 = QtWidgets.QFrame(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy)
        self.frame_4.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.sinusoidals_signals_menu = QtWidgets.QComboBox(self.frame_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sinusoidals_signals_menu.sizePolicy().hasHeightForWidth())
        self.sinusoidals_signals_menu.setSizePolicy(sizePolicy)
        self.sinusoidals_signals_menu.setMaximumSize(QtCore.QSize(225, 25))
        self.sinusoidals_signals_menu.setObjectName("sinusoidals_signals_menu")
        self.horizontalLayout.addWidget(self.sinusoidals_signals_menu)
        self.add_sinusoidal_button = QtWidgets.QPushButton(self.frame_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.add_sinusoidal_button.sizePolicy().hasHeightForWidth())
        self.add_sinusoidal_button.setSizePolicy(sizePolicy)
        self.add_sinusoidal_button.setMinimumSize(QtCore.QSize(80, 30))
        self.add_sinusoidal_button.setMaximumSize(QtCore.QSize(200, 35))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.add_sinusoidal_button.setFont(font)
        self.add_sinusoidal_button.setStyleSheet("\n"
"\n"
"QPushButton {\n"
"    background-color: rgb(0, 85, 255);\n"
"color:rgb(255, 255, 255);\n"
"border-radius:5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(0, 50, 150);\n"
"}\n"
"")
        self.add_sinusoidal_button.setObjectName("add_sinusoidal_button")
        self.horizontalLayout.addWidget(self.add_sinusoidal_button)
        self.delete_sinusoidal_button = QtWidgets.QPushButton(self.frame_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.delete_sinusoidal_button.sizePolicy().hasHeightForWidth())
        self.delete_sinusoidal_button.setSizePolicy(sizePolicy)
        self.delete_sinusoidal_button.setMinimumSize(QtCore.QSize(80, 30))
        self.delete_sinusoidal_button.setMaximumSize(QtCore.QSize(200, 35))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.delete_sinusoidal_button.setFont(font)
        self.delete_sinusoidal_button.setStyleSheet("QPushButton {\n"
"    background-color: rgb(240, 0, 0);\n"
"color:rgb(255, 255, 255);\n"
"border-radius:5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(189, 0, 0);\n"
"}\n"
"")
        self.delete_sinusoidal_button.setObjectName("delete_sinusoidal_button")
        self.horizontalLayout.addWidget(self.delete_sinusoidal_button)
        self.verticalLayout_3.addWidget(self.frame_4)
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_5.setContentsMargins(6, 0, 6, 0)
        self.horizontalLayout_5.setSpacing(10)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.frame_29 = QtWidgets.QFrame(self.frame_2)
        self.frame_29.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_29.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_29.setObjectName("frame_29")
        self.verticalLayout_22 = QtWidgets.QVBoxLayout(self.frame_29)
        self.verticalLayout_22.setContentsMargins(0, 5, 0, 0)
        self.verticalLayout_22.setSpacing(0)
        self.verticalLayout_22.setObjectName("verticalLayout_22")
        self.frame_30 = QtWidgets.QFrame(self.frame_29)
        self.frame_30.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_30.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_30.setObjectName("frame_30")
        self.verticalLayout_23 = QtWidgets.QVBoxLayout(self.frame_30)
        self.verticalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_23.setSpacing(0)
        self.verticalLayout_23.setObjectName("verticalLayout_23")
        self.label_7 = QtWidgets.QLabel(self.frame_30)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_23.addWidget(self.label_7)
        self.verticalLayout_22.addWidget(self.frame_30, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.frame_31 = QtWidgets.QFrame(self.frame_29)
        self.frame_31.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_31.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_31.setObjectName("frame_31")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout(self.frame_31)
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_12.setSpacing(6)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.sinusoidal_frequency_slider = QtWidgets.QSlider(self.frame_31)
        self.sinusoidal_frequency_slider.setOrientation(QtCore.Qt.Horizontal)
        self.sinusoidal_frequency_slider.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.sinusoidal_frequency_slider.setObjectName("sinusoidal_frequency_slider")
        self.horizontalLayout_12.addWidget(self.sinusoidal_frequency_slider)
        self.sinusoidal_frequency_LCD = QtWidgets.QLCDNumber(self.frame_31)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sinusoidal_frequency_LCD.sizePolicy().hasHeightForWidth())
        self.sinusoidal_frequency_LCD.setSizePolicy(sizePolicy)
        self.sinusoidal_frequency_LCD.setMaximumSize(QtCore.QSize(75, 35))
        self.sinusoidal_frequency_LCD.setSmallDecimalPoint(False)
        self.sinusoidal_frequency_LCD.setObjectName("sinusoidal_frequency_LCD")
        self.horizontalLayout_12.addWidget(self.sinusoidal_frequency_LCD)
        self.verticalLayout_22.addWidget(self.frame_31)
        self.horizontalLayout_5.addWidget(self.frame_29)
        self.frame_24 = QtWidgets.QFrame(self.frame_2)
        self.frame_24.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_24.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_24.setObjectName("frame_24")
        self.verticalLayout_19 = QtWidgets.QVBoxLayout(self.frame_24)
        self.verticalLayout_19.setContentsMargins(0, 5, 0, 0)
        self.verticalLayout_19.setSpacing(0)
        self.verticalLayout_19.setObjectName("verticalLayout_19")
        self.frame_27 = QtWidgets.QFrame(self.frame_24)
        self.frame_27.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_27.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_27.setObjectName("frame_27")
        self.verticalLayout_21 = QtWidgets.QVBoxLayout(self.frame_27)
        self.verticalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_21.setSpacing(0)
        self.verticalLayout_21.setObjectName("verticalLayout_21")
        self.label_6 = QtWidgets.QLabel(self.frame_27)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_21.addWidget(self.label_6)
        self.verticalLayout_19.addWidget(self.frame_27, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.frame_28 = QtWidgets.QFrame(self.frame_24)
        self.frame_28.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_28.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_28.setObjectName("frame_28")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.frame_28)
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_10.setSpacing(6)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.sinusoidal_amplitude_slider = QtWidgets.QSlider(self.frame_28)
        self.sinusoidal_amplitude_slider.setOrientation(QtCore.Qt.Horizontal)
        self.sinusoidal_amplitude_slider.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.sinusoidal_amplitude_slider.setObjectName("sinusoidal_amplitude_slider")
        self.horizontalLayout_10.addWidget(self.sinusoidal_amplitude_slider)
        self.sinusoidal_amplitude_LCD = QtWidgets.QLCDNumber(self.frame_28)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sinusoidal_amplitude_LCD.sizePolicy().hasHeightForWidth())
        self.sinusoidal_amplitude_LCD.setSizePolicy(sizePolicy)
        self.sinusoidal_amplitude_LCD.setMaximumSize(QtCore.QSize(75, 35))
        self.sinusoidal_amplitude_LCD.setSmallDecimalPoint(False)
        self.sinusoidal_amplitude_LCD.setObjectName("sinusoidal_amplitude_LCD")
        self.horizontalLayout_10.addWidget(self.sinusoidal_amplitude_LCD)
        self.verticalLayout_19.addWidget(self.frame_28)
        self.horizontalLayout_5.addWidget(self.frame_24)
        self.frame_23 = QtWidgets.QFrame(self.frame_2)
        self.frame_23.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_23.setObjectName("frame_23")
        self.verticalLayout_18 = QtWidgets.QVBoxLayout(self.frame_23)
        self.verticalLayout_18.setContentsMargins(0, 5, 0, 0)
        self.verticalLayout_18.setSpacing(0)
        self.verticalLayout_18.setObjectName("verticalLayout_18")
        self.frame_25 = QtWidgets.QFrame(self.frame_23)
        self.frame_25.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_25.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_25.setObjectName("frame_25")
        self.verticalLayout_20 = QtWidgets.QVBoxLayout(self.frame_25)
        self.verticalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_20.setSpacing(0)
        self.verticalLayout_20.setObjectName("verticalLayout_20")
        self.label_5 = QtWidgets.QLabel(self.frame_25)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_20.addWidget(self.label_5)
        self.verticalLayout_18.addWidget(self.frame_25, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.frame_26 = QtWidgets.QFrame(self.frame_23)
        self.frame_26.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_26.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_26.setObjectName("frame_26")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.frame_26)
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_9.setSpacing(6)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.sinusoidal_phase_slider = QtWidgets.QSlider(self.frame_26)
        self.sinusoidal_phase_slider.setOrientation(QtCore.Qt.Horizontal)
        self.sinusoidal_phase_slider.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.sinusoidal_phase_slider.setObjectName("sinusoidal_phase_slider")
        self.horizontalLayout_9.addWidget(self.sinusoidal_phase_slider)
        self.sinusoidal_phase_LCD = QtWidgets.QLCDNumber(self.frame_26)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sinusoidal_phase_LCD.sizePolicy().hasHeightForWidth())
        self.sinusoidal_phase_LCD.setSizePolicy(sizePolicy)
        self.sinusoidal_phase_LCD.setMaximumSize(QtCore.QSize(75, 35))
        self.sinusoidal_phase_LCD.setSmallDecimalPoint(False)
        self.sinusoidal_phase_LCD.setObjectName("sinusoidal_phase_LCD")
        self.horizontalLayout_9.addWidget(self.sinusoidal_phase_LCD)
        self.verticalLayout_18.addWidget(self.frame_26)
        self.horizontalLayout_5.addWidget(self.frame_23)
        self.verticalLayout_3.addWidget(self.frame_2)
        self.verticalLayout_16.addWidget(self.frame)
        self.frame_5 = QtWidgets.QFrame(self.frame_21)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy)
        self.frame_5.setMaximumSize(QtCore.QSize(16777215, 40))
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frame_5)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.sample_sinusoidals_button = QtWidgets.QPushButton(self.frame_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sample_sinusoidals_button.sizePolicy().hasHeightForWidth())
        self.sample_sinusoidals_button.setSizePolicy(sizePolicy)
        self.sample_sinusoidals_button.setMinimumSize(QtCore.QSize(80, 30))
        self.sample_sinusoidals_button.setMaximumSize(QtCore.QSize(200, 35))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.sample_sinusoidals_button.setFont(font)
        self.sample_sinusoidals_button.setStyleSheet("\n"
"\n"
"QPushButton {\n"
"    background-color: rgb(0, 85, 255);\n"
"color:rgb(255, 255, 255);\n"
"border-radius:5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(0, 50, 150);\n"
"}\n"
"")
        self.sample_sinusoidals_button.setObjectName("sample_sinusoidals_button")
        self.horizontalLayout_6.addWidget(self.sample_sinusoidals_button)
        self.clear_composer_button = QtWidgets.QPushButton(self.frame_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.clear_composer_button.sizePolicy().hasHeightForWidth())
        self.clear_composer_button.setSizePolicy(sizePolicy)
        self.clear_composer_button.setMinimumSize(QtCore.QSize(80, 30))
        self.clear_composer_button.setMaximumSize(QtCore.QSize(200, 35))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.clear_composer_button.setFont(font)
        self.clear_composer_button.setStyleSheet("QPushButton {\n"
"    background-color: rgb(240, 0, 0);\n"
"color:rgb(255, 255, 255);\n"
"border-radius:5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(189, 0, 0);\n"
"}\n"
"")
        self.clear_composer_button.setObjectName("clear_composer_button")
        self.horizontalLayout_6.addWidget(self.clear_composer_button)
        self.verticalLayout_16.addWidget(self.frame_5)
        self.horizontalLayout_8.addWidget(self.frame_21)
        self.horizontalLayout_11.addWidget(self.tab1_2)
        self.WindowTabs.addTab(self.tab_2, "")
        self.verticalLayout.addWidget(self.WindowTabs)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.WindowTabs.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_4.setText(_translate("MainWindow", "Sampling Frequency"))
        self.label_3.setText(_translate("MainWindow", "SNR"))
        self.import_btn.setText(_translate("MainWindow", "Import"))
        self.clear_btn.setText(_translate("MainWindow", "Clear"))
        self.label_8.setText(_translate("MainWindow", "Fmax"))
        self.WindowTabs.setTabText(self.WindowTabs.indexOf(self.tab), _translate("MainWindow", "Viewer"))
        self.add_sinusoidal_button.setText(_translate("MainWindow", "Add"))
        self.delete_sinusoidal_button.setText(_translate("MainWindow", "Delete"))
        self.label_7.setText(_translate("MainWindow", "Frequency"))
        self.label_6.setText(_translate("MainWindow", "Amplitude"))
        self.label_5.setText(_translate("MainWindow", "Phase"))
        self.sample_sinusoidals_button.setText(_translate("MainWindow", "Sample"))
        self.clear_composer_button.setText(_translate("MainWindow", "Clear"))
        self.WindowTabs.setTabText(self.WindowTabs.indexOf(self.tab_2), _translate("MainWindow", "Composer"))
from pyqtgraph import PlotWidget


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
