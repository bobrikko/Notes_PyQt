from PyQt6.QtWidgets import QDialog, QListWidgetItem
from note_list_manager_ui import Ui_NoteListManager
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt

class NoteListManager(QDialog, Ui_NoteListManager):
    def __init__(self, list_name, notes, parent=None, theme="light", font="Arial", font_size=12):
        super().__init__(parent)
        self.setupUi(self)

        self.list_name = list_name
        self.notes = notes
        self.listTitle.setText(f"Список: {list_name}")

        self.populate_note_list()

        self.deleteNoteButton.clicked.connect(self.delete_selected_note)

        self.apply_settings(theme, font, font_size)
        self.populate_note_list()

    def apply_settings(self, theme, font, font_size):
        self.set_theme(theme)
        self.apply_font(font, font_size)

    def set_theme(self, theme):
        if theme.lower() == "dark":
            self.setStyleSheet("background-color: #333; color: #fff;")
        else:
            self.setStyleSheet("background-color: #fff; color: #000;")

    def apply_font(self, font, font_size):
        font = QFont(font, font_size)
        self.setFont(font)
        self.noteList.setFont(font)

    def update_settings(self, theme, font, font_size):
        self.apply_settings(theme, font, font_size)

    def populate_note_list(self):
        self.noteList.clear()
        for note in self.notes:
            item = QListWidgetItem(note.title)
            item.setData(Qt.ItemDataRole.UserRole, note)
            self.noteList.addItem(item)

    def delete_selected_note(self):
        selected_item = self.noteList.currentItem()
        if selected_item:
            note = selected_item.data(Qt.ItemDataRole.UserRole)
            self.notes.remove(note)
            self.populate_note_list()
 