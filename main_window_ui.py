from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 500)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.searchBar = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.searchBar.setObjectName("searchBar")
        self.verticalLayout.addWidget(self.searchBar)
        self.noteList = QtWidgets.QListWidget(parent=self.centralwidget)
        self.noteList.setObjectName("noteList")
        self.verticalLayout.addWidget(self.noteList)
        self.buttonLayout = QtWidgets.QHBoxLayout()
        self.buttonLayout.setObjectName("buttonLayout")
        self.createButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.createButton.setObjectName("createButton")
        self.buttonLayout.addWidget(self.createButton)
        self.deleteButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.deleteButton.setObjectName("deleteButton")
        self.buttonLayout.addWidget(self.deleteButton)
        self.settingsButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.settingsButton.setObjectName("settingsButton")
        self.buttonLayout.addWidget(self.settingsButton)
        self.sortButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.sortButton.setObjectName("sortButton")
        self.buttonLayout.addWidget(self.sortButton)
        self.editButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.editButton.setObjectName("editButton")
        self.buttonLayout.addWidget(self.editButton)
        self.pinButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pinButton.setObjectName("pinButton")
        self.buttonLayout.addWidget(self.pinButton)
        self.verticalLayout.addLayout(self.buttonLayout)
        self.createListButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.createListButton.setObjectName("createListButton")
        self.verticalLayout.addWidget(self.createListButton)
        self.openListButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.openListButton.setObjectName("openListButton")
        self.verticalLayout.addWidget(self.openListButton)
        self.newListSection = QtWidgets.QVBoxLayout()
        self.newListSection.setObjectName("newListSection")
        self.listWidget = QtWidgets.QListWidget(parent=self.centralwidget)
        self.listWidget.setObjectName("listWidget")
        self.newListSection.addWidget(self.listWidget)
        self.addNoteToListButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.addNoteToListButton.setObjectName("addNoteToListButton")
        self.newListSection.addWidget(self.addNoteToListButton)
        self.verticalLayout.addLayout(self.newListSection)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Note List"))
        self.searchBar.setPlaceholderText(_translate("MainWindow", "Поиск по тегам"))
        self.createButton.setText(_translate("MainWindow", "Создать"))
        self.deleteButton.setText(_translate("MainWindow", "Удалить"))
        self.settingsButton.setText(_translate("MainWindow", "Настройки"))
        self.sortButton.setText(_translate("MainWindow", "Сортировать по тегам"))
        self.editButton.setText(_translate("MainWindow", "Открыть/Редактировать"))
        self.pinButton.setText(_translate("MainWindow", "Закрепить/Открепить"))
        self.createListButton.setText(_translate("MainWindow", "Создать список"))
        self.openListButton.setText(_translate("MainWindow", "Открыть список"))
        self.addNoteToListButton.setText(_translate("MainWindow", "Добавить заметку"))