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
    def openAddTrain(self):
        self.addtrain = QtWidgets.QWidget()
        self.ui = AddTrain()
        self.ui.setupUi(self.addtrain)
        self.addtrain.show()
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
        self.pushButton.clicked.connect(self.openAddTrain)
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
        self.pushButton_3.clicked.connect(self.update_add_train)
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
    def update_add_train(self):
            self.form.close()
            self.form = QtWidgets.QWidget()
            self.ui = Ui_Form()
            self.ui.setupUi(self.form)
            self.form.showFullScreen()
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
class AddTrain(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.label = QtWidgets.QLabel(Form)
        self.addtrain = Form 
        self.label.setGeometry(QtCore.QRect(80, 10, 251, 21))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(20, 50, 121, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(20, 110, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(20, 170, 171, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(220, 240, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.comboBox = QtWidgets.QComboBox(Form)
        self.comboBox.setGeometry(QtCore.QRect(20, 140, 91, 22))
        self.comboBox.addItems(["Электричка", "Скороростной поезд"])
        self.comboBox.setObjectName("comboBox")
        self.comboBox_2 = QtWidgets.QComboBox(Form)
        self.comboBox_2.setGeometry(QtCore.QRect(20, 190, 91, 22))
        self.comboBox_2.addItems(["3", "4", "5","6"])
        self.comboBox_2.setObjectName("comboBox_2")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(20, 80, 121, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setValidator(QtGui.QIntValidator())
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        self.db = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="VU0NbHq3",
            database="db_yar_rzd"
        )
        self.cursor = self.db.cursor()
        self.pushButton.clicked.connect(self.add_train)

    def add_train(self):
        train_number = self.lineEdit.text()
        train_type = self.comboBox.currentText()
        wagon_count = self.comboBox_2.currentText()
        if self.is_duplicate(train_number):
            QMessageBox.warning(self.addtrain, "Предупреждение", "Данный номер поезда уже существует.")
            return
        sql = "INSERT INTO train (num_train, type_train, kol_train) VALUES (%s, %s, %s)"
        values = (train_number, train_type, wagon_count)
        try:
            self.cursor.execute(sql, values)
            self.db.commit()
            QMessageBox.information(self.addtrain, "Результат", "Данные успешно добавлены в базу данных")
            self.lineEdit.clear()
        except mysql.connector.Error as err:
            print(f"Ошибка: {err}")
 
    def is_duplicate(self, train_number):
        sql = "SELECT COUNT(*) FROM train WHERE num_train = %s"
        self.cursor.execute(sql, (train_number,))
        result = self.cursor.fetchone()
        return result[0] > 0
 
    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Добавить поезд"))
        self.label.setText(_translate("Form", "Добавление поезда"))
        self.label_2.setText(_translate("Form", "Номер поезда"))
        self.label_3.setText(_translate("Form", "Тип поезда"))
        self.label_4.setText(_translate("Form", "Количество вагонов"))
        self.pushButton.setText(_translate("Form", "Добавить"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())