from PyQt5 import QtCore, QtGui, QtWidgets

from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

import precios_ui

import requests

import time

class Worker(QThread):

	cripto_values = pyqtSignal(dict)

	def run(self):

		while(True):

			response = requests.get('https://api.bitso.com/v3/ticker/')

			json_response = response.json()

			# 0 btc_mxn
			# 1 eth_btc
			# 2 eth_mxn
			# 3 xrp_btc
			# 4 xrp_mxn
			# 5 ltc_btc
			# 6 ltc_mxn
			# 7 bch_btc
			# 8 bch_mxn
			# 9 tusd_btc
			# 10 tusd_mxn
			# 11 mana_btc
			# 12 mana_mxn
			# 13 gnt_btc
			# 14 gnt_mxn
			# 15 bat_btc
			# 16 bat_mxn
			# 17 btc_ars
			# 18 btc_dai
			# 19 dai_mxn
			# 20 btc_usd
			# 21 xrp_usd
			# 22 eth_usd
			# 23 dai_ars

			self.cripto_values.emit({
				"bitcoin": {
					'book': json_response['payload'][0]['book'],
					'last': json_response['payload'][0]['last']
				},
				"xrp": {
					'book': json_response['payload'][4]['book'],
					'last': json_response['payload'][4]['last']
				},
				'litecoin': {
					'book': json_response['payload'][6]['book'],
					'last': json_response['payload'][6]['last']
				},
				'ether': {
					'book': json_response['payload'][2]['book'],
					'last': json_response['payload'][2]['last']
				},
				'gnt_btc': {
					'book': json_response['payload'][13]['book'],
					'last': json_response['payload'][13]['last']
				}
			})

			time.sleep(1)

class MainWindow(QtWidgets.QMainWindow, object):

	def __init__(self):

		try:
			
			super(MainWindow, self).__init__()

			self.setWindowFlags(Qt.WindowStaysOnTopHint)

			self.ui = precios_ui.Ui_MainWindow()

			self.ui.setupUi(self)

			self.thread = QThread()

			self.worker = Worker()

			self.worker.moveToThread(self.thread)

			self.thread.started.connect(self.worker.run)
			self.worker.cripto_values.connect(self.print_value)

			self.thread.start()

		except Exception as e:
			
			print(str(e))

	def print_value(self, monedas):

		self.ui.qt_tabla_precios.setRowCount(0)

		for fila_numero, key in enumerate(monedas):

			self.ui.qt_tabla_precios.insertRow(fila_numero)

			self.ui.qt_tabla_precios.setItem(fila_numero, 0, QtWidgets.QTableWidgetItem(str(monedas[key]['book'])))
			self.ui.qt_tabla_precios.setItem(fila_numero, 1, QtWidgets.QTableWidgetItem(str(monedas[key]['last'])))

if __name__ == "__main__":
	app = QtWidgets.QApplication([])
	application = MainWindow()
	application.show()
	app.exec_()