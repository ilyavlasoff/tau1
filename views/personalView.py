# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'personalView.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class AddEmployeeDialog(QtWidgets.QDialog):
    def __init__(self):
        super(AddEmployeeDialog, self).__init__()
        self.ui = Ui_AddPersonalDialog()
        self.ui.setupUi(self)
        self.exec_()

    @staticmethod
    def getEmployeeProperties():
        dialog = AddEmployeeDialog()
        return (dialog.ui.personalNameEdit.text(), dialog.ui.workTimeValue.value(), dialog.ui.salaryValue.value())

class Ui_AddPersonalDialog(object):
    def setupUi(self, AddPersonalDialog):
        AddPersonalDialog.setObjectName("AddPersonalDialog")
        AddPersonalDialog.resize(309, 159)
        AddPersonalDialog.setModal(True)
        self.addPersonOK = QtWidgets.QDialogButtonBox(AddPersonalDialog)
        self.addPersonOK.setGeometry(QtCore.QRect(120, 120, 181, 32))
        self.addPersonOK.setOrientation(QtCore.Qt.Horizontal)
        self.addPersonOK.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.addPersonOK.setObjectName("addPersonOK")
        self.formLayoutWidget = QtWidgets.QWidget(AddPersonalDialog)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 20, 291, 91))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.formLayoutWidget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.personalNameEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.personalNameEdit.setObjectName("personalNameEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.personalNameEdit)
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.salaryValue = QtWidgets.QDoubleSpinBox(self.formLayoutWidget)
        self.salaryValue.setObjectName("salaryValue")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.salaryValue)
        self.label_3 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.workTimeValue = QtWidgets.QDoubleSpinBox(self.formLayoutWidget)
        self.workTimeValue.setObjectName("workTimeValue")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.workTimeValue)
        self.salaryValue.setMaximum(100000000)
        self.workTimeValue.setMaximum(100000000)

        self.retranslateUi(AddPersonalDialog)
        self.addPersonOK.accepted.connect(AddPersonalDialog.accept)
        self.addPersonOK.rejected.connect(AddPersonalDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(AddPersonalDialog)

    def retranslateUi(self, AddPersonalDialog):
        _translate = QtCore.QCoreApplication.translate
        AddPersonalDialog.setWindowTitle(_translate("AddPersonalDialog", "Добавление персонала"))
        self.label.setText(_translate("AddPersonalDialog", "Наименование"))
        self.label_2.setText(_translate("AddPersonalDialog", "Зараб. плата"))
        self.label_3.setText(_translate("AddPersonalDialog", "Время работы"))

