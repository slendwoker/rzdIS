from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem, QTableWidget, QMessageBox, QDialog, QDateEdit
import mysql.connector
from PyQt5.QtGui import QImage, QPalette, QBrush
import random 
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas
from PyQt5.QtGui import QRegularExpressionValidator
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QRegExpValidator
from PyQt5.QtCore import QRegExp

image_path = "D:\\rzd2\\assets\\rzdwal.jpg"
image_path2 = "D:\\rzd2\\assets\\train2.jpg"
image_path3 = "D:\\rzd2\\assets\\ticket.jpg"

connectconfig = {
    "host": "127.0.0.1",
    "user": "root",
    "password": "VU0NbHq3",
    "database": "db_yar_rzd"
}
stili = {
    'label': """
        QLabel {
            color: #90BBE4;
            background-color: rgba(0, 0, 0, 100);
            border: 2px solid white;
            border-radius: 3px;
            padding: 5px;
        }
    """,
    'combobox': """
        QComboBox {
            color: white;
            background-color: rgba(0, 0, 0, 100);
            border: 2px solid white;
            border-radius: 5px;
            padding: 5px;
        }
        QComboBox::drop-down {
            width: 20px;
        }
    """,
    'lineedit': """
        QLineEdit {
            color: white;
            background-color: rgba(0, 0, 0, 100);
            border: 2px solid white;
            border-radius: 5px;
            padding: 5px;
        }
    """,
    'pushbutton': """
        QPushButton {
                background-color: #C06C84; /* Green */
                color: #7F394C;
                border: 2px solid #C06C84;
                border-radius: 10px;
                padding: 10px 20px;
                font-size: 16px;
                font-weight: bold;
            }

            QPushButton:hover {
                background-color: #B83B5E; /* Darker green on hover */
            }
    """,
    'table_style' : """
    QTableWidget {
        background-color: #B5B8B1; /* White background color */
        border: 2px solid #CCCCCC;
        border-radius: 7px;
        font-size: 16px;
    }
    QTableWidget:item {
        padding: 5px;
    }
    QHeaderView::section {
        background-color: #757873;
        border: 1px solid #BBBBBB;
        font-size: 16px;
    }
""", 
    'timeedit' : """
           QDateTimeEdit {
                color: white;
                background-color: rgba(0, 0, 0, 100);
                border: 2px solid white;
                border-radius: 5px;
                padding: 5px;
            }

            QDateTimeEdit::drop-down {
                subcontrol-origin: padding;
                subcontrol-position: top right;
                width: 20px;
                border-left: 2px solid darkgray;
            }

            QDateTimeEdit::down-arrow {
                image: url(down_arrow.png);
            }
        """
}

class Ui_MainWindow(object):
    def openWindowStatik(self):
        self.statik = QtWidgets.QWidget()
        self.ui = Ui_Statik()
        self.ui.setupUi(self.statik)
        self.statik.showFullScreen()
        MainWindow.close()
    def openWindowTrains(self):
        self.form = QtWidgets.QWidget()
        self.ui = Ui_Form()
        self.ui.setupUi(self.form)
        self.form.showFullScreen()
        MainWindow.close()
    def openRoutesTrains(self):
        self.routform = QtWidgets.QWidget()
        self.ui = Ui_Routes()
        self.ui.setupUi(self.routform)
        self.routform.showFullScreen()
        MainWindow.close()
    def openWindowPassengers(self):
        self.passe = QtWidgets.QWidget()
        self.ui = Ui_Passengers()
        self.ui.setupUi(self.passe)
        self.passe.showFullScreen()
        MainWindow.close()
    def openWindowAddPassengers(self):
        self.addpasse = QtWidgets.QWidget()
        self.ui = Ui_AddPassengers()
        self.ui.setupUi(self.addpasse)
        self.addpasse.showFullScreen()
        MainWindow.close()
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.showFullScreen()

        palette = QPalette()
        image = QImage(image_path)
        scaled_image = image.scaled(MainWindow.size())
        palette.setBrush(QPalette.Window, QBrush(scaled_image))
        MainWindow.setPalette(palette)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(580, 320, 250, 81))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(210, 450, 211, 81))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(460, 450, 211, 81))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(710, 450, 211, 81))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(570, 590, 211, 81))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setObjectName("pushButton_5")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(420, 20, 671, 101))
        font = QtGui.QFont()
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(510, 110, 371, 71))
        font = QtGui.QFont()
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(970, 450, 211, 81))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_6.clicked.connect(self.openWindowStatik)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.pushButton.clicked.connect(self.openWindowAddPassengers)
        self.pushButton_2.clicked.connect(self.openWindowTrains)
        self.pushButton_3.clicked.connect(self.openRoutesTrains)
        self.pushButton_4.clicked.connect(self.openWindowPassengers)
        self.pushButton_5.clicked.connect(MainWindow.close)
        self.pushButton.setStyleSheet(stili['pushbutton'])
        self.pushButton_2.setStyleSheet(stili['pushbutton'])
        self.pushButton_3.setStyleSheet(stili['pushbutton'])
        self.pushButton_4.setStyleSheet(stili['pushbutton'])
        self.pushButton_5.setStyleSheet(stili['pushbutton'])
        self.pushButton_6.setStyleSheet(stili['pushbutton'])

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
        self.pushButton_6.setText(_translate("MainWindow", "Статистика"))

