# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'precios_ui.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(300, 270)
        MainWindow.setMinimumSize(QtCore.QSize(300, 220))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.qt_tabla_precios = QtWidgets.QTableWidget(self.centralwidget)
        self.qt_tabla_precios.setGeometry(QtCore.QRect(10, 10, 280, 250))
        self.qt_tabla_precios.setMinimumSize(QtCore.QSize(280, 200))
        self.qt_tabla_precios.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.qt_tabla_precios.setFont(font)
        self.qt_tabla_precios.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.qt_tabla_precios.setObjectName("qt_tabla_precios")
        self.qt_tabla_precios.setColumnCount(2)
        self.qt_tabla_precios.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.qt_tabla_precios.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.qt_tabla_precios.setHorizontalHeaderItem(1, item)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        item = self.qt_tabla_precios.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "MONEDA"))
        item = self.qt_tabla_precios.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "PRECIO"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
