from PySide6.QtWidgets import QGraphicsDropShadowEffect, QWidget, QApplication, QMessageBox
from PySide6.QtCore import QThread, Slot
from PySide6.QtGui import QIcon
from cube_ui import Ui_Form
import sys
from cube import Cube
from functools import partial


class My_Ui(QWidget):
    def __init__(self):
        super().__init__()
        self.setColorCount = 0
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.button_group = self.group_cubeButton()

        self.cBfs = Cube()
        self.bfs_thread = QThread()

        self.cDfs = Cube()
        self.dfs_thread = QThread()

        self.signal_bind()
        self.add_shadow(self.ui.groupBox)
        self.add_shadow(self.ui.groupBox_2)

    def add_shadow(self, widget):
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(10)
        self.shadow.setOffset(0, 0)
        widget.setGraphicsEffect(self.shadow)

    @Slot()
    def on_bfs_solve_button_clicked(self):
        self.cBfs.pattern = self.getColorCode()
        self.bfs_thread.start()

    @Slot()
    def on_dfs_solve_button_clicked(self):
        self.cDfs.pattern = self.getColorCode()
        self.dfs_thread.start()

    def setButtonColor(self, button):
        if button.text() != 'PushButton':
            return
        elif self.setColorCount <= 3:
            self.setToWhite(button)
            if self.setColorCount == 3:
                self.ui.hint_label.setText('添加蓝色')
        elif self.setColorCount <= 7:
            self.setToBule(button)
            if self.setColorCount == 7:
                self.ui.hint_label.setText('添加绿色')
        elif self.setColorCount <= 11:
            self.setToGreen(button)
            if self.setColorCount == 11:
                self.ui.hint_label.setText('添加红色')
        elif self.setColorCount <= 15:
            self.setToRed(button)
            if self.setColorCount == 15:
                self.ui.hint_label.setText('添加橙色')
        elif self.setColorCount <= 19:
            self.setToOrange(button)
            if self.setColorCount == 19:
                self.ui.hint_label.setText('添加黄色')
        else:
            for button in self.button_group:
                if button.text() == 'PushButton':
                    self.setToYellow(button)
            self.setColorCount = 23

        self.setColorCount += 1

    def getColorCode(self):
        color_string = ""
        for button in self.button_group:
            color_string += button.text()
        return color_string

    def error_message(self, flag=0):
        self.bfs_thread.quit()
        self.dfs_thread.quit()
        self.ui.bfs_solve_button.setEnabled(True)
        self.ui.dfs_solve_button.setEnabled(True)
        msg = QMessageBox()
        msg.setWindowTitle('提示')
        msg.setIcon(QMessageBox.Icon.Warning)
        if self.setColorCount != 24:
            msg.setText('魔方状态不完整')
            msg.exec()
            return False
        elif flag == 1:
            msg.setText('魔方状态输入错误，请重新输入')
            msg.exec()
        else:
            return True

    def setToWhite(self, button):
        button.setText("W")
        button.setStyleSheet(
            'background-color: white;\ncolor: rgba(0,0,0,0);\nborder-radius:5px;\nborder:2px solid black;')

    def setToBule(self, button):
        button.setText("B")
        button.setStyleSheet(
            'background-color: blue;\ncolor: rgba(0,0,0,0);\nborder-radius:5px;\nborder:2px solid black;')

    def setToRed(self, button):
        button.setText("R")
        button.setStyleSheet(
            'background-color: red;\ncolor: rgba(0,0,0,0);\nborder-radius:5px;\nborder:2px solid black;')

    def setToOrange(self, button):
        button.setText("O")
        button.setStyleSheet(
            'background-color: orange;\ncolor: rgba(0,0,0,0);\nborder-radius:5px;\nborder:2px solid black;')

    def setToYellow(self, button):
        button.setText("Y")
        button.setStyleSheet(
            'background-color: rgb(246,254,17);\ncolor: rgba(0,0,0,0);\nborder-radius:5px;\nborder:2px solid black;')

    def setToGreen(self, button):
        button.setText("G")
        button.setStyleSheet(
            'background-color: green;\ncolor: rgba(0,0,0,0);\nborder-radius:5px;\nborder:2px solid black;')

    @Slot()
    def on_reset_button_clicked(self):
        for button in self.button_group:
            button.setStyleSheet(
                'background-color: rgb(119, 119, 119);\ncolor: rgba(0,0,0,0);\nborder-radius:5px;')
            # button.setProperty('reset', 'ok')
            # button.style().unpolish(button)
            # button.style().polish(button)
            # button.update()
            button.setText('PushButton')
        self.setColorCount = 0
        self.ui.hint_label.setText('添加白色')
        self.ui.bfs_result_text.setText('')
        self.ui.dfs_result_text.setText('')

    def on_dfsFinishSignal(self, result):
        self.ui.dfs_result_text.setPlainText(result)
        self.ui.dfs_solve_button.setEnabled(True)
        self.dfs_thread.quit()

    def on_bfsFinishedSignal(self, result):
        self.ui.bfs_result_text.setPlainText(result)
        self.ui.bfs_solve_button.setEnabled(True)
        self.bfs_thread.quit()

    def on_dfsStartedSignal(self, text):
        self.ui.dfs_result_text.setPlainText(text)
        self.ui.dfs_solve_button.setEnabled(False)

    def on_bfsStartedSignal(self, text):
        self.ui.bfs_result_text.setPlainText(text)
        self.ui.bfs_solve_button.setEnabled(False)

    @Slot()
    def on_preSet_button_1_clicked(self):
        self.setToWhite(self.ui.button_9)
        self.setToWhite(self.ui.button_14)
        self.setToWhite(self.ui.button_15)
        self.setToWhite(self.ui.button_19)
        self.setToBule(self.ui.button_2)
        self.setToBule(self.ui.button_8)
        self.setToBule(self.ui.button_12)
        self.setToBule(self.ui.button_18)
        self.setToGreen(self.ui.button_6)
        self.setToGreen(self.ui.button_7)
        self.setToGreen(self.ui.button_11)
        self.setToGreen(self.ui.button_16)
        self.setToRed(self.ui.button_10)
        self.setToRed(self.ui.button_17)
        self.setToRed(self.ui.button_22)
        self.setToRed(self.ui.button_23)
        self.setToOrange(self.ui.button_0)
        self.setToOrange(self.ui.button_1)
        self.setToOrange(self.ui.button_5)
        self.setToOrange(self.ui.button_20)
        self.setToYellow(self.ui.button_3)
        self.setToYellow(self.ui.button_4)
        self.setToYellow(self.ui.button_13)
        self.setToYellow(self.ui.button_21)
        self.setColorCount = 24

    @Slot()
    def on_preSet_button_2_clicked(self):
        self.setToOrange(self.ui.button_0)
        self.setToYellow(self.ui.button_1)
        self.setToBule(self.ui.button_2)
        self.setToRed(self.ui.button_3)
        self.setToOrange(self.ui.button_4)
        self.setToGreen(self.ui.button_5)
        self.setToGreen(self.ui.button_6)
        self.setToGreen(self.ui.button_7)
        self.setToYellow(self.ui.button_8)
        self.setToBule(self.ui.button_9)
        self.setToOrange(self.ui.button_10)
        self.setToYellow(self.ui.button_11)
        self.setToRed(self.ui.button_12)
        self.setToWhite(self.ui.button_13)
        self.setToOrange(self.ui.button_14)
        self.setToBule(self.ui.button_15)
        self.setToBule(self.ui.button_16)
        self.setToYellow(self.ui.button_17)
        self.setToRed(self.ui.button_18)
        self.setToRed(self.ui.button_19)
        self.setToWhite(self.ui.button_20)
        self.setToWhite(self.ui.button_21)
        self.setToWhite(self.ui.button_22)
        self.setToGreen(self.ui.button_23)
        self.setColorCount = 24

    # 将cBfs和cDfs定义为其它线程，并进行相应的信号连接
    def signal_bind(self):
        self.bfs_thread.started.connect(self.cBfs.solve_cube_bfs)
        self.cBfs.bfsStartedSignal.connect(self.on_bfsStartedSignal)
        self.cBfs.bfsFinishedSignal.connect(self.on_bfsFinishedSignal)
        self.cBfs.moveToThread(self.bfs_thread)
        self.cBfs.error_signal.connect(self.error_message)

        self.dfs_thread.started.connect(self.cDfs.solve_cube_dfs)
        self.cDfs.dfsStartedSignal.connect(self.on_dfsStartedSignal)
        self.cDfs.dfsFinishedSignal.connect(self.on_dfsFinishSignal)
        self.cDfs.moveToThread(self.dfs_thread)
        self.cDfs.error_signal.connect(self.error_message)

        for button in self.button_group:
            button.clicked.connect(partial(self.setButtonColor, button))

    def group_cubeButton(self):
        return [
            self.ui.button_0,
            self.ui.button_1,
            self.ui.button_2,
            self.ui.button_3,
            self.ui.button_4,
            self.ui.button_5,
            self.ui.button_6,
            self.ui.button_7,
            self.ui.button_8,
            self.ui.button_9,
            self.ui.button_10,
            self.ui.button_11,
            self.ui.button_12,
            self.ui.button_13,
            self.ui.button_14,
            self.ui.button_15,
            self.ui.button_16,
            self.ui.button_17,
            self.ui.button_18,
            self.ui.button_19,
            self.ui.button_20,
            self.ui.button_21,
            self.ui.button_22,
            self.ui.button_23,
        ]

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("./icon.png"))
    my = My_Ui()
    with open('style.qss', 'r') as f:
        my.setStyleSheet(f.read())
    my.show()
    sys.exit(app.exec())