class Ui_Statik(object):
    def MainWindow(self):
        self.statik.close()
        MainWindow.show()
    def show_date_edit(self, index):
        if index == 0:  # "За день"
            self.date_edit.setDisplayFormat("yyyy-MM-dd")
        elif index == 1: # За месяц
            self.date_edit.setDisplayFormat("yyyy-MM")
        elif index == 2: # за год
            self.date_edit.setDisplayFormat("yyyy")
        self.date_edit.show()
    def show_passenger_count(self, table_widget):
        try:
            config = mysql.connector.connect(**connectconfig)
            cursor = config.cursor()
            selected_date = self.date_edit.date().toString("yyyy-MM-dd")
            selected_date_2 = self.date_edit.date().toString("yyyy-MM")
            selected_date_3 = self.date_edit.date().toString("yyyy")
            selected_route_text = self.comboBox_2.currentText()
            selected_route_num = int(selected_route_text.split('-')[0].strip())
            date_condition = ""

            if self.comboBox.currentIndex() == 0:  # "За день"
                date_condition = "AND routes.dep_time LIKE %s"
                date_param = f"{selected_date}%"
            elif self.comboBox.currentIndex() == 1:  # "За месяц"
                date_condition = "AND DATE_FORMAT(routes.dep_time, '%Y-%m') = %s"
                date_param = selected_date_2
            elif self.comboBox.currentIndex() == 2:  # "За год"
                date_condition = "AND YEAR(routes.dep_time) = %s"
                date_param = selected_date_3

            config = mysql.connector.connect(**connectconfig)
            cursor = config.cursor()
            query = f"""
            SELECT passengers.surname, passengers.name, routes.dep_time
            FROM passengers
            INNER JOIN routes ON passengers.num_routes = routes.num_rout
            WHERE routes.num_rout = %s
            {date_condition}
            """
            cursor.execute(query, (selected_route_num, date_param))
            result = cursor.fetchall()

            table_widget.setRowCount(0)
            for row_num, row_data in enumerate(result):
                table_widget.insertRow(row_num)
                for col_num, col_data in enumerate(row_data):
                    item = QtWidgets.QTableWidgetItem(str(col_data))
                    table_widget.setItem(row_num, col_num, item)

        except Exception as e:
            print(f"Error executing query: {e}")

        finally:
            cursor.close()
            config.close()
    def setupUi(self, Statik):
        Statik.setObjectName("Statik")
        Statik.resize(1366, 781)
        self.statik = Statik
        palette = QPalette()
        image = QImage(image_path)
        scaled_image = image.scaled(Statik.size())
        palette.setBrush(QPalette.Window, QBrush(scaled_image))
        Statik.setPalette(palette)
        self.label = QtWidgets.QLabel(Statik)
        self.label.setGeometry(QtCore.QRect(370, 60, 671, 51))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Statik)
        self.label_2.setGeometry(QtCore.QRect(380, 150, 221, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Statik)
        self.label_3.setGeometry(QtCore.QRect(780, 150, 281, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(Statik)
        self.pushButton.setGeometry(QtCore.QRect(380, 580, 211, 71))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.tableWidget = QtWidgets.QTableWidget(Statik)
        self.tableWidget.setGeometry(QtCore.QRect(460, 250, 520, 241))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        self.tableWidget.horizontalHeaderItem(0).setText("Фамилия")
        self.tableWidget.horizontalHeaderItem(1).setText("Имя")
        self.tableWidget.horizontalHeaderItem(2).setText("Дата отправления")
        self.tableWidget.setColumnWidth(0, 150)
        self.tableWidget.setColumnWidth(1, 150) 
        self.tableWidget.setColumnWidth(2, 200)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(lambda: self.show_passenger_count(self.tableWidget))
        self.pushButton_2 = QtWidgets.QPushButton(Statik)
        self.pushButton_2.setGeometry(QtCore.QRect(910, 580, 211, 71))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.MainWindow)
        self.date_edit = QDateEdit(self.statik)
        self.date_edit.setGeometry(200, 380, 211, 31)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.date_edit.setFont(font)
        self.date_edit.setObjectName("dateEdit")
        self.date_edit.date().toString("yyyy-MM-dd")
        self.comboBox = QtWidgets.QComboBox(Statik)
        self.comboBox.setGeometry(QtCore.QRect(380, 200, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItems(["За день", "За месяц", "За год" ])
        self.comboBox.currentIndexChanged.connect(self.show_date_edit)
        self.comboBox_2 = QtWidgets.QComboBox(Statik)
        self.comboBox_2.setGeometry(QtCore.QRect(780, 200, 270, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.comboBox_2.setFont(font)
        self.comboBox_2.setObjectName("comboBox_2")
        self.load_routes_from_database()
        self.tableWidget.setStyleSheet(stili["table_style"])
        self.comboBox.setStyleSheet(stili["combobox"])
        self.comboBox_2.setStyleSheet(stili["combobox"])
        self.label.setStyleSheet(stili["label"])
        self.label_2.setStyleSheet(stili["label"])
        self.label_3.setStyleSheet(stili["label"])
        self.pushButton.setStyleSheet(stili["pushbutton"])
        self.pushButton_2.setStyleSheet(stili["pushbutton"])
        self.date_edit.setStyleSheet(stili["timeedit"])

        self.retranslateUi(Statik)
        QtCore.QMetaObject.connectSlotsByName(Statik)

    def load_routes_from_database(self):
        config = mysql.connector.connect(**connectconfig)
        cursor = config.cursor()
        query = "SELECT num_rout, from_where, where_rout FROM routes"
        cursor.execute(query)
        result = cursor.fetchall()
        for route in result:
            display_text = f"{route[0]} - {route[1]} - {route[2]}"
            self.comboBox_2.addItem(display_text)

        cursor.close()
        config.close()
    def retranslateUi(self, Statik):
        _translate = QtCore.QCoreApplication.translate
        Statik.setWindowTitle(_translate("Statik", "Statik"))
        self.label.setText(_translate("Statik", "Статистика по количеству пассажиров "))
        self.label_2.setText(_translate("Statik", "Выберите время"))
        self.label_3.setText(_translate("Statik", "Выберите маршрут"))
        self.pushButton.setText(_translate("Statik", "Показать"))
        self.pushButton_2.setText(_translate("Statik", "На главную"))

class Ui_Form(object):
    def openMainWindow(self):
        self.form.close()
        MainWindow.show()
    def openAddTrain(self):
        self.addtrain = QtWidgets.QWidget()
        self.ui = AddTrain()
        self.ui.setupUi(self.addtrain)
        self.addtrain.setWindowModality(QtCore.Qt.ApplicationModal)
        self.addtrain.show()
    def openEditTrain(self):
        selected_items = self.tableWidget.selectedItems()
        if selected_items:
            selected_row = selected_items[0].row()
            train_number = self.tableWidget.item(selected_row, 0).text()
            train_type = self.tableWidget.item(selected_row, 1).text()
            wagon_count = self.tableWidget.item(selected_row, 2).text()
            self.edittrain = QtWidgets.QWidget()
            self.ui_edit = EditTrain(train_number, train_type, wagon_count)
            self.ui_edit.setupUi(self.edittrain)
            self.edittrain.setWindowModality(QtCore.Qt.ApplicationModal)
            self.edittrain.show()
        else:
            QMessageBox.warning(self.form, "Предупреждение", "Выберите запись для редактирования.")
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1366, 768)
        self.form = Form
        palette = QPalette()
        image = QImage(image_path)
        scaled_image = image.scaled(Form.size())
        palette.setBrush(QPalette.Window, QBrush(scaled_image))
        Form.setPalette(palette)
        self.tableWidget = QTableWidget(Form)
        self.tableWidget.setGeometry(QtCore.QRect(430, 100, 520, 311))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setHorizontalHeaderLabels(["Номер поезда", "Тип поезда", "Количество вагонов"])
        self.tableWidget.setColumnWidth(0, 120)
        self.tableWidget.setColumnWidth(1, 170)
        self.tableWidget.setColumnWidth(2, 170)
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(600, 20, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(28)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(210, 470, 181, 71))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.openAddTrain)
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(440, 470, 181, 71))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.openEditTrain)
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(670, 590, 201, 71))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.update_add_train)
        self.pushButton_4 = QtWidgets.QPushButton(Form)
        self.pushButton_4.setGeometry(QtCore.QRect(920, 470, 181, 71))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.clicked.connect(self.delete_selected_train)
        self.pushButton_5 = QtWidgets.QPushButton(Form)
        self.pushButton_5.setGeometry(QtCore.QRect(440, 590, 181, 71))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_5.clicked.connect(self.openMainWindow)
        self.pushButton_6 = QtWidgets.QPushButton(Form)
        self.pushButton_6.setGeometry(QtCore.QRect(670, 470, 201, 71))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_6.clicked.connect(self.openSearchDialog)
        self.pushButton.setStyleSheet(stili["pushbutton"])
        self.pushButton_2.setStyleSheet(stili["pushbutton"])
        self.pushButton_3.setStyleSheet(stili["pushbutton"])
        self.pushButton_4.setStyleSheet(stili["pushbutton"])
        self.pushButton_5.setStyleSheet(stili["pushbutton"])
        self.pushButton_6.setStyleSheet(stili["pushbutton"])
        self.tableWidget.setStyleSheet(stili["table_style"])

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        self.display_data()
    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Добавление поезда"))
        self.label.setText(_translate("Form", "Поезда"))
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
        QMessageBox.information(self.form, "Обновление", "База данных успешна обновлена")
    def delete_selected_train(self):
        selected_row = self.tableWidget.currentRow()
        if selected_row >= 0:
            reply = QMessageBox.question(
                self.form,
                'Подтверждение удаления',
                'Вы уверены, что хотите удалить этот поезд?',
                QMessageBox.Yes | QMessageBox.No,
                QMessageBox.No
            )
            if reply == QMessageBox.Yes:
                train_number = self.tableWidget.item(selected_row, 0).text()
                self.delete_train_from_database(train_number)
                self.display_data()
    def delete_train_from_database(self, train_number):
        config = mysql.connector.connect(**connectconfig)
        cursor = config.cursor()
        query = f"DELETE FROM train WHERE num_train = {train_number}"
        cursor.execute(query)
        config.commit()
        cursor.close()
        config.close()
    def display_data(self):
        config = mysql.connector.connect(**connectconfig)
        cursor = config.cursor()
        query = "SELECT * FROM train"
        cursor.execute(query)
        result = cursor.fetchall()
        self.tableWidget.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.tableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                item = QTableWidgetItem(str(data))
                self.tableWidget.setItem(row_number, column_number, item)
    def openSearchDialog(self):
        search_dialog = QDialog()
        search_dialog.setWindowTitle("Поиск поезда")

        # Создание элементов управления для окна поиска
        line_edit = QtWidgets.QLineEdit(search_dialog)
        line_edit.setGeometry(QtCore.QRect(30, 30, 200, 30))

        search_button = QtWidgets.QPushButton(search_dialog)
        search_button.setGeometry(QtCore.QRect(240, 30, 80, 30))
        search_button.setText("Найти")
        label = QtWidgets.QLabel(search_dialog)
        label.setGeometry(QtCore.QRect(30, 70, 290, 20))
        label.setText("Если выделили столбец, то поиск осуществляется")
        label_2 = QtWidgets.QLabel(search_dialog)
        label_2.setGeometry(QtCore.QRect(30, 90, 290, 20))
        label_2.setText("по данному столбцу, если нет, то по всем столбцам")
        search_button.clicked.connect(lambda: self.search_train(line_edit.text(), search_dialog))
        # Отобразить окно поиска
        search_dialog.exec_()
    def search_train(self, keyword, search_dialog):
        config = mysql.connector.connect(**connectconfig)
        cursor = config.cursor()
        selected_column_index = self.tableWidget.currentColumn()
        column_mapping = {
            0: 'num_train', 
            1: 'type_train',  
            2: 'kol_train'    
        }

        if selected_column_index is None or selected_column_index not in column_mapping:
            columns_to_search = ', '.join(column_mapping.values())
            query = f"SELECT * FROM train WHERE CONCAT({columns_to_search}) LIKE '%{keyword}%'"
        else:
            selected_column_name = column_mapping[selected_column_index]
            query = f"SELECT * FROM train WHERE {selected_column_name} LIKE '%{keyword}%'"

        cursor.execute(query)
        result = cursor.fetchall()

        self.tableWidget.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.tableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                item = QTableWidgetItem(str(data))
                self.tableWidget.setItem(row_number, column_number, item)

        search_dialog.accept()

