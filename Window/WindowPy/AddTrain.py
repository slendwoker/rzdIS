
from PyQt5 import QtCore, QtGui, QtWidgets
import mysql.connector
from PyQt5.QtWidgets import QMessageBox
class AddTrain(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.label = QtWidgets.QLabel(Form)
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
            QMessageBox.warning(Form, "Предупреждение", "Данный номер поезда уже существует.")
            return
        sql = "INSERT INTO train (num_train, type_train, kol_train) VALUES (%s, %s, %s)"
        values = (train_number, train_type, wagon_count)
        try:
            self.cursor.execute(sql, values)
            self.db.commit()
            print("Данные успешно добавлены в базу данных!")
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
    Form = QtWidgets.QWidget()
    ui = AddTrain()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
