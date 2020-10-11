# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'groupsView.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class AddGroupDialog(QtWidgets.QDialog):
    def __init__(self):
        super(AddGroupDialog, self).__init__()
        self.ui = Ui_AddGroupDialog()
        self.ui.setupUi(self)
        self.exec_()

    @staticmethod
    def getGroupProperties():
        dialog = AddGroupDialog()
        group_name = dialog.ui.groupNameEdit.text()
        min_val = dialog.ui.groupVolume.value()
        max_val = dialog.ui.doubleSpinBox.value()
        if min_val >= max_val:
            raise Exception('Bad value')
        return (group_name, min_val, max_val)


class Ui_AddGroupDialog(object):
    def setupUi(self, AddGroupDialog):
        AddGroupDialog.setObjectName("AddGroupDialog")
        AddGroupDialog.resize(310, 156)
        AddGroupDialog.setModal(True)
        self.addGroupOK = QtWidgets.QDialogButtonBox(AddGroupDialog)
        self.addGroupOK.setGeometry(QtCore.QRect(40, 120, 261, 32))
        self.addGroupOK.setOrientation(QtCore.Qt.Horizontal)
        self.addGroupOK.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.addGroupOK.setObjectName("addGroupOK")
        self.formLayoutWidget = QtWidgets.QWidget(AddGroupDialog)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 20, 291, 91))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.formLayoutWidget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.groupNameEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.groupNameEdit.setObjectName("groupNameEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.groupNameEdit)
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.groupVolume = QtWidgets.QDoubleSpinBox(self.formLayoutWidget)
        self.groupVolume.setObjectName("groupVolume")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.groupVolume)
        self.label_3 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.doubleSpinBox = QtWidgets.QDoubleSpinBox(self.formLayoutWidget)
        self.doubleSpinBox.setObjectName("doubleSpinBox")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.doubleSpinBox)
        self.groupVolume.setMaximum(100000000)
        self.doubleSpinBox.setMaximum(100000000)

        self.retranslateUi(AddGroupDialog)
        self.addGroupOK.accepted.connect(AddGroupDialog.accept)
        self.addGroupOK.rejected.connect(AddGroupDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(AddGroupDialog)

    def retranslateUi(self, AddGroupDialog):
        _translate = QtCore.QCoreApplication.translate
        AddGroupDialog.setWindowTitle(_translate("AddGroupDialog", "Добавлние ассорт.группы"))
        self.label.setText(_translate("AddGroupDialog", "Наименование"))
        self.label_2.setText(_translate("AddGroupDialog", "Min. объем"))
        self.label_3.setText(_translate("AddGroupDialog", "Max. объем"))

