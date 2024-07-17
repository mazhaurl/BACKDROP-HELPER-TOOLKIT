

################################################################################
## Form generated from reading UI file 'Backdrop_toolkit_v009EaWROv.ui'
##
## BACKDROP HELPER TOOLKIT 4.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################
import nuke
import nukescripts
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(662, 707)
        self.layoutWidget = QWidget(Form)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 10, 431, 628))
        self.Color_palate = QGridLayout(self.layoutWidget)
        self.Color_palate.setObjectName(u"Color_palate")
        self.Color_palate.setContentsMargins(0, 0, 0, 0)
        self.pushButton_3 = QPushButton(self.layoutWidget)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.Color_palate.addWidget(self.pushButton_3, 3, 2, 1, 1)

        self.label_9 = QLabel(self.layoutWidget)
        self.label_9.setObjectName(u"label_9")

        self.Color_palate.addWidget(self.label_9, 7, 0, 1, 1, Qt.AlignRight)

        self.pushButton_9 = QPushButton(self.layoutWidget)
        self.pushButton_9.setObjectName(u"pushButton_9")

        self.Color_palate.addWidget(self.pushButton_9, 9, 2, 1, 1)

        self.pushButton_10 = QPushButton(self.layoutWidget)
        self.pushButton_10.setObjectName(u"pushButton_10")

        self.Color_palate.addWidget(self.pushButton_10, 13, 2, 1, 1)

        self.pushButton_4 = QPushButton(self.layoutWidget)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.Color_palate.addWidget(self.pushButton_4, 12, 1, 1, 1)

        self.pushButton_7 = QPushButton(self.layoutWidget)
        self.pushButton_7.setObjectName(u"pushButton_7")

        self.Color_palate.addWidget(self.pushButton_7, 13, 1, 1, 1)

        self.label_10 = QLabel(self.layoutWidget)
        self.label_10.setObjectName(u"label_10")

        self.Color_palate.addWidget(self.label_10, 13, 0, 1, 1, Qt.AlignRight)

        self.pushButton_2 = QPushButton(self.layoutWidget)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.Color_palate.addWidget(self.pushButton_2, 8, 1, 1, 4)

        self.pushButton_13 = QPushButton(self.layoutWidget)
        self.pushButton_13.setObjectName(u"pushButton_13")

        self.Color_palate.addWidget(self.pushButton_13, 3, 3, 1, 1)

        self.pushButton = QPushButton(self.layoutWidget)
        self.pushButton.setObjectName(u"pushButton")

        self.Color_palate.addWidget(self.pushButton, 3, 1, 1, 1)

        self.pushButton_14 = QPushButton(self.layoutWidget)
        self.pushButton_14.setObjectName(u"pushButton_14")

        self.Color_palate.addWidget(self.pushButton_14, 4, 4, 1, 1)

        self.pushButton_12 = QPushButton(self.layoutWidget)
        self.pushButton_12.setObjectName(u"pushButton_12")

        self.Color_palate.addWidget(self.pushButton_12, 4, 2, 1, 1)

        self.pushButton_15 = QPushButton(self.layoutWidget)
        self.pushButton_15.setObjectName(u"pushButton_15")

        self.Color_palate.addWidget(self.pushButton_15, 4, 3, 1, 1)

        self.label_5 = QLabel(self.layoutWidget)
        self.label_5.setObjectName(u"label_5")

        self.Color_palate.addWidget(self.label_5, 16, 0, 1, 1, Qt.AlignRight)

        self.label_8 = QLabel(self.layoutWidget)
        self.label_8.setObjectName(u"label_8")

        self.Color_palate.addWidget(self.label_8, 9, 0, 1, 1, Qt.AlignRight)

        self.pushButton_16 = QPushButton(self.layoutWidget)
        self.pushButton_16.setObjectName(u"pushButton_16")

        self.Color_palate.addWidget(self.pushButton_16, 3, 4, 1, 1)

        self.groupBox_2 = QGroupBox(self.layoutWidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.gridLayout = QGridLayout(self.groupBox_2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.button55 = QPushButton(self.groupBox_2)
        self.button55.setObjectName(u"button55")
        self.button55.setStyleSheet(u"background-color: rgb(30, 30, 30);")

        self.horizontalLayout_10.addWidget(self.button55)

        self.button56 = QPushButton(self.groupBox_2)
        self.button56.setObjectName(u"button56")
        self.button56.setStyleSheet(u"background-color: rgb(50,50,50);")

        self.horizontalLayout_10.addWidget(self.button56)

        self.button57 = QPushButton(self.groupBox_2)
        self.button57.setObjectName(u"button57")
        self.button57.setStyleSheet(u"background-color: rgb(100,100,100);")

        self.horizontalLayout_10.addWidget(self.button57)

        self.button58 = QPushButton(self.groupBox_2)
        self.button58.setObjectName(u"button58")
        self.button58.setStyleSheet(u"background-color: rgb(150,150,150);")

        self.horizontalLayout_10.addWidget(self.button58)

        self.button59 = QPushButton(self.groupBox_2)
        self.button59.setObjectName(u"button59")
        self.button59.setStyleSheet(u"background-color: rgb(200,200,200);")

        self.horizontalLayout_10.addWidget(self.button59)

        self.button60 = QPushButton(self.groupBox_2)
        self.button60.setObjectName(u"button60")
        self.button60.setStyleSheet(u"background-color: rgb(229, 231, 233 );")

        self.horizontalLayout_10.addWidget(self.button60)


        self.gridLayout.addLayout(self.horizontalLayout_10, 6, 0, 1, 1)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.button49 = QPushButton(self.groupBox_2)
        self.button49.setObjectName(u"button49")
        self.button49.setStyleSheet(u"background-color: rgb(79, 55, 0);")

        self.horizontalLayout_9.addWidget(self.button49)

        self.button50 = QPushButton(self.groupBox_2)
        self.button50.setObjectName(u"button50")
        self.button50.setStyleSheet(u"background-color: rgb(122, 63, 15);")

        self.horizontalLayout_9.addWidget(self.button50)

        self.button51 = QPushButton(self.groupBox_2)
        self.button51.setObjectName(u"button51")
        self.button51.setStyleSheet(u"background-color: rgb(177, 99, 9);")

        self.horizontalLayout_9.addWidget(self.button51)

        self.button52 = QPushButton(self.groupBox_2)
        self.button52.setObjectName(u"button52")
        self.button52.setStyleSheet(u"background-color: rgb(150, 107, 47);")

        self.horizontalLayout_9.addWidget(self.button52)

        self.button53 = QPushButton(self.groupBox_2)
        self.button53.setObjectName(u"button53")
        self.button53.setStyleSheet(u"background-color: rgb(189, 147, 41);")

        self.horizontalLayout_9.addWidget(self.button53)

        self.button54 = QPushButton(self.groupBox_2)
        self.button54.setObjectName(u"button54")
        self.button54.setStyleSheet(u"background-color: rgb(221, 188, 0);")

        self.horizontalLayout_9.addWidget(self.button54)


        self.gridLayout.addLayout(self.horizontalLayout_9, 1, 0, 1, 1)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.button19 = QPushButton(self.groupBox_2)
        self.button19.setObjectName(u"button19")
        self.button19.setStyleSheet(u"background-color: rgb(74, 35, 90 );")

        self.horizontalLayout_4.addWidget(self.button19)

        self.button20 = QPushButton(self.groupBox_2)
        self.button20.setObjectName(u"button20")
        self.button20.setStyleSheet(u"background-color: rgb(108, 52, 131 );")

        self.horizontalLayout_4.addWidget(self.button20)

        self.button21 = QPushButton(self.groupBox_2)
        self.button21.setObjectName(u"button21")
        self.button21.setStyleSheet(u"background-color: rgb(142, 68, 173 );")

        self.horizontalLayout_4.addWidget(self.button21)

        self.button22 = QPushButton(self.groupBox_2)
        self.button22.setObjectName(u"button22")
        self.button22.setStyleSheet(u"background-color: rgb(165, 105, 189 )")

        self.horizontalLayout_4.addWidget(self.button22)

        self.button23 = QPushButton(self.groupBox_2)
        self.button23.setObjectName(u"button23")
        self.button23.setStyleSheet(u"background-color: rgb(210, 180, 222 );")

        self.horizontalLayout_4.addWidget(self.button23)

        self.button24 = QPushButton(self.groupBox_2)
        self.button24.setObjectName(u"button24")
        self.button24.setStyleSheet(u"background-color: rgb(244, 236, 247);")

        self.horizontalLayout_4.addWidget(self.button24)


        self.gridLayout.addLayout(self.horizontalLayout_4, 3, 0, 1, 1)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.button43 = QPushButton(self.groupBox_2)
        self.button43.setObjectName(u"button43")
        self.button43.setStyleSheet(u"background-color: rgb(89, 106, 34);")

        self.horizontalLayout_8.addWidget(self.button43)

        self.button44 = QPushButton(self.groupBox_2)
        self.button44.setObjectName(u"button44")
        self.button44.setStyleSheet(u"background-color: rgb(159, 180, 82);")

        self.horizontalLayout_8.addWidget(self.button44)

        self.button45 = QPushButton(self.groupBox_2)
        self.button45.setObjectName(u"button45")
        self.button45.setStyleSheet(u"background-color: rgb(108, 168, 80);")

        self.horizontalLayout_8.addWidget(self.button45)

        self.button46 = QPushButton(self.groupBox_2)
        self.button46.setObjectName(u"button46")
        self.button46.setStyleSheet(u"background-color: rgb(163, 212, 0);")

        self.horizontalLayout_8.addWidget(self.button46)

        self.button47 = QPushButton(self.groupBox_2)
        self.button47.setObjectName(u"button47")
        self.button47.setStyleSheet(u"background-color: rgb(167, 213, 97);")

        self.horizontalLayout_8.addWidget(self.button47)

        self.button48 = QPushButton(self.groupBox_2)
        self.button48.setObjectName(u"button48")
        self.button48.setStyleSheet(u"background-color: rgb(191, 255, 42);")

        self.horizontalLayout_8.addWidget(self.button48)


        self.gridLayout.addLayout(self.horizontalLayout_8, 4, 0, 1, 1)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.button13 = QPushButton(self.groupBox_2)
        self.button13.setObjectName(u"button13")
        self.button13.setStyleSheet(u"background-color: rgb(100, 30, 22)")

        self.horizontalLayout_3.addWidget(self.button13)

        self.button14 = QPushButton(self.groupBox_2)
        self.button14.setObjectName(u"button14")
        self.button14.setStyleSheet(u"background-color: rgb(148, 49, 38)")

        self.horizontalLayout_3.addWidget(self.button14)

        self.button15 = QPushButton(self.groupBox_2)
        self.button15.setObjectName(u"button15")
        self.button15.setStyleSheet(u"background-color: rgb(176, 58, 46)")

        self.horizontalLayout_3.addWidget(self.button15)

        self.button16 = QPushButton(self.groupBox_2)
        self.button16.setObjectName(u"button16")
        self.button16.setStyleSheet(u"background-color: rgb(231, 76, 60)")

        self.horizontalLayout_3.addWidget(self.button16)

        self.button17 = QPushButton(self.groupBox_2)
        self.button17.setObjectName(u"button17")
        self.button17.setStyleSheet(u"background-color: rgb(236, 112, 99)")

        self.horizontalLayout_3.addWidget(self.button17)

        self.button18 = QPushButton(self.groupBox_2)
        self.button18.setObjectName(u"button18")
        self.button18.setStyleSheet(u"background-color: rgb(217, 136, 128);")

        self.horizontalLayout_3.addWidget(self.button18)


        self.gridLayout.addLayout(self.horizontalLayout_3, 0, 0, 1, 1)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.button55_2 = QPushButton(self.groupBox_2)
        self.button55_2.setObjectName(u"button55_2")
        self.button55_2.setStyleSheet(u"background-color: rgb(23, 32, 42);")

        self.horizontalLayout_11.addWidget(self.button55_2)

        self.button56_2 = QPushButton(self.groupBox_2)
        self.button56_2.setObjectName(u"button56_2")
        self.button56_2.setStyleSheet(u"background-color: rgb(33, 47, 61);")

        self.horizontalLayout_11.addWidget(self.button56_2)

        self.button57_2 = QPushButton(self.groupBox_2)
        self.button57_2.setObjectName(u"button57_2")
        self.button57_2.setStyleSheet(u"background-color: rgb(44, 62, 80);")

        self.horizontalLayout_11.addWidget(self.button57_2)

        self.button58_2 = QPushButton(self.groupBox_2)
        self.button58_2.setObjectName(u"button58_2")
        self.button58_2.setStyleSheet(u"background-color: rgb(128, 139, 150);")

        self.horizontalLayout_11.addWidget(self.button58_2)

        self.button59_2 = QPushButton(self.groupBox_2)
        self.button59_2.setObjectName(u"button59_2")
        self.button59_2.setStyleSheet(u"background-color: rgb(171, 178, 185);")

        self.horizontalLayout_11.addWidget(self.button59_2)

        self.button60_2 = QPushButton(self.groupBox_2)
        self.button60_2.setObjectName(u"button60_2")
        self.button60_2.setStyleSheet(u"background-color: rgb(213, 216, 220 );")

        self.horizontalLayout_11.addWidget(self.button60_2)


        self.gridLayout.addLayout(self.horizontalLayout_11, 7, 0, 1, 1)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.button25 = QPushButton(self.groupBox_2)
        self.button25.setObjectName(u"button25")
        self.button25.setStyleSheet(u"background-color: rgb(02, 70, 0);")

        self.horizontalLayout_5.addWidget(self.button25)

        self.button26 = QPushButton(self.groupBox_2)
        self.button26.setObjectName(u"button26")
        self.button26.setStyleSheet(u"background-color: rgb(4, 113, 0);")

        self.horizontalLayout_5.addWidget(self.button26)

        self.button27 = QPushButton(self.groupBox_2)
        self.button27.setObjectName(u"button27")
        self.button27.setStyleSheet(u"background-color: rgb(60, 93, 59);")

        self.horizontalLayout_5.addWidget(self.button27)

        self.button28 = QPushButton(self.groupBox_2)
        self.button28.setObjectName(u"button28")
        self.button28.setStyleSheet(u"background-color: rgb(30, 132, 73);")

        self.horizontalLayout_5.addWidget(self.button28)

        self.button29 = QPushButton(self.groupBox_2)
        self.button29.setObjectName(u"button29")
        self.button29.setStyleSheet(u"background-color: rgb(76, 122, 75);")

        self.horizontalLayout_5.addWidget(self.button29)

        self.button30 = QPushButton(self.groupBox_2)
        self.button30.setObjectName(u"button30")
        self.button30.setStyleSheet(u"background-color: rgb(82, 190, 128);")

        self.horizontalLayout_5.addWidget(self.button30)


        self.gridLayout.addLayout(self.horizontalLayout_5, 5, 0, 1, 1)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.button31 = QPushButton(self.groupBox_2)
        self.button31.setObjectName(u"button31")
        self.button31.setStyleSheet(u"background-color: rgb(27, 79, 114 );")

        self.horizontalLayout_6.addWidget(self.button31)

        self.button32 = QPushButton(self.groupBox_2)
        self.button32.setObjectName(u"button32")
        self.button32.setStyleSheet(u"background-color: rgb(40, 116, 166 );")

        self.horizontalLayout_6.addWidget(self.button32)

        self.button33 = QPushButton(self.groupBox_2)
        self.button33.setObjectName(u"button33")
        self.button33.setStyleSheet(u"background-color: rgb(52, 152, 219 );")

        self.horizontalLayout_6.addWidget(self.button33)

        self.button34 = QPushButton(self.groupBox_2)
        self.button34.setObjectName(u"button34")
        self.button34.setStyleSheet(u"background-color: rgb(133, 193, 233);")

        self.horizontalLayout_6.addWidget(self.button34)

        self.button35 = QPushButton(self.groupBox_2)
        self.button35.setObjectName(u"button35")
        self.button35.setStyleSheet(u"background-color: rgb(174, 214, 241 );")

        self.horizontalLayout_6.addWidget(self.button35)

        self.button36 = QPushButton(self.groupBox_2)
        self.button36.setObjectName(u"button36")
        self.button36.setStyleSheet(u"background-color: rgb(214, 234, 248);")

        self.horizontalLayout_6.addWidget(self.button36)


        self.gridLayout.addLayout(self.horizontalLayout_6, 2, 0, 1, 1)


        self.Color_palate.addWidget(self.groupBox_2, 14, 1, 1, 4)

        self.textEdit = QTextEdit(self.layoutWidget)
        self.textEdit.setObjectName(u"textEdit")

        self.Color_palate.addWidget(self.textEdit, 7, 1, 1, 4)

        self.pushButton_11 = QPushButton(self.layoutWidget)
        self.pushButton_11.setObjectName(u"pushButton_11")

        self.Color_palate.addWidget(self.pushButton_11, 4, 1, 1, 1)

        self.label_6 = QLabel(self.layoutWidget)
        self.label_6.setObjectName(u"label_6")

        self.Color_palate.addWidget(self.label_6, 3, 0, 1, 1, Qt.AlignRight)

        self.pushButton_5 = QPushButton(self.layoutWidget)
        self.pushButton_5.setObjectName(u"pushButton_5")

        self.Color_palate.addWidget(self.pushButton_5, 12, 2, 1, 1)

        self.pushButton_8 = QPushButton(self.layoutWidget)
        self.pushButton_8.setObjectName(u"pushButton_8")

        self.Color_palate.addWidget(self.pushButton_8, 9, 1, 1, 1)

        self.label_4 = QLabel(self.layoutWidget)
        self.label_4.setObjectName(u"label_4")

        self.Color_palate.addWidget(self.label_4, 12, 0, 1, 1, Qt.AlignRight)

        self.label = QLabel(self.layoutWidget)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)

        self.Color_palate.addWidget(self.label, 1, 1, 1, 4, Qt.AlignHCenter)

        self.pushButton_6 = QPushButton(self.layoutWidget)
        self.pushButton_6.setObjectName(u"pushButton_6")

        self.Color_palate.addWidget(self.pushButton_6, 16, 1, 1, 4)

        self.line = QFrame(self.layoutWidget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.Color_palate.addWidget(self.line, 2, 1, 1, 4)

        self.line_3 = QFrame(self.layoutWidget)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.Color_palate.addWidget(self.line_3, 15, 0, 1, 5)

        self.line_4 = QFrame(self.layoutWidget)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.HLine)
        self.line_4.setFrameShadow(QFrame.Sunken)

        self.Color_palate.addWidget(self.line_4, 10, 0, 2, 5)

        self.line_6 = QFrame(self.layoutWidget)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setFrameShape(QFrame.HLine)
        self.line_6.setFrameShadow(QFrame.Sunken)

        self.Color_palate.addWidget(self.line_6, 6, 0, 1, 5)

        self.label_11 = QLabel(self.layoutWidget)
        self.label_11.setObjectName(u"label_11")

        self.Color_palate.addWidget(self.label_11, 14, 0, 1, 1, Qt.AlignHCenter)

        self.layoutWidget1 = QWidget(Form)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(10, 650, 431, 43))
        self.Developer = QVBoxLayout(self.layoutWidget1)
        self.Developer.setObjectName(u"Developer")
        self.Developer.setContentsMargins(0, 0, 0, 0)
        self.line_2 = QFrame(self.layoutWidget1)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.Developer.addWidget(self.line_2)

        self.label_2 = QLabel(self.layoutWidget1)
        self.label_2.setObjectName(u"label_2")

        self.Developer.addWidget(self.label_2)

        self.label_7 = QLabel(self.layoutWidget1)
        self.label_7.setObjectName(u"label_7")
        font1 = QFont()
        font1.setItalic(True)
        self.label_7.setFont(font1)

        self.Developer.addWidget(self.label_7)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.pushButton_3.setText(QCoreApplication.translate("Form", u"++\u25ba", None))
        self.label_9.setText(QCoreApplication.translate("Form", u"Label", None))
        self.pushButton_9.setText(QCoreApplication.translate("Form", u"Down\u25bc", None))
        self.pushButton_10.setText(QCoreApplication.translate("Form", u"-------", None))
        self.pushButton_4.setText(QCoreApplication.translate("Form", u"Fill", None))
        self.pushButton_7.setText(QCoreApplication.translate("Form", u"++++", None))
        self.label_10.setText(QCoreApplication.translate("Form", u"Border", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"Set Label", None))
        self.pushButton_13.setText(QCoreApplication.translate("Form", u" \u25c4--", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"\u25c4++", None))
        self.pushButton_14.setText(QCoreApplication.translate("Form", u"\u25bc--", None))
        self.pushButton_12.setText(QCoreApplication.translate("Form", u"\u25bc++", None))
        self.pushButton_15.setText(QCoreApplication.translate("Form", u"\u25b2--", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"Custom Color", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"Font Size", None))
        self.pushButton_16.setText(QCoreApplication.translate("Form", u"\u25ba--", None))
        self.groupBox_2.setTitle("")
        self.button55.setText("")
        self.button56.setText("")
        self.button57.setText("")
        self.button58.setText("")
        self.button59.setText("")
        self.button60.setText("")
        self.button49.setText("")
        self.button50.setText("")
        self.button51.setText("")
        self.button52.setText("")
        self.button53.setText("")
        self.button54.setText("")
        self.button19.setText("")
        self.button20.setText("")
        self.button21.setText("")
        self.button22.setText("")
        self.button23.setText("")
        self.button24.setText("")
        self.button43.setText("")
        self.button44.setText("")
        self.button45.setText("")
        self.button46.setText("")
        self.button47.setText("")
        self.button48.setText("")
        self.button13.setText("")
        self.button14.setText("")
        self.button15.setText("")
        self.button16.setText("")
        self.button17.setText("")
        self.button18.setText("")
        self.button55_2.setText("")
        self.button56_2.setText("")
        self.button57_2.setText("")
        self.button58_2.setText("")
        self.button59_2.setText("")
        self.button60_2.setText("")
        self.button25.setText("")
        self.button26.setText("")
        self.button27.setText("")
        self.button28.setText("")
        self.button29.setText("")
        self.button30.setText("")
        self.button31.setText("")
        self.button32.setText("")
        self.button33.setText("")
        self.button34.setText("")
        self.button35.setText("")
        self.button36.setText("")
        self.pushButton_11.setText(QCoreApplication.translate("Form", u"\u25b2++ ", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"Cover Area", None))
        self.pushButton_5.setText(QCoreApplication.translate("Form", u"Border", None))
        self.pushButton_8.setText(QCoreApplication.translate("Form", u"UP\u25b2", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"Color Style", None))
        self.label.setText(QCoreApplication.translate("Form", u"BACKDROP HELPER TOOLKIT", None))
        self.pushButton_6.setText(QCoreApplication.translate("Form", u"Select Custom Color", None))
        self.label_11.setText(QCoreApplication.translate("Form", u"Color Preset", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Developed by Mazhaurl Islam Shuvo @2024", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"www.shuvofx.com", None))
    # retranslateUi














#############################################################

#DESIGN END

###############################################################

# Hex to RGB


def hex_color_to_rgb(red, green, blue):
    return int('%02x%02x%02x%02x' % (int(red*255),int(green*255),int(blue*255),255),16)


############################# MAIN CODE START #####################


class backdrop_helper_toolkit(QWidget, Ui_Form):
    def __init__(self):
        super(backdrop_helper_toolkit, self).__init__()
        self.setupUi(self) 


        #expand_area_left
        self.pushButton.clicked.connect(self.expand_area)


        #expand_area_rigiht
        self.pushButton_3.clicked.connect(self.expand_area_rigiht)

        #expand_area_bottom
        self.pushButton_12.clicked.connect(self.expand_area_bottom)

        #expand_area_top
        self.pushButton_11.clicked.connect(self.expand_area_top)

        #down_area_top
        self.pushButton_15.clicked.connect(self.down_area_top)

        #down_area_left
        self.pushButton_13.clicked.connect(self.down_area_left)

        #down_area_right
        self.pushButton_16.clicked.connect(self.down_area_right)

        #down_area_down
        self.pushButton_14.clicked.connect(self.down_area_down)





        #Label
        self.pushButton_2.clicked.connect(self.set_label)

        #font_UP
        self.pushButton_8.clicked.connect(self.font_up)
        #Font_down
        self.pushButton_9.clicked.connect(self.font_down)
        #Fill
        self.pushButton_4.clicked.connect(self.fill)

        #Border
        self.pushButton_5.clicked.connect(self.border)



        #Border_Plus
        self.pushButton_7.clicked.connect(self.border_plus)
        #Border_Min
        self.pushButton_10.clicked.connect(self.border_min)

        #Custom Color
        
        self.pushButton_6.clicked.connect(self.custom_color)

        #Color
        self.button13.clicked.connect(self.color_1)
        self.button14.clicked.connect(self.color_2)
        self.button15.clicked.connect(self.color_3)
        self.button16.clicked.connect(self.color_4)
        self.button17.clicked.connect(self.color_5)
        self.button18.clicked.connect(self.color_6)
        self.button49.clicked.connect(self.color_49)
        self.button50.clicked.connect(self.color_50)
        self.button51.clicked.connect(self.color_51)
        self.button52.clicked.connect(self.color_52)
        self.button53.clicked.connect(self.color_53)
        self.button54.clicked.connect(self.color_54)
        self.button31.clicked.connect(self.color_31)
        self.button32.clicked.connect(self.color_32)
        self.button33.clicked.connect(self.color_33)
        self.button34.clicked.connect(self.color_34)
        self.button35.clicked.connect(self.color_35)
        self.button36.clicked.connect(self.color_36)
        self.button19.clicked.connect(self.color_19)
        self.button20.clicked.connect(self.color_20)
        self.button21.clicked.connect(self.color_21)
        self.button22.clicked.connect(self.color_22)
        self.button23.clicked.connect(self.color_23)
        self.button24.clicked.connect(self.color_24)
        self.button43.clicked.connect(self.color_43)
        self.button44.clicked.connect(self.color_44)
        self.button45.clicked.connect(self.color_45)
        self.button46.clicked.connect(self.color_46)
        self.button47.clicked.connect(self.color_47)
        self.button48.clicked.connect(self.color_48)
        self.button25.clicked.connect(self.color_25)
        self.button26.clicked.connect(self.color_26)
        self.button27.clicked.connect(self.color_27)
        self.button28.clicked.connect(self.color_28)
        self.button29.clicked.connect(self.color_29)
        self.button30.clicked.connect(self.color_30)

        self.button55.clicked.connect(self.color_55)
        self.button56.clicked.connect(self.color_56)
        self.button57.clicked.connect(self.color_57)
        self.button58.clicked.connect(self.color_58)
        self.button59.clicked.connect(self.color_59)
        self.button60.clicked.connect(self.color_60)



        self.button55_2.clicked.connect(self.color_55_2)
        self.button56_2.clicked.connect(self.color_56_2)
        self.button57_2.clicked.connect(self.color_57_2)
        self.button58_2.clicked.connect(self.color_58_2)
        self.button59_2.clicked.connect(self.color_59_2)
        self.button60_2.clicked.connect(self.color_60_2)



#expand_area_left

    def expand_area(self):
    
        selected_nodes = nuke.selectedNodes()
        
        backdrop_node = None
        
        for node in selected_nodes:
            if node.Class() == "BackdropNode":
                backdrop_node = node
                break

        



        backdrop_node["xpos"].setValue(backdrop_node["xpos"].value()-250)
        backdrop_node["bdwidth"].setValue(backdrop_node["bdwidth"].value()+250)
        #backdrop_node["ypos"].setValue(backdrop_node["ypos"].value()+100)
        #backdrop_node["bdheight"].setValue(backdrop_node["bdheight"].value()+100)



#expand_area_rigiht

    def expand_area_rigiht(self):
    
        selected_nodes = nuke.selectedNodes()
        
        backdrop_node = None
        
        for node in selected_nodes:
            if node.Class() == "BackdropNode":
                backdrop_node = node
                break

        



        #backdrop_node["xpos"].setValue(backdrop_node["xpos"].value()-250)
        backdrop_node["bdwidth"].setValue(backdrop_node["bdwidth"].value()+250)
        #backdrop_node["ypos"].setValue(backdrop_node["ypos"].value()+100)
        #backdrop_node["bdheight"].setValue(backdrop_node["bdheight"].value()+100)


#expand_area_bottom


    def expand_area_bottom(self):
    
        selected_nodes = nuke.selectedNodes()
        
        backdrop_node = None
        
        for node in selected_nodes:
            if node.Class() == "BackdropNode":
                backdrop_node = node
                break

        



        #backdrop_node["xpos"].setValue(backdrop_node["xpos"].value()-250)
        #backdrop_node["bdwidth"].setValue(backdrop_node["bdwidth"].value()+250)
        #backdrop_node["ypos"].setValue(backdrop_node["ypos"].value()+100)
        backdrop_node["bdheight"].setValue(backdrop_node["bdheight"].value()+250)



        
#expand_area_top

    def expand_area_top(self):
    
        selected_nodes = nuke.selectedNodes()
        
        backdrop_node = None
        
        for node in selected_nodes:
            if node.Class() == "BackdropNode":
                backdrop_node = node
                break

        



        #backdrop_node["xpos"].setValue(backdrop_node["xpos"].value()-250)
        #backdrop_node["bdwidth"].setValue(backdrop_node["bdwidth"].value()250)
        backdrop_node["ypos"].setValue(backdrop_node["ypos"].value()-250)
        backdrop_node["bdheight"].setValue(backdrop_node["bdheight"].value()+250)



#down_area_top


    def down_area_top(self):
    
        selected_nodes = nuke.selectedNodes()
        
        backdrop_node = None
        
        for node in selected_nodes:
            if node.Class() == "BackdropNode":
                backdrop_node = node
                break

        



        #backdrop_node["xpos"].setValue(backdrop_node["xpos"].value()+250)
        #backdrop_node["bdwidth"].setValue(backdrop_node["bdwidth"].value()250)
        backdrop_node["ypos"].setValue(backdrop_node["ypos"].value()+250)
        backdrop_node["bdheight"].setValue(backdrop_node["bdheight"].value()-250)




#down_area_left


    def down_area_left(self):
    
        selected_nodes = nuke.selectedNodes()
        
        backdrop_node = None
        
        for node in selected_nodes:
            if node.Class() == "BackdropNode":
                backdrop_node = node
                break

        



        backdrop_node["xpos"].setValue(backdrop_node["xpos"].value()+250)
        backdrop_node["bdwidth"].setValue(backdrop_node["bdwidth"].value()-250)
        #backdrop_node["ypos"].setValue(backdrop_node["ypos"].value()+250)
        #backdrop_node["bdheight"].setValue(backdrop_node["bdheight"].value()-250)


#down_area_right


    def down_area_right(self):
    
        selected_nodes = nuke.selectedNodes()
        
        backdrop_node = None
        
        for node in selected_nodes:
            if node.Class() == "BackdropNode":
                backdrop_node = node
                break

        



        backdrop_node["xpos"].setValue(backdrop_node["xpos"].value()+0)
        backdrop_node["bdwidth"].setValue(backdrop_node["bdwidth"].value()-250)
        #backdrop_node["ypos"].setValue(backdrop_node["ypos"].value()+250)
        #backdrop_node["bdheight"].setValue(backdrop_node["bdheight"].value()-250)



#down_area_down


    def down_area_down(self):
    
        selected_nodes = nuke.selectedNodes()
        
        backdrop_node = None
        
        for node in selected_nodes:
            if node.Class() == "BackdropNode":
                backdrop_node = node
                break

        



        #backdrop_node["xpos"].setValue(backdrop_node["xpos"].value()-250)
        #backdrop_node["bdwidth"].setValue(backdrop_node["bdwidth"].value()-250)
        #backdrop_node["ypos"].setValue(backdrop_node["ypos"].value()+250)
        backdrop_node["bdheight"].setValue(backdrop_node["bdheight"].value()-250)








#set_label


    def set_label(self):

        self.textEdit.toPlainText()


    def set_label(self):

        
    
        selected_nodes = nuke.selectedNodes()
        
        backdrop_node = None
        
        for node in selected_nodes:
            if node.Class() == "BackdropNode":
                backdrop_node = node
                break


        backdrop_node['label'].setValue(self.textEdit.toPlainText())

        backdrop_node['note_font_size'].setValue(50)

        backdrop_node['note_font'].setValue('bold')


#Font_UP
    def font_up(self):
    
        selected_nodes = nuke.selectedNodes()
        
        backdrop_node = None
        
        for node in selected_nodes:
            if node.Class() == "BackdropNode":
                backdrop_node = node
                break


        curr_font_val = backdrop_node['note_font_size'].getValue()

        if curr_font_val < 200:
           backdrop_node['note_font_size'].setValue(curr_font_val + 10)
        else:
            pass



#Font_Down

    def font_down(self):
    
        selected_nodes = nuke.selectedNodes()
        
        backdrop_node = None
        
        for node in selected_nodes:
            if node.Class() == "BackdropNode":
                backdrop_node = node
                break


        curr_font_val = backdrop_node['note_font_size'].getValue()

        if curr_font_val > 100:
           backdrop_node['note_font_size'].setValue(curr_font_val - 10)
        else:
            pass


#Fill
    
    def fill(self):

        
        selected_nodes = nuke.selectedNodes()
        
        backdrop_node = None
        
        for node in selected_nodes:
            if node.Class() == "BackdropNode":
                backdrop_node = node
                break

        backdrop_node['appearance'].setValue('Fill')
        
        
#Border
    
    def border(self):

        
        selected_nodes = nuke.selectedNodes()
        
        backdrop_node = None
        
        for node in selected_nodes:
            if node.Class() == "BackdropNode":
                backdrop_node = node
                break

        backdrop_node['appearance'].setValue('Border')


#Border_Plus
        
    def border_plus(self):
    
        selected_nodes = nuke.selectedNodes()
        
        backdrop_node = None
        
        for node in selected_nodes:
            if node.Class() == "BackdropNode":
                backdrop_node = node
                break
        
        
        curr_border_val = backdrop_node['border_width'].getValue()
        
        if curr_border_val < 20:
           backdrop_node['border_width'].setValue(curr_border_val + 5 )
        else:
            pass

#Border_Min
        
    def border_min(self):
    
        selected_nodes = nuke.selectedNodes()
        
        backdrop_node = None
        
        for node in selected_nodes:
            if node.Class() == "BackdropNode":
                backdrop_node = node
                break
        
        
        curr_border_val = backdrop_node['border_width'].getValue()
        
        if curr_border_val > 1:
           backdrop_node['border_width'].setValue(curr_border_val - 5 )
        else:
            pass


#Color1

    def color_1(self):

    
        selected_nodes = nuke.selectedNodes()
        
        backdrop_node = None
        
        for node in selected_nodes:
            if node.Class() == "BackdropNode":
                backdrop_node = node
                break
        
        
        backdrop_node['tile_color'].setValue(hex_color_to_rgb(0.392,0.118,0.086))


#Color2

    def color_2(self):

    
        selected_nodes = nuke.selectedNodes()
        
        backdrop_node = None
        
        for node in selected_nodes:
            if node.Class() == "BackdropNode":
                backdrop_node = node
                break
        
        
        backdrop_node['tile_color'].setValue(hex_color_to_rgb(0.58,0.192,0.149))

        
#Color3

    def color_3(self):

    
        selected_nodes = nuke.selectedNodes()
        
        backdrop_node = None
        
        for node in selected_nodes:
            if node.Class() == "BackdropNode":
                backdrop_node = node
                break
        
        
        backdrop_node['tile_color'].setValue(hex_color_to_rgb(0.69, 0.227, 0.18))

#Color4

    def color_4(self):

    
        selected_nodes = nuke.selectedNodes()
        
        backdrop_node = None
        
        for node in selected_nodes:
            if node.Class() == "BackdropNode":
                backdrop_node = node
                break
        
        
        backdrop_node['tile_color'].setValue(hex_color_to_rgb(0.835, 0.298, 0.235))


#Color5

    def color_5(self):

    
        selected_nodes = nuke.selectedNodes()
        
        backdrop_node = None
        
        for node in selected_nodes:
            if node.Class() == "BackdropNode":
                backdrop_node = node
                break
        
        
        backdrop_node['tile_color'].setValue(hex_color_to_rgb(0.925, 0.439, 0.388))


#Color6

    def color_6(self):

    
        selected_nodes = nuke.selectedNodes()
        
        backdrop_node = None
        
        for node in selected_nodes:
            if node.Class() == "BackdropNode":
                backdrop_node = node
                break
        
        
        backdrop_node['tile_color'].setValue(hex_color_to_rgb(0.851, 0.533, 0.502))



#Color49

    def color_49(self):

    
        selected_nodes = nuke.selectedNodes()
        
        backdrop_node = None
        
        for node in selected_nodes:
            if node.Class() == "BackdropNode":
                backdrop_node = node
                break
        
        
        backdrop_node['tile_color'].setValue(hex_color_to_rgb(0.31, 0.216, 0))

#Color50

    def color_50(self):

    
        selected_nodes = nuke.selectedNodes()
        
        backdrop_node = None
        
        for node in selected_nodes:
            if node.Class() == "BackdropNode":
                backdrop_node = node
                break
        
        
        backdrop_node['tile_color'].setValue(hex_color_to_rgb(0.478, 0.247, 0.059))

#Color51

    def color_51(self):

    
        selected_nodes = nuke.selectedNodes()
        
        backdrop_node = None
        
        for node in selected_nodes:
            if node.Class() == "BackdropNode":
                backdrop_node = node
                break
        
        
        backdrop_node['tile_color'].setValue(hex_color_to_rgb(0.694, 0.388, 0.035))

#Color52

    def color_52(self):

    
        selected_nodes = nuke.selectedNodes()
        
        backdrop_node = None
        
        for node in selected_nodes:
            if node.Class() == "BackdropNode":
                backdrop_node = node
                break
        
        
        backdrop_node['tile_color'].setValue(hex_color_to_rgb(0.588, 0.42, 0.184))

#Color53

    def color_53(self):

    
        selected_nodes = nuke.selectedNodes()
        
        backdrop_node = None
        
        for node in selected_nodes:
            if node.Class() == "BackdropNode":
                backdrop_node = node
                break
        
        
        backdrop_node['tile_color'].setValue(hex_color_to_rgb(0.741, 0.576, 0.161))

#Color54

    def color_54(self):

    
        selected_nodes = nuke.selectedNodes()
        
        backdrop_node = None
        
        for node in selected_nodes:
            if node.Class() == "BackdropNode":
                backdrop_node = node
                break
        
        
        backdrop_node['tile_color'].setValue(hex_color_to_rgb(0.867, 0.737, 0))


#Color31

    def color_31(self):

    
        selected_nodes = nuke.selectedNodes()
        
        backdrop_node = None
        
        for node in selected_nodes:
            if node.Class() == "BackdropNode":
                backdrop_node = node
                break
        
        
        backdrop_node['tile_color'].setValue(hex_color_to_rgb(0.106, 0.31, 0.447))

#Color32

    def color_32(self):

    
        selected_nodes = nuke.selectedNodes()
        
        backdrop_node = None
        
        for node in selected_nodes:
            if node.Class() == "BackdropNode":
                backdrop_node = node
                break
        
        
        backdrop_node['tile_color'].setValue(hex_color_to_rgb(0.157, 0.455, 0.651))


#Color33

    def color_33(self):

    
        selected_nodes = nuke.selectedNodes()
        
        backdrop_node = None
        
        for node in selected_nodes:
            if node.Class() == "BackdropNode":
                backdrop_node = node
                break
        
        
        backdrop_node['tile_color'].setValue(hex_color_to_rgb(0.204, 0.596, 0.859))

#Color34

    def color_34(self):

    
        selected_nodes = nuke.selectedNodes()
        
        backdrop_node = None
        
        for node in selected_nodes:
            if node.Class() == "BackdropNode":
                backdrop_node = node
                break
        
        
        backdrop_node['tile_color'].setValue(hex_color_to_rgb(0.522, 0.757, 0.914))

#Color35

    def color_35(self):

    
        selected_nodes = nuke.selectedNodes()
        
        backdrop_node = None
        
        for node in selected_nodes:
            if node.Class() == "BackdropNode":
                backdrop_node = node
                break
        
        
        backdrop_node['tile_color'].setValue(hex_color_to_rgb(0.682, 0.839, 0.957))

#Color36

    def color_36(self):

    
        selected_nodes = nuke.selectedNodes()
        
        backdrop_node = None
        
        for node in selected_nodes:
            if node.Class() == "BackdropNode":
                backdrop_node = node
                break
        
        
        backdrop_node['tile_color'].setValue(hex_color_to_rgb(0.839, 0.918, 0.973))

#Color19

    def color_19(self):

    
        selected_nodes = nuke.selectedNodes()
        
        backdrop_node = None
        
        for node in selected_nodes:
            if node.Class() == "BackdropNode":
                backdrop_node = node
                break
        
        
        backdrop_node['tile_color'].setValue(hex_color_to_rgb(0.29, 0.137, 0.353))


#Color20

    def color_20(self):

    
        selected_nodes = nuke.selectedNodes()
        
        backdrop_node = None
        
        for node in selected_nodes:
            if node.Class() == "BackdropNode":
                backdrop_node = node
                break
        
        
        backdrop_node['tile_color'].setValue(hex_color_to_rgb(0.424, 0.204, 0.514))

#Color21

    def color_21(self):

    
        selected_nodes = nuke.selectedNodes()
        
        backdrop_node = None
        
        for node in selected_nodes:
            if node.Class() == "BackdropNode":
                backdrop_node = node
                break
        
        
        backdrop_node['tile_color'].setValue(hex_color_to_rgb(0.557, 0.267, 0.678))

#Color22

    def color_22(self):

    
        selected_nodes = nuke.selectedNodes()
        
        backdrop_node = None
        
        for node in selected_nodes:
            if node.Class() == "BackdropNode":
                backdrop_node = node
                break
        
        
        backdrop_node['tile_color'].setValue(hex_color_to_rgb(0.647, 0.412, 0.741))

#Color23

    def color_23(self):

    
        selected_nodes = nuke.selectedNodes()
        
        backdrop_node = None
        
        for node in selected_nodes:
            if node.Class() == "BackdropNode":
                backdrop_node = node
                break
        
        
        backdrop_node['tile_color'].setValue(hex_color_to_rgb(0.824, 0.706, 0.871))

#Color24

    def color_24(self):

    
        selected_nodes = nuke.selectedNodes()
        
        backdrop_node = None
        
        for node in selected_nodes:
            if node.Class() == "BackdropNode":
                backdrop_node = node
                break
        
        
        backdrop_node['tile_color'].setValue(hex_color_to_rgb(0.957, 0.925, 0.969))


#Color43

    def color_43(self):

    
        selected_nodes = nuke.selectedNodes()
        
        backdrop_node = None
        
        for node in selected_nodes:
            if node.Class() == "BackdropNode":
                backdrop_node = node
                break
        
        
        backdrop_node['tile_color'].setValue(hex_color_to_rgb(0.349, 0.416, 0.133))

#Color44

    def color_44(self):

    
        selected_nodes = nuke.selectedNodes()
        
        backdrop_node = None
        
        for node in selected_nodes:
            if node.Class() == "BackdropNode":
                backdrop_node = node
                break
        
        
        backdrop_node['tile_color'].setValue(hex_color_to_rgb(0.624, 0.706, 0.322))
        
#Color45

    def color_45(self):

    
        selected_nodes = nuke.selectedNodes()
        
        backdrop_node = None
        
        for node in selected_nodes:
            if node.Class() == "BackdropNode":
                backdrop_node = node
                break
        
        
        backdrop_node['tile_color'].setValue(hex_color_to_rgb(0.424, 0.659, 0.314))
        
#Color46

    def color_46(self):

    
        selected_nodes = nuke.selectedNodes()
        
        backdrop_node = None
        
        for node in selected_nodes:
            if node.Class() == "BackdropNode":
                backdrop_node = node
                break
        
        
        backdrop_node['tile_color'].setValue(hex_color_to_rgb(0.639, 0.831, 0))
        
#Color47

    def color_47(self):

    
        selected_nodes = nuke.selectedNodes()
        
        backdrop_node = None
        
        for node in selected_nodes:
            if node.Class() == "BackdropNode":
                backdrop_node = node
                break
        
        
        backdrop_node['tile_color'].setValue(hex_color_to_rgb(0.655, 0.835, 0.38))
        
#Color48

    def color_48(self):

    
        selected_nodes = nuke.selectedNodes()
        
        backdrop_node = None
        
        for node in selected_nodes:
            if node.Class() == "BackdropNode":
                backdrop_node = node
                break
        
        
        backdrop_node['tile_color'].setValue(hex_color_to_rgb(0.749, 1, 0.165))



#Color25

    def color_25(self):

    
        selected_nodes = nuke.selectedNodes()
        
        backdrop_node = None
        
        for node in selected_nodes:
            if node.Class() == "BackdropNode":
                backdrop_node = node
                break
        
        
        backdrop_node['tile_color'].setValue(hex_color_to_rgb(0.008, 0.275, 0))


#Color26

    def color_26(self):

    
        selected_nodes = nuke.selectedNodes()
        
        backdrop_node = None
        
        for node in selected_nodes:
            if node.Class() == "BackdropNode":
                backdrop_node = node
                break
        
        
        backdrop_node['tile_color'].setValue(hex_color_to_rgb(0.016, 0.443, 0))

#Color27

    def color_27(self):

    
        selected_nodes = nuke.selectedNodes()
        
        backdrop_node = None
        
        for node in selected_nodes:
            if node.Class() == "BackdropNode":
                backdrop_node = node
                break
        
        
        backdrop_node['tile_color'].setValue(hex_color_to_rgb(0.235, 0.365, 0.231))

#Color28

    def color_28(self):

    
        selected_nodes = nuke.selectedNodes()
        
        backdrop_node = None
        
        for node in selected_nodes:
            if node.Class() == "BackdropNode":
                backdrop_node = node
                break
        
        
        backdrop_node['tile_color'].setValue(hex_color_to_rgb(0.118, 0.518, 0.286))

#Color29

    def color_29(self):

    
        selected_nodes = nuke.selectedNodes()
        
        backdrop_node = None
        
        for node in selected_nodes:
            if node.Class() == "BackdropNode":
                backdrop_node = node
                break
        
        
        backdrop_node['tile_color'].setValue(hex_color_to_rgb(0.298, 0.478, 0.294))

#Color30

    def color_30(self):

    
        selected_nodes = nuke.selectedNodes()
        
        backdrop_node = None
        
        for node in selected_nodes:
            if node.Class() == "BackdropNode":
                backdrop_node = node
                break
        
        
        backdrop_node['tile_color'].setValue(hex_color_to_rgb(0.322, 0.745, 0.502))


#Color55

    def color_55(self):

    
        selected_nodes = nuke.selectedNodes()
        
        backdrop_node = None
        
        for node in selected_nodes:
            if node.Class() == "BackdropNode":
                backdrop_node = node
                break
        
        
        backdrop_node['tile_color'].setValue(hex_color_to_rgb(0.118, 0.118, 0.118))


#Color56

    def color_56(self):

    
        selected_nodes = nuke.selectedNodes()
        
        backdrop_node = None
        
        for node in selected_nodes:
            if node.Class() == "BackdropNode":
                backdrop_node = node
                break
        
        
        backdrop_node['tile_color'].setValue(hex_color_to_rgb(0.196, 0.196, 0.196))


#Color57

    def color_57(self):

    
        selected_nodes = nuke.selectedNodes()
        
        backdrop_node = None
        
        for node in selected_nodes:
            if node.Class() == "BackdropNode":
                backdrop_node = node
                break
        
        
        backdrop_node['tile_color'].setValue(hex_color_to_rgb(0.392, 0.392, 0.392))
#Color58

    def color_58(self):

    
        selected_nodes = nuke.selectedNodes()
        
        backdrop_node = None
        
        for node in selected_nodes:
            if node.Class() == "BackdropNode":
                backdrop_node = node
                break
        
        
        backdrop_node['tile_color'].setValue(hex_color_to_rgb(0.588, 0.588, 0.588))


#Color59

    def color_59(self):

    
        selected_nodes = nuke.selectedNodes()
        
        backdrop_node = None
        
        for node in selected_nodes:
            if node.Class() == "BackdropNode":
                backdrop_node = node
                break
        
        
        backdrop_node['tile_color'].setValue(hex_color_to_rgb(0.784, 0.784, 0.784))


#Color60

    def color_60(self):

    
        selected_nodes = nuke.selectedNodes()
        
        backdrop_node = None
        
        for node in selected_nodes:
            if node.Class() == "BackdropNode":
                backdrop_node = node
                break
        
        
        backdrop_node['tile_color'].setValue(hex_color_to_rgb(0.898, 0.906, 0.914))



#Color55_2

    def color_55_2(self):

    
        selected_nodes = nuke.selectedNodes()
        
        backdrop_node = None
        
        for node in selected_nodes:
            if node.Class() == "BackdropNode":
                backdrop_node = node
                break
        
        
        backdrop_node['tile_color'].setValue(hex_color_to_rgb(0.898, 0.906, 0.914))



#Color55_2

    def color_55_2(self):

    
        selected_nodes = nuke.selectedNodes()
        
        backdrop_node = None
        
        for node in selected_nodes:
            if node.Class() == "BackdropNode":
                backdrop_node = node
                break
        
        
        backdrop_node['tile_color'].setValue(hex_color_to_rgb(0.898, 0.906, 0.914))


#Color55_2

    def color_55_2(self):

    
        selected_nodes = nuke.selectedNodes()
        
        backdrop_node = None
        
        for node in selected_nodes:
            if node.Class() == "BackdropNode":
                backdrop_node = node
                break
        
        
        backdrop_node['tile_color'].setValue(hex_color_to_rgb(0.09, 0.125, 0.165))

#Color56_2

    def color_56_2(self):

    
        selected_nodes = nuke.selectedNodes()
        
        backdrop_node = None
        
        for node in selected_nodes:
            if node.Class() == "BackdropNode":
                backdrop_node = node
                break
        
        
        backdrop_node['tile_color'].setValue(hex_color_to_rgb(0.129, 0.184, 0.239))

#Color57_2

    def color_57_2(self):

    
        selected_nodes = nuke.selectedNodes()
        
        backdrop_node = None
        
        for node in selected_nodes:
            if node.Class() == "BackdropNode":
                backdrop_node = node
                break
        
        
        backdrop_node['tile_color'].setValue(hex_color_to_rgb(0.173, 0.243, 0.314))

#Color58_2

    def color_58_2(self):

    
        selected_nodes = nuke.selectedNodes()
        
        backdrop_node = None
        
        for node in selected_nodes:
            if node.Class() == "BackdropNode":
                backdrop_node = node
                break
        
        
        backdrop_node['tile_color'].setValue(hex_color_to_rgb(0.502, 0.545, 0.588))


#Color59_2

    def color_59_2(self):

    
        selected_nodes = nuke.selectedNodes()
        
        backdrop_node = None
        
        for node in selected_nodes:
            if node.Class() == "BackdropNode":
                backdrop_node = node
                break
        
        
        backdrop_node['tile_color'].setValue(hex_color_to_rgb(0.671, 0.698, 0.725))



#Color60_2

    def color_60_2(self):

    
        selected_nodes = nuke.selectedNodes()
        
        backdrop_node = None
        
        for node in selected_nodes:
            if node.Class() == "BackdropNode":
                backdrop_node = node
                break
        
        
        backdrop_node['tile_color'].setValue(hex_color_to_rgb(0.835, 0.847, 0.863))
        


        
        

#custom_color

    def custom_color(self):


        selected_nodes = nuke.selectedNodes()
        
        backdrop_node = None
        
        for node in selected_nodes:
            if node.Class() == "BackdropNode":
                backdrop_node = node
                break

        tile_col = nuke.getColor()
        
        backdrop_node['tile_color'].setValue(tile_col)

        




############################# MAIN CODE END #####################


















