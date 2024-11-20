from PyQt6.QtWidgets import QApplication
import sys
from main_window import MainWindow


app = QApplication(sys.argv)
main_window = MainWindow()
main_window.show()
sys.exit(app.exec())