from PyQt6.QtWidgets import QDialog, QFileDialog, QMessageBox
from editor_window_ui import Ui_NoteEditor
from PyQt6.QtGui import QTextCursor, QFont
from PyQt6.QtCore import pyqtSignal
import markdown2
from fpdf import FPDF

class NoteEditor(QDialog, Ui_NoteEditor):
    note_saved = pyqtSignal(str, str)

    def __init__(self, content="", tags="Новая заметка", theme="light", font="Arial", font_size=12):
        super().__init__()
        self.setupUi(self)

        self.tags = tags
        self.content = content
        self.editor.setText(content)
        self.tagInput.setText(tags)

        self.markdown_converter = markdown2.Markdown()
        self.editor.textChanged.connect(self.update_preview)

        self.saveButton.clicked.connect(self.save_note)
        self.exportButton.clicked.connect(self.export_to_pdf)
        self.insertImageButton.clicked.connect(self.insert_image)

        self.update_preview()

        self.apply_theme(theme)
        self.apply_font(font, font_size)

    def apply_theme(self, theme):
        if theme.lower() == "dark":
            self.setStyleSheet("background-color: #333; color: #fff;")
        else:
            self.setStyleSheet("background-color: #fff; color: #000;")

    def apply_font(self, font, font_size):
        font = QFont(font, font_size)
        self.setFont(font)
        self.editor.setFont(font)

    def update_preview(self):
        html_content = self.markdown_converter.convert(self.editor.toPlainText())
        self.previewArea.setHtml(html_content)
        cursor = self.previewArea.textCursor()
        cursor.movePosition(QTextCursor.MoveOperation.Start)
        self.previewArea.setTextCursor(cursor)

    def save_note(self):
        updated_tags = self.tagInput.text()
        updated_content = self.editor.toPlainText()
        self.note_saved.emit(updated_tags, updated_content)
        self.accept()

    def insert_image(self):
        image_path, _ = QFileDialog.getOpenFileName(self, "Выберите изображение", "", "Images (*.png *.jpg *.jpeg *.bmp *.gif)")
        if image_path:
            markdown_image = f"![Image]({image_path})"
            self.editor.insertPlainText(markdown_image)
            self.update_preview()

    def export_to_pdf(self):
        pdf_path, _ = QFileDialog.getSaveFileName(self, "Сохранить в PDF", "", "PDF Files (*.pdf)")
        if pdf_path:
            pdf = FPDF()
            pdf.add_page()
            pdf.set_auto_page_break(auto=True, margin=15)
    
            pdf.add_font("DejaVu", "", "DejaVuSans.ttf", uni=True)
            pdf.set_font("DejaVu", size=12)
    
            note_content = self.editor.toPlainText()
    
            if not note_content.strip():
                QMessageBox.warning(self, "Ошибка экспорта", "Заметка пуста, не может быть экспортирована в PDF.")
                return
    
            pdf.multi_cell(0, 10, note_content)
    
            try:
                pdf.output(pdf_path)
                QMessageBox.information(self, "Экспорт завершен", "Заметка успешно сохранена в PDF.")
            except Exception as e:
                QMessageBox.critical(self, "Ошибка экспорта", f"Не удалось сохранить PDF: {str(e)}")