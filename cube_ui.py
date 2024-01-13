# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'cube.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject, QSize, Qt)
from PySide6.QtGui import (QCursor,
    QFont)
from PySide6.QtWidgets import (QGridLayout, QGroupBox, QHBoxLayout,
    QLabel, QPushButton, QSizePolicy, QSpacerItem,
    QTextEdit, QVBoxLayout)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(960, 921)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QSize(960, 921))
        Form.setMaximumSize(QSize(960, 921))
        Form.setBaseSize(QSize(960, 921))
        font = QFont()
        font.setPointSize(10)
        Form.setFont(font)
        Form.setCursor(QCursor(Qt.ArrowCursor))
        Form.setStyleSheet(u"")
        self.verticalLayout_3 = QVBoxLayout(Form)
        self.verticalLayout_3.setSpacing(15)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(-1, 15, 15, 15)
        self.groupBox = QGroupBox(Form)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setFont(font)
        self.groupBox.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(45, 30, 45, 30)
        self.preSet_button_2 = QPushButton(self.groupBox)
        self.preSet_button_2.setObjectName(u"preSet_button_2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.preSet_button_2.sizePolicy().hasHeightForWidth())
        self.preSet_button_2.setSizePolicy(sizePolicy1)
        font1 = QFont()
        font1.setPointSize(11)
        self.preSet_button_2.setFont(font1)
        self.preSet_button_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.preSet_button_2.setStyleSheet(u"")

        self.verticalLayout_4.addWidget(self.preSet_button_2)

        self.verticalSpacer_3 = QSpacerItem(20, 50, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_4.addItem(self.verticalSpacer_3)

        self.preSet_button_1 = QPushButton(self.groupBox)
        self.preSet_button_1.setObjectName(u"preSet_button_1")
        sizePolicy1.setHeightForWidth(self.preSet_button_1.sizePolicy().hasHeightForWidth())
        self.preSet_button_1.setSizePolicy(sizePolicy1)
        self.preSet_button_1.setFont(font1)
        self.preSet_button_1.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_4.addWidget(self.preSet_button_1)


        self.horizontalLayout.addLayout(self.verticalLayout_4)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.button_0 = QPushButton(self.groupBox)
        self.button_0.setObjectName(u"button_0")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.button_0.sizePolicy().hasHeightForWidth())
        self.button_0.setSizePolicy(sizePolicy2)
        self.button_0.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_0.setAutoDefault(False)

        self.gridLayout.addWidget(self.button_0, 0, 0, 1, 1)

        self.button_1 = QPushButton(self.groupBox)
        self.button_1.setObjectName(u"button_1")
        sizePolicy2.setHeightForWidth(self.button_1.sizePolicy().hasHeightForWidth())
        self.button_1.setSizePolicy(sizePolicy2)
        self.button_1.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_1.setStyleSheet(u"")
        self.button_1.setAutoDefault(False)

        self.gridLayout.addWidget(self.button_1, 0, 1, 1, 1)

        self.button_2 = QPushButton(self.groupBox)
        self.button_2.setObjectName(u"button_2")
        sizePolicy2.setHeightForWidth(self.button_2.sizePolicy().hasHeightForWidth())
        self.button_2.setSizePolicy(sizePolicy2)
        self.button_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_2.setAutoDefault(False)

        self.gridLayout.addWidget(self.button_2, 1, 0, 1, 1)

        self.button_3 = QPushButton(self.groupBox)
        self.button_3.setObjectName(u"button_3")
        sizePolicy2.setHeightForWidth(self.button_3.sizePolicy().hasHeightForWidth())
        self.button_3.setSizePolicy(sizePolicy2)
        self.button_3.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_3.setAutoDefault(False)

        self.gridLayout.addWidget(self.button_3, 1, 1, 1, 1)

        self.gridLayout.setRowStretch(0, 1)
        self.gridLayout.setRowStretch(1, 1)
        self.gridLayout.setColumnStretch(0, 1)
        self.gridLayout.setColumnStretch(1, 1)

        self.horizontalLayout.addLayout(self.gridLayout)

        self.textEdit = QTextEdit(self.groupBox)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setReadOnly(True)

        self.horizontalLayout.addWidget(self.textEdit)

        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 1)
        self.horizontalLayout.setStretch(2, 2)

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.button_16 = QPushButton(self.groupBox)
        self.button_16.setObjectName(u"button_16")
        sizePolicy2.setHeightForWidth(self.button_16.sizePolicy().hasHeightForWidth())
        self.button_16.setSizePolicy(sizePolicy2)
        self.button_16.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_16.setAutoDefault(False)

        self.gridLayout_2.addWidget(self.button_16, 0, 0, 1, 1)

        self.button_17 = QPushButton(self.groupBox)
        self.button_17.setObjectName(u"button_17")
        sizePolicy2.setHeightForWidth(self.button_17.sizePolicy().hasHeightForWidth())
        self.button_17.setSizePolicy(sizePolicy2)
        self.button_17.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_17.setAutoDefault(False)

        self.gridLayout_2.addWidget(self.button_17, 0, 1, 1, 1)

        self.button_18 = QPushButton(self.groupBox)
        self.button_18.setObjectName(u"button_18")
        sizePolicy2.setHeightForWidth(self.button_18.sizePolicy().hasHeightForWidth())
        self.button_18.setSizePolicy(sizePolicy2)
        self.button_18.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_18.setAutoDefault(False)

        self.gridLayout_2.addWidget(self.button_18, 1, 0, 1, 1)

        self.button_19 = QPushButton(self.groupBox)
        self.button_19.setObjectName(u"button_19")
        sizePolicy2.setHeightForWidth(self.button_19.sizePolicy().hasHeightForWidth())
        self.button_19.setSizePolicy(sizePolicy2)
        self.button_19.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_19.setAutoDefault(False)

        self.gridLayout_2.addWidget(self.button_19, 1, 1, 1, 1)

        self.gridLayout_2.setRowStretch(0, 1)
        self.gridLayout_2.setRowStretch(1, 1)
        self.gridLayout_2.setColumnStretch(0, 1)
        self.gridLayout_2.setColumnStretch(1, 1)

        self.horizontalLayout_2.addLayout(self.gridLayout_2)

        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setSpacing(6)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.button_5 = QPushButton(self.groupBox)
        self.button_5.setObjectName(u"button_5")
        sizePolicy2.setHeightForWidth(self.button_5.sizePolicy().hasHeightForWidth())
        self.button_5.setSizePolicy(sizePolicy2)
        self.button_5.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_5.setAutoDefault(False)

        self.gridLayout_3.addWidget(self.button_5, 0, 1, 1, 1)

        self.button_4 = QPushButton(self.groupBox)
        self.button_4.setObjectName(u"button_4")
        sizePolicy2.setHeightForWidth(self.button_4.sizePolicy().hasHeightForWidth())
        self.button_4.setSizePolicy(sizePolicy2)
        self.button_4.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_4.setAutoDefault(False)

        self.gridLayout_3.addWidget(self.button_4, 0, 0, 1, 1)

        self.button_7 = QPushButton(self.groupBox)
        self.button_7.setObjectName(u"button_7")
        sizePolicy2.setHeightForWidth(self.button_7.sizePolicy().hasHeightForWidth())
        self.button_7.setSizePolicy(sizePolicy2)
        self.button_7.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_7.setAutoDefault(False)

        self.gridLayout_3.addWidget(self.button_7, 1, 1, 1, 1)

        self.button_6 = QPushButton(self.groupBox)
        self.button_6.setObjectName(u"button_6")
        sizePolicy2.setHeightForWidth(self.button_6.sizePolicy().hasHeightForWidth())
        self.button_6.setSizePolicy(sizePolicy2)
        self.button_6.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_6.setAutoDefault(False)

        self.gridLayout_3.addWidget(self.button_6, 1, 0, 1, 1)

        self.gridLayout_3.setRowStretch(0, 1)
        self.gridLayout_3.setRowStretch(1, 1)
        self.gridLayout_3.setColumnStretch(0, 1)
        self.gridLayout_3.setColumnStretch(1, 1)

        self.horizontalLayout_2.addLayout(self.gridLayout_3)

        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.button_8 = QPushButton(self.groupBox)
        self.button_8.setObjectName(u"button_8")
        sizePolicy2.setHeightForWidth(self.button_8.sizePolicy().hasHeightForWidth())
        self.button_8.setSizePolicy(sizePolicy2)
        self.button_8.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_8.setAutoDefault(False)

        self.gridLayout_4.addWidget(self.button_8, 0, 0, 1, 1)

        self.button_9 = QPushButton(self.groupBox)
        self.button_9.setObjectName(u"button_9")
        sizePolicy2.setHeightForWidth(self.button_9.sizePolicy().hasHeightForWidth())
        self.button_9.setSizePolicy(sizePolicy2)
        self.button_9.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_9.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.button_9.setAutoDefault(False)

        self.gridLayout_4.addWidget(self.button_9, 0, 1, 1, 1)

        self.button_10 = QPushButton(self.groupBox)
        self.button_10.setObjectName(u"button_10")
        sizePolicy2.setHeightForWidth(self.button_10.sizePolicy().hasHeightForWidth())
        self.button_10.setSizePolicy(sizePolicy2)
        self.button_10.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_10.setStyleSheet(u"")
        self.button_10.setAutoDefault(False)

        self.gridLayout_4.addWidget(self.button_10, 1, 0, 1, 1)

        self.button_11 = QPushButton(self.groupBox)
        self.button_11.setObjectName(u"button_11")
        sizePolicy2.setHeightForWidth(self.button_11.sizePolicy().hasHeightForWidth())
        self.button_11.setSizePolicy(sizePolicy2)
        self.button_11.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_11.setStyleSheet(u"")
        self.button_11.setAutoDefault(False)

        self.gridLayout_4.addWidget(self.button_11, 1, 1, 1, 1)

        self.gridLayout_4.setRowStretch(0, 1)
        self.gridLayout_4.setRowStretch(1, 1)
        self.gridLayout_4.setColumnStretch(0, 1)
        self.gridLayout_4.setColumnStretch(1, 1)

        self.horizontalLayout_2.addLayout(self.gridLayout_4)

        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.button_12 = QPushButton(self.groupBox)
        self.button_12.setObjectName(u"button_12")
        sizePolicy2.setHeightForWidth(self.button_12.sizePolicy().hasHeightForWidth())
        self.button_12.setSizePolicy(sizePolicy2)
        self.button_12.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_12.setAutoDefault(False)

        self.gridLayout_5.addWidget(self.button_12, 0, 0, 1, 1)

        self.button_13 = QPushButton(self.groupBox)
        self.button_13.setObjectName(u"button_13")
        sizePolicy2.setHeightForWidth(self.button_13.sizePolicy().hasHeightForWidth())
        self.button_13.setSizePolicy(sizePolicy2)
        self.button_13.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_13.setAutoDefault(False)

        self.gridLayout_5.addWidget(self.button_13, 0, 1, 1, 1)

        self.button_14 = QPushButton(self.groupBox)
        self.button_14.setObjectName(u"button_14")
        sizePolicy2.setHeightForWidth(self.button_14.sizePolicy().hasHeightForWidth())
        self.button_14.setSizePolicy(sizePolicy2)
        self.button_14.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_14.setAutoDefault(False)

        self.gridLayout_5.addWidget(self.button_14, 1, 0, 1, 1)

        self.button_15 = QPushButton(self.groupBox)
        self.button_15.setObjectName(u"button_15")
        sizePolicy2.setHeightForWidth(self.button_15.sizePolicy().hasHeightForWidth())
        self.button_15.setSizePolicy(sizePolicy2)
        self.button_15.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_15.setAutoDefault(False)

        self.gridLayout_5.addWidget(self.button_15, 1, 1, 1, 1)

        self.gridLayout_5.setRowStretch(0, 1)
        self.gridLayout_5.setRowStretch(1, 1)
        self.gridLayout_5.setColumnStretch(0, 1)
        self.gridLayout_5.setColumnStretch(1, 1)

        self.horizontalLayout_2.addLayout(self.gridLayout_5)

        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 1)
        self.horizontalLayout_2.setStretch(2, 1)
        self.horizontalLayout_2.setStretch(3, 1)

        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_4.addWidget(self.label_3)

        self.gridLayout_6 = QGridLayout()
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.button_20 = QPushButton(self.groupBox)
        self.button_20.setObjectName(u"button_20")
        sizePolicy2.setHeightForWidth(self.button_20.sizePolicy().hasHeightForWidth())
        self.button_20.setSizePolicy(sizePolicy2)
        self.button_20.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_20.setAutoDefault(False)

        self.gridLayout_6.addWidget(self.button_20, 0, 0, 1, 1)

        self.button_21 = QPushButton(self.groupBox)
        self.button_21.setObjectName(u"button_21")
        sizePolicy2.setHeightForWidth(self.button_21.sizePolicy().hasHeightForWidth())
        self.button_21.setSizePolicy(sizePolicy2)
        self.button_21.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_21.setAutoDefault(False)

        self.gridLayout_6.addWidget(self.button_21, 0, 1, 1, 1)

        self.button_22 = QPushButton(self.groupBox)
        self.button_22.setObjectName(u"button_22")
        sizePolicy2.setHeightForWidth(self.button_22.sizePolicy().hasHeightForWidth())
        self.button_22.setSizePolicy(sizePolicy2)
        self.button_22.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_22.setAutoDefault(False)

        self.gridLayout_6.addWidget(self.button_22, 1, 0, 1, 1)

        self.button_23 = QPushButton(self.groupBox)
        self.button_23.setObjectName(u"button_23")
        sizePolicy2.setHeightForWidth(self.button_23.sizePolicy().hasHeightForWidth())
        self.button_23.setSizePolicy(sizePolicy2)
        self.button_23.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_23.setAutoDefault(False)

        self.gridLayout_6.addWidget(self.button_23, 1, 1, 1, 1)

        self.gridLayout_6.setRowStretch(0, 1)
        self.gridLayout_6.setRowStretch(1, 1)
        self.gridLayout_6.setColumnStretch(0, 1)
        self.gridLayout_6.setColumnStretch(1, 1)

        self.horizontalLayout_4.addLayout(self.gridLayout_6)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.hint_label = QLabel(self.groupBox)
        self.hint_label.setObjectName(u"hint_label")
        font2 = QFont()
        font2.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1"])
        font2.setPointSize(16)
        font2.setBold(True)
        font2.setUnderline(False)
        font2.setStyleStrategy(QFont.PreferDefault)
        font2.setHintingPreference(QFont.PreferDefaultHinting)
        self.hint_label.setFont(font2)
        self.hint_label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.hint_label)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(50, 10, 50, 10)
        self.bfs_solve_button = QPushButton(self.groupBox)
        self.bfs_solve_button.setObjectName(u"bfs_solve_button")
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.bfs_solve_button.sizePolicy().hasHeightForWidth())
        self.bfs_solve_button.setSizePolicy(sizePolicy3)
        self.bfs_solve_button.setBaseSize(QSize(30, 10))
        font3 = QFont()
        font3.setFamilies([u"Microsoft YaHei UI"])
        font3.setPointSize(11)
        self.bfs_solve_button.setFont(font3)
        self.bfs_solve_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.bfs_solve_button.setStyleSheet(u"")

        self.verticalLayout_2.addWidget(self.bfs_solve_button)

        self.verticalSpacer = QSpacerItem(20, 15, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.dfs_solve_button = QPushButton(self.groupBox)
        self.dfs_solve_button.setObjectName(u"dfs_solve_button")
        sizePolicy3.setHeightForWidth(self.dfs_solve_button.sizePolicy().hasHeightForWidth())
        self.dfs_solve_button.setSizePolicy(sizePolicy3)
        self.dfs_solve_button.setBaseSize(QSize(10, 10))
        self.dfs_solve_button.setFont(font3)
        self.dfs_solve_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.dfs_solve_button.setStyleSheet(u"")

        self.verticalLayout_2.addWidget(self.dfs_solve_button)

        self.verticalSpacer_2 = QSpacerItem(20, 15, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)

        self.reset_button = QPushButton(self.groupBox)
        self.reset_button.setObjectName(u"reset_button")
        sizePolicy3.setHeightForWidth(self.reset_button.sizePolicy().hasHeightForWidth())
        self.reset_button.setSizePolicy(sizePolicy3)
        self.reset_button.setBaseSize(QSize(0, 10))
        font4 = QFont()
        font4.setFamilies([u"Microsoft YaHei UI"])
        font4.setPointSize(11)
        font4.setBold(False)
        self.reset_button.setFont(font4)
        self.reset_button.setCursor(QCursor(Qt.PointingHandCursor))
        self.reset_button.setStyleSheet(u"")

        self.verticalLayout_2.addWidget(self.reset_button)


        self.horizontalLayout_3.addLayout(self.verticalLayout_2)


        self.horizontalLayout_4.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4.setStretch(0, 1)
        self.horizontalLayout_4.setStretch(1, 1)
        self.horizontalLayout_4.setStretch(2, 2)

        self.verticalLayout.addLayout(self.horizontalLayout_4)


        self.verticalLayout_3.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(Form)
        self.groupBox_2.setObjectName(u"groupBox_2")
        font5 = QFont()
        font5.setPointSize(10)
        font5.setBold(False)
        font5.setItalic(False)
        self.groupBox_2.setFont(font5)
        self.groupBox_2.setStyleSheet(u"")
        self.horizontalLayout_5 = QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.bfs_result_text = QTextEdit(self.groupBox_2)
        self.bfs_result_text.setObjectName(u"bfs_result_text")
        self.bfs_result_text.setStyleSheet(u"")
        self.bfs_result_text.setReadOnly(True)

        self.horizontalLayout_5.addWidget(self.bfs_result_text)

        self.dfs_result_text = QTextEdit(self.groupBox_2)
        self.dfs_result_text.setObjectName(u"dfs_result_text")
        self.dfs_result_text.setReadOnly(True)

        self.horizontalLayout_5.addWidget(self.dfs_result_text)


        self.verticalLayout_3.addWidget(self.groupBox_2)

        self.verticalLayout_3.setStretch(0, 3)
        self.verticalLayout_3.setStretch(1, 1)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"\u4e8c\u9636\u9b54\u65b9\u6c42\u89e3\u5668", None))
        self.groupBox.setTitle("")
        self.preSet_button_2.setText(QCoreApplication.translate("Form", u"\u9884\u8bbe1", None))
        self.preSet_button_1.setText(QCoreApplication.translate("Form", u"\u9884\u8bbe2", None))
        self.button_0.setText(QCoreApplication.translate("Form", u"PushButton", None))
        self.button_1.setText(QCoreApplication.translate("Form", u"PushButton", None))
        self.button_2.setText(QCoreApplication.translate("Form", u"PushButton", None))
        self.button_3.setText(QCoreApplication.translate("Form", u"PushButton", None))
        self.textEdit.setHtml(QCoreApplication.translate("Form", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Sans Serif'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Microsoft YaHei UI'; font-size:11pt;\">\u8bf4\u660e\uff1a</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Microsoft YaHei UI'; font-size:11pt;\">1.\u6c42\u89e3\u7ed3\u679c\u4e2d\uff0cF\u3001B\u3001L\u3001R\u3001U\u3001D\u5206\u522b\u4ee3\u8868\u524d\u3001\u540e"
                        "\u3001\u5de6\u3001\u53f3\u3001\u4e0a\u3001\u4e0b\u9762\u3002'\u4ee3\u8868\u9006\u65f6\u9488\u8f6c\u52a8\u4e00\u6b21\uff0c2\u4ee3\u8868\u987a\u65f6\u9488\u8f6c\u52a82\u6b21\u3002</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Microsoft YaHei UI'; font-size:11pt;\">2.\u7b2c\u4e8c\u884c\u7b2c\u4e8c\u4e2a\u9762\u4e3aF\u9762\u3002</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Microsoft YaHei UI'; font-size:11pt;\">3.\u82e5\u624b\u8fb9\u65e0\u9b54\u65b9\uff0c\u53ef\u4f7f\u7528\u9884\u8bbe\u6d4b\u8bd5\u7ed3\u679c\u3002</span></p></body></html>", None))
        self.button_16.setText(QCoreApplication.translate("Form", u"PushButton", None))
        self.button_17.setText(QCoreApplication.translate("Form", u"PushButton", None))
        self.button_18.setText(QCoreApplication.translate("Form", u"PushButton", None))
        self.button_19.setText(QCoreApplication.translate("Form", u"PushButton", None))
        self.button_5.setText(QCoreApplication.translate("Form", u"PushButton", None))
        self.button_4.setText(QCoreApplication.translate("Form", u"PushButton", None))
        self.button_7.setText(QCoreApplication.translate("Form", u"PushButton", None))
        self.button_6.setText(QCoreApplication.translate("Form", u"PushButton", None))
        self.button_8.setText(QCoreApplication.translate("Form", u"PushButton", None))
        self.button_9.setText(QCoreApplication.translate("Form", u"PushButton", None))
        self.button_10.setText(QCoreApplication.translate("Form", u"PushButton", None))
        self.button_11.setText(QCoreApplication.translate("Form", u"PushButton", None))
        self.button_12.setText(QCoreApplication.translate("Form", u"PushButton", None))
        self.button_13.setText(QCoreApplication.translate("Form", u"PushButton", None))
        self.button_14.setText(QCoreApplication.translate("Form", u"PushButton", None))
        self.button_15.setText(QCoreApplication.translate("Form", u"PushButton", None))
        self.label_3.setText("")
        self.button_20.setText(QCoreApplication.translate("Form", u"PushButton", None))
        self.button_21.setText(QCoreApplication.translate("Form", u"PushButton", None))
        self.button_22.setText(QCoreApplication.translate("Form", u"PushButton", None))
        self.button_23.setText(QCoreApplication.translate("Form", u"PushButton", None))
        self.hint_label.setText(QCoreApplication.translate("Form", u"\u6dfb\u52a0\u767d\u8272", None))
        self.bfs_solve_button.setText(QCoreApplication.translate("Form", u"BFS\u6c42\u89e3", None))
        self.dfs_solve_button.setText(QCoreApplication.translate("Form", u"DFS\u6c42\u89e3", None))
        self.reset_button.setText(QCoreApplication.translate("Form", u"\u91cd\u7f6e", None))
        self.groupBox_2.setTitle("")
    # retranslateUi

