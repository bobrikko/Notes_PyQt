from PyQt6.QtWidgets import QDialog, QVBoxLayout, QRadioButton, QPushButton
from PyQt6.QtCore import pyqtSignal

class SortOptionsDialog(QDialog):
    sorting_selected = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Выберите тип сортировки")

        self.alpha_asc = QRadioButton("По алфавиту (A-Z)")
        self.alpha_desc = QRadioButton("По алфавиту (Z-A)")
        self.date_asc = QRadioButton("По дате добавления (старые сначала)")
        self.date_desc = QRadioButton("По дате добавления (новые сначала)")

        self.apply_button = QPushButton("Применить")
        self.apply_button.clicked.connect(self.apply_sorting)

        layout = QVBoxLayout()
        layout.addWidget(self.alpha_asc)
        layout.addWidget(self.alpha_desc)
        layout.addWidget(self.date_asc)
        layout.addWidget(self.date_desc)
        layout.addWidget(self.apply_button)

        self.setLayout(layout)

    def apply_sorting(self):
        if self.alpha_asc.isChecked():
            self.sorting_selected.emit("alpha_asc")
        elif self.alpha_desc.isChecked():
            self.sorting_selected.emit("alpha_desc")
        elif self.date_asc.isChecked():
            self.sorting_selected.emit("date_asc")
        elif self.date_desc.isChecked():
            self.sorting_selected.emit("date_desc")
        self.accept()