from PyQt6.QtWidgets import QApplication
import sys
from noteapp import NoteApp

app = QApplication(sys.argv)
main_window = NoteApp()
main_window.show()
sys.exit(app.exec())
