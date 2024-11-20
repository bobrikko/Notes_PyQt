from PyQt6.QtWidgets import QMainWindow, QListWidgetItem, QInputDialog, QDialog
from main_window_ui import Ui_MainWindow
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont
from editor_window import NoteEditor
from sortoptions import SortOptionsDialog
from settings import SettingsDialog
from note import Note
from notelist_manager import NoteListManager
from select_notes_dialog import SelectNotesDialog
from Class_select import ClassSelectionDialog

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.createButton.clicked.connect(self.open_editor_for_new_note)
        self.deleteButton.clicked.connect(self.delete_note)
        self.sortButton.clicked.connect(self.open_sort_options)
        self.searchBar.textChanged.connect(self.filter_notes_by_tag)
        self.settingsButton.clicked.connect(self.open_settings)
        self.editButton.clicked.connect(self.open_selected_note)
        self.pinButton.clicked.connect(self.toggle_pin_note)
        self.createListButton.clicked.connect(self.create_new_list)
        self.openListButton.clicked.connect(self.open_selected_list)
        self.addNoteToListButton.clicked.connect(self.add_note_to_selected_list)

        self.current_theme = "Light"
        self.current_font = "Arial"
        self.current_font_size = 12
        self.notes = []
        self.lists = {}
        self.note_list_managers = {}
        self.update_list_display()
        self.selected_list_name = None

        self.sort_options_dialog = SortOptionsDialog()
        self.sort_options_dialog.sorting_selected.connect(self.sort_notes_by_option)

        self.apply_settings()

    def open_settings(self):
        settings_dialog = SettingsDialog(self.current_theme, self.current_font, self.current_font_size)
        settings_dialog.theme_changed.connect(self.update_theme)
        settings_dialog.font_changed.connect(self.update_font)
        settings_dialog.exec()

    def update_theme(self, theme):
        self.current_theme = theme
        self.apply_settings()
        for manager in self.note_list_managers.values():
            manager.update_settings(self.current_theme, self.current_font, self.current_font_size)

    def update_font(self, font, font_size):
        self.current_font = font
        self.current_font_size = font_size
        self.apply_settings()
        for manager in self.note_list_managers.values():
            manager.update_settings(self.current_theme, self.current_font, self.current_font_size)

    def apply_settings(self):
        if self.current_theme.lower() == "dark":
            self.setStyleSheet("background-color: #333; color: #fff;")
        else:
            self.setStyleSheet("background-color: #fff; color: #000;")

        font = QFont(self.current_font, self.current_font_size)
        self.setFont(font)
        self.noteList.setFont(font)
        self.listWidget.setFont(font)

    def update_list_display(self):
        self.listWidget.clear()
        for list_name in self.lists.keys():
            self.listWidget.addItem(list_name)

    def create_new_list(self):
        list_name, ok = QInputDialog.getText(self, "Создать новый список", "Название списка:")
        if ok and list_name:
            if list_name not in self.lists:
                self.lists[list_name] = []
                self.selected_list_name = list_name
                self.update_list_list_display()
            else:
                print("Список с таким названием уже существует.")

    def open_selected_list(self):
        list_name, ok = QInputDialog.getItem(self, "Выберите список", "Список:", list(self.lists.keys()), 0, False)
        if ok and list_name:
            notes = self.lists[list_name]
            if list_name not in self.note_list_managers:
                note_list_manager = NoteListManager(
                    list_name,
                    notes,
                    theme=self.current_theme,
                    font=self.current_font,
                    font_size=self.current_font_size
                )
                self.note_list_managers[list_name] = note_list_manager
            self.note_list_managers[list_name].show()

    def add_note_to_selected_list(self):
        class_selection_dialog = ClassSelectionDialog(self.lists)
        if class_selection_dialog.exec() == QDialog.DialogCode.Accepted:
            self.selected_list_name = class_selection_dialog.get_selected_list_name()
            if self.selected_list_name:
                select_notes_dialog = SelectNotesDialog(self.notes, self.lists[self.selected_list_name])
                if select_notes_dialog.exec() == QDialog.DialogCode.Accepted:
                    selected_note = select_notes_dialog.get_selected_note()
                    if selected_note and selected_note not in self.lists[self.selected_list_name]:
                        self.lists[self.selected_list_name].append(selected_note)
                        self.update_list_display()

    def update_list_display(self):
       self.listWidget.clear()
       if self.selected_list_name:
           list_to_display = self.lists.get(self.selected_list_name, [])
           for note in list_to_display:
               self.listWidget.addItem(note.title)

    def update_list_display_for_selected_list(self):
        self.listWidget.clear()
        if self.selected_list_name:
            list_to_display = self.lists.get(self.selected_list_name, [])
            for note in list_to_display:
                for tag in note.title:
                    self.listWidget.addItem(tag)

    def open_list(self, list_name):
        if list_name in self.lists:
            self.listWidget.clear()

            for note in self.lists[list_name]:
                self.listWidget.addItem(note.title)

            print(f"Открыт список '{list_name}'")
        else:
            print(f"Список '{list_name}' не найден.")

    def open_selected_note_from_list(self, note):
        self.noteEditor = NoteEditor(
            theme=self.current_theme,
            font=self.current_font,
            font_size=self.current_font_size,
            tags=note.title,
            content=note.content
        )
        self.noteEditor.note_saved.connect(lambda title, content: self.update_note(note, title, content))
        self.noteEditor.show()

    def delete_note_from_list(self, note):
        for list_name in self.lists:
            if note in self.lists[list_name]:
                self.lists[list_name].remove(note)
                break

    def open_editor_for_new_note(self):
        self.noteEditor = NoteEditor(theme=self.current_theme, font=self.current_font, font_size=self.current_font_size)
        self.noteEditor.note_saved.connect(self.save_new_note)
        self.noteEditor.show()

    def save_new_note(self, title, content):
        new_note = Note(title=title, content=content)
        self.notes.append(new_note)
        self.add_note_to_list(new_note)
    
    def add_note_to_list(self, note, list_name=None):
        display_text = f"📌 {note.title}" if note.is_pinned else note.title
        item = QListWidgetItem(display_text)
        item.setData(Qt.ItemDataRole.UserRole, note)

        if list_name is None:
            self.noteList.addItem(item)
        else:
            self.lists[list_name].append(note)

    def delete_note(self):
        selected_item = self.noteList.currentItem()
        if selected_item:
            row = self.noteList.row(selected_item)
            note = selected_item.data(Qt.ItemDataRole.UserRole)
            self.noteList.takeItem(row)
            self.notes.remove(note)

    def sort_notes_by_option(self, sort_option):
        pinned_notes = [note for note in self.notes if note.is_pinned]
        unpinned_notes = [note for note in self.notes if not note.is_pinned]

        if sort_option == "alpha_asc":
            unpinned_notes.sort(key=lambda note: note.title.lower())
        elif sort_option == "alpha_desc":
            unpinned_notes.sort(key=lambda note: note.title.lower(), reverse=True)
        elif sort_option == "date_asc":
            unpinned_notes.sort(key=lambda note: note.date_added)
        elif sort_option == "date_desc":
            unpinned_notes.sort(key=lambda note: note.date_added, reverse=True)

        self.notes = pinned_notes + unpinned_notes

        self.update_list_display()

    def update_list_display(self):
        self.noteList.clear()
        for note in self.notes:
            display_text = f"📌 {note.title}" if note.is_pinned else note.title
            item = QListWidgetItem(display_text)
            item.setData(Qt.ItemDataRole.UserRole, note)
            self.noteList.addItem(item)

    def update_list_list_display(self):
        self.listWidget.clear()

        for list_name in self.lists.keys():
            item = QListWidgetItem(list_name)
            self.listWidget.addItem(item)

    def open_sort_options(self):
        self.sort_options_dialog.exec()

    def toggle_pin_note(self):
        selected_item = self.noteList.currentItem()
        if selected_item:
            note = selected_item.data(Qt.ItemDataRole.UserRole)
            note.is_pinned = not note.is_pinned
            
            if note.is_pinned:
                self.notes.insert(0, self.notes.pop(self.notes.index(note)))
            else:
                self.notes.append(self.notes.pop(self.notes.index(note)))

        self.update_list_display()

    def update_note_display(self, item, note):
        display_text = f"📌 {note.title}" if note.is_pinned else note.title
        item.setText(display_text)

    def open_selected_note(self):
        selected_item = self.noteList.currentItem()
        if selected_item:
            note = selected_item.data(Qt.ItemDataRole.UserRole)
            if isinstance(note, Note):
                self.open_note_editor(note)

    def open_note_editor(self, note):
        self.noteEditor = NoteEditor(
            theme=self.current_theme,
            font=self.current_font,
            font_size=self.current_font_size,
            tags=note.title,
            content=note.content
        )
        self.noteEditor.note_saved.connect(lambda title, content: self.update_note(note, title, content))
        self.noteEditor.show()

    def update_note(self, note, updated_title, updated_content):
        note.title = updated_title
        note.content = updated_content
        self.update_note_display_for_note(note)
        self.update_list_display()

    def update_note_display_for_note(self, note):
        for index in range(self.noteList.count()):
            item = self.noteList.item(index)
            if item.data(Qt.ItemDataRole.UserRole) == note:
                display_text = f"📌 {note.title}" if note.is_pinned else note.title
                item.setText(display_text)
                break

    def filter_notes_by_tag(self):
        filter_text = self.searchBar.text().strip().lower()
        self.noteList.clear()

        pinned_notes = []
        unpinned_notes = []

        for note in self.notes:
            if filter_text in note.title.lower():
                if note.is_pinned:
                    pinned_notes.append(note)
                else:
                    unpinned_notes.append(note)

        for note in pinned_notes + unpinned_notes:
            self.add_note_to_list(note)
