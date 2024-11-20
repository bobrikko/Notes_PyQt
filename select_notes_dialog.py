from PyQt6.QtWidgets import QDialog, QComboBox, QPushButton, QVBoxLayout

class SelectNotesDialog(QDialog):
    def __init__(self, notes, target_list):
        super().__init__()
        self.setWindowTitle("Выбор заметок")
        
        self.notes = notes
        self.target_list = target_list
        self.comboBox = QComboBox(self)
        self.populate_notes()
        
        self.okButton = QPushButton("Добавить", self)
        self.okButton.clicked.connect(self.accept)
        
        layout = QVBoxLayout()
        layout.addWidget(self.comboBox)
        layout.addWidget(self.okButton)
        self.setLayout(layout)

    def populate_notes(self):
        self.comboBox.clear()
        for note in self.notes:
            if note not in self.target_list:
                self.comboBox.addItem(note.title)

    def get_selected_note(self):
        selected_title = self.comboBox.currentText()
        for note in self.notes:
            if note.title == selected_title:
                return note
        return None