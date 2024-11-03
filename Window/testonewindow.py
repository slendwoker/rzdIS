from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem, QTableWidget, QMessageBox
import mysql.connector
class Ui_MainWindow(object):
    def openWindowTrains(self):
        self.form = QtWidgets.QWidget()
        self.ui = Ui_Form()
        self.ui.setupUi(self.form)
        self.form.showFullScreen()
        MainWindow.close()
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.showFullScreen()
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(590, 390, 151, 61))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(330, 470, 151, 61))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.openWindowTrains)

        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(520, 470, 151, 61))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(700, 470, 151, 61))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(880, 470, 151, 61))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_5.clicked.connect(MainWindow.close)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(410, 80, 671, 101))
        font = QtGui.QFont()
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(500, 170, 371, 71))
        font = QtGui.QFont()
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Регистрация пассажира"))
        self.pushButton_2.setText(_translate("MainWindow", "Поезда"))
        self.pushButton_3.setText(_translate("MainWindow", "Маршруты"))
        self.pushButton_4.setText(_translate("MainWindow", "Пассажиры"))
        self.pushButton_5.setText(_translate("MainWindow", "Выход"))
        self.label.setText(_translate("MainWindow", "Учет перевозки пассажиров"))
        self.label_2.setText(_translate("MainWindow", "на электропоездах"))
class Ui_Form(object):
    def openMainWindow(self):
        self.form.close()
        MainWindow.show()
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(802, 576)
        self.form = Form
        self.tableWidget = QTableWidget(Form)
        self.tableWidget.setGeometry(QtCore.QRect(30, 30, 741, 271))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setHorizontalHeaderLabels(["Номер поезда", "Тип поезда", "Количество вагонов"])
        self.tableWidget.setColumnWidth(0,100)
        self.tableWidget.setColumnWidth(1,150)
        self.tableWidget.setColumnWidth(2,150)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(30, 330, 161, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(210, 330, 161, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(400, 330, 161, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(Form)
        self.pushButton_4.setGeometry(QtCore.QRect(400, 430, 161, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(Form)
        self.pushButton_5.setGeometry(QtCore.QRect(30, 430, 161, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_5.clicked.connect(self.openMainWindow)
        self.pushButton_6 = QtWidgets.QPushButton(Form)
        self.pushButton_6.setGeometry(QtCore.QRect(610, 330, 161, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setObjectName("pushButton_6")
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        self.display_data()

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Добавление поезда"))
        self.pushButton.setText(_translate("Form", "Добавить поезд"))
        self.pushButton_2.setText(_translate("Form", "Редактировать"))
        self.pushButton_3.setText(_translate("Form", "Обновить таблицу"))
        self.pushButton_4.setText(_translate("Form", "Удалить"))
        self.pushButton_5.setText(_translate("Form", "На главную "))
        self.pushButton_6.setText(_translate("Form", "Поиск поезда"))

    def display_data(self):
        # Подключение к базе данных
        connection = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="VU0NbHq3",
            database="db_yar_rzd"
        )
        cursor = connection.cursor()
        query = "SELECT * FROM train"
        cursor.execute(query)
        result = cursor.fetchall()
        self.tableWidget.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.tableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                item = QTableWidgetItem(str(data))
                self.tableWidget.setItem(row_number, column_number, item)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())