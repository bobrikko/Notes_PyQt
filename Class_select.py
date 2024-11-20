from PyQt6.QtWidgets import QDialog, QComboBox, QPushButton, QVBoxLayout

class ClassSelectionDialog(QDialog):
    def __init__(self, lists):
        super().__init__()
        self.setWindowTitle("Выбор списка")
        
        self.comboBox = QComboBox(self)
        self.comboBox.addItems(lists.keys())
        
        self.okButton = QPushButton("Выбрать", self)
        self.okButton.clicked.connect(self.accept)
        
        layout = QVBoxLayout()
        layout.addWidget(self.comboBox)
        layout.addWidget(self.okButton)
        self.setLayout(layout)

    def get_selected_list_name(self):
        return self.comboBox.currentText()