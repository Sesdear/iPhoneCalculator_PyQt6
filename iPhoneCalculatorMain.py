import sys
from PyQt6.QtWidgets import QApplication, QFrame
from PyQt6 import uic

class Calculator(QFrame):
    def __init__(self):
        super().__init__()
        self.ui = uic.loadUi("iPhone_Calculator.ui", self)
        self.show()

        self.ui.butEqu.clicked.connect(self.butEqu_click) #Ровно

        self.ui.butAdd.clicked.connect(self.butAdd_click)
        self.ui.butMin.clicked.connect(self.butMin_click)
        self.ui.butMulti.clicked.connect(self.butMulti_click)
        self.ui.butDiv.clicked.connect(self.butDiv_click)
        self.ui.butPro.clicked.connect(self.butPro_click)

        self.ui.butPM.clicked.connect(self.butPM_click)
        self.ui.butClear.clicked.connect(self.butClear_click)
        self.ui.butZap.clicked.connect(self.butZap_click)

        self.ui.but0.clicked.connect(self.but0_click)
        self.ui.but1.clicked.connect(self.but1_click)
        self.ui.but2.clicked.connect(self.but2_click)
        self.ui.but3.clicked.connect(self.but3_click)
        self.ui.but4.clicked.connect(self.but4_click)
        self.ui.but5.clicked.connect(self.but5_click)
        self.ui.but6.clicked.connect(self.but6_click)
        self.ui.but7.clicked.connect(self.but7_click)
        self.ui.but8.clicked.connect(self.but8_click)
        self.ui.but9.clicked.connect(self.but9_click)

        self.reset_input_on_next_number = False
        self.first_number = ""
        self.operator = ""

    def butAdd_click(self):
        self.reset_input_on_next_number = True
        self.first_number = self.ui.label.text()
        self.operator = "+"
        self.ui.label.setText("")

    def butMin_click(self):
        self.reset_input_on_next_number = True
        self.first_number = self.ui.label.text()
        self.operator = "-"
        self.ui.label.setText("")
    def butMulti_click(self):
        self.reset_input_on_next_number = True
        self.first_number = self.ui.label.text()
        self.operator = "*"
        self.ui.label.setText("")
    def butDiv_click(self):
        self.reset_input_on_next_number = True
        self.first_number = self.ui.label.text()
        self.operator = "/"
        self.ui.label.setText("")
    def butPro_click(self):
        self.reset_input_on_next_number = True
        self.first_number = self.ui.label.text()
        self.operator = "%"
        self.ui.label.setText("")

    def butEqu_click(self):
        try:
            second_number = self.ui.label.text()
            if self.operator:
                if self.operator == "+":
                    result = float(self.first_number) + float(second_number)
                elif self.operator == "-":
                    result = float(self.first_number) - float(second_number)
                elif self.operator == "*":
                    result = float(self.first_number) * float(second_number)
                elif self.operator == "/":
                    result = float(self.first_number) / float(second_number)
                elif self.operator == "%":
                    result = float(self.first_number) % float(second_number)
                else:
                    result = 0

                self.ui.label.setText(str(result))
                self.reset_input_on_next_number = True
                self.operator = ""
        except Exception:
            self.ui.label.setText("Error")
    def butZap_click(self):
        text = self.ui.label.text()
        self.ui.label.setText(text + ".")
    def butClear_click(self):
        self.ui.label.setText("")
        self.first_number = ""
        self.operator = ""

    def butPM_click(self):
        try:
            text = self.ui.label.text()
            result = eval(text)
            if isinstance(result, (int, float)):
                negated_result = result * -1
                self.ui.label.setText(str(negated_result))
            else:
                self.ui.label.setText("Invalid Input")
        except Exception:
            self.ui.label.setText("Error")

    def but1_click(self):
        text = self.ui.label.text()
        self.ui.label.setText(text + "1")
    def but2_click(self):
        text = self.ui.label.text()
        self.ui.label.setText(text + "2")
    def but3_click(self):
        text = self.ui.label.text()
        self.ui.label.setText(text + "3")
    def but4_click(self):
        text = self.ui.label.text()
        self.ui.label.setText(text + "4")
    def but5_click(self):
        text = self.ui.label.text()
        self.ui.label.setText(text + "5")
    def but6_click(self):
        text = self.ui.label.text()
        self.ui.label.setText(text + "6")
    def but7_click(self):
        text = self.ui.label.text()
        self.ui.label.setText(text + "7")
    def but8_click(self):
        text = self.ui.label.text()
        self.ui.label.setText(text + "8")
    def but9_click(self):
        text = self.ui.label.text()
        self.ui.label.setText(text + "9")
    def but0_click(self):
        text = self.ui.label.text()
        self.ui.label.setText(text + "0")







if __name__ == '__main__':
    app = QApplication(sys.argv)
    CalcWindow = Calculator()
    sys.exit(app.exec())