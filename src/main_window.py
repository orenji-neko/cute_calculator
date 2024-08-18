"""
    Main Window of Calculator.
"""

from PyQt5.QtWidgets import QWidget, QGridLayout, QLineEdit
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QKeyEvent
import numexpr as ne

from button import Push_Button

class Main_Window(QWidget):
    """ 
        Main window class for calculator.
    """

    def __init__(self, parent = None):
        super(Main_Window, self).__init__(parent)

        self.setWindowTitle("Calculator")
        self.setFixedSize(320, 480)

        self.setStyleSheet(
            "QWidget {"
                "background-color: #2E2E2E;"
            "}"
        )

        self.__create_gui()
        self.equation:str = ""

        self.has_error:bool = False

    def __create_gui(self):
        numbers:list[str] = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        self.number_buttons:list[Push_Button] = []

        # number grid
        self.calculator_grid:QGridLayout = QGridLayout(self)
        self.calculator_grid.setSpacing(3)

        # number buttons
        column_length:int = 3
        for count, value in enumerate(numbers):
            self.number_buttons.append(Push_Button(value))

        self.calculator_grid.addWidget(self.number_buttons[7], 2, 0) # 7
        self.calculator_grid.addWidget(self.number_buttons[8], 2, 1) # 8
        self.calculator_grid.addWidget(self.number_buttons[9], 2, 2) # 9
        self.calculator_grid.addWidget(self.number_buttons[4], 3, 0) # 4
        self.calculator_grid.addWidget(self.number_buttons[5], 3, 1) # 5
        self.calculator_grid.addWidget(self.number_buttons[6], 3, 2) # 6
        self.calculator_grid.addWidget(self.number_buttons[1], 4, 0) # 1
        self.calculator_grid.addWidget(self.number_buttons[2], 4, 1) # 2
        self.calculator_grid.addWidget(self.number_buttons[3], 4, 2) # 3
        self.calculator_grid.addWidget(self.number_buttons[0], 5, 0) # 0

        # decimal point
        self.decimal_button = Push_Button(".")
        self.calculator_grid.addWidget(self.decimal_button, 5, 1)
        # percent
        self.percent_button = Push_Button("mod")
        self.percent_button.setToolTip("Modulo")
        self.calculator_grid.addWidget(self.percent_button, 5, 2)
        # clear
        self.clear_button = Push_Button("C")
        self.calculator_grid.addWidget(self.clear_button, 1, 0)
        # parenthesis
        self.open_parenthesis_button = Push_Button("(")
        self.close_parenthesis_button = Push_Button(")")
        self.calculator_grid.addWidget(self.open_parenthesis_button, 1, 1)
        self.calculator_grid.addWidget(self.close_parenthesis_button, 1, 2)

        # operations
        self.divide_button = Push_Button("/")
        self.multiply_button = Push_Button("*")
        self.minus_button = Push_Button("-")
        self.plus_button = Push_Button("+")
        self.calculator_grid.addWidget(self.divide_button, 1, 3)
        self.calculator_grid.addWidget(self.multiply_button, 2, 3)
        self.calculator_grid.addWidget(self.minus_button, 3, 3)
        self.calculator_grid.addWidget(self.plus_button, 4, 3)

        # equals
        self.equals_button = Push_Button("=", color = "#FFFFFF", bg_color = "#723680", hover_bg = "#8E5E99")
        self.calculator_grid.addWidget(self.equals_button, 5, 3)

        # textbox
        self.equation_box = QLineEdit()
        self.equation_box.setStyleSheet(
            "QLineEdit {"
                "border: none;"
                "color: #FFFFFF;"
            "}"
        )
        f:QFont = QFont()
        f.setPointSize(20)
        self.equation_box.setFont(f)
        self.equation_box.setReadOnly(True)
        self.equation_box.setMinimumHeight(50)
        self.calculator_grid.addWidget(self.equation_box, 0, 0, 1, 4)

        # adding connectors

        # numbers
        self.number_buttons[0].clicked.connect(lambda: self.__append_to_equation("0"))
        self.number_buttons[1].clicked.connect(lambda: self.__append_to_equation("1"))
        self.number_buttons[2].clicked.connect(lambda: self.__append_to_equation("2"))
        self.number_buttons[3].clicked.connect(lambda: self.__append_to_equation("3"))
        self.number_buttons[4].clicked.connect(lambda: self.__append_to_equation("4"))
        self.number_buttons[5].clicked.connect(lambda: self.__append_to_equation("5"))
        self.number_buttons[6].clicked.connect(lambda: self.__append_to_equation("6"))
        self.number_buttons[7].clicked.connect(lambda: self.__append_to_equation("7"))
        self.number_buttons[8].clicked.connect(lambda: self.__append_to_equation("8"))
        self.number_buttons[9].clicked.connect(lambda: self.__append_to_equation("9"))

        # operations
        self.divide_button.clicked.connect(lambda: self.__append_to_equation("/"))
        self.multiply_button.clicked.connect(lambda: self.__append_to_equation("*"))
        self.minus_button.clicked.connect(lambda: self.__append_to_equation("-"))
        self.plus_button.clicked.connect(lambda: self.__append_to_equation("+"))

        # symbols
        self.percent_button.clicked.connect(lambda: self.__append_to_equation("%"))
        self.decimal_button.clicked.connect(lambda: self.__append_to_equation("."))

        # parenthesis
        self.open_parenthesis_button.clicked.connect(lambda: self.__append_to_equation("("))
        self.close_parenthesis_button.clicked.connect(lambda: self.__append_to_equation(")"))

        # clear
        self.clear_button.clicked.connect(lambda: self.__clear_equation())

        # equals
        self.equals_button.clicked.connect(lambda: self.__evaluate())

        # window layout
        self.setLayout(self.calculator_grid)

        #keyboard events

    def __append_to_equation(self, text:str):
        if self.has_error:
            self.__clear_equation()
            self.__set_equation_box_text(self.equation + text)
            self.has_error = False
        else:
            self.__set_equation_box_text(self.equation + text)

    def __evaluate(self):
        try:
            self.__set_equation_box_text(str(ne.evaluate(str(self.equation))))
        except:
            self.__set_equation_box_text("ERROR")
            self.has_error = True

    def __clear_equation(self):
        self.__set_equation_box_text("")

    def __set_equation_box_text(self, text:str):
        self.equation = text
        self.equation_box.setText(text)

    def keyPressEvent(self, event: QKeyEvent) -> None:
        if event.key() == Qt.Key_Escape and self.equation.find("69") >= 0: # type: ignore
            self.__set_equation_box_text("NICE!!!")

        super(Main_Window, self).keyPressEvent(event)