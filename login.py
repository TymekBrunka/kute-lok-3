# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

'''
pyuic5 -x login.ui -o login.py
'''

from PyQt5 import QtCore, QtGui, QtWidgets
import hashlib
from PyQt5.QtGui import QPixmap
from db_conn import dbConnection
from mess import messagebox
from adresy import Ui_FormMainWindow


class Ui_FormLogin(object):
    def setupUi(self, FormLogin):
        FormLogin.setObjectName("FormLogin")
        FormLogin.setEnabled(True)
        FormLogin.resize(400, 300)
        FormLogin.setMinimumSize(QtCore.QSize(400, 300))
        FormLogin.setMaximumSize(QtCore.QSize(400, 300))
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(FormLogin)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.img = QtWidgets.QLabel(FormLogin)
        self.img.setMinimumSize(QtCore.QSize(120, 200))
        self.img.setMaximumSize(QtCore.QSize(120, 200))
        self.img.setAutoFillBackground(False)
        self.img.setText("")
        self.img.setObjectName("img")
        self.horizontalLayout.addWidget(self.img)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(FormLogin)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.gmail = QtWidgets.QLineEdit(FormLogin)
        self.gmail.setObjectName("gmail")
        self.verticalLayout.addWidget(self.gmail)
        self.label_2 = QtWidgets.QLabel(FormLogin)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.passwort = QtWidgets.QLineEdit(FormLogin)
        self.passwort.setObjectName("passwort")
        self.passwort.setEchoMode(QtWidgets.QLineEdit.Password)
        self.verticalLayout.addWidget(self.passwort)
        self.logmein = QtWidgets.QPushButton(FormLogin)
        self.logmein.setObjectName("logmein")
        self.verticalLayout.addWidget(self.logmein)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.retranslateUi(FormLogin)
        QtCore.QMetaObject.connectSlotsByName(FormLogin)

        self.logmein.clicked.connect(self.key_loguj)

    def retranslateUi(self, FormLogin):
        _translate = QtCore.QCoreApplication.translate
        FormLogin.setWindowTitle(_translate("FormLogin", "Logowanie (rest in piss)"))
        self.label.setText(_translate("FormLogin", "E-mail"))
        self.label_2.setText(_translate("FormLogin", "Passwort"))
        self.logmein.setText(_translate("FormLogin", "rest in piss"))

        pixmap = QPixmap('kys.jpg')
        self.img.setPixmap(pixmap)
    
    def OpenWindow(self):
        FormLogin.hide()
        self.window = QtWidgets.QWidget()
        self.ui = Ui_FormMainWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    def key_loguj(self):
        email = self.gmail.text()
        passwort = hashlib.md5(self.passwort.text().encode('utf-8')).hexdigest()
        print(passwort)
        db = dbConnection()
        db.connect()

        query = """
                select count(*) from users where email=%s and pass=%s
                """
        params = (email, passwort)
        row = db.fetchone(query, params)
        db.close()
        print(row)
        if len(row[0]) == 1:
            messagebox("Logged in", f"You are logged in as {email}", "Information", "Ok")
            FormLogin.hide()
            self.window = QtWidgets.QMainWindow()
            self.OpenWindow()
        else:
            print("Problem?")
        

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    FormLogin = QtWidgets.QWidget()
    ui = Ui_FormLogin()
    ui.setupUi(FormLogin)
    FormLogin.show()
    sys.exit(app.exec_())
