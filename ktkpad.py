# Form implementation generated from reading ui file 'my.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets

import getpass


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1124, 665)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(90, 0, 1031, 601))
        font = QtGui.QFont()
        font.setFamily("D2Coding")
        font.setPointSize(16)
        self.textEdit.setFont(font)
        self.textEdit.setObjectName("textEdit")
        self.spinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox.setGeometry(QtCore.QRect(0, 550, 91, 51))
        font = QtGui.QFont()
        font.setFamily("나눔스퀘어 ExtraBold")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.spinBox.setFont(font)
        self.spinBox.setProperty("value", 16)
        self.spinBox.setObjectName("spinBox")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 520, 71, 17))
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(0, 0, 91, 81))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(0, 80, 91, 81))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(0, 481, 91, 31))
        self.pushButton_3.setObjectName("pushButton_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1124, 29))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.pushButton_3.clicked.connect(self.update_font)
        self.pushButton.clicked.connect(self.showdialogopen)
        self.pushButton_2.clicked.connect(self.showdialogsave)

    def update_font(self):
        font = QtGui.QFont()
        font.setFamily("D2Coding")
        font.setPointSize(self.spinBox.value())
        self.textEdit.setFont(font)

    def showdialogopen(self):
        filename = QtWidgets.QFileDialog.getOpenFileName(
            MainWindow, "파일 열기", ("C:/Users/"+getpass.getuser()), "TXT 파일 (*.txt)")
        if not filename[0] == '':
            f = open(filename[0], 'r')

            self.textEdit.setText(f.read())
            f.close()

    def showdialogsave(self):
        filename = QtWidgets.QFileDialog.getSaveFileName(
            MainWindow, "파일 저장", ("C:/Users/"+getpass.getuser()), "TXT 파일 (*.txt)")
        if not filename[0] == '':
            f = open(filename[0], 'w')

            f.write(self.textEdit.toPlainText())
            f.close()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ktkpad(windows)"))
        self.label.setText(_translate("MainWindow", "글씨크기"))
        self.pushButton.setText(_translate("MainWindow", "열기"))
        self.pushButton_2.setText(_translate("MainWindow", "저장"))
        self.pushButton_3.setText(_translate("MainWindow", "적용"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
