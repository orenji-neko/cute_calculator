"""
    Core Application of Calculator
"""

from PyQt5.QtWidgets import QApplication
import sys

from main_window import Main_Window

def run() -> None:
    app = QApplication(sys.argv)

    main_window = Main_Window()
    main_window.show()

    sys.exit(app.exec())