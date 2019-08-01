# -*- coding: utf-8 -*-
#
# Created by: deividneves

import sys
import random

from PyQt5.Qt import QApplication, QMainWindow, QWidget, QGridLayout
from PyQt5 import QtCore, QtGui, QtWidgets

upper_char = ('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
low_char = str('abcdefghijklmnopqrstuvwxyz')
num_char = str('1234567890')
jokey_char = str('!@#$%¨&*()')


class MiPass(QMainWindow):
    def __init__(self, parent=None):
        super(MiPass, self).__init__(parent)
        self.setWindowTitle('MiPass')
        #        MiPass.setObjectName('MiPass')
        self.setFixedSize(600, 350)
        self.MiPass = QWidget()
        self.grid = QGridLayout(self.MiPass)
        self.setCentralWidget(self.MiPass)

        self.groupBox = QtWidgets.QGroupBox(self.MiPass)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 580, 331))
        font = QtGui.QFont()
        font.setFamily("Calibri Light")
        font.setPointSize(14)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.groupBox.setTitle("Configurações")

        self.label1 = QtWidgets.QLabel(self.groupBox)
        self.label1.setGeometry(QtCore.QRect(30, 60, 130, 20))
        font = QtGui.QFont()
        font.setFamily("Calibri Light")
        font.setPointSize(12)
        self.label1.setFont(font)
        self.label1.setObjectName("label1")
        self.label1.setText("Tamanho da senha:")

        self.sizepass = QtWidgets.QSpinBox(self.groupBox)
        self.sizepass.setGeometry(QtCore.QRect(180, 60, 100, 20))
        font = QtGui.QFont()
        font.setFamily("Calibri Light")
        font.setPointSize(12)
        self.sizepass.setFont(font)
        self.sizepass.setContextMenuPolicy(QtCore.Qt.PreventContextMenu)
        self.sizepass.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.sizepass.setStyleSheet("")
        self.sizepass.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.sizepass.setObjectName("sizepass")

        self.upperchar = QtWidgets.QCheckBox(self.groupBox)
        self.upperchar.setGeometry(QtCore.QRect(30, 120, 240, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.upperchar.setFont(font)
        self.upperchar.setObjectName("upperchar")
        self.upperchar.setText("Incluir Letras Maiúsculas (ABC...)")
        self.upperchar.toggled.connect(self.senha)

        self.lowchar = QtWidgets.QCheckBox(self.groupBox)
        self.lowchar.setGeometry(QtCore.QRect(300, 120, 240, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lowchar.setFont(font)
        self.lowchar.setObjectName("lowchar")
        self.lowchar.setText("Incluir Letras Minúsculas (abc...)")
        self.lowchar.toggled.connect(self.senha)

        self.num = QtWidgets.QCheckBox(self.groupBox)
        self.num.setGeometry(QtCore.QRect(30, 150, 180, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.num.setFont(font)
        self.num.setObjectName("num")
        self.num.setText("Incluir Números (123...)")
        self.num.toggled.connect(self.senha)

        self.jokeychar = QtWidgets.QCheckBox(self.groupBox)
        self.jokeychar.setGeometry(QtCore.QRect(300, 150, 260, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.jokeychar.setFont(font)
        self.jokeychar.setObjectName("jokeychar")
        self.jokeychar.setText("Incluir Caracteres Especiais (!@#...)")
        self.jokeychar.toggled.connect(self.senha)

        self.outputpass = QtWidgets.QLineEdit(self.groupBox)
        self.outputpass.setGeometry(QtCore.QRect(30, 225, 530, 30))
        self.outputpass.setObjectName("outputpass")

        self.label2 = QtWidgets.QLabel(self.groupBox)
        self.label2.setGeometry(QtCore.QRect(30, 200, 100, 20))
        font = QtGui.QFont()
        font.setFamily("Calibri Light")
        font.setPointSize(12)
        self.label2.setFont(font)
        self.label2.setObjectName("label2")
        self.label2.setText("Senha gerada:")

        self.copypass = QtWidgets.QPushButton(self.groupBox)
        self.copypass.setGeometry(QtCore.QRect(250, 280, 80, 28))
        self.copypass.setObjectName("copypass")
        self.copypass.setText("Copiar")
        self.copypass.clicked.connect(self.copypass_function)


    def senha(self):
        passwd = int(self.sizepass.text())

        if self.upperchar.isChecked() == True and self.lowchar.isChecked() == True and self.num.isChecked() == True and self.jokeychar.isChecked() == True:
            print(self.outputpass.setText(''.join(random.choice(upper_char + low_char + num_char + jokey_char) for i in range(passwd))))

        if self.upperchar.isChecked() == False and self.lowchar.isChecked() == True and self.num.isChecked() == True and self.jokeychar.isChecked() == True:
            print(self.outputpass.setText(''.join(random.choice(low_char + num_char + jokey_char) for i in range(passwd))))

        if self.upperchar.isChecked() == False and self.lowchar.isChecked() == False and self.num.isChecked() == True and self.jokeychar.isChecked() == True:
            print(self.outputpass.setText(''.join(random.choice(num_char + jokey_char) for i in range(passwd))))

        if self.upperchar.isChecked() == False and self.lowchar.isChecked() == False and self.num.isChecked() == False and self.jokeychar.isChecked() == True:
            print(self.outputpass.setText(''.join(random.choice(jokey_char) for i in range(passwd))))

        if self.upperchar.isChecked() == True and self.lowchar.isChecked() == False and self.num.isChecked() == False and self.jokeychar.isChecked() == True:
            print(self.outputpass.setText(''.join(random.choice(upper_char + jokey_char) for i in range(passwd))))

        if self.upperchar.isChecked() == True and self.lowchar.isChecked() == False and self.num.isChecked() == True and self.jokeychar.isChecked() == False:
            print(self.outputpass.setText(''.join(random.choice(upper_char + num_char) for i in range(passwd))))

        if self.upperchar.isChecked() == False and self.lowchar.isChecked() == True and self.num.isChecked() == True and self.jokeychar.isChecked() == False:
            print(self.outputpass.setText(''.join(random.choice(low_char + num_char) for i in range(passwd))))

        if self.upperchar.isChecked() == False and self.lowchar.isChecked() == True and self.num.isChecked() == False and self.jokeychar.isChecked() == True:
            print(self.outputpass.setText(''.join(random.choice(low_char + jokey_char) for i in range(passwd))))

        if self.upperchar.isChecked() == True and self.lowchar.isChecked() == False and self.num.isChecked() == False and self.jokeychar.isChecked() == False:
            print(self.outputpass.setText(''.join(random.choice(upper_char) for i in range(passwd))))

        if self.upperchar.isChecked() == True and self.lowchar.isChecked() == True and self.num.isChecked() == False and self.jokeychar.isChecked() == False:
            print(self.outputpass.setText(''.join(random.choice(upper_char + low_char) for i in range(passwd))))

        if self.upperchar.isChecked() == True and self.lowchar.isChecked() == True and self.num.isChecked() == True and self.jokeychar.isChecked() == False:
            print(self.outputpass.setText(''.join(random.choice(upper_char + low_char + num_char) for i in range(passwd))))

        if self.upperchar.isChecked() == False and self.lowchar.isChecked() == True and self.num.isChecked() == False and self.jokeychar.isChecked() == False:
            print(self.outputpass.setText(''.join(random.choice(low_char) for i in range(passwd))))

        if self.upperchar.isChecked() == False and self.lowchar.isChecked() == False and self.num.isChecked() == True and self.jokeychar.isChecked() == False:
            print(self.outputpass.setText(''.join(random.choice(num_char) for i in range(passwd))))

        if self.upperchar.isChecked() == True and self.lowchar.isChecked() == True and self.num.isChecked() == False and self.jokeychar.isChecked() == True:
            print(self.outputpass.setText(''.join(random.choice(upper_char + low_char + jokey_char) for i in range(passwd))))

        if self.upperchar.isChecked() == True and self.lowchar.isChecked() == False and self.num.isChecked() == True and self.jokeychar.isChecked() == True:
            print(self.outputpass.setText(''.join(random.choice(upper_char + num_char + jokey_char) for i in range(passwd))))

        if self.upperchar.isChecked() == False and self.lowchar.isChecked() == False and self.num.isChecked() == False and self.jokeychar.isChecked() == False:
            print(self.outputpass.setText(''))

    def copypass_function(self):
        self.outputpass.selectAll()
        self.outputpass.copy()


if __name__ == '__main__':
    qt = QApplication(sys.argv)
    MiPass = MiPass()
    MiPass.show()
    qt.exec()
