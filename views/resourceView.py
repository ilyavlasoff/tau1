# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'resourceView.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class AddResourceDialog(QtWidgets.QDialog):
    def __init__(self):
        super(AddResourceDialog, self).__init__()
        self.ui = Ui_AddRawMaterialDialog()
        self.ui.setupUi(self)
        self.exec_()

    @staticmethod
    def getResourceProperties():
        dialog = AddResourceDialog()
        return (dialog.ui.resourceNameEdit.text(), dialog.ui.resourceValue.value())

class Ui_AddRawMaterialDialog(object):
    def setupUi(self, AddRawMaterialDialog):
        AddRawMaterialDialog.setObjectName("AddRawMaterialDialog")
        AddRawMaterialDialog.resize(308, 155)
        AddRawMaterialDialog.setModal(True)
        self.addResourceOK = QtWidgets.QDialogButtonBox(AddRawMaterialDialog)
        self.addResourceOK.setGeometry(QtCore.QRect(120, 120, 181, 32))
        self.addResourceOK.setOrientation(QtCore.Qt.Horizontal)
        self.addResourceOK.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.addResourceOK.setObjectName("addResourceOK")
        self.formLayoutWidget = QtWidgets.QWidget(AddRawMaterialDialog)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 20, 291, 91))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.formLayoutWidget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.resourceNameEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.resourceNameEdit.setObjectName("resourceNameEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.resourceNameEdit)
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.resourceValue = QtWidgets.QDoubleSpinBox(self.formLayoutWidget)
        self.resourceValue.setObjectName("resourceValue")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.resourceValue)
        self.resourceValue.setMaximum(100000000)

        self.retranslateUi(AddRawMaterialDialog)
        self.addResourceOK.accepted.connect(AddRawMaterialDialog.accept)
        self.addResourceOK.rejected.connect(AddRawMaterialDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(AddRawMaterialDialog)

    def retranslateUi(self, AddRawMaterialDialog):
        _translate = QtCore.QCoreApplication.translate
        AddRawMaterialDialog.setWindowTitle(_translate("AddRawMaterialDialog", "Добавление ресурса"))
        self.label.setText(_translate("AddRawMaterialDialog", "Наименование"))
        self.label_2.setText(_translate("AddRawMaterialDialog", "Ресурс"))

