# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'page3.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCan  
import matplotlib.pyplot as plt


class Ui_page3(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1920, 1080)
        MainWindow.setStyleSheet("background-color: #E5E8E8;\n"
"\n"
"\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(240, 120, 151, 41))
        self.pushButton.setStyleSheet("QPushButton{\n"
"    background: #FFFFFF;\n"
"    background-color:#CCD1D1;\n"
"    font: 25 11pt \"URW Bookman\";\n"
"    border: 2px solid #000000; \n"
"    border-radius: 5px; \n"
"    font-size:20px;\n"
"    color: #19060f;\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"     border: 2px solid #6E89E2; \n"
"     background: #FFFFFF;\n"
"      background-color:#FFFFFF;\n"
"      color: #000000;\n"
"}")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("box-plot.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.pushButton.setIcon(icon)
        self.pushButton.setAutoRepeatDelay(300)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(80, 60, 151, 41))
        self.pushButton_2.setStyleSheet("QPushButton{\n"
"    background: #FFFFFF;\n"
"    background-color:#CCD1D1;\n"
"    font: 25 11pt \"URW Bookman\";\n"
"    border: 2px solid #000000; \n"
"    border-radius: 5px; \n"
"    font-size:20px;\n"
"    color: #19060f;\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"     border: 2px solid #6E89E2; \n"
"     background: #FFFFFF;\n"
"      background-color:#FFFFFF;\n"
"      color: #000000;\n"
"}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(79, 120, 151, 41))
        self.pushButton_3.setStyleSheet("QPushButton{\n"
"    background: #FFFFFF;\n"
"    background-color:#CCD1D1;\n"
"    font: 25 11pt \"URW Bookman\";\n"
"    border: 2px solid #000000; \n"
"    border-radius: 5px; \n"
"    font-size:20px;\n"
"    color: #19060f;\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"     border: 2px solid #6E89E2; \n"
"     background: #FFFFFF;\n"
"      background-color:#FFFFFF;\n"
"      color: #000000;\n"
"}")
        self.pushButton_3.setObjectName("pushButton_3")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(330, 310, 113, 25))
        self.lineEdit.setStyleSheet("QLineEdit{\n"
"    background: #FFFFFF;\n"
"    background-color:#CCD1D1;\n"
"    font: 25 11pt \"URW Bookman\";\n"
"    border: 2px solid #000000; \n"
"    border-radius: 5px; \n"
"    font-size:20px;\n"
"    color: #000000;\n"
"\n"
"}\n"
"QLineEdit:hover{\n"
"     border: 2px solid #6E89E2; \n"
"     background: #FFFFFF;\n"
"      background-color:#FFFFFF;\n"
"      color: #000000;\n"
"}")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(330, 360, 113, 25))
        self.lineEdit_2.setStyleSheet("QLineEdit{\n"
"    background: #FFFFFF;\n"
"    background-color:#CCD1D1;\n"
"    font: 25 11pt \"URW Bookman\";\n"
"    border: 2px solid #000000; \n"
"    border-radius: 5px; \n"
"    font-size:20px;\n"
"    color: #000000;\n"
"\n"
"}\n"
"QLineEdit:hover{\n"
"     border: 2px solid #6E89E2; \n"
"     background: #FFFFFF;\n"
"      background-color:#FFFFFF;\n"
"      color: #000000;\n"
"}")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(320, 260, 161, 31))
        self.label.setStyleSheet("QLabel{\n"
" \n"
"   background-color: #E5E8E8;\n"
"    font: 25 11pt \"URW Bookman\";\n"
"    font-size:25px;\n"
"    color: #000000;\n"
"\n"
"}\n"
"")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(70, 260, 171, 31))
        self.label_2.setStyleSheet("QLabel{\n"
" \n"
"   background-color: #E5E8E8;\n"
"    font: 25 20pt \"URW Bookman\";\n"
"    font-size: 25px;\n"
"    color: #000000;\n"
"\n"
"}\n"
"")
        self.label_2.setObjectName("label_2")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(50, 600, 171, 41))
        self.pushButton_4.setAutoFillBackground(False)
        self.pushButton_4.setStyleSheet("QPushButton{\n"
"    background: #FFFFFF;\n"
"    background-color:#CCD1D1;\n"
"    font: 25 11pt \"URW Bookman\";\n"
"    border: 2px solid #000000; \n"
"    border-radius: 5px; \n"
"    font-size:20px;\n"
"    color: #19060f;\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"     border: 2px solid #6E89E2; \n"
"     background: #FFFFFF;\n"
"      background-color:#FFFFFF;\n"
"      color: #000000;\n"
"}")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("administration.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.pushButton_4.setIcon(icon)
        self.pushButton_4.setAutoRepeatDelay(296)
        self.pushButton_4.setObjectName("pushButton_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(60, 700, 201, 31))
        self.label_5.setStyleSheet("QLabel{\n"
" \n"
"   background-color: #E5E8E8;\n"
"    font: 25 11pt \"URW Bookman\";\n"
"    font-size:25px;\n"
"    color: #000000;\n"
"\n"
"}\n"
"")
        self.label_5.setObjectName("label_5")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(290, 700, 161, 41))
        self.textBrowser.setStyleSheet("QTextBrowser{\n"
" \n"
"   background-color: #E5E8E8;\n"
"    font: 25 11pt \"URW Bookman\";\n"
"    font-size:20px;\n"
"    border-radius: 20px;\n"
"    color: #000000;\n"
"\n"
"}\n"
"")
        self.textBrowser.setObjectName("textBrowser")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(70, 290, 235, 291))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.radioButton = QtWidgets.QRadioButton(self.layoutWidget)
        self.radioButton.setStyleSheet("QRadioButton {\n"
"   background-color: #E5E8E8;\n"
"   color: black;\n"
"   font: 25 15pt \"URW Bookman\";\n"
"   \n"
"}\n"
"QRadioButton::indicator {\n"
"   width: 10px;\n"
"   height: 10px;\n"
"   border-radius: 5px;\n"
"}\n"
"QRadioButton::indicator::unchecked{ \n"
"   border: 1px solid; \n"
"   border-color: #6E89E2;\n"
"   border-radius: 7px;\n"
"   background-color: #E5E8E8; \n"
"   width: 15px; \n"
"   height: 15px; \n"
"}\n"
"QRadioButton::indicator::checked{ \n"
"   border: 1px solid; \n"
"   border-color: #000000;\n"
"   border-radius: 8px;\n"
"   background-color: #6E89E2; \n"
"   width: 15px; \n"
"   height: 15px; \n"
"}\n"
"QRadioButton:hover{\n"
"\n"
"     color: #6E89E2;\n"
"     font: 25 11pt  #6E89E2;\n"
"}")
        self.radioButton.setObjectName("radioButton")
        self.verticalLayout.addWidget(self.radioButton)
        self.radioButton_2 = QtWidgets.QRadioButton(self.layoutWidget)
        self.radioButton_2.setStyleSheet("QRadioButton {\n"
"   background-color: #E5E8E8;\n"
"   color: black;\n"
"    font: 25 15pt \"URW Bookman\";\n"
"   \n"
"}\n"
"QRadioButton::indicator {\n"
"   width: 10px;\n"
"   height: 10px;\n"
"   border-radius: 5px;\n"
"}\n"
"QRadioButton::indicator::unchecked{ \n"
"   border: 1px solid; \n"
"   border-color: #6E89E2;\n"
"   border-radius: 7px;\n"
"   background-color: #E5E8E8; \n"
"   width: 15px; \n"
"   height: 15px; \n"
"}\n"
"QRadioButton::indicator::checked{ \n"
"   border: 1px solid; \n"
"   border-color: #000000;\n"
"   border-radius: 8px;\n"
"   background-color: #6E89E2; \n"
"   width: 15px; \n"
"   height: 15px; \n"
"}\n"
"QRadioButton:hover{\n"
"\n"
"     color: #6E89E2;\n"
"     font: 25 11pt  #6E89E2;\n"
"}")
        self.radioButton_2.setObjectName("radioButton_2")
        self.verticalLayout.addWidget(self.radioButton_2)
        self.radioButton_3 = QtWidgets.QRadioButton(self.layoutWidget)
        self.radioButton_3.setStyleSheet("QRadioButton {\n"
"   background-color: #E5E8E8;\n"
"   color: black;\n"
"   font: 25 15pt \"URW Bookman\";\n"
"   \n"
"}\n"
"QRadioButton::indicator {\n"
"   width: 10px;\n"
"   height: 10px;\n"
"   border-radius: 5px;\n"
"}\n"
"QRadioButton::indicator::unchecked{ \n"
"   border: 1px solid; \n"
"   border-color: #6E89E2;\n"
"   border-radius: 7px;\n"
"   background-color: #E5E8E8; \n"
"   width: 15px; \n"
"   height: 15px; \n"
"}\n"
"QRadioButton::indicator::checked{ \n"
"   border: 1px solid; \n"
"   border-color: #000000;\n"
"   border-radius: 8px;\n"
"   background-color: #6E89E2; \n"
"   width: 15px; \n"
"   height: 15px; \n"
"}\n"
"QRadioButton:hover{\n"
"\n"
"     color: #6E89E2;\n"
"     font: 25 11pt  #6E89E2;\n"
"}")
        self.radioButton_3.setObjectName("radioButton_3")
        self.verticalLayout.addWidget(self.radioButton_3)
        self.radioButton_4 = QtWidgets.QRadioButton(self.layoutWidget)
        self.radioButton_4.setStyleSheet("QRadioButton {\n"
"   background-color: #E5E8E8;\n"
"   color: black;\n"
"   font: 25 15pt \"URW Bookman\";\n"
"   \n"
"}\n"
"QRadioButton::indicator {\n"
"   width: 10px;\n"
"   height: 10px;\n"
"   border-radius: 5px;\n"
"}\n"
"QRadioButton::indicator::unchecked{ \n"
"   border: 1px solid; \n"
"   border-color: #6E89E2;\n"
"   border-radius: 7px;\n"
"   background-color: #E5E8E8; \n"
"   width: 15px; \n"
"   height: 15px; \n"
"}\n"
"QRadioButton::indicator::checked{ \n"
"   border: 1px solid; \n"
"   border-color: #000000;\n"
"   border-radius: 8px;\n"
"   background-color: #6E89E2; \n"
"   width: 15px; \n"
"   height: 15px; \n"
"}\n"
"QRadioButton:hover{\n"
"\n"
"     color: #6E89E2;\n"
"     font: 25 11pt  #6E89E2;\n"
"}")
        self.radioButton_4.setObjectName("radioButton_4")
        self.verticalLayout.addWidget(self.radioButton_4)
        self.radioButton_5 = QtWidgets.QRadioButton(self.layoutWidget)
        self.radioButton_5.setStyleSheet("QRadioButton {\n"
"   background-color: #E5E8E8;\n"
"   color: black;\n"
"   font: 25 15pt \"URW Bookman\";\n"
"   \n"
"}\n"
"QRadioButton::indicator {\n"
"   width: 10px;\n"
"   height: 10px;\n"
"   border-radius: 5px;\n"
"}\n"
"QRadioButton::indicator::unchecked{ \n"
"   border: 1px solid; \n"
"   border-color: #6E89E2;\n"
"   border-radius: 7px;\n"
"   background-color: #E5E8E8; \n"
"   width: 15px; \n"
"   height: 15px; \n"
"}\n"
"QRadioButton::indicator::checked{ \n"
"   border: 1px solid; \n"
"   border-color: #000000;\n"
"   border-radius: 8px;\n"
"   background-color: #6E89E2; \n"
"   width: 15px; \n"
"   height: 15px; \n"
"}\n"
"QRadioButton:hover{\n"
"\n"
"     color: #6E89E2;\n"
"     font: 25 11pt  #6E89E2;\n"
"}")
        self.radioButton_5.setObjectName("radioButton_5")
        self.verticalLayout.addWidget(self.radioButton_5)
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(986, 41, 459, 462))
        self.frame_2.setStyleSheet("border-radius: 20px;")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setGeometry(QtCore.QRect(1451, 41, 459, 462))
        self.frame_3.setStyleSheet("border-radius: 20px;")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.frame_4 = QtWidgets.QFrame(self.centralwidget)
        self.frame_4.setGeometry(QtCore.QRect(521, 509, 459, 461))
        self.frame_4.setStyleSheet("border-radius: 20px;")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.frame_5 = QtWidgets.QFrame(self.centralwidget)
        self.frame_5.setGeometry(QtCore.QRect(986, 509, 459, 461))
        self.frame_5.setStyleSheet("border-radius: 20px;")
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.frame_6 = QtWidgets.QFrame(self.centralwidget)
        self.frame_6.setGeometry(QtCore.QRect(1451, 509, 459, 461))
        self.frame_6.setBaseSize(QtCore.QSize(0, 3))
        self.frame_6.setStyleSheet("border-radius: 20px;")
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(520, 40, 461, 461))
        self.tableWidget.setStyleSheet("border-radius: 20px;")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(240, 60, 151, 41))
        self.pushButton_5.setStyleSheet("QPushButton{\n"
"    background: #FFFFFF;\n"
"    background-color:#CCD1D1;\n"
"    font: 25 11pt \"URW Bookman\";\n"
"    border: 2px solid #000000; \n"
"    border-radius: 5px; \n"
"    font-size:20px;\n"
"    color: #19060f;\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"     border: 2px solid #6E89E2; \n"
"     background: #FFFFFF;\n"
"      background-color:#FFFFFF;\n"
"      color: #000000;\n"
"}")
        self.pushButton_5.setObjectName("pushButton_5")
        self.textBrowser_3 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_3.setGeometry(QtCore.QRect(290, 770, 161, 41))
        self.textBrowser_3.setStyleSheet("QTextBrowser{\n"
" \n"
"   background-color: #E5E8E8;\n"
"    font: 25 11pt \"URW Bookman\";\n"
"    font-size:20px;\n"
"    border-radius: 20px;\n"
"    color: #000000;\n"
"\n"
"}\n"
"")
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(60, 770, 201, 31))
        self.label_6.setStyleSheet("QLabel{\n"
" \n"
"   background-color: #E5E8E8;\n"
"    font: 25 11pt \"URW Bookman\";\n"
"    font-size:25px;\n"
"    color: #000000;\n"
"\n"
"}\n"
"")
        self.label_6.setObjectName("label_6")
        self.textBrowser_4 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_4.setGeometry(QtCore.QRect(290, 840, 161, 41))
        self.textBrowser_4.setStyleSheet("QTextBrowser{\n"
" \n"
"   background-color: #E5E8E8;\n"
"    font: 25 11pt \"URW Bookman\";\n"
"    font-size:20px;\n"
"    border-radius: 20px;\n"
"    color: #000000;\n"
"\n"
"}\n"
"")
        self.textBrowser_4.setObjectName("textBrowser_4")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(60, 840, 201, 31))
        self.label_7.setStyleSheet("QLabel{\n"
" \n"
"   background-color: #E5E8E8;\n"
"    font: 25 11pt \"URW Bookman\";\n"
"    font-size:25px;\n"
"    color: #000000;\n"
"\n"
"}\n"
"")
        self.label_7.setObjectName("label_7")
        self.textBrowser_5 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_5.setGeometry(QtCore.QRect(250, 930, 161, 41))
        self.textBrowser_5.setStyleSheet("QTextBrowser{\n"
" \n"
"   background-color: #E5E8E8;\n"
"    font: 25 11pt \"URW Bookman\";\n"
"    font-size:20px;\n"
"    border-radius: 20px;\n"
"    color: #000000;\n"
"\n"
"}\n"
"")
        self.textBrowser_5.setObjectName("textBrowser_5")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(60, 910, 161, 31))
        self.label_8.setStyleSheet("QLabel{\n"
" \n"
"   background-color: #E5E8E8;\n"
"    font: 25 11pt \"URW Bookman\";\n"
"    font-size:25px;\n"
"    color: #000000;\n"
"\n"
"}\n"
"")
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(60, 940, 161, 31))
        self.label_9.setStyleSheet("QLabel{\n"
" \n"
"   background-color: #E5E8E8;\n"
"    font: 25 11pt \"URW Bookman\";\n"
"    font-size:25px;\n"
"    color: #000000;\n"
"\n"
"}\n"
"")
        self.label_9.setObjectName("label_9")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(150, 180, 171, 41))
        self.pushButton_6.setStyleSheet("QPushButton{\n"
"    background: #FFFFFF;\n"
"    background-color:#CCD1D1;\n"
"    font: 25 11pt \"URW Bookman\";\n"
"    border: 2px solid #000000; \n"
"    border-radius: 5px; \n"
"    font-size:20px;\n"
"    color: #19060f;\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"     border: 2px solid #6E89E2; \n"
"     background: #FFFFFF;\n"
"      background-color:#FFFFFF;\n"
"      color: #000000;\n"
"}")
        self.pushButton_6.setObjectName("pushButton_6")
        # oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo
        self.horizontalLayout_12 = QtWidgets.QVBoxLayout(self.frame_2)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.figure = plt.figure(facecolor="#E5E8E8")
        self.canvas2 = FigureCan(self.figure)
        self.horizontalLayout_12.addWidget(self.canvas2)
        # oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo
        self.horizontalLayout_13 = QtWidgets.QVBoxLayout(self.frame_3)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.canvas3 = FigureCan(self.figure)
        self.horizontalLayout_13.addWidget(self.canvas3)
        # oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo
        self.horizontalLayout_14 = QtWidgets.QVBoxLayout(self.frame_4)
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.canvas4 = FigureCan(self.figure)
        self.horizontalLayout_14.addWidget(self.canvas4)
        # oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo
        self.horizontalLayout_15 = QtWidgets.QVBoxLayout(self.frame_5)
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.canvas5 = FigureCan(self.figure)
        self.horizontalLayout_15.addWidget(self.canvas5)
        # oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo
        self.horizontalLayout_16 = QtWidgets.QVBoxLayout(self.frame_6)
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.canvas6 = FigureCan(self.figure)
        self.horizontalLayout_16.addWidget(self.canvas6)
        # oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo

        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(240, 600,  171, 41))
        self.pushButton_7.setStyleSheet("QPushButton{\n"
        "    background: #FFFFFF;\n"
        "    background-color:#CCD1D1;\n"
        "    font: 25 11pt \"URW Bookman\";\n"
        "    border: 2px solid #000000; \n"
        "    border-radius: 5px; \n"
        "    font-size:20px;\n"
        "    color: #19060f;\n"
        "\n"
        "}\n"
        "QPushButton:hover{\n"
        "     border: 2px solid #6E89E2; \n"
        "     background: #FFFFFF;\n"
        "      background-color:#FFFFFF;\n"
        "      color: #000000;\n"
        "}")
        self.pushButton_7.setObjectName("pushButton_7")        



        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Apprentissage Non Supervisé"))
        self.pushButton.setText(_translate("MainWindow", "Box-Plot"))
        self.pushButton_2.setText(_translate("MainWindow", "Data-Num"))
        self.pushButton_3.setText(_translate("MainWindow", "Vésualisation"))
        self.label.setText(_translate("MainWindow", "Paramètres :"))
        self.label_2.setText(_translate("MainWindow", "Algorithme :"))
        self.pushButton_4.setText(_translate("MainWindow", " Exécuter"))
        self.label_5.setText(_translate("MainWindow", "inertie intra :"))
        self.radioButton.setText(_translate("MainWindow", "K-means "))
        self.radioButton_2.setText(_translate("MainWindow", "K-Medoids "))
        self.radioButton_3.setText(_translate("MainWindow", "AGNES "))
        self.radioButton_4.setText(_translate("MainWindow", "DIANA "))
        self.radioButton_5.setText(_translate("MainWindow", "DBScan "))
        self.pushButton_5.setText(_translate("MainWindow", "Normalisation"))
        self.label_6.setText(_translate("MainWindow", "inertie intre :"))
        self.label_7.setText(_translate("MainWindow", "inertie total :"))
        self.label_8.setText(_translate("MainWindow", "coefficient de corrélation :"))
        self.label_9.setText(_translate("MainWindow", " corrélation :"))
        self.pushButton_6.setText(_translate("MainWindow", "courbe d’Elbow"))
        self.pushButton_7.setText(_translate("MainWindow", "comparaison "))


"""
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_page3()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

"""