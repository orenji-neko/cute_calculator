"""
    Default Button for Calculator
"""

from PyQt5.QtWidgets import QPushButton

class Push_Button(QPushButton):
    """
        Standard Push Button for Calculator
    """

    def __init__(self, text:str = "", parent = None, color:str = "#EAEAEA", bg_color:str = "#434343", hover_bg:str = "#6D6D6D"):
        super(Push_Button, self).__init__(parent)

        self.setText(text)
        self.setMinimumSize(50, 50)

        self.setStyleSheet(
            "QPushButton {"
                "background: none;"
                f"background-color: {bg_color};"
                f"color: {color};"
                "border: none;"
                "border-radius: 5;"
            "}"
            "QPushButton::hover {"
                f"background-color: {hover_bg}"
            "}"
        )