class EditTrain(object):
    def __init__(self, train_number, train_type, wagon_count):
        self.train_number = train_number
        self.train_type = train_type
        self.wagon_count = wagon_count
        self.new_train_number = train_number 
        self.new_train_type = train_type
        self.new_wagon_count = wagon_count
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(585, 478)
        Form.setFixedSize(Form.size())
        Form.setWindowFlags(Form.windowFlags() & ~Qt.WindowMinimizeButtonHint)
        font_size = 14
        self.edittrain = Form
        palette = QPalette()
        image = QImage(image_path2)
        scaled_image = image.scaled(Form.size())
        palette.setBrush(QPalette.Window, QBrush(scaled_image))
        Form.setPalette(palette)
        self.comboBox_2 = QtWidgets.QComboBox(Form)
        self.comboBox_2.setGeometry(QtCore.QRect(200, 330, 141, 31))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItems(["3", "4", "5","6"])
        self.comboBox = QtWidgets.QComboBox(Form)
        self.comboBox.setGeometry(QtCore.QRect(200, 230, 180, 31))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItems(["Электричка", "Скоростной поезд"])
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(140, 10, 320, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(180, 400, 191, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.save_changes)
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(200, 180, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(180, 80, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(180, 280, 221, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(200, 130, 141, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setText(self.train_number)
        self.lineEdit.setValidator(QtGui.QIntValidator())
        self.lineEdit.textChanged.connect(self.check_input)
        self.lineEdit.setMaxLength(6)
        self.comboBox.setCurrentText(self.train_type)
        self.comboBox_2.setCurrentText(self.wagon_count)
        self.comboBox.setFont(QtGui.QFont('MS Shell Dlg 2', font_size))
        self.comboBox_2.setFont(QtGui.QFont('MS Shell Dlg 2', font_size))
        self.lineEdit.setFont(QtGui.QFont('MS Shell Dlg 2', font_size))
        self.label.setStyleSheet(stili['label'])
        self.label_2.setStyleSheet(stili['label'])
        self.label_3.setStyleSheet(stili['label'])
        self.label_4.setStyleSheet(stili['label'])
        self.comboBox.setStyleSheet(stili['combobox'])
        self.comboBox_2.setStyleSheet(stili['combobox'])
        self.lineEdit.setStyleSheet(stili['lineedit'])
        self.pushButton.setStyleSheet(stili['pushbutton'])
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        self.config = mysql.connector.connect(**connectconfig)
        self.cursor = self.config.cursor()
    def check_input(self):
        if self.lineEdit.text() == "0":
            QMessageBox.warning(self.edittrain, "Предупреждение", "Запрещено добавлять число, начинающиеся с 0")
            self.lineEdit.clear()
    def save_changes(self):
        self.new_train_number = self.lineEdit.text()
        self.new_train_type = self.comboBox.currentText()
        self.new_wagon_count = self.comboBox_2.currentText()

        if not self.new_train_number:
            QMessageBox.warning(self.edittrain, "Предупреждение", "Введите номер поезда.")
            return

        self.update_train_in_database(
            self.train_number, self.new_train_number, self.new_train_type, self.new_wagon_count
        )

        # Close the dialog
        self.edittrain.close()

    def update_train_in_database(self, old_train_number, new_train_number, train_type, wagon_count):
        try:
            config = mysql.connector.connect(**connectconfig)
            cursor = config.cursor()
            query = "UPDATE train SET num_train = %s, type_train = %s, kol_train = %s WHERE num_train = %s"
            values = (new_train_number, train_type, wagon_count, old_train_number)
            cursor.execute(query, values)
            config.commit()
            QMessageBox.information(self.edittrain, "Результат", 'Запись обновлена. Пожалуйста нажмите на кнопку "Обновить", чтобы увидеть новую запись')
        except mysql.connector.Error as err:
            print(f"Error: {err}")
    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Редактирование записи"))
        self.pushButton.setText(_translate("Form", "Сохранить"))
        self.label_3.setText(_translate("Form", "Тип поезда"))
        self.label_2.setText(_translate("Form", "Номер поезда"))
        self.label_4.setText(_translate("Form", "Количество вагонов"))

class Edit_Routes(object):
    def __init__(self, routes_num, from_whhere, whhere_rout, train_num, ddep_time, arrr_time, price_num):
        self.routes_num = routes_num
        self.from_whhere = from_whhere
        self.whhere_rout = whhere_rout
        self.train_num = train_num
        self.ddep_time = ddep_time
        self.arrr_time = arrr_time
        self.price_num = price_num
        self.new_routes_num = routes_num
        self.new_from_whhere = from_whhere
        self.new_whhere_rout = whhere_rout
        self.new_train_num = train_num
        self.new_ddep_time = ddep_time
        self.new_arrr_time = arrr_time
        self.new_price_num = price_num
    def setupUi(self, EditRoutes):
        EditRoutes.setObjectName("EditRoutes")
        EditRoutes.resize(674, 481)
        EditRoutes.setFixedSize(EditRoutes.size())
        EditRoutes.setWindowFlags(EditRoutes.windowFlags() & ~Qt.WindowMinimizeButtonHint)
        palette = QPalette()
        image = QImage(image_path2)
        scaled_image = image.scaled(EditRoutes.size())
        palette.setBrush(QPalette.Window, QBrush(scaled_image))
        EditRoutes.setPalette(palette)
        self.editroutes = EditRoutes
        self.label = QtWidgets.QLabel(EditRoutes)
        self.label.setGeometry(QtCore.QRect(210, 10, 320, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(EditRoutes)
        self.label_2.setGeometry(QtCore.QRect(30, 70, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(EditRoutes)
        self.label_3.setGeometry(QtCore.QRect(40, 160, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(EditRoutes)
        self.label_4.setGeometry(QtCore.QRect(40, 250, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(EditRoutes)
        self.label_5.setGeometry(QtCore.QRect(240, 80, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(EditRoutes)
        self.label_6.setGeometry(QtCore.QRect(240, 160, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(EditRoutes)
        self.label_7.setGeometry(QtCore.QRect(240, 250, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(EditRoutes)
        self.label_8.setGeometry(QtCore.QRect(450, 160, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.comboBox = QtWidgets.QComboBox(EditRoutes)
        self.comboBox.setGeometry(QtCore.QRect(30, 290, 161, 31))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItems(["Киров", "Котельнич", "Нижний Новгород", "Зуевка", "Глазов", "Фаленки", "Оричи", "Ленинское","Лянгасово","Шахунья", "Яр"])
        self.comboBox.setFont(QtGui.QFont('MS Shell Dlg 2', 11))
        self.comboBox_2 = QtWidgets.QComboBox(EditRoutes)
        self.comboBox_2.setGeometry(QtCore.QRect(30, 200, 161, 31))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItems(["Киров", "Котельнич", "Нижний Новгород", "Зуевка", "Глазов", "Фаленки", "Оричи", "Ленинское","Лянгасово","Шахунья", "Яр"])
        self.comboBox_2.setFont(QtGui.QFont('MS Shell Dlg 2', 11))
        self.lineEdit = QtWidgets.QLineEdit(EditRoutes)
        self.lineEdit.setGeometry(QtCore.QRect(30, 120, 141, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setFont(QtGui.QFont('MS Shell Dlg 2', 11))
        self.lineEdit.setMaxLength(6)
        self.lineEdit_2 = QtWidgets.QLineEdit(EditRoutes)
        self.lineEdit_2.setGeometry(QtCore.QRect(450, 200, 141, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.setFont(QtGui.QFont('MS Shell Dlg 2', 11))
        self.lineEdit_2.setMaxLength(10)
        self.dateTimeEdit = QtWidgets.QDateTimeEdit(EditRoutes)
        self.dateTimeEdit.setGeometry(QtCore.QRect(240, 200, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.dateTimeEdit.setFont(font)
        self.dateTimeEdit.setObjectName("dateTimeEdit")
        self.lineEdit_3 = QtWidgets.QLineEdit(EditRoutes)
        self.lineEdit_3.setGeometry(QtCore.QRect(240, 120, 141, 31))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_3.setFont(QtGui.QFont('MS Shell Dlg 2', 11))
        self.lineEdit_3.setMaxLength(6)
        self.dateTimeEdit_2 = QtWidgets.QDateTimeEdit(EditRoutes)
        self.dateTimeEdit_2.setGeometry(QtCore.QRect(240, 290, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.dateTimeEdit_2.setFont(font)
        self.dateTimeEdit_2.setObjectName("dateTimeEdit_2")
        self.pushButton = QtWidgets.QPushButton(EditRoutes)
        self.pushButton.setGeometry(QtCore.QRect(220, 380, 201, 71))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.save_changes)
        self.lineEdit.setText(self.routes_num)
        self.comboBox.setCurrentText(self.whhere_rout)
        self.comboBox_2.setCurrentText(self.whhere_rout)
        self.lineEdit_3.setText(self.train_num)
        self.lineEdit_2.setText(self.price_num)
        self.dateTimeEdit_2.setDisplayFormat(self.ddep_time)
        self.dateTimeEdit.setDisplayFormat(self.arrr_time)
        self.label.setStyleSheet(stili['label'])
        self.label_2.setStyleSheet(stili['label'])
        self.label_3.setStyleSheet(stili['label'])
        self.label_4.setStyleSheet(stili['label'])
        self.label_5.setStyleSheet(stili['label'])
        self.label_6.setStyleSheet(stili['label'])
        self.label_7.setStyleSheet(stili['label'])
        self.label_8.setStyleSheet(stili['label'])
        self.comboBox.setStyleSheet(stili['combobox'])
        self.comboBox_2.setStyleSheet(stili['combobox'])
        self.dateTimeEdit.setStyleSheet(stili['timeedit'])
        self.dateTimeEdit_2.setStyleSheet(stili['timeedit'])
        self.lineEdit.setStyleSheet(stili['lineedit'])
        self.lineEdit_2.setStyleSheet(stili['lineedit'])
        self.lineEdit_3.setStyleSheet(stili['lineedit'])
        self.pushButton.setStyleSheet(stili['pushbutton'])
        self.line_edits = [self.lineEdit, self.lineEdit_2, self.lineEdit_3]
        for line_edit in self.line_edits:
            line_edit.textChanged.connect(self.check_input)
        self.retranslateUi(EditRoutes)
        QtCore.QMetaObject.connectSlotsByName(EditRoutes)
        self.config = mysql.connector.connect(**connectconfig)
        self.cursor = self.config.cursor()
    def check_input(self):
        sender = self.editroutes.sender()
        if sender.text() == "0":
            QMessageBox.warning(self.editroutes, "Предупреждение", "Запрещено добавлять число, начинающиеся с 0")
            sender.clear()
    def save_changes(self):
        self.new_routes_num = self.lineEdit.text()
        self.new_from_whhere = self.comboBox.currentText()
        self.new_whhere_rout = self.comboBox_2.currentText()
        self.new_train_num = self.lineEdit_3.text()
        self.new_ddep_time= self.dateTimeEdit.text()
        self.new_arrr_time= self.dateTimeEdit_2.text()
        self.new_price_num = self.lineEdit_2.text()

        if self.new_ddep_time > self.new_arrr_time:
            QMessageBox.warning(self.editroutes, "Предупреждение", "Дата отправления не может быть позже даты прибытия.")
            return
        if not self.new_routes_num:
            QMessageBox.warning(self.editroutes, "Предупреждение", "Введите номер маршрута.")
            return

        self.update_routes_in_database(
            self.routes_num, self.new_routes_num, self.new_from_whhere, self.new_whhere_rout, self.new_train_num,
            self.new_ddep_time, self.new_arrr_time, self.new_price_num
        )

        self.editroutes.close()

    def update_routes_in_database(self, old_routes_num, new_routes_num, from_whhere, whhere_rout, train_num, ddep_time, arr_time, price_num):
        try:
            config = mysql.connector.connect(**connectconfig)
            cursor = config.cursor()
            check_train_query = "SELECT num_train FROM train WHERE num_train = %s"
            cursor.execute(check_train_query, (train_num,))
            if cursor.fetchone() is None:
                QMessageBox.warning(self.editroutes, "Предупреждение", "Такого поезда не существует.")
                print(f"Ошибка: Значение id_train={train_num} не существует в таблице train.")
                return
            query = """UPDATE routes SET num_rout = %s, from_where = %s, where_rout = %s, 
            id_train = %s,
            dep_time = %s,
            arr_time = %s,
            price = %s
            WHERE num_rout = %s
            """
            values = (new_routes_num, from_whhere, whhere_rout, train_num, ddep_time, arr_time, price_num, old_routes_num)
            cursor.execute(query, values)
            config.commit()
            QMessageBox.information(self.editroutes, "Результат", 'Запись обновлена. Пожалуйста нажмите на кнопку "Обновить", чтобы увидеть новую запись')
        except mysql.connector.Error as err:
            if err.errno == 1366:
                QMessageBox.warning(self.editroutes, "Предупреждение", "Вы заполнили не все поля.")
            elif err.errno ==1062:
                QMessageBox.warning(self.editroutes, "Предупреждение", "Номер маршрута уже существует")
            else:
                print(f"Error: {err}")
    def retranslateUi(self, EditRoutes):
        _translate = QtCore.QCoreApplication.translate
        EditRoutes.setWindowTitle(_translate("AddRoutes", "Редактирование маршрута"))
        self.label.setText(_translate("AddRoutes", "Редактирование маршрута"))
        self.label_2.setText(_translate("AddRoutes", "Номер маршрута"))
        self.label_3.setText(_translate("AddRoutes", "Откуда"))
        self.label_4.setText(_translate("AddRoutes", "Куда"))
        self.label_5.setText(_translate("AddRoutes", "Номер поезда"))
        self.label_6.setText(_translate("AddRoutes", "Дата отправления"))
        self.label_7.setText(_translate("AddRoutes", "Дата прибытия"))
        self.label_8.setText(_translate("AddRoutes", "Цена билета"))
        self.dateTimeEdit.setDisplayFormat(_translate("AddRoutes", "yyyy.MM.dd H:mm"))
        self.dateTimeEdit_2.setDisplayFormat(_translate("AddRoutes", "yyyy.MM.dd H:mm"))
        self.pushButton.setText(_translate("AddRoutes", "Сохранить"))

class Ui_EditPass(object):
    def __init__(self, trip_id_num, passport, surname, name, nums_routes):
        self.trip_id_num = trip_id_num
        self.passport = passport
        self.surname = surname
        self.name = name 
        self.nums_routes = nums_routes

        self.new_trip_id_num = trip_id_num
        self.new_passport = passport
        self.new_surname = surname
        self.new_name = name
        self.new_nums_routes = nums_routes
    def setupUi(self, EditPass):
        EditPass.setObjectName("EditPass")
        EditPass.resize(489, 452)
        palette = QPalette()
        image = QImage(image_path2)
        scaled_image = image.scaled(EditPass.size())
        palette.setBrush(QPalette.Window, QBrush(scaled_image))
        EditPass.setPalette(palette)
        self.label = QtWidgets.QLabel(EditPass)
        self.label.setGeometry(QtCore.QRect(100, 10, 330, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.edit_pass = EditPass
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(EditPass)
        self.label_2.setGeometry(QtCore.QRect(30, 50, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(EditPass)
        self.label_3.setGeometry(QtCore.QRect(270, 50, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(EditPass)
        self.label_4.setGeometry(QtCore.QRect(30, 150, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(EditPass)
        self.label_5.setGeometry(QtCore.QRect(270, 150, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(EditPass)
        self.label_6.setGeometry(QtCore.QRect(30, 240, 210, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.pushButton = QtWidgets.QPushButton(EditPass)
        self.pushButton.setGeometry(QtCore.QRect(290, 380, 151, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.save_changes)
        self.lineEdit = QtWidgets.QLineEdit(EditPass)
        self.lineEdit.setGeometry(QtCore.QRect(30, 90, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setMaxLength(10)
        self.lineEdit_2 = QtWidgets.QLineEdit(EditPass)
        self.lineEdit_2.setGeometry(QtCore.QRect(270, 90, 141, 31))
        self.lineEdit_2.setMaxLength(20)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(EditPass)
        self.lineEdit_3.setGeometry(QtCore.QRect(270, 190, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_3.setMaxLength(6)
        self.lineEdit_4 = QtWidgets.QLineEdit(EditPass)
        self.lineEdit_4.setGeometry(QtCore.QRect(30, 190, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_4.setMaxLength(6)
        self.comboBox = QtWidgets.QComboBox(EditPass)
        self.comboBox.setGeometry(QtCore.QRect(30, 290, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        self.load_routes_from_database()
        self.lineEdit.setText(self.passport)
        self.lineEdit_2.setText(self.surname)
        self.lineEdit_3.setText(self.name)
        self.lineEdit_4.setText(str(self.trip_id_num))
        for index in range(self.comboBox.count()):
            item_text = self.comboBox.itemText(index)
            if item_text.startswith(f"{self.nums_routes} -"):
                self.comboBox.setCurrentIndex(index)
                break
        self.label.setStyleSheet(stili['label'])
        self.label_2.setStyleSheet(stili['label'])
        self.label_3.setStyleSheet(stili['label'])
        self.label_4.setStyleSheet(stili['label'])
        self.label_5.setStyleSheet(stili['label'])
        self.label_6.setStyleSheet(stili['label'])
        self.lineEdit.setStyleSheet(stili['lineedit'])
        self.comboBox.setStyleSheet(stili['combobox'])
        self.lineEdit_2.setStyleSheet(stili['lineedit'])
        self.lineEdit_3.setStyleSheet(stili['lineedit'])
        self.lineEdit_4.setStyleSheet(stili['lineedit'])
        self.pushButton.setStyleSheet(stili['pushbutton'])
        self.line_edits = [self.lineEdit, self.lineEdit_2, self.lineEdit_3, self.lineEdit_4]
        for line_edit in self.line_edits:
            line_edit.textChanged.connect(self.check_input)

        self.retranslateUi(EditPass)
        QtCore.QMetaObject.connectSlotsByName(EditPass)
        self.config = mysql.connector.connect(**connectconfig)
        self.cursor = self.config.cursor()
    def check_input(self):
        sender = self.edit_pass.sender()
        if sender.text() == "0":
            QMessageBox.warning(self.edit_pass, "Предупреждение", "Запрещено добавлять число, начинающиеся с 0")
            sender.clear()
    def save_changes(self):
        self.new_trip_id_num = self.lineEdit_4.text()
        self.new_passport = self.lineEdit.text()
        self.new_surname = self.lineEdit_2.text()
        self.new_name = self.lineEdit_3.text()
        self.new_nums_routes = self.comboBox.currentText().split(' ')[0]


        if not self.new_trip_id_num:
            QMessageBox.warning(self.edit_pass, "Предупреждение", "Введите номер поездки.")
            return

        self.update_routes_in_database(
            self.trip_id_num, self.new_trip_id_num, self.new_passport, self.new_surname, self.new_name, self.new_nums_routes
        )

        self.edit_pass.close()

    def update_routes_in_database(self, old_trip_id_num, new_trip_id_num, passport, surname, name, nums_routes):
        try:
            config = mysql.connector.connect(**connectconfig)
            cursor = config.cursor()
            check_train_query = "SELECT num_rout FROM routes WHERE num_rout = %s"
            cursor.execute(check_train_query, (nums_routes,))
            if cursor.fetchone() is None:
                print(f"Ошибка: Значение id_train={nums_routes} не существует в таблице train.")
                return
            query = """UPDATE passengers SET trip_id = %s,passport = %s, surname = %s, name = %s, num_routes = %s 
            
            WHERE trip_id = %s
            """
            values = (new_trip_id_num, passport, surname, name, nums_routes, old_trip_id_num)
            cursor.execute(query, values)
            config.commit()
            QMessageBox.information(self.edit_pass, "Результат", 'Запись обновлена. Пожалуйста нажмите на кнопку "Обновить", чтобы увидеть новую запись')
        except mysql.connector.Error as err:
            if err.errno == 1366:
                QMessageBox.warning(self.edit_pass, "Ошибка", "Некорректное значение для поля 'passport'.")
            else:
                QMessageBox.warning(self.edit_pass, "Ошибка", f"Ошибка при сохранении изменений: {err}")
    def load_routes_from_database(self):
        config = mysql.connector.connect(**connectconfig)
        cursor = config.cursor()
        query = "SELECT num_rout, from_where, where_rout FROM routes"
        cursor.execute(query)
        result = cursor.fetchall()

        for route in result:
        # Concatenate the columns and add to the comboBox
            display_text = f"{route[0]} - {route[1]} - {route[2]}"
            self.comboBox.addItem(display_text)

        cursor.close()
        config.close()
    def retranslateUi(self, EditPass):
        _translate = QtCore.QCoreApplication.translate
        EditPass.setWindowTitle(_translate("EditPass", "Редактирование пассажира"))
        self.label.setText(_translate("EditPass", "Редактирование пассажира"))
        self.label_2.setText(_translate("EditPass", "Паспорт"))
        self.label_3.setText(_translate("EditPass", "Фамилия"))
        self.label_4.setText(_translate("EditPass", "Номер поездки"))
        self.label_5.setText(_translate("EditPass", "Имя"))
        self.label_6.setText(_translate("EditPass", "Выберите маршрут"))
        self.pushButton.setText(_translate("EditPass", "Изменить"))

class AddTrain(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(585, 478)
        Form.setFixedSize(Form.size())
        Form.setWindowFlags(Form.windowFlags() & ~Qt.WindowMinimizeButtonHint)
        font_size = 14
        palette = QPalette()
        image = QImage(image_path2)
        scaled_image = image.scaled(Form.size())
        palette.setBrush(QPalette.Window, QBrush(scaled_image))
        Form.setPalette(palette)
        self.label = QtWidgets.QLabel(Form)
        self.addtrain = Form 
        self.label.setGeometry(QtCore.QRect(140, 10, 320, 51))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(180, 80, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(200, 180, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(180, 280, 221, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(180, 400, 191, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.comboBox = QtWidgets.QComboBox(Form)
        self.comboBox.setGeometry(QtCore.QRect(200, 230, 180, 31))
        self.comboBox.addItems(["Электричка", "Скоростной поезд"])
        self.comboBox.setObjectName("comboBox")
        self.comboBox.setFont(QtGui.QFont('MS Shell Dlg 2', font_size))
        self.comboBox_2 = QtWidgets.QComboBox(Form)
        self.comboBox_2.setGeometry(QtCore.QRect(200, 330, 141, 31))
        self.comboBox_2.addItems(["3", "4", "5","6"])
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.setFont(QtGui.QFont('MS Shell Dlg 2', font_size))
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(200, 130, 141, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setFont(QtGui.QFont('MS Shell Dlg 2', font_size))
        self.lineEdit.setValidator(QtGui.QIntValidator())
        self.lineEdit.textChanged.connect(self.check_input)
        self.lineEdit.setMaxLength(6)
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        self.config = mysql.connector.connect(**connectconfig)
        self.cursor = self.config.cursor()
        self.pushButton.clicked.connect(self.add_train)
        self.label.setStyleSheet(stili['label'])
        self.label_2.setStyleSheet(stili['label'])
        self.label_3.setStyleSheet(stili['label'])
        self.label_4.setStyleSheet(stili['label'])
        self.comboBox.setStyleSheet(stili['combobox'])
        self.comboBox_2.setStyleSheet(stili['combobox'])
        self.lineEdit.setStyleSheet(stili['lineedit'])
        self.pushButton.setStyleSheet(stili['pushbutton'])
    def check_input(self):
        if self.lineEdit.text() == "0":
            QMessageBox.warning(self.addtrain, "Предупреждение", "Запрещено добавлять число, начинающиеся с 0")
            self.lineEdit.clear()
    def add_train(self):
        train_number = self.lineEdit.text()
        train_type = self.comboBox.currentText()
        wagon_count = self.comboBox_2.currentText()
        if not all([train_number, train_type, wagon_count]):
            QMessageBox.warning(self.addtrain, "Предупреждение", "Вы заполнили не все поля.")
            return
        if self.is_duplicate(train_number):
            QMessageBox.warning(self.addtrain, "Предупреждение", "Данный номер поезда уже существует.")
            return
        sql = "INSERT INTO train (num_train, type_train, kol_train) VALUES (%s, %s, %s)"
        values = (train_number, train_type, wagon_count)
        try:
            self.cursor.execute(sql, values)
            self.config.commit()
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

class Ui_AddPassengers(object):
    def openMainWindow(self):
        self.addpasse.close()
        MainWindow.show()
    def setupUi(self, AddPassengers):
        validator = QRegularExpressionValidator(QtCore.QRegularExpression("[а-яА-Я]*"))
        font_size = 14
        AddPassengers.setObjectName("AddPassengers")
        AddPassengers.resize(1366, 768)
        palette = QPalette()
        image = QImage(image_path)
        scaled_image = image.scaled(AddPassengers.size())
        palette.setBrush(QPalette.Window, QBrush(scaled_image))
        AddPassengers.setPalette(palette)
        self.label = QtWidgets.QLabel(AddPassengers)
        self.label.setGeometry(QtCore.QRect(480, 30, 425, 51))
        font = QtGui.QFont()
        self.addpasse = AddPassengers
        self.addpass = AddPassengers
        font.setPointSize(28)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(AddPassengers)
        self.label_3.setGeometry(QtCore.QRect(800, 150, 130, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_7 = QtWidgets.QLabel(AddPassengers)
        self.label_7.setGeometry(QtCore.QRect(600, 400, 240, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.lineEdit_7 = QtWidgets.QLineEdit(AddPassengers)
        self.lineEdit_7.setGeometry(QtCore.QRect(600, 450, 281, 61))
        self.lineEdit_7.setMaxLength(10)
        self.lineEdit_7.setValidator(QtGui.QIntValidator())
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lineEdit_7.setFont(font)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.label_4 = QtWidgets.QLabel(AddPassengers)
        self.label_4.setGeometry(QtCore.QRect(800, 290, 71, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(AddPassengers)
        self.label_5.setGeometry(QtCore.QRect(350, 150, 125, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.pushButton = QtWidgets.QPushButton(AddPassengers)
        self.pushButton.setGeometry(QtCore.QRect(150, 590, 231, 71))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.add_passenger)
        self.lineEdit_2 = QtWidgets.QLineEdit(AddPassengers)
        self.lineEdit_2.setGeometry(QtCore.QRect(800, 200, 231, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.setValidator(validator)
        self.lineEdit_2.setMaxLength(20)
        self.lineEdit_3 = QtWidgets.QLineEdit(AddPassengers)
        self.lineEdit_3.setGeometry(QtCore.QRect(800, 330, 231, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_3.setValidator(validator)
        self.lineEdit_3.setMaxLength(20)
        self.lineEdit_4 = QtWidgets.QLineEdit(AddPassengers)
        self.lineEdit_4.setGeometry(QtCore.QRect(350, 200, 281, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_4.setValidator(QtGui.QIntValidator())
        self.lineEdit_4.setMaxLength(10)
        self.comboBox = QtWidgets.QComboBox(AddPassengers)
        self.comboBox.setGeometry(QtCore.QRect(350, 330, 281, 61))
        self.comboBox.setObjectName("comboBox")
        self.load_routes_from_database()
        self.comboBox.setFont(QtGui.QFont('MS Shell Dlg 2', font_size))
        self.label_6 = QtWidgets.QLabel(AddPassengers)
        self.label_6.setGeometry(QtCore.QRect(350, 290, 261, 36))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.pushButton_2 = QtWidgets.QPushButton(AddPassengers)
        self.pushButton_2.setGeometry(QtCore.QRect(1070, 590, 231, 71))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.openMainWindow)
        self.config = mysql.connector.connect(**connectconfig)
        self.cursor = self.config.cursor()
        self.pushButton.setStyleSheet(stili["pushbutton"])
        self.pushButton_2.setStyleSheet(stili["pushbutton"])
        self.label.setStyleSheet(stili['label'])
        self.label_7.setStyleSheet(stili['label'])
        self.label_3.setStyleSheet(stili['label'])
        self.label_4.setStyleSheet(stili['label'])
        self.label_5.setStyleSheet(stili['label'])
        self.label_6.setStyleSheet(stili['label'])
        self.comboBox.setStyleSheet(stili['combobox'])
        self.lineEdit_2.setStyleSheet(stili['lineedit'])
        self.lineEdit_3.setStyleSheet(stili['lineedit'])
        self.lineEdit_4.setStyleSheet(stili['lineedit'])
        self.lineEdit_7.setStyleSheet(stili['lineedit'])
        self.line_edits = [self.lineEdit_4, self.lineEdit_2, self.lineEdit_3, self.lineEdit_7]
        for line_edit in self.line_edits:
            line_edit.textChanged.connect(self.check_input)
        self.retranslateUi(AddPassengers)
        QtCore.QMetaObject.connectSlotsByName(AddPassengers)
    def check_input(self):
        sender = self.addpass.sender()
        if sender.text() == "0":
            QMessageBox.warning(self.addpass, "Предупреждение", "Запрещено добавлять число, начинающиеся с 0")
            sender.clear()
    def load_routes_from_database(self):
        config = mysql.connector.connect(**connectconfig)
        cursor = config.cursor()
        query = "SELECT num_rout, from_where, where_rout FROM routes"
        cursor.execute(query)
        result = cursor.fetchall()

        for route in result:
        # Concatenate the columns and add to the comboBox
            display_text = f"{route[0]} - {route[1]} - {route[2]}"
            self.comboBox.addItem(display_text)

        cursor.close()
        config.close()
    def add_passenger(self):
        passport = self.lineEdit_4.text()
        surname = self.lineEdit_2.text()
        name = self.lineEdit_3.text()
        trip_id = self.lineEdit_7.text()
        routes_text = self.comboBox.currentText()
        route_number = routes_text.split()[0]
        if not (passport and surname and name and trip_id):
            QMessageBox.warning(self.addpass, "Предупреждение", "Заполните все записи")
            return
        if self.is_duplicate(trip_id):
            QMessageBox.warning(self.addpass, "Предупреждение", "Номер поездки должен быть разный")
            return
        sql = "INSERT INTO passengers (passport, trip_id, surname, name, num_routes) VALUES (%s, %s, %s, %s, %s)"
        values = (passport, trip_id, surname, name, route_number)
        try:
            self.cursor.execute(sql, values)
            self.config.commit()
            QMessageBox.information(self.addpass, "Результат", "Данные успешно добавлены в базу данных")
            self.lineEdit_4.clear()
            self.lineEdit_2.clear()
            self.lineEdit_3.clear()
            self.lineEdit_7.clear()
        except mysql.connector.Error as err:
            print(f"Ошибка: {err}")
    

    def is_duplicate(self, trip_id):
        sql = "SELECT COUNT(*) FROM passengers WHERE trip_id = %s"
        self.cursor.execute(sql, (trip_id,))
        result = self.cursor.fetchone()
        return result[0] > 0

    def retranslateUi(self, AddPassengers):
        _translate = QtCore.QCoreApplication.translate
        AddPassengers.setWindowTitle(_translate("AddPassengers", "Регистрация пассажира"))
        self.label.setText(_translate("AddPassengers", "Регистрация пассажира"))
        self.label_3.setText(_translate("AddPassengers", "Фамилия"))
        self.label_4.setText(_translate("AddPassengers", "Имя"))
        self.label_5.setText(_translate("AddPassengers", "Паспорт"))
        self.pushButton.setText(_translate("AddPassengers", "Зарегистрировать"))
        self.label_6.setText(_translate("AddPassengers", "Выберите маршрут"))
        self.label_7.setText(_translate("AddPassengers", "Номер поездки"))
        self.pushButton_2.setText(_translate("AddPassengers", "На главную"))

class Ui_AddRoutes(object):
    def setupUi(self, AddRoutes):
        AddRoutes.setObjectName("AddRoutes")
        AddRoutes.resize(674, 481)
        AddRoutes.setFixedSize(AddRoutes.size())
        AddRoutes.setWindowFlags(AddRoutes.windowFlags() & ~Qt.WindowMinimizeButtonHint)
        palette = QPalette()
        image = QImage(image_path2)
        scaled_image = image.scaled(AddRoutes.size())
        palette.setBrush(QPalette.Window, QBrush(scaled_image))
        AddRoutes.setPalette(palette)
        self.label = QtWidgets.QLabel(AddRoutes)
        self.label.setGeometry(QtCore.QRect(210, 10, 271, 41))
        font = QtGui.QFont()
        self.addrout = AddRoutes
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(AddRoutes)
        self.label_2.setGeometry(QtCore.QRect(30, 70, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(AddRoutes)
        self.label_3.setGeometry(QtCore.QRect(40, 160, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(AddRoutes)
        self.label_4.setGeometry(QtCore.QRect(40, 250, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(AddRoutes)
        self.label_5.setGeometry(QtCore.QRect(240, 80, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(AddRoutes)
        self.label_6.setGeometry(QtCore.QRect(240, 160, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(AddRoutes)
        self.label_7.setGeometry(QtCore.QRect(240, 250, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(AddRoutes)
        self.label_8.setGeometry(QtCore.QRect(450, 160, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.comboBox = QtWidgets.QComboBox(AddRoutes)
        self.comboBox.setGeometry(QtCore.QRect(30, 290, 161, 31))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.setFont(QtGui.QFont('MS Shell Dlg 2', 11))
        self.comboBox_2 = QtWidgets.QComboBox(AddRoutes)
        self.comboBox_2.setGeometry(QtCore.QRect(30, 200, 161, 31))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.setFont(QtGui.QFont('MS Shell Dlg 2', 11))
        self.comboBox.addItems(["Киров", "Котельнич", "Нижний Новгород", "Зуевка", "Глазов", "Фаленки", "Оричи", "Ленинское","Лянгасово","Шахунья", "Яр"])
        self.comboBox_2.addItems(["Киров", "Котельнич", "Нижний Новгород", "Зуевка", "Глазов", "Фаленки", "Оричи", "Ленинское","Лянгасово","Шахунья", "Яр"])
        self.comboBox.setCurrentIndex(-1)
        self.comboBox_2.setCurrentIndex(-1)
        self.lineEdit = QtWidgets.QLineEdit(AddRoutes)
        self.lineEdit.setGeometry(QtCore.QRect(30, 120, 141, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setFont(QtGui.QFont('MS Shell Dlg 2', 11))
        self.lineEdit.setValidator(QtGui.QIntValidator())
        self.lineEdit.setMaxLength(6)
        self.lineEdit_2 = QtWidgets.QLineEdit(AddRoutes)
        self.lineEdit_2.setGeometry(QtCore.QRect(450, 200, 141, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.setFont(QtGui.QFont('MS Shell Dlg 2', 11))
        self.lineEdit_2.setValidator(QtGui.QIntValidator())
        self.lineEdit_2.setMaxLength(6)
        self.dateTimeEdit = QtWidgets.QDateTimeEdit(AddRoutes)
        self.dateTimeEdit.setGeometry(QtCore.QRect(240, 200, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.dateTimeEdit.setFont(font)
        self.dateTimeEdit.setObjectName("dateTimeEdit")
        self.lineEdit_3 = QtWidgets.QLineEdit(AddRoutes)
        self.lineEdit_3.setGeometry(QtCore.QRect(240, 120, 141, 31))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_3.setValidator(QtGui.QIntValidator())
        self.lineEdit_3.setFont(QtGui.QFont('MS Shell Dlg 2', 11))
        self.lineEdit_3.setMaxLength(6)
        self.dateTimeEdit_2 = QtWidgets.QDateTimeEdit(AddRoutes)
        self.dateTimeEdit_2.setGeometry(QtCore.QRect(240, 290, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.dateTimeEdit_2.setFont(font)
        self.dateTimeEdit_2.setObjectName("dateTimeEdit_2")
        self.pushButton = QtWidgets.QPushButton(AddRoutes)
        self.pushButton.setGeometry(QtCore.QRect(220, 380, 201, 71))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.add_routes)
        self.config = mysql.connector.connect(**connectconfig)
        self.cursor = self.config.cursor()
        self.retranslateUi(AddRoutes)
        self.label.setStyleSheet(stili['label'])
        self.label_2.setStyleSheet(stili['label'])
        self.label_3.setStyleSheet(stili['label'])
        self.label_4.setStyleSheet(stili['label'])
        self.label_5.setStyleSheet(stili['label'])
        self.label_6.setStyleSheet(stili['label'])
        self.label_7.setStyleSheet(stili['label'])
        self.label_8.setStyleSheet(stili['label'])
        self.comboBox.setStyleSheet(stili['combobox'])
        self.comboBox_2.setStyleSheet(stili['combobox'])
        self.dateTimeEdit.setStyleSheet(stili['timeedit'])
        self.dateTimeEdit_2.setStyleSheet(stili['timeedit'])
        self.lineEdit.setStyleSheet(stili['lineedit'])
        self.lineEdit_2.setStyleSheet(stili['lineedit'])
        self.lineEdit_3.setStyleSheet(stili['lineedit'])
        self.pushButton.setStyleSheet(stili['pushbutton'])
        self.line_edits = [self.lineEdit, self.lineEdit_2, self.lineEdit_3]
        for line_edit in self.line_edits:
            line_edit.textChanged.connect(self.check_input)
        self.comboBox.currentIndexChanged.connect(self.check_combobox_values)
        self.comboBox_2.currentIndexChanged.connect(self.check_combobox_values)
        QtCore.QMetaObject.connectSlotsByName(AddRoutes)
    def check_input(self):
        sender = self.addrout.sender()
        if sender.text() == "0":
            QMessageBox.warning(self.addrout, "Предупреждение", "Запрещено добавлять число, начинающиеся с 0")
            sender.clear()
    def add_routes(self):
        routes_number = self.lineEdit.text()
        from_where_type = self.comboBox.currentText()
        where_count = self.comboBox_2.currentText()
        train_number =self.lineEdit_3.text()
        dep_time = self.dateTimeEdit.dateTime().toString("yyyy.MM.dd H:mm")
        arr_time = self.dateTimeEdit_2.dateTime().toString("yyyy.MM.dd H:mm")
        price_number =self.lineEdit_2.text()
        if dep_time > arr_time:
            QMessageBox.warning(self.addrout, "Предупреждение", "Дата отправления не может быть позже даты прибытия.")
            return
        if self.is_duplicate(routes_number):
            QMessageBox.warning(self.addrout, "Предупреждение", "Данный номер маршрута уже существует.")
            return
        sql = "INSERT INTO routes (num_rout, from_where, where_rout, id_train, dep_time, arr_time, price, is_hidden) VALUES (%s, %s, %s,%s, %s, %s,%s, %s )"
        values = (routes_number, from_where_type, where_count, train_number, dep_time, arr_time,price_number, False)
        try:
            self.cursor.execute(sql, values)
            self.config.commit()
            QMessageBox.information(self.addrout, "Результат", "Данные успешно добавлены в базу данных")
            self.lineEdit.clear()
            self.lineEdit_2.clear()
            self.lineEdit_3.clear()
            
        except mysql.connector.Error as err:
            if err.errno == 1062:
                QMessageBox.warning(self.addrout, "Предупреждение", "Данный номер поезда уже приклеплен к маршруту. Только один поезд может ездить по одному маршруту")
            elif err.errno == 1452:
                QMessageBox.warning(self.addrout, "Предупреждение", 'Вы не можете добавить маршрут, потому что такого поезда не существует. Вы можете его добавить в "Поезда"')
            elif err.errno == 1366:
                QMessageBox.warning(self.addrout, "Предупреждение", "Вы заполнили не все поля.")
            else:
                print(f"Ошибка: {err}")
    def check_combobox_values(self):
        value1 = self.comboBox.currentText()
        value2 = self.comboBox_2.currentText()

        if value1 == value2:
            QMessageBox.warning(self.addrout, "Предупреждение", "Точки маршрута не могут совподать")
            # Сбросить текущее значение в одном из comboBox
            sender = self.addrout.sender()
            sender.setCurrentIndex(-1)
 
    def is_duplicate(self, routes_number):
        sql = "SELECT COUNT(*) FROM routes WHERE num_rout = %s"
        self.cursor.execute(sql, (routes_number,))
        result = self.cursor.fetchone()
        return result[0] > 0
    def retranslateUi(self, AddRoutes):
        _translate = QtCore.QCoreApplication.translate
        AddRoutes.setWindowTitle(_translate("AddRoutes", "Добавление маршрута"))
        self.label.setText(_translate("AddRoutes", "Добавление маршрута"))
        self.label_2.setText(_translate("AddRoutes", "Номер маршрута"))
        self.label_3.setText(_translate("AddRoutes", "Откуда"))
        self.label_4.setText(_translate("AddRoutes", "Куда"))
        self.label_5.setText(_translate("AddRoutes", "Номер поезда"))
        self.label_6.setText(_translate("AddRoutes", "Дата отправления"))
        self.label_7.setText(_translate("AddRoutes", "Дата прибытия"))
        self.dateTimeEdit.setDisplayFormat(_translate("AddRoutes", "yyyy.MM.dd H:mm"))
        self.dateTimeEdit_2.setDisplayFormat(_translate("AddRoutes", "yyyy.MM.dd H:mm"))
        self.label_8.setText(_translate("AddRoutes", "Цена билета"))
        self.pushButton.setText(_translate("AddRoutes", "Добавить маршрут"))

class Ui_Routes(object):
    def openMainWindow(self):
        self.routform.close()
        MainWindow.show()
    def openAddRoutes(self):
        self.addrout = QtWidgets.QWidget()
        self.ui = Ui_AddRoutes()
        self.ui.setupUi(self.addrout)
        self.addrout.setWindowModality(QtCore.Qt.ApplicationModal)
        self.addrout.show()
    def openEditRoutes(self):
        selected_row = self.tableWidget.currentRow()
        if selected_row >= 0:
            rout_number = self.tableWidget.item(selected_row, 0).text()
            from_where = self.tableWidget.item(selected_row, 1).text()
            where = self.tableWidget.item(selected_row, 2).text()
            id_train = self.tableWidget.item(selected_row, 3).text()
            dep_time = self.tableWidget.item(selected_row, 4).text()
            arr_time = self.tableWidget.item(selected_row, 5).text()
            price = self.tableWidget.item(selected_row, 6).text()
            self.editroutes = QtWidgets.QWidget()
            self.ui = Edit_Routes(rout_number, from_where, where, id_train, dep_time, arr_time, price)
            self.ui.setupUi(self.editroutes)
            self.editroutes.setWindowModality(QtCore.Qt.ApplicationModal)
            self.editroutes.show()
        else:
            QMessageBox.warning(self.routform, "Предупреждение", "Выберите запись для редактирования.")
    def setupUi(self, Routes):
        Routes.setObjectName("Routes")
        Routes.resize(1366, 768)
        palette = QPalette()
        image = QImage(image_path)
        scaled_image = image.scaled(Routes.size())
        palette.setBrush(QPalette.Window, QBrush(scaled_image))
        Routes.setPalette(palette)
        self.pushButton_3 = QtWidgets.QPushButton(Routes)
        self.pushButton_3.setGeometry(QtCore.QRect(670, 590, 201, 71))
        font = QtGui.QFont()
        self.routform = Routes
        self.editroutes= Routes
        font.setPointSize(12)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.update_add_train)
        self.pushButton_2 = QtWidgets.QPushButton(Routes)
        self.pushButton_2.setGeometry(QtCore.QRect(440, 470, 181, 71))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.openEditRoutes)
        self.tableWidget = QTableWidget(Routes)
        self.tableWidget.setGeometry(QtCore.QRect(150, 120, 1105, 281))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setHorizontalHeaderLabels(["Номер маршрута", "Откуда", "Куда", "Номер поезда", "Дата отправления", "Дата прибытия", "Цена билета"])
        self.tableWidget.setColumnWidth(0, 150)
        self.tableWidget.setColumnWidth(1, 150)
        self.tableWidget.setColumnWidth(2, 150)
        self.tableWidget.setColumnWidth(3, 150)
        self.tableWidget.setColumnWidth(4, 160)
        self.tableWidget.setColumnWidth(5, 160)
        self.tableWidget.setColumnWidth(6, 150)
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.pushButton_6 = QtWidgets.QPushButton(Routes)
        self.pushButton_6.setGeometry(QtCore.QRect(670, 470, 201, 71))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_6.clicked.connect(self.openSearchDialogRoutes)
        self.pushButton_4 = QtWidgets.QPushButton(Routes)
        self.pushButton_4.setGeometry(QtCore.QRect(920, 470, 181, 71))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.clicked.connect(self.delete_selected_routes)
        self.pushButton = QtWidgets.QPushButton(Routes)
        self.pushButton.setGeometry(QtCore.QRect(210, 470, 203, 71))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.openAddRoutes)
        self.pushButton_5 = QtWidgets.QPushButton(Routes)
        self.pushButton_5.setGeometry(QtCore.QRect(440, 590, 191, 71))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_5.clicked.connect(self.openMainWindow)
        self.label = QtWidgets.QLabel(Routes)
        self.label.setGeometry(QtCore.QRect(550, 20, 210, 71))
        font = QtGui.QFont()
        font.setPointSize(28)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.retranslateUi(Routes)
        QtCore.QMetaObject.connectSlotsByName(Routes)
        self.display_data_routes()
        self.pushButton.setStyleSheet(stili["pushbutton"])
        self.pushButton_2.setStyleSheet(stili["pushbutton"])
        self.pushButton_3.setStyleSheet(stili["pushbutton"])
        self.pushButton_4.setStyleSheet(stili["pushbutton"])
        self.pushButton_5.setStyleSheet(stili["pushbutton"])
        self.pushButton_6.setStyleSheet(stili["pushbutton"])
        self.tableWidget.setStyleSheet(stili["table_style"])
    def update_add_train(self):
        self.routform.close()
        self.routform = QtWidgets.QWidget()
        self.ui = Ui_Routes()
        self.ui.setupUi(self.routform)
        self.routform.showFullScreen()
        QMessageBox.information(self.routform, "Обновление", "База данных успешна обновлена")
    def delete_selected_routes(self):
        selected_row = self.tableWidget.currentRow()
        if selected_row >= 0:
            reply = QMessageBox.question(
                self.routform,
                'Подтверждение удаления',
                'Вы уверены, что хотите удалить этот маршрут',
                QMessageBox.Yes | QMessageBox.No,
                QMessageBox.No
            )
            if reply == QMessageBox.Yes:
                routes_number = self.tableWidget.item(selected_row, 0).text()
                self.delete_routes_from_database(routes_number)
                self.display_data_routes()
    def delete_routes_from_database(self, routes_number):
        config = mysql.connector.connect(**connectconfig)
        cursor = config.cursor()
        query = f"DELETE FROM routes WHERE num_rout = {routes_number}"
        cursor.execute(query)
        config.commit()
        cursor.close()
        config.close()
    def openSearchDialogRoutes(self):
        search_dialog = QDialog()
        search_dialog.setWindowTitle("Поиск маршрута")

        # Создание элементов управления для окна поиска
        line_edit = QtWidgets.QLineEdit(search_dialog)
        line_edit.setGeometry(QtCore.QRect(30, 30, 200, 30))
        label = QtWidgets.QLabel(search_dialog)
        label.setGeometry(QtCore.QRect(30, 70, 290, 20))
        label.setText("Если выделили столбец, то поиск осуществляется")
        label_2 = QtWidgets.QLabel(search_dialog)
        label_2.setGeometry(QtCore.QRect(30, 90, 290, 20))
        label_2.setText("по данному столбцу, если нет, то по всем столбцам")
        search_button = QtWidgets.QPushButton(search_dialog)
        search_button.setGeometry(QtCore.QRect(240, 30, 80, 30))
        search_button.setText("Найти")
        search_button.clicked.connect(lambda: self.search_routes(line_edit.text(), search_dialog))

        # Отобразить окно поиска
        search_dialog.exec_()
    def search_routes(self, keyword, search_dialog):
        config = mysql.connector.connect(**connectconfig)
        cursor = config.cursor()

        selected_column_index = self.tableWidget.currentColumn()
        column_mapping = {
            0: 'num_rout',
            1: 'from_where',
            2: 'where_rout',
            3: 'id_train',
            4: 'dep_time',
            5: 'arr_time',
            6: 'price'
        }

        if selected_column_index is None or selected_column_index not in column_mapping:
            columns_to_search = ', '.join(column_mapping.values())
            query = f"SELECT * FROM routes WHERE CONCAT({columns_to_search}) LIKE '%{keyword}%'"
        else:
            selected_column_name = column_mapping[selected_column_index]
            query = f"SELECT * FROM routes WHERE {selected_column_name} LIKE '%{keyword}%'"

        cursor.execute(query)
        result = cursor.fetchall()

        self.tableWidget.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.tableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                item = QTableWidgetItem(str(data))
                self.tableWidget.setItem(row_number, column_number, item)

        search_dialog.accept()
    
    def retranslateUi(self, Routes):
        _translate = QtCore.QCoreApplication.translate
        Routes.setWindowTitle(_translate("AddRoutes", "Маршруты"))
        self.pushButton_3.setText(_translate("AddRoutes", "Обновить таблицу"))
        self.pushButton_2.setText(_translate("AddRoutes", "Редактировать"))
        self.pushButton_6.setText(_translate("AddRoutes", "Поиск маршрута"))
        self.pushButton_4.setText(_translate("AddRoutes", "Удалить запись"))
        self.pushButton.setText(_translate("AddRoutes", "Добавить маршрут"))
        self.pushButton_5.setText(_translate("AddRoutes", "На главную "))
        self.label.setText(_translate("AddRoutes", "Маршруты"))
    def display_data_routes(self):
        config = mysql.connector.connect(**connectconfig)
        cursor = config.cursor()
        query = "SELECT * FROM routes"
        cursor.execute(query)
        result = cursor.fetchall()
        self.tableWidget.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.tableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                item = QTableWidgetItem(str(data))
                self.tableWidget.setItem(row_number, column_number, item)

class Ui_Passengers(object):
    def openEditRoutes(self):
        selected_row = self.tableWidget.currentRow()
        if selected_row >= 0:
            trip_id = self.tableWidget.item(selected_row, 0).text()
            passport = self.tableWidget.item(selected_row, 1).text()
            surname = self.tableWidget.item(selected_row, 2).text()
            name = self.tableWidget.item(selected_row, 3).text()
            num_routes = self.tableWidget.item(selected_row, 4).text()
            self.editpass = QtWidgets.QWidget()
            self.ui = Ui_EditPass(trip_id, passport, surname, name, num_routes)
            self.editpass.setWindowModality(QtCore.Qt.ApplicationModal)
            self.ui.setupUi(self.editpass)
            self.editpass.show()
    def openTicket(self):
        selected_row = self.tableWidget.currentRow()
        if selected_row >= 0:
            surname = self.tableWidget.item(selected_row, 2).text()
            name = self.tableWidget.item(selected_row, 3).text()
            from_where = self.tableWidget.item(selected_row, 5).text()
            where_rout = self.tableWidget.item(selected_row, 6).text()
            price = self.tableWidget.item(selected_row, 9).text()
            random_number = str(random.randint(1000, 9999))
            pdf_filename = f'D:\\rzd2\\Ticket\\{random_number}.pdf'
            image_path = "D:\\rzd2\\assets\\ticket.jpg"
            self.createTicketPDF(pdf_filename, surname, name, from_where, where_rout, price, random_number,image_path)
            # Отображение сообщения
            message_box = QMessageBox()
            message_box.setWindowTitle("Билет сохранен")
            message_box.setText(f"Билет сохранен в файле:\n{pdf_filename}")
            message_box.exec_()
            self.tik = QtWidgets.QWidget()
            self.ui = Ui_Ticket()
            self.ui.setupUi(self.tik, surname, name, from_where, where_rout, price, random_number)
            self.tik.show()
    def createTicketPDF(self, filename, surname, name, from_where, where_rout, price, random_number,image_path):
        pdfmetrics.registerFont(TTFont('Arial', 'D:\\rzd\\assets\\arialmt.ttf'))
        c = canvas.Canvas(filename)
        image_width = 422  
        image_height = 529 
        c.drawImage(image_path, 100, 500, width=image_width, height=image_height)
        c.setFont("Arial", 14)
        c.drawString(250, 800, f"Билет №: {random_number}")
        c.drawString(250, 750, f"Ф амилия: {surname}")
        c.drawString(250, 720, f"Имя: {name}")
        c.drawString(250, 690, f"Откуда: {from_where}")
        c.drawString(250, 660, f"Куда: {where_rout}")
        c.drawString(250, 630, f"Цена билета: {price} руб.")
        c.save()
    def openWindowTrip(self):
        selected_row = self.tableWidget.currentRow()
        if selected_row >= 0:
            passport = self.tableWidget.item(selected_row, 1).text()
            self.passe.close()
            self.tripse = QtWidgets.QWidget()
            self.ui = Ui_Trips()
            self.ui.setupUi(self.tripse, passport=passport)
            self.tripse.showFullScreen()
    def openMainWindow(self):
        self.passe.close()
        MainWindow.show()
    def setupUi(self, Passengers):
        Passengers.setObjectName("Passengers")
        Passengers.resize(1366, 768)
        palette = QPalette()
        image = QImage(image_path)
        scaled_image = image.scaled(Passengers.size())
        palette.setBrush(QPalette.Window, QBrush(scaled_image))
        Passengers.setPalette(palette)
        self.passe = Passengers
        self.editpass= Passengers
        self.pushButton_3 = QtWidgets.QPushButton(Passengers)
        self.pushButton_3.setGeometry(QtCore.QRect(670, 480, 161, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.openSearchDialogPassenger)
        self.pushButton_2 = QtWidgets.QPushButton(Passengers)
        self.pushButton_2.setGeometry(QtCore.QRect(450, 480, 171, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self. delete_selected_passengers)
        self.tableWidget = QTableWidget(Passengers)
        self.tableWidget.setGeometry(QtCore.QRect(40, 120, 1270, 290))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(10)
        self.tableWidget.setHorizontalHeaderLabels([ "Паспорт", "Фамилия", "Имя", "Номер маршрута"])
        self.tableWidget.setColumnWidth(0, 120)
        self.tableWidget.setColumnWidth(1, 120)
        self.tableWidget.setColumnWidth(2, 120)
        self.tableWidget.setColumnWidth(3, 110)
        self.tableWidget.setColumnWidth(4, 140)
        self.tableWidget.setColumnWidth(5, 120)
        self.tableWidget.setColumnWidth(6, 120)
        self.tableWidget.setColumnWidth(7, 150)
        self.tableWidget.setColumnWidth(8, 120)
        self.tableWidget.setColumnWidth(9, 120)
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.pushButton_6 = QtWidgets.QPushButton(Passengers)
        self.pushButton_6.setGeometry(QtCore.QRect(890, 480, 161, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_6.clicked.connect(self.update_add_passengers)
        self.pushButton_4 = QtWidgets.QPushButton(Passengers)
        self.pushButton_4.setGeometry(QtCore.QRect(650, 580, 210, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.clicked.connect(self.openWindowTrip)
        self.pushButton = QtWidgets.QPushButton(Passengers)
        self.pushButton.setGeometry(QtCore.QRect(230, 480, 185, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.openEditRoutes)
        self.pushButton_5 = QtWidgets.QPushButton(Passengers)
        self.pushButton_5.setGeometry(QtCore.QRect(230, 570, 161, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_5.clicked.connect(self.openMainWindow)
        self.label = QtWidgets.QLabel(Passengers)
        self.label.setGeometry(QtCore.QRect(510, 20, 231, 41))
        font = QtGui.QFont()
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton_7 = QtWidgets.QPushButton(Passengers)
        self.pushButton_7.setGeometry(QtCore.QRect(890, 580, 181, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_7.clicked.connect(self.openTicket)

        self.retranslateUi(Passengers)
        QtCore.QMetaObject.connectSlotsByName(Passengers)
        self.display_data()
        self.pushButton.setStyleSheet(stili["pushbutton"])
        self.pushButton_2.setStyleSheet(stili["pushbutton"])
        self.pushButton_3.setStyleSheet(stili["pushbutton"])
        self.pushButton_4.setStyleSheet(stili["pushbutton"])
        self.pushButton_5.setStyleSheet(stili["pushbutton"])
        self.pushButton_6.setStyleSheet(stili["pushbutton"])
        self.pushButton_7.setStyleSheet(stili["pushbutton"])
        self.tableWidget.setStyleSheet(stili["table_style"])
    def delete_selected_passengers(self):
        selected_row = self.tableWidget.currentRow()
        if selected_row >= 0:
            reply = QMessageBox.question(
                self.passe,
                'Подтверждение удаления',
                'Вы уверены, что хотите удалить данного пассажира?',
                QMessageBox.Yes | QMessageBox.No,
                QMessageBox.No
            )
            if reply == QMessageBox.Yes:
                pass_number = self.tableWidget.item(selected_row, 0).text()
                route_number = self.tableWidget.item(selected_row, 4).text()
                self.delete_passengers_from_database(pass_number, route_number)
                self.display_data()
    def delete_passengers_from_database(self, pass_number,route_number):
        config = mysql.connector.connect(**connectconfig)
        cursor = config.cursor()
        query = f"DELETE FROM passengers WHERE trip_id = {pass_number}"
        cursor.execute(query)
        query_routes = f"UPDATE routes SET is_hidden = 0 WHERE num_rout = {route_number}"
        cursor.execute(query_routes)
        config.commit()
        cursor.close()
        config.close()

    def display_data(self):
        config = mysql.connector.connect(**connectconfig)
        cursor = config.cursor()
        query = """
        SELECT  passengers.trip_id, passengers.passport,  passengers.surname, passengers.name, passengers.num_routes,
        routes.from_where, routes.where_rout,
        routes.dep_time, routes.arr_time, routes.price
        FROM passengers
        INNER JOIN routes ON passengers.num_routes = routes.num_rout
        """
        cursor.execute(query)
        result = cursor.fetchall()

        # Update the column count and header labels
        self.tableWidget.setColumnCount(10)
        self.tableWidget.setHorizontalHeaderLabels([
            "Номер поездки","Паспорт", "Фамилия", "Имя", "Номер маршрута",
            "Откуда", "Куда", 
            "Дата отправления", "Дата прибытия", "Цена билета"
        ])

        self.tableWidget.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.tableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                item = QTableWidgetItem(str(data))
                self.tableWidget.setItem(row_number, column_number, item)
    def update_add_passengers(self):
        self.passe.close()
        self.passe = QtWidgets.QWidget()
        self.ui = Ui_Passengers()
        self.ui.setupUi(self.passe)
        self.passe.showFullScreen()
        QMessageBox.information(self.passe, "Обновление", "База данных успешна обновлена")
    def openSearchDialogPassenger(self):
        search_dialog = QDialog()
        search_dialog.setWindowTitle("Поиск пассажира")

        label = QtWidgets.QLabel(search_dialog)
        label.setGeometry(QtCore.QRect(30, 10, 460, 20))
        label.setText("Пассажир найдется по параметрам: имя, фамилия, паспортные данные, номер маршрута")
        # Создание элементов управления для окна поиска
        line_edit = QtWidgets.QLineEdit(search_dialog)
        line_edit.setGeometry(QtCore.QRect(30, 30, 200, 30))

        search_button = QtWidgets.QPushButton(search_dialog)
        search_button.setGeometry(QtCore.QRect(240, 30, 80, 30))
        search_button.setText("Найти")
        search_button.clicked.connect(lambda: self.search_passeners(line_edit.text(), search_dialog))

        # Отобразить окно поиска
        search_dialog.exec_()
    def search_passeners(self, keyword, search_dialog):
        config = mysql.connector.connect(**connectconfig)
        cursor = config.cursor()
        query = f"""
    SELECT passengers.passport, passengers.trip_id, passengers.surname, passengers.name, passengers.num_routes,
           routes.from_where, routes.where_rout,
           routes.dep_time, routes.arr_time, routes.price
    FROM passengers
    INNER JOIN routes ON passengers.num_routes = routes.num_rout
    WHERE passengers.passport LIKE '%{keyword}%' OR 
          passengers.trip_id LIKE '%{keyword}%' OR 
          passengers.surname LIKE '%{keyword}%' OR 
          passengers.name LIKE '%{keyword}%' OR 
          passengers.num_routes LIKE '%{keyword}%' OR
          routes.from_where LIKE '%{keyword}%' OR 
          routes.where_rout LIKE '%{keyword}%' OR 
          routes.dep_time LIKE '%{keyword}%' OR 
          routes.arr_time LIKE '%{keyword}%' OR 
          routes.price LIKE '%{keyword}%'
    """
        cursor.execute(query)
        result = cursor.fetchall()
        self.tableWidget.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.tableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                item = QTableWidgetItem(str(data))
                self.tableWidget.setItem(row_number, column_number, item)
        search_dialog.accept()
    def retranslateUi(self, Passengers):
        _translate = QtCore.QCoreApplication.translate
        Passengers.setWindowTitle(_translate("Passengers", "Пассажиры"))
        self.pushButton_3.setText(_translate("Passengers", "Поиск"))
        self.pushButton_2.setText(_translate("Passengers", "Удалить запись"))
        self.pushButton_6.setText(_translate("Passengers", "Обновить "))
        self.pushButton_4.setText(_translate("Passengers", "Посмотреть поезки"))
        self.pushButton.setText(_translate("Passengers", "Изменить запись"))
        self.pushButton_5.setText(_translate("Passengers", "На главную "))
        self.label.setText(_translate("Passengers", "Пассажиры"))
        self.pushButton_7.setText(_translate("Passengers", "Печать билета"))
class Ui_Trips(object):
    def openWindowPassengers(self):
        self.passe = QtWidgets.QWidget()
        self.ui = Ui_Passengers()
        self.ui.setupUi(self.passe)
        self.passe.showFullScreen()
        self.tripse.close()
    def openMainWindow(self):
        self.tripse.close()
        MainWindow.show()
    def setupUi(self, Trips, passport):
        Trips.setObjectName("Trips")
        Trips.resize(1366, 768)
        palette = QPalette()
        image = QImage(image_path)
        scaled_image = image.scaled(Trips.size())
        palette.setBrush(QPalette.Window, QBrush(scaled_image))
        Trips.setPalette(palette)
        self.tripse = Trips
        self.label = QtWidgets.QLabel(Trips)
        self.label.setGeometry(QtCore.QRect(550, 10, 330, 51))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.tableWidget = QTableWidget(Trips)
        self.tableWidget.setGeometry(240, 120, 920, 300)
        self.tableWidget.setColumnCount(9)
        self.tableWidget.setHorizontalHeaderLabels(["Паспорт", "Фамилия", "Имя", "Откуда", "Куда", "Время отправления", "Время прибытия", "Цена"])
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.pushButton = QtWidgets.QPushButton(Trips)
        self.pushButton.setGeometry(QtCore.QRect(420, 590, 171, 71))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Trips)
        self.pushButton_2.setGeometry(QtCore.QRect(1010, 590, 171, 71))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.openMainWindow)
        self.pushButton.clicked.connect(self.openWindowPassengers)
        self.display_trips(passport=passport)
        self.retranslateUi(Trips)
        self.pushButton.setStyleSheet(stili["pushbutton"])
        self.pushButton_2.setStyleSheet(stili["pushbutton"])
        self.tableWidget.setStyleSheet(stili["table_style"])
        QtCore.QMetaObject.connectSlotsByName(Trips)
    def display_trips(self, passport):
        config = mysql.connector.connect(**connectconfig)
        cursor = config.cursor()

        query = """
        SELECT passengers.passport, passengers.trip_id, passengers.surname, passengers.name,
            routes.from_where, routes.where_rout,
            routes.dep_time, routes.arr_time, routes.price
        FROM passengers
        INNER JOIN routes ON passengers.num_routes = routes.num_rout
        WHERE passengers.passport = %s
        """
        cursor.execute(query, (passport,))
        result = cursor.fetchall()
        self.tableWidget.setColumnCount(9)
        self.tableWidget.setHorizontalHeaderLabels([
            "Паспорт", "Номер поездки", "Фамилия", "Имя",
            "Откуда", "Куда", "Дата отправления", "Дата прибытия", "Цена билета"
        ])

        self.tableWidget.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.tableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                item = QTableWidgetItem(str(data))
                self.tableWidget.setItem(row_number, column_number, item)
    def retranslateUi(self, Trips):
        _translate = QtCore.QCoreApplication.translate
        Trips.setWindowTitle(_translate("Trips", "Поездки"))
        self.label.setText(_translate("Trip", "Поездки пассажира"))
        self.pushButton_2.setText(_translate("Trips", "На главную"))
        self.pushButton.setText(_translate("Trips", "К пассажирам"))

class Ui_Ticket(object):
    def setupUi(self, Ticket, surname, name, from_where, where_rout, price, random_number):
        Ticket.setObjectName("Ticket")
        Ticket.resize(422, 529)
        palette = QPalette()
        image = QImage(image_path3)
        scaled_image = image.scaled(Ticket.size())
        palette.setBrush(QPalette.Window, QBrush(scaled_image))
        Ticket.setPalette(palette)
        self.tik = Ticket
        self.label = QtWidgets.QLabel(Ticket)
        self.label.setGeometry(QtCore.QRect(90, 0, 121, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Ticket)
        self.label_2.setGeometry(QtCore.QRect(20, 60, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Ticket)
        self.label_3.setGeometry(QtCore.QRect(30, 120, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Ticket)
        self.label_4.setGeometry(QtCore.QRect(20, 180, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Ticket)
        self.label_5.setGeometry(QtCore.QRect(30, 240, 81, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Ticket)
        self.label_6.setGeometry(QtCore.QRect(20, 290, 131, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_number = QtWidgets.QLabel(Ticket)
        self.label_number.setGeometry(QtCore.QRect(220, 10, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_number.setFont(font)
        self.label_number.setText("")
        self.label_number.setObjectName("label_number")
        self.label_number.setText(random_number)
        self.label_surname = QtWidgets.QLabel(Ticket)
        self.label_surname.setGeometry(QtCore.QRect(130, 60, 200, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_surname.setFont(font)
        self.label_surname.setText("")
        self.label_surname.setObjectName("label_surname")
        self.label_surname.setText(surname)
        self.label_name = QtWidgets.QLabel(Ticket)
        self.label_name.setGeometry(QtCore.QRect(100, 120, 200, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_name.setFont(font)
        self.label_name.setText("")
        self.label_name.setObjectName("label_name")
        self.label_name.setText(name)
        self.label_from_where = QtWidgets.QLabel(Ticket)
        self.label_from_where.setGeometry(QtCore.QRect(110, 180, 300, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_from_where.setFont(font)
        self.label_from_where.setText("")
        self.label_from_where.setObjectName("label_from_where")
        self.label_from_where.setText(from_where)
        self.label_where = QtWidgets.QLabel(Ticket)
        self.label_where.setGeometry(QtCore.QRect(110, 240, 200, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_where.setFont(font)
        self.label_where.setText("")
        self.label_where.setObjectName("label_where")
        self.label_where.setText(where_rout)
        self.label_price = QtWidgets.QLabel(Ticket)
        self.label_price.setGeometry(QtCore.QRect(170, 300, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_price.setFont(font)
        self.label_price.setText("")
        self.label_price.setObjectName("label_price")
        self.label_price.setText(price)
        self.retranslateUi(Ticket)
        QtCore.QMetaObject.connectSlotsByName(Ticket)

    def retranslateUi(self, Ticket):
        _translate = QtCore.QCoreApplication.translate
        Ticket.setWindowTitle(_translate("Ticket", "Билет пассажира"))
        self.label.setText(_translate("Ticket", "Билет №"))
        self.label_2.setText(_translate("Ticket", "Фамилия:"))
        self.label_3.setText(_translate("Ticket", "Имя:"))
        self.label_4.setText(_translate("Ticket", "Откуда:"))
        self.label_5.setText(_translate("Ticket", "Куда:"))
        self.label_6.setText(_translate("Ticket", "Цена билета:"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())