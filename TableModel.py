import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
import numpy as np


class TableModel(QtCore.QAbstractTableModel):

    def __init__(self, data, header):
        super(TableModel, self).__init__()
        self.data_matrix = data
        self.rowCount = len(data)
        if len(data) == 0:
            self.columnCount = len(header)
        else:
            self.columnCount = len(data[0])
        if self.columnCount > len(header):
            for i in range(len(header), self.columnCount):
                header.append(i)
        self.header = header

    def data(self, index, role):
        if role == Qt.DisplayRole:
            return self.data_matrix[index.row()][index.column()]

    def rowCount(self, index) -> int:
        return self.rowCount

    def columnCount(self, index) -> int:
        return self.columnCount

    def headerData(self, section, orientation, role):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return QVariant(self.header[section])
        return

    def addColumn(self, col, header=None):
        if len(col) < self.rowCount:
            for i in range(len(col), self.rowCount):
                col.append(0)
        for i in range(self.rowCount):
            try:
                self.data_matrix[i].append(float(col[i]))
            except ValueError:
                self.data_matrix[i].append(col[i])
        if header:
            self.header.append(header)
        else:
            self.header.append(self.columnCount)
        self.columnCount += 1
        self.layoutChanged.emit()
        return self

    def addRow(self, row):
        if len(row) < self.columnCount:
            for i in range(len(row), self.columnCount):
                row.append(0)
        temp_row = []
        for i in row:
            try:
                temp_row.append(float(i))
            except ValueError:
                temp_row.append(i)
        self.data_matrix.append(temp_row)
        self.rowCount += 1
        self.layoutChanged.emit()
        return self

    def removeRow(self, row = -1):
        del self.data_matrix[row]
        self.rowCount -= 1

    def removeColumn(self, col = -1):
        for i in self.data_matrix:
            del self.data_matrix[col]
        self.columnCount -= 1

    def flags(self, index: QModelIndex):
        return QtCore.Qt.ItemIsEditable | QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable

    def setData(self, index, value, role):
        try:
            self.data_matrix[index.row()][index.column()] = float(value)
        except ValueError:
            self.data_matrix[index.row()][index.column()] = value
        return True

    def getDataMatrix(self):
        return np.array(self.data_matrix, dtype=object)





