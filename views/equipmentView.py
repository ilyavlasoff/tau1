# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'equipmentView.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class AddEquipmentDialog(QtWidgets.QDialog):
    def __init__(self):
        super(AddEquipmentDialog, self).__init__()
        self.ui = Ui_AddEquipmentDialog()
        self.ui.setupUi(self)
        self.exec_()

    @staticmethod
    def getEquipmentProperties():
        dialog = AddEquipmentDialog()
        return (dialog.ui.equipmentNameEdit.text(), dialog.ui.equipmentResourceValue.value())


class Ui_AddEquipmentDialog(object):
    def setupUi(self, AddEquipmentDialog):
        AddEquipmentDialog.setObjectName("AddEquipmentDialog")
        AddEquipmentDialog.resize(310, 161)
        AddEquipmentDialog.setModal(True)
        self.addEquipmentOK = QtWidgets.QDialogButtonBox(AddEquipmentDialog)
        self.addEquipmentOK.setGeometry(QtCore.QRect(30, 120, 271, 32))
        self.addEquipmentOK.setOrientation(QtCore.Qt.Horizontal)
        self.addEquipmentOK.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.addEquipmentOK.setObjectName("addEquipmentOK")
        self.formLayoutWidget = QtWidgets.QWidget(AddEquipmentDialog)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 20, 291, 91))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.formLayoutWidget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.equipmentNameEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.equipmentNameEdit.setObjectName("equipmentNameEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.equipmentNameEdit)
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.equipmentResourceValue = QtWidgets.QDoubleSpinBox(self.formLayoutWidget)
        self.equipmentResourceValue.setObjectName("equipmentResourceValue")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.equipmentResourceValue)
        self.equipmentResourceValue.setMaximum(100000000)

        self.retranslateUi(AddEquipmentDialog)
        self.addEquipmentOK.accepted.connect(AddEquipmentDialog.accept)
        self.addEquipmentOK.rejected.connect(AddEquipmentDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(AddEquipmentDialog)

    def retranslateUi(self, AddEquipmentDialog):
        _translate = QtCore.QCoreApplication.translate
        AddEquipmentDialog.setWindowTitle(_translate("AddEquipmentDialog", "Добавление оборудования"))
        self.label.setText(_translate("AddEquipmentDialog", "Наименование"))
        self.label_2.setText(_translate("AddEquipmentDialog", "Ресурс"))







