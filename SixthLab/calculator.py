import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QHBoxLayout, QVBoxLayout, QPushButton, QLabel

class Calculator(QWidget):
    def __init__(self):
        super(Calculator, self).__init__()
        self.count = 0
        #Оси выравнивания
        self.vbox = QVBoxLayout(self)
        self.hbox_label = QHBoxLayout()
        self.hbox_input = QHBoxLayout()
        self.hbox_irst = QHBoxLayout()
        self.hbox_second = QHBoxLayout()
        self.hbox_operations = QHBoxLayout()
        self.hbox_result = QHBoxLayout()

        #Оси выравнивания (горизонтальные)
        self.vbox.addLayout(self.hbox_label)
        self.vbox.addLayout(self.hbox_input)
        self.vbox.addLayout(self.hbox_irst)
        self.vbox.addLayout(self.hbox_second)
        self.vbox.addLayout(self.hbox_operations)
        self.vbox.addLayout(self.hbox_result)

        #Расположение виджетов
        self.lab = QLabel(self)
        self.hbox_label.addWidget(self.lab)

        self.input = QLineEdit(self)
        self.hbox_input.addWidget(self.input)

        self.b_1 = QPushButton("1", self)
        self.hbox_irst.addWidget(self.b_1)

        self.b_2 = QPushButton("2", self)
        self.hbox_irst.addWidget(self.b_2)

        self.b_3 = QPushButton("3", self)
        self.hbox_irst.addWidget(self.b_3)

        self.b_4 = QPushButton("4", self)
        self.hbox_irst.addWidget(self.b_4)

        self.b_5 = QPushButton("5", self)
        self.hbox_irst.addWidget(self.b_5)

        self.b_6 = QPushButton("6", self)
        self.hbox_second.addWidget(self.b_6)

        self.b_7 = QPushButton("7", self)
        self.hbox_second.addWidget(self.b_7)

        self.b_8 = QPushButton("8", self)
        self.hbox_second.addWidget(self.b_8)

        self.b_9 = QPushButton("9", self)
        self.hbox_second.addWidget(self.b_9)

        self.b_10 = QPushButton("0", self)
        self.hbox_second.addWidget(self.b_10)

        self.b_11 = QPushButton(".", self)
        self.hbox_second.addWidget(self.b_11)

        self.b_clean = QPushButton('C', self)
        self.hbox_operations.addWidget(self.b_clean)

        self.b_plus = QPushButton("+", self)
        self.hbox_operations.addWidget(self.b_plus)

        self.b_minus = QPushButton("-", self)
        self.hbox_operations.addWidget(self.b_minus)

        self.b_multiplication = QPushButton("*", self)
        self.hbox_operations.addWidget(self.b_multiplication)

        self.b_division = QPushButton("/", self)
        self.hbox_operations.addWidget(self.b_division)

        self.b_result = QPushButton("=", self)
        self.hbox_result.addWidget(self.b_result)

        #Создаем события, отвечающие за реакции на нажатия по кнопкам
        self.b_plus.clicked.connect(lambda: self._operation("+"))
        self.b_minus.clicked.connect(lambda: self._operation("-"))
        self.b_multiplication.clicked.connect(lambda: self._operation("*"))
        self.b_division.clicked.connect(lambda: self._operation("/"))
        self.b_result.clicked.connect(self._result)
        self.b_clean.clicked.connect(self._clean)

        self.b_1.clicked.connect(lambda: self._button("1"))
        self.b_2.clicked.connect(lambda: self._button("2"))
        self.b_3.clicked.connect(lambda: self._button("3"))
        self.b_4.clicked.connect(lambda: self._button("4"))
        self.b_5.clicked.connect(lambda: self._button("5"))
        self.b_6.clicked.connect(lambda: self._button("6"))
        self.b_7.clicked.connect(lambda: self._button("7"))
        self.b_8.clicked.connect(lambda: self._button("8"))
        self.b_9.clicked.connect(lambda: self._button("9"))
        self.b_10.clicked.connect(lambda: self._button("0"))
        self.b_11.clicked.connect(lambda: self._button("."))

    #Создаем методы для обработки нажатия
    def _button(self, param):
        line = self.input.text()
        self.input.setText(line + param)
        self.lab.setText(self.lab.text() + param)

    #Исключение, если первое число не введено, а сразу нажат знак операции. Так же, если введено больше двух чисел - выбрасывается исключение
    def _operation(self, op):
        try:
            self.num_1 = float(self.input.text())
            self.op = op
            self.input.setText("")
            self.lab.setText(self.lab.text() + op)
            self.count += 1
            if self.count >= 2:
                self.lab.setText("Введите только два числа")
        except:
            self.lab.setText("Введите первое число")

    #Очистка полей
    def _clean(self):
        self.count=0
        self.lab.setText("")
        self.num_1 = ""
        self.num_1 = ""
        self.input.setText("")

    #Исключение, если второе число не введено, деление на ноль
    def _result(self):
        try:
            self.num_2 = float(self.input.text())
            self.lab.setText(self.lab.text() + "=")
            if self.op == "+":
                self.input.setText(str(self.num_1 + self.num_2))
                self.lab.setText(self.lab.text() + str(self.num_1 + self.num_2))
            if self.op == "-":
                self.input.setText(str((self.num_1 - self.num_2)))
                self.lab.setText(self.lab.text() + str(self.num_1 - self.num_2))
            if self.op == "*":
                self.input.setText(str((self.num_1 * self.num_2)))
                self.lab.setText(self.lab.text() + str(self.num_1 * self.num_2))
            if self.op == "/":
                if self.num_2 == 0:
                    self.lab.setText("Ошибка: деление на ноль")
                else:
                    self.input.setText(str((self.num_1 / self.num_2)))
                    self.lab.setText(self.lab.text() + str(self.num_1 / self.num_2))
        except:
            self.lab.setText("Введите два числа")

#Запуск приложения
app = QApplication(sys.argv)
win = Calculator()
win.show()
sys.exit(app.exec_())