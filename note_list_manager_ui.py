from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_NoteListManager(object):
    def setupUi(self, NoteListManager):
        NoteListManager.setObjectName("NoteListManager")
        NoteListManager.resize(300, 400)
        self.verticalLayout = QtWidgets.QVBoxLayout(NoteListManager)
        self.verticalLayout.setObjectName("verticalLayout")
        self.listTitle = QtWidgets.QLabel(parent=NoteListManager)
        self.listTitle.setObjectName("listTitle")
        self.verticalLayout.addWidget(self.listTitle)
        self.noteList = QtWidgets.QListWidget(parent=NoteListManager)
        self.noteList.setObjectName("noteList")
        self.verticalLayout.addWidget(self.noteList)
        self.buttonLayout = QtWidgets.QHBoxLayout()
        self.buttonLayout.setObjectName("buttonLayout")
        self.deleteNoteButton = QtWidgets.QPushButton(parent=NoteListManager)
        self.deleteNoteButton.setObjectName("deleteNoteButton")
        self.buttonLayout.addWidget(self.deleteNoteButton)
        self.verticalLayout.addLayout(self.buttonLayout)

        self.retranslateUi(NoteListManager)
        QtCore.QMetaObject.connectSlotsByName(NoteListManager)

    def retranslateUi(self, NoteListManager):
        _translate = QtCore.QCoreApplication.translate
        NoteListManager.setWindowTitle(_translate("NoteListManager", "Управление списком заметок"))
        self.listTitle.setText(_translate("NoteListManager", "Название списка"))
        self.deleteNoteButton.setText(_translate("NoteListManager", "Удалить заметку"))