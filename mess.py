from PyQt5 import QtCore, QtGui, QtWidgets

def messagebox(title, message, icon, StdBtns):
    mess = QtWidgets.QMessageBox()
    mess.setWindowTitle(title)
    mess.setText(message)

    if icon == 'Information':
        mess.setIcon(QtWidgets.QMessageBox.Information)
    elif icon == 'Critical':
        mess.setIcon(QtWidgets.QMessageBox.Critical)
    elif icon == "Warning":
        mess.setIcon(QtWidgets.QMessageBox.Warning)
    elif icon == "Question":
        mess.setIcon(QtWidgets.QMessageBox.Question)
    else:
        mess.setIcon(QtWidgets.QMessageBox.NoIcon)
        
    if StdBtns == "Ok":
        mess.setStandardButtons(QtWidgets.QMessageBox.Ok)
    else:
        mess.setStandardButtons(QtWidgets.QMessageBox.Cancel)

    mess.exec_()