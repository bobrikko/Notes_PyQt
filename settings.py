from settings_window_ui import Ui_SettingsDialog
from PyQt6.QtWidgets import QDialog, QFontComboBox, QSpinBox, QPushButton, QRadioButton
from PyQt6.QtGui import QFontDatabase
from PyQt6.QtCore import pyqtSignal

class SettingsDialog(QDialog, Ui_SettingsDialog):
    theme_changed = pyqtSignal(str) 
    font_changed = pyqtSignal(str, int)

    def __init__(self, current_theme, current_font, current_font_size):
        super().__init__()
        self.setupUi(self)

        self.darkThemeRadio = self.findChild(QRadioButton, "darkThemeRadio")
        self.lightThemeRadio = self.findChild(QRadioButton, "lightThemeRadio")
        self.fontComboBox = self.findChild(QFontComboBox, "fontComboBox")
        self.sizeSpinBox = self.findChild(QSpinBox, "sizeSpinBox")
        self.applyButton = self.findChild(QPushButton, "applyButton")

        if current_theme.lower() == "dark":
            self.darkThemeRadio.setChecked(True)
        else:
            self.lightThemeRadio.setChecked(True)

        self.sizeSpinBox.setRange(8, 48)
        self.fontComboBox.addItems(QFontDatabase.families())
        self.fontComboBox.setCurrentText(current_font)
        self.sizeSpinBox.setValue(current_font_size)

        self.applyButton.clicked.connect(self.apply_settings)

    def apply_settings(self):
        theme = "dark" if self.darkThemeRadio.isChecked() else "light"
        font = self.fontComboBox.currentText()
        font_size = self.sizeSpinBox.value()

        self.theme_changed.emit(theme)
        self.font_changed.emit(font, font_size)
        self.accept()