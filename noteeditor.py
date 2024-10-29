from PyQt6.QtWidgets import QDialog, QFileDialog, QMessageBox
from PyQt6 import uic
from PyQt6.QtCore import pyqtSignal
from PyQt6.QtGui import QTextCursor
import markdown2
from note import Note
from fpdf import FPDF

class NoteEditor(QDialog):
    note_saved = pyqtSignal(Note)

    def __init__(self, note_content="", tags="Новая заметка", theme="light"):
        super().__init__()
        uic.loadUi("editor_window.ui", self)
        self.editor.setText(note_content)
        self.tagInput.setText(tags)
        self.apply_theme(theme)

        self.markdown_converter = markdown2.Markdown()
        self.editor.textChanged.connect(self.update_preview)
        self.saveButton.clicked.connect(self.save_note)
        self.exportButton.clicked.connect(self.export_to_pdf)
        self.insertImageButton.clicked.connect(self.insert_image)

        self.update_preview()

    def update_preview(self):
        html_content = self.markdown_converter.convert(self.editor.toPlainText())
        self.previewArea.setHtml(html_content)
        cursor = self.previewArea.textCursor()
        cursor.movePosition(QTextCursor.MoveOperation.Start)
        self.previewArea.setTextCursor(cursor)

    def get_note_content(self):
        return self.editor.toPlainText(), self.tagInput.text()

    def save_note(self):
        content, tags = self.get_note_content()
        if content.strip() or tags.strip():
            self.note_saved.emit(Note(content, tags.split(",")))
            self.accept()
