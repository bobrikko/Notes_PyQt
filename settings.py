from PyQt6.QtWidgets import QDialog
from PyQt6 import uic
from PyQt6.QtCore import pyqtSignal

class SettingsDialog(QDialog):
    theme_changed = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        uic.loadUi("settings_window.ui", self)

        self.applyButton.clicked.connect(self.apply_settings)

    def apply_settings(self):
        if self.darkThemeRadio.isChecked():
            self.theme_changed.emit("dark")
        elif self.lightThemeRadio.isChecked():
            self.theme_changed.emit("light")

        self.accept()
