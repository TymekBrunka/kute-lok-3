# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'adres.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from db_conn import dbConnection
from mess import messagebox

class Ui_FormMainWindow(object):
    def setupUi(self, FormMainWindow):
        FormMainWindow.setObjectName("FormMainWindow")
        FormMainWindow.resize(400, 309)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(FormMainWindow)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.ulica = QtWidgets.QLineEdit(FormMainWindow)
        self.ulica.setObjectName("ulica")
        self.verticalLayout.addWidget(self.ulica)
        self.label = QtWidgets.QLabel(FormMainWindow)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.kod_pocztowy = QtWidgets.QLineEdit(FormMainWindow)
        self.kod_pocztowy.setObjectName("kod_pocztowy")
        self.verticalLayout.addWidget(self.kod_pocztowy)
        self.label_2 = QtWidgets.QLabel(FormMainWindow)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.miejscowosc = QtWidgets.QLineEdit(FormMainWindow)
        self.miejscowosc.setObjectName("miejscowosc")
        self.verticalLayout.addWidget(self.miejscowosc)
        self.label_3 = QtWidgets.QLabel(FormMainWindow)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.pushButton = QtWidgets.QPushButton(FormMainWindow)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(FormMainWindow)
        QtCore.QMetaObject.connectSlotsByName(FormMainWindow)
        self.pushButton.clicked.connect(self.insertRecord)
    
    def insertRecord(self):
        ulica = self.ulica.text()
        kod = self.kod_pocztowy.text()
        miejscowosc = self.miejscowosc.text()
        params = (ulica, kod, miejscowosc)

        query = """
                insert into adresy (ulica, kod, miejscowosc) values (%s, %s, %s);
                """

        db = dbConnection()
        db.connect()
        curs = db.execute(query, params)
        db.close()
        if curs.statusmessage == "INSERT 0 1":
            messagebox("Record inserted", "Record has been inserted", "Information", "Ok")
        else:
            messagebox("Record has not been inserted", "Record has not been inserted", "Critical", "Ok")

    def retranslateUi(self, FormMainWindow):
        _translate = QtCore.QCoreApplication.translate
        FormMainWindow.setWindowTitle(_translate("FormMainWindow", "Moja apka"))
        self.label.setText(_translate("FormMainWindow", "Ulica"))
        self.label_2.setText(_translate("FormMainWindow", "Kod pocztowy"))
        self.label_3.setText(_translate("FormMainWindow", "Miejscowośc"))
        self.pushButton.setText(_translate("FormMainWindow", "Wstaw rekord"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    FormMainWindow = QtWidgets.QWidget()
    ui = Ui_FormMainWindow()
    ui.setupUi(FormMainWindow)
    FormMainWindow.show()
    sys.exit(app.exec_())
