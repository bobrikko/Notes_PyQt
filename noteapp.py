from PyQt6.QtWidgets import QMainWindow, QListWidgetItem, QDialog
from PyQt6 import uic
from noteeditor import NoteEditor
from PyQt6.QtCore import Qt
from settings import SettingsDialog

class NoteApp(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("main_window.ui", self)

        self.createButton.clicked.connect(self.open_editor_for_new_note)
        self.editButton.clicked.connect(self.open_editor_for_edit_note)
        self.deleteButton.clicked.connect(self.delete_note)
        self.sortButton.clicked.connect(self.sort_notes)
        self.searchBar.textChanged.connect(self.filter_notes_by_tag)
        self.settingsButton.clicked.connect(self.open_settings)
        
        self.current_theme = "light"

        self.notes = []

    def open_editor_for_new_note(self):
        self.noteEditor = NoteEditor(theme=self.current_theme)
        if self.noteEditor.exec() == QDialog.DialogCode.Accepted:
            new_note_content, tags = self.noteEditor.get_note_content()
            self.add_note_to_list(tags, new_note_content)

    def open_settings(self):
        self.settingsDialog = SettingsDialog()
        self.settingsDialog.theme_changed.connect(self.apply_theme)
        self.settingsDialog.exec()
