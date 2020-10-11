from functools import reduce
from PyQt5 import QtWidgets
from views.mainView import Ui_Form
from views.equipmentView import AddEquipmentDialog
from views.groupsView import AddGroupDialog
from  views.personalView import AddEmployeeDialog
from views.resourceView import AddResourceDialog
from views.productView import AddProductDialog
from TableModel import TableModel
import numpy as np
from LinearOptimizer import LinearOptimizer
from serializer import Serializer
import math


class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.ui.addItemButton.clicked.connect(lambda: self.add_item())
        self.ui.makeCalculationButton.clicked.connect(lambda: self.make_optimization())
        self.ui.addEmployeeButton.clicked.connect(lambda: self.add_employee())
        self.ui.addRawMaterialKindButton.clicked.connect(lambda: self.add_raw_material_kind())
        self.ui.addRangeGroupButton.clicked.connect(lambda: self.add_range_group_button())
        self.ui.addEquipmentButton.clicked.connect(lambda: self.add_equipment_type())
        self.ui.loadButton.clicked.connect(lambda: self.load_from_file())
        self.ui.saveButton.clicked.connect(lambda: self.save_to_file())

        try:
            self.create_models()
        except Exception:
            QtWidgets.QMessageBox.critical(self, 'Error', 'Ошибка создания моделей', QtWidgets.QMessageBox.Ok,
                                           QtWidgets.QMessageBox.Ok)
            return

        for t in (
            self.ui.producedItemsTable,
            self.ui.producedItemsRestrictionsTable,
            self.ui.wholesalePricesTable,
            self.ui.costPriceTable,
            self.ui.salaryTable,
            self.ui.laborCostsTable,
            self.ui.rawMaterialResourcesTable,
            self.ui.rawMaterialConsumptionTable,
            self.ui.itemsToGroupAttachmentTable,
            self.ui.groupVolumeTable,
            self.ui.equipmentResourcesTable,
            self.ui.equipmentResourceConsumptionTable
        ):
            t.resizeColumnsToContents()
            t.resizeRowsToContents()
        self.items_count = 0

    def load_from_file(self):
        try:
            file_path = QtWidgets.QFileDialog.getOpenFileName(self, 'Open file', './')[0]
            restored_data = Serializer.deserialize(file_path)
            if not restored_data:
                raise Exception('Error while reading or parsing file')
            self.create_models(
                restored_data['itemsCount'],
                restored_data['producedItemsTable'],
                restored_data['producedItemsRestrictionsTable'],
                restored_data['wholesalePricesTable'],
                restored_data['costPriceTable'],
                restored_data['salaryTable'],
                restored_data['laborCostsTable'],
                restored_data['rawMaterialResourcesTable'],
                restored_data['rawMaterialConsumptionTable'],
                restored_data['itemsToGroupAttachmentTable'],
                restored_data['groupVolumeTable'],
                restored_data['equipmentResourcesTable'],
                restored_data['equipmentResourceConsumptionTable'],
                restored_data['salaryTotalBudget'],
                restored_data['minCostCriteria'],
                restored_data['maxProdCriteria'],
                restored_data['maxProfitCriteria'],
            )
        except Exception:
            QtWidgets.QMessageBox.critical(self, 'Error', 'Ошибка загрузки значений', QtWidgets.QMessageBox.Ok,
                                           QtWidgets.QMessageBox.Ok)
            return

    def save_to_file(self):
        try:
            file_path = QtWidgets.QFileDialog.getSaveFileName(self, 'Save file', './')[0]
            data = dict()
            data['producedItemsTable'] = self.ui.producedItemsTable.model().getDataMatrix()
            data['producedItemsRestrictionsTable'] = self.ui.producedItemsRestrictionsTable.model().getDataMatrix()
            data['wholesalePricesTable'] = self.ui.wholesalePricesTable.model().getDataMatrix()
            data['costPriceTable'] = self.ui.costPriceTable.model().getDataMatrix()
            data['salaryTable'] = self.ui.salaryTable.model().getDataMatrix()
            data['laborCostsTable'] = self.ui.laborCostsTable.model().getDataMatrix()
            data['rawMaterialResourcesTable'] = self.ui.rawMaterialResourcesTable.model().getDataMatrix()
            data['rawMaterialConsumptionTable'] = self.ui.rawMaterialConsumptionTable.model().getDataMatrix()
            data['itemsToGroupAttachmentTable'] = self.ui.itemsToGroupAttachmentTable.model().getDataMatrix()
            data['groupVolumeTable'] = self.ui.groupVolumeTable.model().getDataMatrix()
            data['equipmentResourcesTable'] = self.ui.equipmentResourcesTable.model().getDataMatrix()
            data['equipmentResourceConsumptionTable'] = self.ui.equipmentResourceConsumptionTable.model().getDataMatrix()
            data['minCostCriteria'] = float(self.ui.minCostCriteria.text())
            data['maxProdCriteria'] = float(self.ui.maxProdCriteria.text())
            data['maxProfitCriteria'] = float(self.ui.maxProfitCriteria.text())
            data['salaryTotalBudget'] = float(self.ui.salaryTotalBudget.text())
            data['itemsCount'] = self.items_count
            Serializer.serialize(file_path, data)
        except Exception:
            QtWidgets.QMessageBox.critical(self, 'Error', 'Ошибка сохранения значений', QtWidgets.QMessageBox.Ok,
                                           QtWidgets.QMessageBox.Ok)
            return

    def create_models(self, items_count = 0, produced_items_table = [],produced_items_restrictions_table = [],
                        wholesale_prices_table = [],cost_price_table = [], salary_table = [],labor_costs_table = [],
                        raw_material_resources_table = [], raw_material_consumption_table = [], items_to_group_attachment_table = [],
                        group_volume_table = [], equipment_resources_table = [], equipment_resource_consumption_table = [],
                        salary_total_budget = 0, min_cost_criteria = 0, max_prod_criteria = 0, max_profit_criteria = 0
                      ):
        produced_table_data_model = TableModel(produced_items_table, ['Наименование'])
        produced_items_restrictions_data_model = TableModel(produced_items_restrictions_table, ['Мин.', 'Макс.'])
        wholesale_prices_data_model = TableModel(wholesale_prices_table, ['Наименование', 'Оптовая цена'])
        cost_price_data_model = TableModel(cost_price_table, ['Наименование', 'Себестоимость'])
        salary_data_model = TableModel(salary_table, ['Должность', 'Время работы', 'Зарплата'])
        raw_material_resource_data_model = TableModel(raw_material_resources_table, ['Наименование', 'Запас'])
        items_to_group_attachment_data_model = TableModel(items_to_group_attachment_table, ['Наименование товара', 'Группа'])
        groups_volume_data_model = TableModel(group_volume_table, ['Наименование', 'Min', 'Max'])
        equipment_resource_data_model = TableModel(equipment_resources_table, ['Наименование', 'Количество'])
        labor_costs_data_model = TableModel(labor_costs_table, [])
        raw_material_data_model = TableModel(raw_material_consumption_table, [])
        equipment_resource_consumption_data_model = TableModel(equipment_resource_consumption_table, [])

        self.ui.producedItemsTable.setModel(produced_table_data_model)
        self.ui.producedItemsRestrictionsTable.setModel(produced_items_restrictions_data_model)
        self.ui.wholesalePricesTable.setModel(wholesale_prices_data_model)
        self.ui.costPriceTable.setModel(cost_price_data_model)
        self.ui.laborCostsTable.setModel(labor_costs_data_model)
        self.ui.salaryTable.setModel(salary_data_model)
        self.ui.rawMaterialConsumptionTable.setModel(raw_material_data_model)
        self.ui.rawMaterialResourcesTable.setModel(raw_material_resource_data_model)
        self.ui.itemsToGroupAttachmentTable.setModel(items_to_group_attachment_data_model)
        self.ui.groupVolumeTable.setModel(groups_volume_data_model)
        self.ui.equipmentResourceConsumptionTable.setModel(equipment_resource_consumption_data_model)
        self.ui.equipmentResourcesTable.setModel(equipment_resource_data_model)

        self.ui.salaryTotalBudget.setText(str(salary_total_budget))
        self.ui.minCostCriteria.setText(str(min_cost_criteria))
        self.ui.maxProdCriteria.setText(str(max_prod_criteria))
        self.ui.maxProfitCriteria.setText(str(max_profit_criteria))

        self.items_count = items_count

    def add_item(self):
        product_name, max_production, min_production, wholesale_price, cost_price = AddProductDialog.getProductProperties()
        self.ui.producedItemsTable.model().addRow([product_name])
        self.ui.producedItemsRestrictionsTable.model().addRow([min_production, max_production])
        self.ui.wholesalePricesTable.model().addRow([product_name, wholesale_price])
        self.ui.costPriceTable.model().addRow([product_name, cost_price])
        self.ui.laborCostsTable.model().addColumn([])
        self.ui.rawMaterialConsumptionTable.model().addColumn([])
        self.ui.itemsToGroupAttachmentTable.model().addRow([product_name, 0])
        self.ui.equipmentResourceConsumptionTable.model().addColumn([])
        self.items_count += 1

    def make_optimization(self):
        try:
            # Ограничения по ресурсам оборудования
            equipment_consumption = self.ui.equipmentResourceConsumptionTable.model().getDataMatrix()
            left_restrictions = equipment_consumption
            equipment_restrictions = self.ui.equipmentResourcesTable.model().getDataMatrix()[:, 1]
            right_restrictions = equipment_restrictions

            # Ограничения по сырью
            raw_material_consumption = self.ui.rawMaterialConsumptionTable.model().getDataMatrix()
            left_restrictions = np.concatenate((left_restrictions, raw_material_consumption), axis=0)
            raw_material_resources = self.ui.rawMaterialResourcesTable.model().getDataMatrix()[:, 1]
            right_restrictions = np.concatenate((right_restrictions, raw_material_resources), axis=0)

            # Ограничения по трудовым ресурсам и заработной плате
            labor_costs = self.ui.laborCostsTable.model().getDataMatrix()
            employee_data = self.ui.salaryTable.model().getDataMatrix()
            salary_sum = self.ui.salaryTotalBudget.text()
            working_time = employee_data[:, 1]
            salary = employee_data[:, 2]
            salary_matrix = (labor_costs * salary[:, np.newaxis]).sum(axis=0)
            left_restrictions = np.concatenate((left_restrictions, labor_costs), axis=0)
            right_restrictions = np.concatenate((right_restrictions, working_time), axis=0)
            left_restrictions = np.concatenate((left_restrictions, [salary_matrix]), axis=0)
            right_restrictions = np.concatenate((right_restrictions, [float(salary_sum)]), axis=0)

            # Ограничения по выпуску продукции
            min_restriction_items = self.ui.producedItemsRestrictionsTable.model().getDataMatrix()[:, 0] * -1
            max_restriction_items = self.ui.producedItemsRestrictionsTable.model().getDataMatrix()[:, 1]
            max_restriction_matrix = np.identity(len(max_restriction_items))
            min_restriction_matrix = np.identity(len(min_restriction_items)) * -1
            left_restrictions = np.concatenate((left_restrictions, max_restriction_matrix), axis=0)
            right_restrictions = np.concatenate((right_restrictions, max_restriction_items), axis=0)
            left_restrictions = np.concatenate((left_restrictions, min_restriction_matrix), axis=0)
            right_restrictions = np.concatenate((right_restrictions, min_restriction_items), axis=0)

            # Ограничения по ассортиментным группам
            group_attachments = self.ui.itemsToGroupAttachmentTable.model().getDataMatrix()[:, 1]
            groups_volumes = self.ui.groupVolumeTable.model().getDataMatrix()[:, 1] * -1
            for gr in range(len(groups_volumes)):
                items_attached = [x for x in range(len(group_attachments)) if group_attachments[x] == gr]
                if len(items_attached) == 0:
                    continue
                restriction_row = np.zeros(len(group_attachments))
                for it in items_attached:
                    restriction_row[it] = -1
                left_restrictions = np.concatenate((left_restrictions, [restriction_row]), axis=0)
                right_restrictions = np.concatenate((right_restrictions, [groups_volumes[gr]]), axis=0)

            # Целевая функция
            target = dict()
            opt_target = dict()
            target['wholesale_price'] = self.ui.wholesalePricesTable.model().getDataMatrix()[:, 1]
            opt_target['wholesale_price'] = 'max'
            target['cost_price'] = self.ui.costPriceTable.model().getDataMatrix()[:, 1]
            opt_target['cost_price'] = 'min'
            target['profit'] = target['wholesale_price'] - target['cost_price']
            opt_target['profit'] = 'max'
        except Exception:
            QtWidgets.QMessageBox.critical(self, 'Error', 'Ошибка при заполнении значений', QtWidgets.QMessageBox.Ok,
                                           QtWidgets.QMessageBox.Ok)
            return

        try:
            compromise_weight = [
                float(self.ui.maxProdCriteria.text()),
                float(self.ui.minCostCriteria.text()),
                float(self.ui.maxProfitCriteria.text())
            ]
        except ValueError:
            QtWidgets.QMessageBox.critical(self, 'Error', 'Ошибка преобразования значимостей', QtWidgets.QMessageBox.Ok,
                                           QtWidgets.QMessageBox.Ok)
            return

        if reduce((lambda x, y: x + y), compromise_weight) != 1:
            QtWidgets.QMessageBox.critical(self, 'Error', 'Сумма значений значимостей не равна 1',
                                           QtWidgets.QMessageBox.Ok, QtWidgets.QMessageBox.Ok)
            return

        non_zero_left_ineq = []
        non_zero_right_ineq = []
        for i in range(len(right_restrictions)):
            if math.isfinite(right_restrictions[i]):
                non_zero_left_ineq.append(left_restrictions[i])
                non_zero_right_ineq.append(right_restrictions[i])
        non_zero_left_ineq = np.array(non_zero_left_ineq)
        non_zero_right_ineq = np.array(non_zero_right_ineq)

        optimizer = LinearOptimizer(self.items_count, non_zero_left_ineq,
                                    non_zero_right_ineq, target,
                                    opt_target, compromise_weight)
        try:
            plain_opt = optimizer.plain_linear_optimize()
            hybrid_opt = optimizer.hybrid_linear_optimize()
        except Exception:
            QtWidgets.QMessageBox.critical(self, 'Error', 'Произошла ошибка', QtWidgets.QMessageBox.Ok,
                                           QtWidgets.QMessageBox.Ok)
            return

        if self.ui.producedItemsTable.model().rowCount > self.items_count:
            cl_mat = np.reshape(self.ui.producedItemsTable.model().getDataMatrix()[: self.items_count, 0], (self.items_count, 1))
            self.ui.producedItemsTable.setModel(TableModel(cl_mat.tolist(), ['Наименование']))
        self.ui.producedItemsTable.model().addRow(['Значение F'])
        self.ui.producedItemsTable.model().addColumn(
            np.concatenate((plain_opt['wholesale_price']['X'], np.array([plain_opt['wholesale_price']['F']]))).tolist(), 'Qm')
        self.ui.producedItemsTable.model().addColumn(
            np.concatenate((plain_opt['cost_price']['X'], np.array([plain_opt['cost_price']['F']]))).tolist(), 'Qc')
        self.ui.producedItemsTable.model().addColumn(
            np.concatenate((plain_opt['profit']['X'], np.array([plain_opt['profit']['F']]))).tolist(), 'Qp')
        self.ui.producedItemsTable.model().addColumn(
            np.concatenate((hybrid_opt['X'][:self.items_count], np.array([hybrid_opt['F']]))).tolist(), 'Qh')
        return


    def add_employee(self):
        employee_type, work_time, salary = AddEmployeeDialog.getEmployeeProperties()
        self.ui.salaryTable.model().addRow([employee_type, work_time, salary])
        self.ui.laborCostsTable.model().addRow([])

    def add_raw_material_kind(self):
        resource_name, resource_value = AddResourceDialog.getResourceProperties()
        self.ui.rawMaterialConsumptionTable.model().addRow([])
        self.ui.rawMaterialResourcesTable.model().addRow([resource_name, resource_value])

    def add_range_group_button(self):
        group_name, min_val, max_val = AddGroupDialog.getGroupProperties()
        self.ui.groupVolumeTable.model().addRow([group_name, min_val, max_val])

    def add_equipment_type(self):
        equipment_name, equipment_resources = AddEquipmentDialog.getEquipmentProperties()
        self.ui.equipmentResourceConsumptionTable.model().addRow([])
        self.ui.equipmentResourcesTable.model().addRow([equipment_name, equipment_resources])