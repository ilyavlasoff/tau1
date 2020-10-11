# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'productView.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class AddProductDialog(QtWidgets.QDialog):
    def __init__(self):
        super(AddProductDialog, self).__init__()
        self.ui = Ui_AddProductDialog()
        self.ui.setupUi(self)
        self.exec_()

    @staticmethod
    def getProductProperties():
        dialog = AddProductDialog()
        product_name = dialog.ui.productEdit.text()
        max_production = dialog.ui.maxProductProduction.value()
        min_production = dialog.ui.minProductProduction.value()
        wholesale_price = dialog.ui.wholesaleProductPrice.value()
        cost_price = dialog.ui.costProductPrice.value()
        return (product_name, max_production, min_production, wholesale_price, cost_price)

class Ui_AddProductDialog(object):
    def setupUi(self, AddProductDialog):
        AddProductDialog.setObjectName("AddProductDialog")
        AddProductDialog.resize(406, 218)
        AddProductDialog.setModal(True)
        self.addProductOK = QtWidgets.QDialogButtonBox(AddProductDialog)
        self.addProductOK.setGeometry(QtCore.QRect(210, 180, 181, 32))
        self.addProductOK.setOrientation(QtCore.Qt.Horizontal)
        self.addProductOK.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.addProductOK.setObjectName("addProductOK")
        self.formLayoutWidget = QtWidgets.QWidget(AddProductDialog)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 10, 381, 161))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.productName = QtWidgets.QLabel(self.formLayoutWidget)
        self.productName.setObjectName("productName")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.productName)
        self.productEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.productEdit.setObjectName("productEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.productEdit)
        self.label = QtWidgets.QLabel(self.formLayoutWidget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label)
        self.minProductProduction = QtWidgets.QDoubleSpinBox(self.formLayoutWidget)
        self.minProductProduction.setObjectName("minProductProduction")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.minProductProduction)
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.maxProductProduction = QtWidgets.QDoubleSpinBox(self.formLayoutWidget)
        self.maxProductProduction.setObjectName("maxProductProduction")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.maxProductProduction)
        self.label_3 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.wholesaleProductPrice = QtWidgets.QDoubleSpinBox(self.formLayoutWidget)
        self.wholesaleProductPrice.setObjectName("wholesaleProductPrice")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.wholesaleProductPrice)
        self.label_4 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.costProductPrice = QtWidgets.QDoubleSpinBox(self.formLayoutWidget)
        self.costProductPrice.setObjectName("costProductPrice")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.costProductPrice)
        self.minProductProduction.setMaximum(100000000)
        self.maxProductProduction.setMaximum(100000000)
        self.wholesaleProductPrice.setMaximum(100000000)
        self.costProductPrice.setMaximum(100000000)

        self.retranslateUi(AddProductDialog)
        self.addProductOK.accepted.connect(AddProductDialog.accept)
        self.addProductOK.rejected.connect(AddProductDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(AddProductDialog)

    def retranslateUi(self, AddProductDialog):
        _translate = QtCore.QCoreApplication.translate
        AddProductDialog.setWindowTitle(_translate("AddProductDialog", "Добавление товара"))
        self.productName.setText(_translate("AddProductDialog", "Наименование"))
        self.label.setText(_translate("AddProductDialog", "Мин. выпуск"))
        self.label_2.setText(_translate("AddProductDialog", "Макс. выпуск"))
        self.label_3.setText(_translate("AddProductDialog", "Опт. цена"))
        self.label_4.setText(_translate("AddProductDialog", "Себестоимость"))

