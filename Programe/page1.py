# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog, QFileDialog




class Ui_DATAMINING(QDialog):
    def setupUi(self, DATAMINING):
        DATAMINING.setObjectName("DATAMINING")
        DATAMINING.resize(1920, 1000)
        DATAMINING.setStyleSheet("background-color: #E5E8E8;")
        self.browse = QtWidgets.QPushButton(DATAMINING)
        self.browse.setGeometry(QtCore.QRect(1390, 500, 170, 40))
        font = QtGui.QFont()
        font.setFamily("URW Bookman")
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(3)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.browse.setFont(font)
        self.browse.setStyleSheet("QPushButton{\n"
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
        icon.addPixmap(QtGui.QPixmap("/home/mherez/Documents/Documents/TP FD/Interface/icons8-import-64.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.browse.setIcon(icon)
        self.browse.setIconSize(QtCore.QSize(30, 30))
        self.browse.setObjectName("browse")
        self.widget = QtWidgets.QWidget(DATAMINING)
        self.widget.setGeometry(QtCore.QRect(360, -110, 1200, 560))
        self.widget.setStyleSheet("background-image: url(/home/mherez/Documents/Documents/TP FD/Interface/social-data-mining.png);")
        self.widget.setObjectName("widget")
        self.pushButton = QtWidgets.QPushButton(DATAMINING)
        self.pushButton.setGeometry(QtCore.QRect(1600, 890, 201, 51))
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
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("/home/mherez/Documents/Documents/TP FD/Interface/right.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.pushButton.setIcon(icon1)
        self.pushButton.setIconSize(QtCore.QSize(30, 30))
        self.pushButton.setObjectName("pushButton")
        self.layoutWidget = QtWidgets.QWidget(DATAMINING)
        self.layoutWidget.setGeometry(QtCore.QRect(460, 640, 711, 61))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.radioButton = QtWidgets.QRadioButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.radioButton.setFont(font)
        self.radioButton.setStyleSheet("QRadioButton {\n"
"   background-color: #E5E8E8;\n"
"   color: black;\n"
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
        self.horizontalLayout.addWidget(self.radioButton)
        self.radioButton_2 = QtWidgets.QRadioButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.radioButton_2.setFont(font)
        self.radioButton_2.setStyleSheet("QRadioButton {\n"
"   background-color: #E5E8E8;\n"
"   color: black;\n"
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
        self.horizontalLayout.addWidget(self.radioButton_2)
        self.textEdit = QtWidgets.QTextEdit(DATAMINING)
        self.textEdit.setGeometry(QtCore.QRect(360, 500, 900, 39))
        self.textEdit.setStyleSheet("QTextEdit{\n"
"    background: #FFFFFF;\n"
"    background-color:#CCD1D1;\n"
"    font: 25 11pt \"URW Bookman\";\n"
"    border: 2px solid #000000; \n"
"    border-radius: 5px; \n"
"    font-size:20px;\n"
"    color: #000000;\n"
"\n"
"}\n"
"QTextEdit:hover{\n"
"     border: 2px solid #6E89E2; \n"
"     background: #FFFFFF;\n"
"      background-color:#FFFFFF;\n"
"      color: #000000;\n"
"}")
        self.textEdit.setObjectName("textEdit")

        self.retranslateUi(DATAMINING)
        QtCore.QMetaObject.connectSlotsByName(DATAMINING)

    def retranslateUi(self, DATAMINING):
        _translate = QtCore.QCoreApplication.translate
        DATAMINING.setWindowTitle(_translate("DATAMINING", "DATA MINING"))
        self.browse.setText(_translate("DATAMINING", "Data"))
        self.pushButton.setText(_translate("DATAMINING", " Next"))
        self.radioButton.setText(_translate("DATAMINING", "Apprentissage Supervisé"))
        self.radioButton_2.setText(_translate("DATAMINING", "Apprentissage Non Supervisé"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    DATAMINING = QtWidgets.QMainWindow()
    ui = Ui_DATAMINING()
    ui.setupUi(DATAMINING)
    DATAMINING.show()
    
    

    sys.exit(app.exec_())
