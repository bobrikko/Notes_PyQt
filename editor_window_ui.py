from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_NoteEditor(object):
    def setupUi(self, NoteEditor):
        NoteEditor.setObjectName("NoteEditor")
        self.verticalLayout = QtWidgets.QVBoxLayout(NoteEditor)
        self.verticalLayout.setObjectName("verticalLayout")
        self.editor = QtWidgets.QTextEdit(parent=NoteEditor)
        self.editor.setObjectName("editor")
        self.verticalLayout.addWidget(self.editor)
        self.tagInput = QtWidgets.QLineEdit(parent=NoteEditor)
        self.tagInput.setObjectName("tagInput")
        self.verticalLayout.addWidget(self.tagInput)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.saveButton = QtWidgets.QPushButton(parent=NoteEditor)
        self.saveButton.setObjectName("saveButton")
        self.horizontalLayout.addWidget(self.saveButton)
        self.exportButton = QtWidgets.QPushButton(parent=NoteEditor)
        self.exportButton.setObjectName("exportButton")
        self.horizontalLayout.addWidget(self.exportButton)
        self.insertImageButton = QtWidgets.QPushButton(parent=NoteEditor)
        self.insertImageButton.setObjectName("insertImageButton")
        self.horizontalLayout.addWidget(self.insertImageButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.previewArea = QtWidgets.QTextBrowser(parent=NoteEditor)
        self.previewArea.setObjectName("previewArea")
        self.verticalLayout.addWidget(self.previewArea)

        self.retranslateUi(NoteEditor)
        QtCore.QMetaObject.connectSlotsByName(NoteEditor)

    def retranslateUi(self, NoteEditor):
        _translate = QtCore.QCoreApplication.translate
        NoteEditor.setWindowTitle(_translate("NoteEditor", "Редактирование заметки"))
        self.tagInput.setPlaceholderText(_translate("NoteEditor", "Введите тег, через запятую"))
        self.saveButton.setText(_translate("NoteEditor", "Сохранить"))
        self.exportButton.setText(_translate("NoteEditor", "Экспорт в PDF"))
        self.insertImageButton.setText(_translate("NoteEditor", "Вставить изображение"))